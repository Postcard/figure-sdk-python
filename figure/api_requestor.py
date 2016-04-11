import requests
import json
from urlparse import urljoin

from figure import api_base
from figure import error



def __set_content_type(headers, ctype):
    headers.update({'Content-Type': ctype})

def __set_authorization(headers, token):
    headers.update(
        {'Authorization': 'Bearer {:s}'.format(token)})

def __get(url, headers, data=None):
    return requests.get(url, headers=headers)

def __post(url, headers, data):
    __set_content_type(headers, 'application/json')
    return requests.post(url, data=json.dumps(data), headers=headers)

def __put(url, headers, data=None):
    __set_content_type(headers, 'application/json')
    return requests.put(url, data=json.dumps(data), headers=headers)

def __patch(url, headers, data=None):
    __set_content_type(headers, 'application/json')
    return requests.patch(url, data=json.dumps(data), headers=headers)

def __head(url, headers, data=None, stream=None):
    return requests.head(url, headers=headers)

def _format_filters(filters):
    query_elements = []
    for (k, v) in filters.iteritems():
        query_elements.append("%s=%s" % (k, v))
    if query_elements:
        return '?{0}'.format('&'.join(query_elements))

def _handle_api_error(rbody, rcode):

    if rcode == 401:
        raise error.AuthenticationError()

    if rcode == 404:
        raise error.PortraitDoesNotExist()

    if rcode == 429:
        raise error.RateLimitError()

    if rcode == 500:
        raise error.APIError("Internal server error")


def _interpret_response(rbody, rcode):
    try:
        resp = json.loads(rbody)
    except Exception:
        raise error.APIError(
            "Invalid response body from API: %s "
            "(HTTP response code was %d)" % (rbody, rcode))
    if not (200 <= rcode < 300):
        _handle_api_error(rbody, rcode)
    return resp


def request(method, url, data=None, filters=None, headers=None):

    headers = headers or {}

    METHODS = {
        'get': __get,
        'post': __post,
        'put': __put,
        'head': __head,
        'patch': __patch
    }
    request_method = METHODS[method.lower()]

    url = urljoin(api_base, url)

    if filters:
        params = _format_filters(filters)
        url = urljoin(url, params)

    from figure import token

    if token:
        __set_authorization(headers, token)

    response = request_method(url, headers, data)
    return _interpret_response(response.text, response.status_code)




