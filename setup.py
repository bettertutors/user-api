from setuptools import setup
from user_api import __version__

if __name__ == '__main__':
    package_name = 'bettertutors_user_api'
    setup(name=package_name, version=__version__,
          author='Samuel Marks', license='MIT', py_modules=[package_name],
          test_suite='tests')
