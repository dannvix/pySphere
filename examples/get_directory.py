#!/usr/bin/env python
from pysphere import VIServer

server = VIServer()
server.connect("my.esx.host.example.org", "username", "secret")

vm = server.get_vm_by_path("[datastore] path/to/file.vmx")
vm.wait_for_tools()
vm.login_in_guest("Administrator", "secret")
vm.get_directory("C:/HelloWorld", "./Test", overwrite=True)

server.disconnect()
