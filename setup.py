import sys

extra = {}
if sys.version_info >= (3, 0):
    extra.update(use_2to3=True)

try:
    from setuptools import setup, find_packages, Command
except ImportError:
    from distutils.core import setup, find_packages, Command

author = "Marc Abramowitz"
email = "marc@marc-abramowitz.com"
version = "0.0.1-dev"
desc = """Provides a common interface to various serialization methods"""
long_desc = open('README.markdown').read()

class PyTest(Command):
    user_options = []
    def initialize_options(self):
        pass
    def finalize_options(self):
        pass
    def run(self):
        import sys,subprocess
        errno = subprocess.call([sys.executable, 'runtests.py'])
        raise SystemExit(errno)

setup(name='anyserializer',
      version=version,
      description=desc,
      long_description=long_desc,
      data_files=[('', ['README.markdown'])],
      classifiers=[
            'License :: OSI Approved :: BSD License',
            'Intended Audience :: Developers',
            'Programming Language :: Python',
            'Programming Language :: Python :: 2',
            'Programming Language :: Python :: 2.4',
            'Programming Language :: Python :: 2.5',
            'Programming Language :: Python :: 2.6',
            'Programming Language :: Python :: 2.7',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.1',
          ],
      keywords='json',
      author=author,
      author_email=email,
      url='http://github.com/msabramo/anyserializer',
      license='BSD',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      zip_safe=False,
      platforms=["any"],
      cmdclass={'test': PyTest},
      # test_suite = 'nose.collector',
      **extra
)
