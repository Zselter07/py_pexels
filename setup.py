import setuptools, os

readme_path = 'README.md'

if os.path.exists(readme_path):
    with open(readme_path, 'r') as f:
        long_description = f.read()
else:
    long_description = 'pexels'

setuptools.setup(
    name='pexels',
    version='0.0.5',
    author='Pentek Zsolt',
    description='pexels',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/Zselter07/py_pexels',
    packages=setuptools.find_packages(),
    install_requires=["selenium_firefox", "randomua"],
    classifiers=[
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.4',
)