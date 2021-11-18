from setuptools import setup, find_packages

setup(name="airflow-iguazio",
      version="1.0",
      packages = find_packages(),
      install_requires=[
          'apache-airflow',
          'mlrun'
      ])