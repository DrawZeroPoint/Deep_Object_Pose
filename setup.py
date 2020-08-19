## ! DO NOT MANUALLY INVOKE THIS setup.py, USE CATKIN INSTEAD

# setuptools is not recommended since it generates files into your src folder
# https://wiki.ros.org/rospy_tutorials/Tutorials/Makefile
from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup

# fetch values from package.xml
setup_args = generate_distutils_setup(
    packages=['dope'],
    package_dir={'': 'src'})

setup(**setup_args)
