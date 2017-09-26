import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_ping(host):
    if host.run('hostname').stdout == 'stretch':
        host.run('ping -c3 -t1 10.99.0.2')
    elif host.run('hostname').stdout == 'xenial':
        host.run('ping -c3 -t1 10.99.0.1')
