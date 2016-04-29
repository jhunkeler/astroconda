#!/usr/bin/env python
from __future__ import print_function

import os
import math
from collections import OrderedDict

try:
    from github3 import login
    from github3 import GitHubError
except ImportError:
    print('github3.py required.')
    print('pip install https+git://github.com/sigmavirus24/github3.py')
    exit(1)

try:
    import pypandoc
except ImportError:
    print('pypandoc required.')
    print('conda install -c https://conda.anaconda.org/janschulz pypandoc')
    exit(1)


header = """
# Release Notes
"""
title = """
## {name}
"""
message = """
### {title}

*{date}*

{body}

"""


def explode_newlines(s):
    """Normalize newlines and double them up for MD->RST conversion.
    """
    tmp = ''
    for line in s.splitlines():
        line = line.replace('\r\n', '\n')
        line = line + '\n\n'
        tmp += line

    return tmp

def transform_headings(s):
    """Trust no one.
    Header levels less than or equal to 3 are up-converted.

    1 = 4
    2 = 4
    3 = 5
    4 = 6
    5 = 6
    6 = 6

    Oh well, sucks right?
    """
    delim = '#'
    headings = OrderedDict(
        h6=delim * 6,
        h5=delim * 5,
        h4=delim * 4,
        h3=delim * 3,
        h2=delim * 2,
        h1=delim * 1
    )
    output = ''

    for line in s.splitlines():
        length = len(line)
        stop = len(headings.keys()) + 1

        if length < stop:
            stop = length

        block = line[:stop]
        depth = 0
        for i, ch in enumerate(block, 1):
            if ch != '#': break
            depth = i

        if depth == 0 or depth > 3:
            output += explode_newlines(line)
            continue

        #print('length={:<10d} stop={:<10d} depth={:<10d} block={:>20s}'.format(length, stop, depth, block))

        current = headings['h'+str(depth)]
        try:
            required = headings['h'+str(math.ceil(depth + depth / depth + 1))]
        except KeyError:
            required = headings['h'+str(len(headings) - 1)]

        if depth > 0 and depth <= 3:
            print("Heading levels 1, 2, and 3 are allocated by this script...")
            print("Offending line: '{0}'".format(line))
            print("Automatically converted to: '{0}'".format(required))
            print("(FIX YOUR RELEASE NOTES)\n\n")

        #print('Transformed "{0}" -> "{1}"'.format(current, required))
        line = line.replace(current, required)
        output += explode_newlines(line)

    return output

def read_token(filename):
    """For the sake of security, paste your github auth token in a file and reference it using this function

    Expected file format (one-liner):
    GITHUB_USER_AUTH_TOKEN_HERE
    """
    with open(filename, 'r') as f:
        # Obtain the first line in the token file
        token = f.readline().rstrip()

    if not token:
        return None

    for i, ch in enumerate(token):
        if not ch.isalnum():
            raise ValueError('Invalid token: Non-alphanumeric character detected (Value: "{0}", ASCII: {1}, Index: {2}) '.format(ch, ord(ch), i))

    return token


def pull_release_notes(tmpfile, outfile):
    with open(tmpfile, 'w+') as mdout:
        # Write header (main title)
        print(header, file=mdout)

        # Sort repositories inline alphabetically, because otherwise its seemingly random order
        for repository in sorted(list(org.repositories()), key=lambda k: k.as_dict()['name']):
            repo = repository.as_dict()
            repo_name = repo['name'].upper()

            # Ignore repositories without release notes
            releases = list(repository.releases())
            if not releases:
                continue

            # Write repository title
            print(title.format(name=repo_name), file=mdout)

            for note in repository.releases():
                # RST is EXTREMELY particular about newlines.
                body = explode_newlines(note.body)
                body = transform_headings(note.body)
                # Write release notes structure
                print(message.format(title=note.name,
                                 date=note.published_at,
                                 body=body), file=mdout)


if __name__ == '__main__':
    owner = 'spacetelescope'
    tmpfile = 'release_notes.md'
    outfile = 'release_notes.rst'

    gh = login(token=read_token('TOKEN'))
    org = gh.organization(owner)

    try:
        pull_release_notes(tmpfile, outfile)
    except GitHubError as e:
        print(e)
        exit(1)

    if os.path.exists(outfile):
        os.unlink(outfile)

    if os.path.exists(tmpfile):
        pypandoc.convert(source=tmpfile,
                         to='rst',
                         outputfile=outfile)
        os.unlink(tmpfile)
