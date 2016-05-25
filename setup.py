from setuptools import setup, find_packages

setup(name='butterfly',
      version='0.1',
      license='AGPLv3+',
      install_requires=[
          'Flask',
          'Flask-Script',
          'Flask-SeaSurf',
          'Flask-SQLAlchemy',
      ],
      packages=find_packages(),
      entry_points={
          'console_scripts': [
              'butterfly=butterfly.app:main',
          ],
      })
