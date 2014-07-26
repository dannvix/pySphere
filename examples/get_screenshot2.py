#!/usr/bin/env python
from pysphere import VIServer
import os
import re

server = VIServer()
server.connect("my.esx.host.example.org", "username", "secret")

vm = server.get_vm_by_path("[datastore] path/to/file.vmx")
vm.wait_for_tools()
vm.login_in_guest("Administrator", "secret")

"""
Here we use VIVirtualMachine.create_screenshot() to create screenshot
on the datastore, and use VIDataStore.get_file() to retrieve it.
"""
result = vm.create_screenshot()
datastore_name, resource_path = re.findall(r"^\[([^\[\]]+)\] (.*)", result)[0]

datastore = server.get_datastore_by_name(datastore_name)
datastore.get_file(resource_path, os.path.basename(resource_path))

server.disconnect()
