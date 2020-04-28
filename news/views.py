from rest_framework.response import Response
import requests
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from rest_framework.decorators import api_view


# Create your views here.
@swagger_auto_schema(method='get',
                     responses={
                         '200': "OK",
                         '400': 'Bad Request',
                         '401': 'Unauthorized',
                         '404': 'Not Found',
                     })
@api_view(['GET', ])
def read_news(request):
    if request.method == 'GET':
        url = (
            'https://newsapi.org/v2/top-headlines?q=saúde&''country=br&''apiKey=dccfb437209844f7b79b0ddf32bf4f95')
        response = requests.get(url)
        content = response.json()
        # content[0]["content"]
        return Response(content)
