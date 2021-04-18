from setuptools import setup

setup(
    name=dw_profiler,
    version=0.1.0,
    description="Tool to profile data warehouses",
    author="Guillermo Sanchez Dionis",
    author_email="gsdionis@gmail.com",
    url="https://github.com/guillesd/dw-profiler",
    install_requires=[
        'google-cloud-core>=1.3.0,<2',
        'google-cloud-bigquery>=1.25.0,<3',
        'google-api-core>=1.16.0,<2',
        'googleapis-common-protos>=1.6.0,<2'
    ],
    python_requires=">=3.7.0",
)