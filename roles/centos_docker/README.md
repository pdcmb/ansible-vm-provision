Role Name
=========

Ansible role that installs and configures docker on CentOS

Example Playbook
----------------

You can specify username (it will be added to docker group)

    - hosts: vms
      roles:
        - role: centos_docker
        vars:
          username: username

Or using newer syntax:

    - hosts: vms
      tasks:
        - include_role:
            name: centos_docker
          vars:
            username: username
          


License
-------

MIT

Author Information
------------------

Ziomek Mateusz
