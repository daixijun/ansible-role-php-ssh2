daixijun.php-ssh2
=========

[![Build Status](https://travis-ci.org/daixijun/ansible-role-php-ssh2.svg?branch=master)](https://travis-ci.org/daixijun/ansible-role-php-ssh2)

Ansible 安装php ssh2扩展

Requirements
------------

* RHEL/Centos 7
* Ansible 2.7 +

Role Variables
--------------

```yaml
php_ssh2_version: 4.3.0
php_ssh2_download_url: http://pecl.php.net/get/ssh2-{{ php_ssh2_version }}.tgz

```

Dependencies
------------

[daixijun.php](https://galaxy.ansible.com/daixijun/php)

Example Playbook
----------------

```yaml
- hosts: servers
  roles:
    - role: daixijun.php
    - role: daixijun.php-ssh2
```

License
-------

BSD

Author Information
------------------

Xijun Dai <daixijun1990@gmail.com>
