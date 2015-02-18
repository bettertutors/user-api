from setuptools import setup

if __name__ == '__main__':
    package_name = 'bettertutors_user_api'
    setup(
        name=package_name,
        version='0.2.12',
        author='Samuel Marks',
        py_modules=[package_name],
        test_suite='tests',
        install_requires=[
            'bottle', 'webtest'
        ],
        dependency_links=['https://github.com/bettertutors/sql-models/tarball/master#egg=sql-models']
    )
