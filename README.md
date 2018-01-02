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
  ...
```

To avoid complexity, the role itself will **not** distribute keys between the nodes and also will **not** restart or
reload the tinc daemon process. This needs to be taken care of in playbook-layer:

```yaml
  ...
  post_tasks:
    - name: cleanup fetch-bin to remove artifacts from previously failed runs
      file:
        path: /tmp/fetched/etc/tinc
        state: absent
      delegate_to: localhost
    - name: download tinc configurations from all nodes
      fetch:
        src: /etc/tinc/{{ tinc_interface }}/hosts/{{ inventory_hostname_short }}
        dest: /tmp/fetched/etc/tinc/{{ tinc_interface }}/hosts/{{ inventory_hostname_short }}
        flat: yes
        fail_on_missing: yes
    - name: upload tinc configurations to all nodes
      copy:
        src: /tmp/fetched/etc/tinc/{{ tinc_interface }}/hosts
        dest: /etc/tinc/{{ tinc_interface }}/
        owner: root
        group: root
        mode: 0644
      notify: restart tinc
    - name: cleanup fetch-bin to remove all artifacts for subsequent runs
      file:
        path: /tmp/fetched/etc/tinc
        state: absent
      delegate_to: localhost
  handlers:
    - name: restart tinc
      service:
        name: tinc@{{ tinc_interface }}
        state: restarted
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
