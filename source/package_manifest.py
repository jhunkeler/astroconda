from __future__ import print_function

import json
import os
from collections import OrderedDict
try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen

from pprint import pprint

ARCHITECTURE = [ 'linux-64', 'osx-64']
METAPACKAGES = [('stsci', '3.0.0'),
                ('stsci-data-analysis', '2.0.2'),
                ('stsci-hst', '3.0.0'),
                ('iraf-all', '1.0'),
                ('pyraf-all', '1.0')]

REPODATA_URL='http://ssb.stsci.edu/astroconda/{arch}/repodata.json'
MESSAGE = """
Packaging reference key:

::

    [package]-[version]-[glob]_[build_number]
    ^Name     ^Version  ^      ^Conda package revision
                        |
                        npXXpyYY
                          ^   ^
                          |   |
                          |   Compiled for Python version
                          |
                          Compiled for NumPY version


"""

def get_repodata(architecture):
    """ Retrieves repository data but strips the info key (there's never anything there)
    """
    url = REPODATA_URL.format(arch=architecture)
    with urlopen(url) as response:
        data = OrderedDict(json.loads(response.read().decode())['packages'])

    return data

def generate_manifest():
        python_versions = dict(
            py35='3.5'
        )

        with open(os.path.join('source', 'package_manifest.rst'), 'w+') as pfile:
            print('Packages', file=pfile)
            print('========\n\n', file=pfile)
            print('{0}\n\n'.format(MESSAGE), file=pfile)

            repo_data = OrderedDict()
            for arch in ARCHITECTURE:
                repo_data[arch] = get_repodata(arch)

                metapackages = []
                for mpkg, mpkg_version in METAPACKAGES:
                    for key, value in repo_data[arch].items():
                        if mpkg == repo_data[arch][key]['name']:
                            if mpkg_version == repo_data[arch][key]['version']:
                                metapackages.append(('-'.join([value['name'], value['version']]), value['build'], value['depends']))
                                break

                print('{arch} metapackages'.format(arch=arch), file=pfile)
                print('------------------------\n\n', file=pfile)

                #metapackages = sorted(metapackages, key=lambda k: k[0])
                for name, build, dependencies in metapackages:
                    print('- **{name}**\n'.format(name=name), file=pfile)
                    for pkg in dependencies:
                        if pkg.split()[0] == 'python':
                            continue
                        print('    - {:<20s}\n'.format(pkg), file=pfile)

                print('{arch} packages'.format(arch=arch), file=pfile)
                print('------------------------\n\n', file=pfile)

                _packages = sorted(repo_data[arch].values(), key=lambda k: k['name'])
                packages = set(['-'.join([d['name'], d['version']]) for d in _packages])

                for record in sorted(packages):
                    print('- {name}\n'.format(name=record, header='-' * len(record)), file=pfile)


if __name__ == '__main__':
    generate_manifest()
