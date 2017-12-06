# Ansible Role Tinc

This role installs and configures the meshed VPN service tinc.

# Example Playbook

```yaml
- hosts: tinc-hosts
  vars:
    tinc_enabled: yes
    tinc_node: foo_example_com
    tinc_subnets:
      - 10.100.0.1/32
    tinc_addresses: 10.100.0.1/24
    tinc_connect_to:
      - bar_example_com
  roles:
     - blunix.role-tinc
```

# License

Apache-2.0

# Author Information

Service and support for orchestrated hosting environments,
continuous integration/deployment/delivery and various Linux
and open-source technology stacks are available from:

```
Blunix GmbH - Consulting for Linux Hosting 24/7
Glogauer Straße 21
10999 Berlin - Germany

Web: www.blunix.org
Email: service[at]blunix.org
Phone: (+49) 30 / 12 08 39 90
```
