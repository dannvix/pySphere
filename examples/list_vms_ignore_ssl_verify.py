#!/usr/bin/env python
from pysphere import VIServer

server = VIServer()
server.set_ssl_no_verify()
server.connect("example.com", "username", "password")

# datacenter is case-senstive
vmlist = server.get_registered_vms(datacenter="ha-datacenter")
for vm_path in vmlist:
  vm = server.get_vm_by_path(vm_path)
  status = vm.get_status()
  print "vm_path=[%s], status=[%s]" % (vm_path, status)

server.disconnect()
