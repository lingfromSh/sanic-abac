from sanic.response import HTTPResponse


class AllowHTTPResponse(HTTPResponse):
    pass


class DeniedHTTPResponse(HTTPResponse):
    pass


async def authenticate(request):
    """
    Return the request whether is allowed to execute or not.

    request.resource -> rules -> constraints -> Allowed/Denied.

    :param request: Request
    :return:
    """
    print(request)
    pass
