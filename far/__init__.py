from pkg_resources import get_distribution, DistributionNotFound
from .far import Far

try:
    __version__ = get_distribution('far').version
except DistributionNotFound:
    __version__ = '0.0.0'
