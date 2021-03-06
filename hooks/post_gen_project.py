#!/usr/bin/env python
import os
import shutil

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_file(filepath):
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))


if __name__ == '__main__':
    if '{{cookiecutter.chef_template}}' != 'Sushi Chef':
        remove_file('sushichef.py')
        remove_file('examples{}{}'.format(os.path.sep, 'openstax_sushichef.py'))
        remove_file('examples{}{}'.format(os.path.sep, 'wikipedia_sushichef.py'))

    if '{{cookiecutter.chef_template}}' != 'Sous Chef':
        remove_file('souschef.py')
        remove_file('Quickstart.ipynb')
        remove_file('examples{}{}'.format(os.path.sep, 'openstax_souschef.py'))
        remove_file('examples{}{}'.format(os.path.sep, 'wikipedia_souschef.py'))
        shutil.rmtree('examples{}templates'.format(os.path.sep))
        remove_file('examples{}{}'.format(os.path.sep, 'Sample Channel.zip'))

    print("DONE: Project created at {}".format(PROJECT_DIRECTORY))
