
from setuptools import setup


setup(name='pywebperf',
      version='0.1',
      description='A tool for checking performance of web frameworks',
      keywords='performance, web framework, ',
      url='https://github.com/edilio/PyWebPerf',
      author='Edilio',
      author_email='edilio@degconnect.com',
      license='MIT',
      packages=["pywebperf", ],
      install_requires=[
      ],
      zip_safe=False,
      scripts=['bin/bench'])