from setuptools import setup,find_packages

classifiers=[
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Education',
    'Operating System :: Microsoft :: Windows :: Windows 10',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3'
]

setup(
    name='pypattern',
    version='0.0.1',
    description='Simple Python module for printing patterns for characters (Lower case and Upper case), numbers and special characters.',
    long_description=open('README.txt').read()+'\n\n'+open('CHANGELOG.txt').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/fazil2003/pypattern',
    author='Mohamed Fazil',
    author_email='mohamedfazil463@gmail.com',
    license='MIT',
    classifiers=classifiers,
    keywords='fazil, pypattern, pattern, patterns, printing, stars',
    packages=find_packages(),
    install_requires=['']
)
