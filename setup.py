from setuptools import setup

__version__ = '0.2.5'

if __name__ == '__main__':  # Version might be imported from setup... if that's possible
    package_name = 'bettertutors_user_api'
    setup(name=package_name, version=__version__,
          author='Samuel Marks', license='MIT', py_modules=[package_name],
          test_suite='tests')
