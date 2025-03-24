import platform
import sys

def test_os_is_linux():
    """Checks if the operating system is Linux."""
    assert platform.system() == "Linux", "This test suite is designed to run on Linux."

def test_python_version():
    """Checks if the Python version is 3.10 or 3.11."""
    major, minor = sys.version_info[:2]
    expected_versions = [(3, 10), (3, 11)]
    assert (major, minor) in expected_versions, 
    f"Python version {major}.{minor} is not supported. Supported versions are 3.10 and 3.11."
