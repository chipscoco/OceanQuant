"""
OceanQuant -  A big quantification system to help you make big money.
"""

import pkgutil
import sys
import warnings


__all__ = [
    '__version__', 'version_info',
]


# OceanMonkey's version
__version__ = (pkgutil.get_data(__package__, "VERSION") or b"").decode("ascii").strip()
version_info = tuple(int(v) if v.isdigit() else v for v in __version__.split('.'))


# Check minimum required Python version
if sys.version_info < (3, 5):
    print("Scrapy %s requires Python 3.5+" % __version__)
    sys.exit(1)


del pkgutil
del sys
del warnings
