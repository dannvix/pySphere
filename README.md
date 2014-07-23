pySphere
========
VMware vSphere Web Service client in Python.


Preface
-------
* This is a enhanced fork of Sebastian Tello's [PySphere](https://code.google.com/p/pysphere/), not just a git-svn mirror.
* All trademarks and registered trademarks are the property of their respective owners.
* Pull requests are welcome.


Features
--------
* Connect to VMWare's ESX, ESXi, Virtual Center, Virtual Server hosts
* Query hosts, datacenters, datastores, resource pools, virtual machines
* VMs: Power on, power off, reset, revert to snapshot, get properties, update vmware tools, clone, migrate
* vSphere 5.0 Guest operations: Create/delete/move files and directories. Upload/download files and directories from the guest system. List/start/stop processes in the guest system
* Create and delete snapshots
* Create and download screenshots of guest display
* vSphere 5.0 Datastore operations: Upload/download files from the datastore file system
* Get hosts statistics and monitor performance

And of course, you can use it to access all the vSphere API through python.

It's built upon a slightly modified version of [ZSI](http://pywebsvcs.sourceforge.net/zsi.html) (that comes bundled-in) which makes it really fast in contrast to other python SOAP libraries that don't
provide code generation.


Installation
------------
The “pysphere” package in PyPI is the original version (Sebastian's). Currently the only way to install this package is to download this repository and run `python setup.py install`.


Quick Example
-------------
Here's an example of how to query and power on all virtual machines in the specified datacenter and cluster.

```python
from pysphere import VIServer
server = VIServer()
server.connect("my.esx.host.example.com", "username", "secret")
vms = server.get_registered_vms(datacenter="MyDataCenter", cluster="MyCluster")
for vm_path in vms:
    print "vm_path = [%s]" % vm_path # "[datastore] path/to/file.vmx"
    vm = server.get_vm_by_path(vm_path)
    vm.power_on()
    print vm.get_status() # "POWERED ON"
```


Resource
--------
* [Getting Started](http://code.google.com/p/pysphere/wiki/GettingStarted) guide
* Some examples are located in `examples/`
* More examples and use cases can be found in the [discussion group](http://groups.google.com/group/pysphere)
* [pyVmomi](https://github.com/vmware/pyvmomi) — official VMware vSphere API Python Bindings. [What is the Difference between PySphere and PyVmomi?](http://stackoverflow.com/questions/21326448)



License
-------
Copyright (c) 2012, Sebastian Tello  
Copyright (c) 2014, Shao-Chung Chen  
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

  * Redistributions of source code must retain the above copyright notice,
    this list of conditions and the following disclaimer.
  * Redistributions in binary form must reproduce the above copyright notice,
    this list of conditions and the following disclaimer in the documentation
    and/or other materials provided with the distribution.
  * Neither the name of copyright holders nor the names of its contributors
    may be used to endorse or promote products derived from this software
    without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.



License of `ZSI`
----------------
Copyright (c) 2003, The Regents of the University of California,
through Lawrence Berkeley National Laboratory (subject to receipt of
any required approvals from the U.S. Dept. of Energy). All rights
reserved. Redistribution and use in source and binary forms, with or
without modification, are permitted provided that the following
conditions are met:

(1) Redistributions of source code must retain the above copyright
notice, this list of conditions and the following disclaimer.
(2) Redistributions in binary form must reproduce the above copyright
notice, this list of conditions and the following disclaimer in the
documentation and/or other materials provided with the distribution.
(3) Neither the name of the University of California, Lawrence Berkeley
National Laboratory, U.S. Dept. of Energy nor the names of its contributors
may be used to endorse or promote products derived from this software without
specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
"AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED
TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS
BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE
GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY
OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF
SUCH DAMAGE.

You are under no obligation whatsoever to provide any bug fixes,
patches, or upgrades to the features, functionality or performance of
the source code ("Enhancements") to anyone; however, if you choose to
make your Enhancements available either publicly, or directly to
Lawrence Berkeley National Laboratory, without imposing a separate
written license agreement for such Enhancements, then you hereby grant
the following license: a non-exclusive, royalty-free perpetual license
to install, use, modify, prepare derivative works, incorporate into
other computer software, distribute, and sublicense such Enhancements
or derivative works thereof, in binary and source code form.