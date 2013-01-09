#
# Copyright (C) 2013 KKBOX Technologies Ltd.
# Copyright (C) 2013 Gasol Wu <gasol.wu@gmail.com>
#
# This software is licensed as described in the file COPYING, which
# you should have received as part of this distribution.

from setuptools import find_packages, setup

PACKAGE = 'TracAttachmentNotifyPlugin'
VERSION = 'UNRELEASE'

try:
    import trac
    if trac.__version__ < '0.11.6':
        print "%s %s requires Trac >= 0.11.6" % (PACKAGE, VERSION)
        sys.exit(1)
except ImportError:
    pass

setup(
    name = PACKAGE,
    version = VERSION,
    author = 'Gasol Wu',
    author_email = 'gasolwu@kkbox.com',
    license = 'BSD',
    packages = find_packages(),
    entry_points = {
        'trac.plugins': [
            'attachment.notify = attachment.notify',
        ],
    },
)

