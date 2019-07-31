import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(os.environ["MOLECULE_INVENTORY_FILE"]).get_hosts("all")


def test_ssh2_extension(host):
    output = host.check_output("/usr/local/php/bin/php -m | grep ssh2")

    assert output == "ssh2"


def test_ssh2_so(host):
    extension_dir = host.check_output("/usr/local/php/bin/php-config --extension-dir")

    so = host.file(os.path.join(extension_dir.strip(), "ssh2.so"))

    assert so.exists


def test_ssh2_config_file(host):
    cf = host.file("/usr/local/php/etc/php.d/ssh2.ini")

    assert cf.exists
