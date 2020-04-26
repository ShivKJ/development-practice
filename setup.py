from setuptools import setup

dependencies = list(map(str.strip, open('requirement.txt').readlines()))

setup(
    name='development',
    version='0.1',
    packages=['development', 'development.math',
              'development.using_resources'],
    package_data={'development': ['data/info.json']},
    url='https://github.com/ShivKJ/development-practice',
    license='MIT License',
    install_requires=dependencies,
    author='Shiv',
    author_email='shivkj001@gmail.com',
    description='development-practice'
)
