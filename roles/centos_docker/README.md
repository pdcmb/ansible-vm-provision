Role Name
=========

Ansible role that installs and configures docker on CentOS

Requirements
------------


Role Variables
--------------


Dependencies
------------

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

BSD

Author Information
------------------

Ziomek Mateusz
