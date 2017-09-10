from setuptools import find_packages
from setuptools import setup

pip_requirements = []
for line in open('requirements.txt').readlines():
    li = line.strip()
    if not li.startswith('#'):
        pip_requirements.append(line)

setup(
    name='nickficano',
    author='Nick Ficano',
    author_email='nficano@gmail.com',
    version='0.1.0',
    packages=find_packages(exclude=['tests*']),
    url='https://nickficano.com',
    license='Apache License 2.0',
    description='My landing page',
    zip_safe=False,
    install_requires=pip_requirements,
)
