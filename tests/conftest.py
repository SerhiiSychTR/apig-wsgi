import pytest


def pytest_collection_modifyitems(items):
    """
    auto marks for unit and integration tests according
    to the following naming conventions:
     unittests: files pattern *_test.py, class pattern "class *Test():"
     integration: files pattern *_it.py, class pattern "class *IT():"
    """
    for item in items:
        path, class_name, method_name = item.nodeid.split("::")

        if "Test" in class_name and "_test" in path:
            item.add_marker(pytest.mark.unit)
        elif "IT" in class_name and "_it" in path:
            item.add_marker(pytest.mark.integration)
