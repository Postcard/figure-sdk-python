

__version__ = "0.1.0"

token = None
api_base = 'https://api.figuredevices.com'

# Resources
from figure.resource import (
    Photobooth,
    Place,
    Event,
    TicketTemplate,
    Text,
    TextVariable,
    Image,
    ImageVariable,
    Portrait,
    PosterOrder,
    User,
    Auth
)

from figure.error import (
    APIConnectionError,
    BadRequestError,
    AuthenticationError,
    AuthorizationError,
    NotFoundError,
    RateLimitError,
    InternalServerError,
    NotAvailableYetError
)




