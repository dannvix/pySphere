#!/usr/bin/env python
from pysphere import VIServer

server = VIServer()
server.set_ssl_no_verify()
server.connect("my.esx.host.example.org", "username", "secret")
vm = server.get_vm_by_name("MyGuestVMName", datacenter="MyCluster")

vm.wait_for_tools(timeout=30)
print "VMware tool status: {0}".format(vm.get_tools_status())
if not vm.get_tools_status() == "RUNNING":
    print "VMware tool status: {0}".format(vm.get_tools_status())
    raise Exception("VMWare tools is not running")

vm.login_in_guest("GuestAccount", "GuestPassword")
try:
    vm.start_process("C:\\Windows\\System32\\cmd.exe", args=["/K timeout /t 50"], sync_run=True, timeout=10)
except Exception as e:
    print e

server.disconnect()
