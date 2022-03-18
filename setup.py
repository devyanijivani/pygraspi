"""PyGraspi - Python implementation of Graspi

"""

from setuptools import setup, find_packages


def setup_args():
    """Get the setup arguments not configured in setup.cfg"""
    return dict(
        packages=find_packages(),
        data_files=["setup.cfg"],
        version='0.1',
    )


setup(**setup_args())
