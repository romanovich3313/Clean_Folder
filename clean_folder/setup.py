from setuptools import setup, find_packages

setup(
    name='clean_folder',
    version='1',
    description='You can clean your computer with this code',
    url='https://github.com/romanovich3313/Clean_Folder',
    author='Roman Palij',
    author_email='roman.romanovich.pl@gmail.com',
    license='MIT',
    packages=find_packages(),
    entry_points={'console_scripts': ['clean_folder = clean_folder.clean_folder.clean:main']})
