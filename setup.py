from setuptools import setup, find_packages

setup(name = 'django_extjs4_examples',
      description = 'Example apps for django_extjs4.',
      version = '1.0',
      url = 'https://github.com/espenak/django_extjs4_examples',
      license = 'BSD',
      author = 'Espen Angell Kristiansen',
      packages=find_packages(exclude=['ez_setup']),
      install_requires = ['setuptools', 'Django']
)
