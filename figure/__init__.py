

__version__ = "0.1.0"

token = None
api_base = 'https://api.figuredevices.com'

# Resources
from figure.resource import (
    Portrait
)

from figure.error import (
    APIError,
    AuthenticationError,
    PortraitDoesNotExist,
    RateLimitError
)




