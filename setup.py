from setuptools import setup

if __name__ == '__main__':
    package_name = 'bettertutors_user_api'
    setup(
        name=package_name,
        version='0.2.6',
        author='Samuel Marks',
        py_modules=[package_name],
        test_suite='tests',
        install_requires=[
            'bottle', 'webtest', 'bettertutors_sql_models'
        ],
        dependency_links=[
            'git+https://github.com/bettertutors/sql-models#egg=bettertutors_sql_models'
        ]
    )
