from setuptools import setup, find_packages

setup(
    name='remotecv_kmk',
    version='1.0',
    description='Remotecv Hydra S3 loader',
    author='Kreatif Media Karya',
    author_email='admin.it@kmklabs.com',
    zip_safe=False,
    include_package_data=True,
    packages=find_packages(),
    install_requires=[
        'boto',
    ],
    extras_require={
    },
)
