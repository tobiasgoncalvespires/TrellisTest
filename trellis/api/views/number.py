from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.request import Request
from trellis.api.util import http_util, num_to_english_util


class NumberView(viewsets.ViewSet):

    def num_to_english(self, request: Request) -> HttpResponse:
        try:
            number = self.get_number_param(request)
            result = num_to_english_util.to_english(number)

            return http_util.ok(result)
        except Exception as e:
            return http_util.handle_exception(e)

    def get_number_param(self, request: Request):
        number = http_util.get_query_param(request, 'number')
        if number is None:
            number = request.data['number']

        return int(number)
