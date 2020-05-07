import os.path

from setuptools import Command, find_packages, setup

INSTALL_REQUIRES = [
    'pysam',
]

DEV_REQUIRES = [
    'pytest',
    'pytest-cov',
    'flake8',
    'mock',
    'pre-commit',
    'isort',
]


class Requirements(Command):
    descripton = 'foobar'
    user_options = [
        ('dev', None, 'Bundles all requirements'),
    ]

    def initialize_options(self):
        self.dev = False

    def finalize_options(self):
        self.dev = True

    def run(self):
        if self.dev:
            path = os.path.join('.', 'requirements.in')
            self.write_requirements(path, INSTALL_REQUIRES + DEV_REQUIRES)
        return

    def write_requirements(self, path, reqs):
        with open(path, 'w') as fh:
            fh.write('\n'.join(reqs) + '\n')


setup(
    name="gdc-sanger-tools",
    author="Kyle Hernandez",
    author_email="kmhernan@uchicago.edu",
    version=0.1,
    description="Utility tool for GDC Sanger Somatic Workflow",
    license="Apache 2.0",
    packages=find_packages(),
    python_requires='>=3.5',
    install_requires=INSTALL_REQUIRES,
    tests_require=DEV_REQUIRES,
    entry_points={
        'console_scripts': ['gdc-sanger-tools=gdc_sanger_tools.__main__:main']
    },
    cmdclass={'capture_requirements': Requirements,},
)
