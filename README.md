# ansible-vm-provision [![Build Status](https://travis-ci.com/pdcmb/ansible-vm-provision.svg?branch=master)](https://travis-ci.com/pdcmb/ansible-vm-provision)
Basic ansible playbook that creates azure virtual machines and installs docker on them

## Usage
First add `users` variable and add user for every virtual machine you want to create. The best way to do it is by adding a file with list of user inside ` group_vars `.

Sample file look like this:

    users:
      - { id: 1, username: "azureuser", password: "Pa$$word12345" }
      - { id: 2, username: "azureuser", password: "Pa$$word67890" } 
      ...

Upload files to azure and run
 
    ansible-playbook main.yml
 
 from cloud shell
