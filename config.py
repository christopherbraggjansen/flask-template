# See the configure documentation for more about
# this library.
# http://configure.readthedocs.io/en/latest/#
from configure import Configuration

# The configure library provides a pretty interface to our
# configuration data. This module doesn't do anything other
# than
config = Configuration.from_file('config.yaml').configure()

# This adds the application's base directory to the
# configuration object, so that the rest of the application
# can reference it.
import os
config.sys.base_dir = os.path.abspath(os.path.dirname(__file__))
