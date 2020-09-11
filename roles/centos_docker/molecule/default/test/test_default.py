# import os
import pytest


# expected installed packages
@pytest.mark.parametrize('package', [
  ('docker'),
])
def test_installed_packages(host, package):
    pkg = host.package(package)
    assert pkg.is_installed


# expected services are running and enabled
@pytest.mark.parametrize('service', [
    ('docker'),
])
def test_running_services(host, service):
    svc = host.service(service)
    assert svc.is_running
    assert svc.is_enabled

