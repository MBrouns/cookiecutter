import os

from setuptools import setup, find_packages

base_packages = []
dev_packages = ['pytest']

{%- if cookiecutter.cli %}
base_packages.append("click")
{%- endif %}


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name='{{ cookiecutter.project_name }}',
    packages=find_packages(where='src'),
    package_dir={"": "src"},
    install_requires=base_packages,
    extras_require={
      'dev': dev_packages
    },
    {%- if cookiecutter.cli %}
    entry_points={
        'console_scripts':[
            '{{ cookiecutter.project_slug }} = {{ cookiecutter.project_name }}.command:main',
        ]
    },
    {%- endif %}
    description='{{ cookiecutter.description }}',
    author='{{ cookiecutter.full_name }}',
    long_description=read('readme.md'),
    long_description_content_type='text/markdown',
)
