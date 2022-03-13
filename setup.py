from setuptools import setup

setup(
    name="biorhythm",
    packages=["biorhythm"],
    include_package_data=True,
    install_requires=["flask[async]", "Flask-PyMongo", "pymongo[srv]"],
)
