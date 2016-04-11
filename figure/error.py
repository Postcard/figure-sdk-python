

class FigureError(Exception):

    def __init__(self, message=None):
        super(FigureError, self).__init__(message)
        self._message = message

    def __unicode__(self):
        return self._message

    def __str__(self):
        return unicode(self).encode('utf-8')


class APIError(FigureError):
    pass


class AuthenticationError(FigureError):

    def __init__(self):
        message = "Your token is invalid or you are not authorized to access this resource"
        super(AuthenticationError, self).__init__(message)


class PortraitDoesNotExist(FigureError):

    def __init__(self):
        message = "This portrait does not exists"
        super(PortraitDoesNotExist, self).__init__(message)


class RateLimitError(FigureError):

    def __init__(self):
        message = "You have exceeded your quota for today"
        super(RateLimitError, self).__init__(message)
