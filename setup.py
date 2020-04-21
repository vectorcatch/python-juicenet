from setuptools import find_packages, setup

setup(name='python-juicenet',
      version='1.0.1',
      description='Read and control Juicenet/Juicepoint/Juicebox based EVSE devices',
      url='http://github.com/jesserockz/python-juicenet',
      author='@jesserockz',
      license='MIT',
      install_requires=[
            'aiohttp',
            'asyncio'
      ],
      packages=find_packages(exclude=["dist"]),
      zip_safe=True)
