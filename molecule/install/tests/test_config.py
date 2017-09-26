import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_tinc_conf(File):
    f = File('/etc/tinc/tinc/tinc.conf')

    assert f.exists
    assert f.contains("Name = ")
    assert f.contains("Interface = tinc")
    assert f.contains("Device = /dev/net/tun")
    assert f.contains("AddressFamily = ipv4")
    assert f.contains("Port = 655")
    assert f.contains("ConnectTo = ")
