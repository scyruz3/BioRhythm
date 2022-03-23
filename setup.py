from setuptools import setup

setup(
    name="biorhythm",
    packages=["biorhythm"],
    include_package_data=True,
    install_requires=[
        "flask[async]",
        "flask_pymongo",
        "python-dotenv",
        "pymongo[srv]",
        "flask_wtf",
        "email_validator",
        "flask-bootstrap",
        "flask-datepicker",
        "mongoengine",
        "Pillow"
    ],
)
