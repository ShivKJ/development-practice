from setuptools import setup

setup(
    name='development',
    version='0.1',
    packages=['development', 'development.math',
              'development.using_resources'],
    package_data={'development': ['data/info.json']},
    url='https://github.com/ShivKJ/development-practice',
    license='',
    author='Shiv',
    author_email='shivkj001@gmail.com',
    description='development-practice'
)
