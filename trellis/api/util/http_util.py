from rest_framework.request import Request
from rest_framework.response import Response
from trellis.api.exceptions.exceptions import BusinessException, InternalErrorException


def get_query_param(request: Request, name: str):
    if name in request.query_params:
        return request.query_params[name]

    return None


def handle_exception(e: Exception):
    if isinstance(e, BusinessException):
        http_code = 400
    elif isinstance(e, InternalErrorException):
        http_code = 500
    else:
        http_code = 500

    return error(str(e), http_code)


def ok(num_in_english: str):
    return build_response('ok', 200, num_in_english)


def error(msg_error: str, http_code: int):
    return build_response(msg_error, http_code, None)


def build_response(status: str, status_code: int, num_in_english: str):
    json_body = {
        'status': status,
        'num_in_english': num_in_english
    }
    return Response(json_body, status=status_code, content_type='json/application')

