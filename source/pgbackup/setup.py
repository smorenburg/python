from setuptools import setup, find_packages

with open('README.rst', encoding='UTF-8') as f:
    readme = f.read()

setup(
    name='pgbackup',
    version='0.1.0',
    description='Database backups locally or to AWS S3.',
    long_description=readme,
    author='Robin Smorenburg',
    author_email='robin@smorenburg.io',
    install_requires=[],
    packages=find_packages('source'),
    package_dir={'': 'source'}
)
