from setuptools import setup, find_packages


setup(
    name="wcc-python-sdk-notification",
    version="0.3.7",
    author="aiden_lu",
    author_email="aiden_lu@wochacha.com",
    description="Django message notification package",
    packages=["notification"],
    zip_safe=False,
    include_package_data=True,
    install_requires=["channels", "channels-redis",],
    platforms="x86_64 Linux and MacOS X",
    classifiers=[
        "Development Status :: 1 - Pre-Production",
        "Intended Audience :: Developers",
        "Environment :: Web Environment",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: C",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
)
