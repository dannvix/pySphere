#!/usr/bin/env python
from pysphere import VIServer

server = VIServer()
server.connect("my.esx.host.example.org", "username", "secret")

# datacenter is case-senstive
vmlist = server.get_registered_vms(datacenter="MyDataCenter", cluster="MyCluster")
for vm_path in vmlist:
  vm = server.get_vm_by_path(vm_path)
  status = vm.get_status()
  print "vm_path=[%s], status=[%s]" % (vm_path, status)

server.disconnect()
