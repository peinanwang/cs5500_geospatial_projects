import pytest
import os
import sys

# Modify the path to import the module
sys.path.append('/Users/glenn_hyh/Desktop/CS5500/cs5500_geospatial_projects')
from view import app

"""Initialize the testing environment

Creates an app for testing that has the configuration flag ``TESTING`` set to
``True``.

"""

# The following function is derived from an example in the Flask documentation
# found at the following URL: http://flask.pocoo.org/docs/1.0/testing/. The
# Flask license statement has been included below as attribution.
#
# Copyright (c) 2010 by the Pallets team.
#
# Some rights reserved.
#
# Redistribution and use in source and binary forms of the software as well as
# documentation, with or without modification, are permitted provided that the
# following conditions are met:
#
#     * Redistributions of source code must retain the above copyright notice,
#       this list of conditions and the following disclaimer.
#     * Redistributions in binary form must reproduce the above copyright
#       notice, this list of conditions and the following disclaimer in the
#       documentation and/or other materials provided with the distribution.
#     * Neither the name of the copyright holder nor the names of its
#       contributors may be used to endorse or promote products derived from
#       this software without specific prior written permission.


@pytest.fixture
def client():
    """Configures the app for testing

    Sets app config variable ``TESTING`` to ``True``

    :return: App for testing
    """

    app.config['TESTING'] = True
    client = app.test_client()

    yield client