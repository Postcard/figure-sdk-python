
from figure import api_requestor

class Portrait(object):

    @classmethod
    def get_all_public(cls):
        return api_requestor.request("GET", "/portraits/public")

    @classmethod
    def get(cls, code):
        assert code is not None
        url = "/portraits/%s" % code
        return api_requestor.request("GET", url)

    @classmethod
    def edit(cls, code, data):
        assert code is not None
        url = "/portraits/%s/" % code
        return api_requestor.request("PUT", url, data)
