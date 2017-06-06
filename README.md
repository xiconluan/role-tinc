Ansible Role Tinc
=========

This role installs and configures the meshed VPN service tinc.

Example Playbook
----------------

    - hosts: foo
      vars:
        tinc_enabled: yes
        tinc_node: foo_example_com
        tinc_subnets:
          - 10.100.0.1/32
        tinc_addresses: 10.100.0.1/24
        tinc_connect_to:
          - bar_example_com
      roles:
         - blunix.role-sudo
    
    - hosts: bar
      vars:
        tinc_enabled: yes
        tinc_node: bar_example_com
        tinc_subnet: 

License
-------

Apache

Author Information
------------------

Service and support for orchestrated hosting environments, continuous integration/deployment/delivery and various Linux and open-source technology stacks are available from:

```
Blunix GmbH - Professional Linux Service
Glogauer Straße 21
10999 Berlin - Germany

Web: www.blunix.org
Email: mailto:service@blunix.org
```
