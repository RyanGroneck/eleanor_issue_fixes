"""Initialize the public eleanor package namespace.

This module records the package directory path and re-exports the primary
classes and helpers that users are expected to import from `eleanor` directly.
It pulls in version metadata, target discovery, target data extraction,
postcard access, crossmatching, FFI utilities, and sector update tools.
AI generated summary.
"""
import os
PACKAGEDIR = os.path.abspath(os.path.dirname(__file__))

from .version import __version__
from .eleanor import *
from .targetdata import *
from .postcard import *
from .source import *
from .crossmatch import *
from .ffi import *
from .update import *
