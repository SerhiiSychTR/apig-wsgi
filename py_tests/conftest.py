import pytest


def pytest_collection_modifyitems(items):
    for item in items:
        nodeid_parts = item.nodeid.split("::")

        # tests written in function style haven't classname
        if len(nodeid_parts) == 2:
            path, method_name = nodeid_parts
            if "_test" in path:
                item.add_marker(pytest.mark.py_unit)
            elif "_it" in path:
                item.add_marker(pytest.mark.py_integration)
        else:
            path, class_name, method_name = nodeid_parts
            if "Test" in class_name and "_test" in path:
                item.add_marker(pytest.mark.py_unit)
            elif "IT" in class_name and "_it" in path:
                item.add_marker(pytest.mark.py_integration)
