#--
# Copyright (c) 2012, Sebastian Tello
# Copyright (c) 2014, Shao-Chung Chen
# All rights reserved.

# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
#   * Redistributions of source code must retain the above copyright notice,
#     this list of conditions and the following disclaimer.
#   * Redistributions in binary form must reproduce the above copyright notice,
#     this list of conditions and the following disclaimer in the documentation
#     and/or other materials provided with the distribution.
#   * Neither the name of copyright holders nor the names of its contributors
#     may be used to endorse or promote products derived from this software
#     without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#
#--

# ref. https://code.google.com/p/pysphere/issues/detail?id=12
# ref. https://code.google.com/p/pysphere/issues/detail?id=22

import urllib, urllib2
import os
import sys

from pysphere.resources.vi_exception import VIException, VIApiException, \
                                            FaultTypes

# todo: add heredocs
# todo: add unit tests
class VIDatastore:
    def __init__(self, server_instance, datacenter, datastore):
        self._server = server_instance
        self._datacenter = datacenter
        self._datastore = datastore
        self._auth_handler = self.__build_auth_handler()

    # todo: implement
    def list_file(self, remote_path):
        raise VIException("Operation not support yet",
                          FaultTypes.NOT_SUPPORTED)

    # todo: add overwrite option
    # todo: handle non-exist local file
    def send_file(self, local_path, remote_path):
        with open(local_path, "rb") as fd:
            data = fd.read()

            resource_path = "/folder/%s" % remote_path.lstrip("/")
            request_url = self.__build_request_url(resource_path)
            response = self.__send_request(request_url, data)
        return response.code == 200
        

    def get_file(self, remote_path, local_path=None, overwrite="False"):
        if local_path is None:
            local_path = os.path.basename(remote_path)

        if os.path.exists(local_path) and not overwrite:
            raise VIException("Local file already exists",
                              FaultTypes.PARAMETER_ERROR)

        resource_path = "/folder/%s" % remote_path.lstrip("/")
        request_url = self.__build_request_url(resource_path)

        if sys.version_info >= (2, 6):
            response = self.__send_request(request_url)
            chunk_size = 16 * 1024
            with open(local_path, "wb") as fd:
                while True:
                    chunk = response.read(chunk_size)
                    if not chunk: break
                    fd.write(chunk)
            return response.code == 200
        else:
            # SSL protocol error when executing this on Python < 2.6
            urllib.urlretrieve(request_url, local_path)

    # todo: implement
    def move_file(self, src_path, dst_path, overwrite=True):
        raise VIException("Operatoin not supported yet",
                          FaultTypes.NOT_SUPPORTED)

    # todo: implement
    def delete_file(self, remote_path):
        raise VIException("Operation not supported yet",
                          FaultTypes.NOT_SUPPORTED)

    # todo: implement
    def create_directory(self, remote_path, create_parents=True):
        raise VIException("Operation not supported yet",
                          FaultTypes.NOT_SUPPORTED)

    # todo: implement
    def move_directory(self, src_path, dst_path, overwrite=True):
        raise VIException("Operation not supported yet",
                          FaultTypes.NOT_SUPPORTED)

    # todo: implement
    def delete_directory(self, remote_path):
        raise VIException("Operation not supported yet",
                          FaultTypes.NOT_SUPPORTED)

    # todo: implement
    def get_directory(self, remote_path, local_path, overwrite=True):
        raise VIException("Operation not supported yet",
                          FaultTypes.NOT_SUPPORTED)

    # todo: implement
    def send_directory(self, local_path, remote_path, overwrite=True):
        raise VIException("Operation not supported yet",
                          FaultTypes.NOT_SUPPORTED)

    #---------------------#
    #-- PRIVATE METHODS --#
    #---------------------#

    def __send_request(self, request_url, data=None):
        opener = urllib2.build_opener(self._auth_handler)
        request = urllib2.Request(request_url, data=data)
        if data:
            request.get_method = lambda: 'PUT'
        return opener.open(request)

    def __build_request_url(self, resource_path):
        if not resource_path.startswith("/"):
          resource_path = "/" + resource_path

        params_dict = {
          "dsName": self._datastore,
          "dcPath": self._datacenter
        }
        params = urllib.urlencode(params_dict)
        return "%s%s?%s" % (self.__get_service_url(), resource_path, params)      

    def __get_service_url(self):
        service_url = self._server._proxy.binding.url
        return service_url[:service_url.rindex("/sdk")]

    def __build_auth_handler(self):
        service_url = self.__get_service_url()
        username = self._server._VIServer__user
        password = self._server._VIServer__password
        auth_manager = urllib2.HTTPPasswordMgrWithDefaultRealm()
        auth_manager.add_password(None, service_url, username, password)
        return urllib2.HTTPBasicAuthHandler(auth_manager)
