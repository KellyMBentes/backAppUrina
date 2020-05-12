from json import JSONDecodeError

from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from drf_yasg.utils import swagger_auto_schema
import requests


@swagger_auto_schema(method='get',
                     responses={
                         '200': "OK",
                         '400': 'Bad Request',
                         '401': 'Unauthorized',
                         '404': 'Not Found',
                         '405': 'Method Not Allowed',
                     })
@api_view(['GET', ])
def read_news(request):
    data = {}
    if request.method == 'GET':
        url = (
            'https://newsapi.org/v2/top-headlines?q=saúde&''country=br&''apiKey=dccfb437209844f7b79b0ddf32bf4f95')
        response = requests.get(url)
        try:
            content = response.json()
            if content["status"] == "error":
                return Response(content, status=status.HTTP_400_BAD_REQUEST)

            return Response(content)

        except JSONDecodeError:
            data['error'] = "File or directory not found."
            return Response(data=data, status=status.HTTP_404_NOT_FOUND)



