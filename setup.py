import setuptools


with open('README.md', 'r') as file:
    long_description = file.read()

setuptools.setup(
    name='googlenewspy',
    version='0.0.1',
    author='Fernando Rodrigues',
    author_email='fernandoarrj@gmail.com',
    description='Scraping google news',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/fernandoarrj/googlenewspy',
    packages=setuptools.find_packages(),
        classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
