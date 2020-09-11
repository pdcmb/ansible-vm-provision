Role Name
=========

Ansible role that installs and configures docker on CentOS

Requirements
------------


Role Variables
--------------

- ```docker_edition``` docker edition to install, can be ```ce | ee``` 
- ```docker_containers_number``` container to create
- ```docker_container_name``` name of created container
- ```docker_container_image```: image to deploy in the container
- ```docker_packages```: packages required in order to install docker. **Should not be changed**



Dependencies
------------

A list of other roles hosted on Galaxy should go here, plus any details in regards to parameters that may need to be set for other roles, or variables that are used from other roles.

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
         - { role: username.rolename, x: 42 }

License
-------

BSD

Author Information
------------------

An optional section for the role authors to include contact information, or a website (HTML is not allowed).
