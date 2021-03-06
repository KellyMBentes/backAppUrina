import pyrebase
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import ImageSerializer
from .models import Image

image_response = openapi.Response('OK', ImageSerializer)

config = {
    "apiKey": "AIzaSyBm9bfdB6TKD9fxj9PZ4IreIZvbU-fbKhA",
    "authDomain": "urinapp-a4beb.firebaseapp.com",
    "databaseURL": "https://urinapp-a4beb.firebaseio.com",
    "storageBucket": "urinapp-a4beb.appspot.com",
    "serviceAccount": "urinapp-a4beb-firebase-adminsdk-zsqee-7e25f33ae2.json"
}

firebase = pyrebase.initialize_app(config)

# Get a reference to the auth service
auth = firebase.auth()

# Log the user in
user = auth.sign_in_with_email_and_password("conectaservicos9@gmail.com", "tridentcanela2019")

# Get a reference to the database service
db = firebase.database()


@swagger_auto_schema(method='post', request_body=ImageSerializer,
    responses={
        '201': 'Created',
        '400': 'Bad Request',
        '401': 'Unauthorized',
    })
@api_view(['POST', ])
def create_image(request):
    user = request.user

    if request.method == 'POST':
        db = firebase.database()
        data = {"user": user.id, "image": request.data["image"]}
        img = db.child("image").push(data)
        image = Image(user=user)
        data = {}
        data['firebaseKey'] = img['name']
        serializer = ImageSerializer(image, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        data['error'] = serializer.errors
        return Response(data=data, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(method='get',
    responses={
        '200': image_response,
        '400': 'Bad Request',
        '401': 'Unauthorized',
        '404': 'Not Found',
    })
@api_view(['GET', ])
def read_image(request, id):
    data = {}
    try:
        image = Image.objects.get(id=id)
        db = firebase.database()
        img = db.child("image").child(image.firebaseKey).get()
        data = img.val()
    except Image.DoesNotExist:
        data['error'] = "Object Not Found."
        return Response(data=data, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        return Response(data, status=status.HTTP_200_OK)


@swagger_auto_schema(method='put', request_body=ImageSerializer,
    responses={
        '202': 'Accepted',
        '400': 'Bad Request',
        '401': 'Unauthorized',
        '404': 'Not Found',
    })
@swagger_auto_schema(method='delete', request_body=ImageSerializer,
    responses={
        '200': 'OK',
        '401': 'Unauthorized',
        '404': 'Not Found',
    })
@api_view(['PUT', 'DELETE'])
def update_delete_image(request, id):
    data = {}
    try:
        image = Image.objects.get(id=id)
    except Image.DoesNotExist:
        data['error'] = 'Object Not Found.'
        return Response(data=data, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        db = firebase.database()
        db.child("image").child(image.firebaseKey).update({"image": request.data["image"]})
        data = {}
        data['response'] = 'Update successful'
        return Response(data=data, status=status.HTTP_202_ACCEPTED)

    elif request.method == 'DELETE':
        db = firebase.database()
        db.child("image").child(image.firebaseKey).remove()
        operation = image.delete()
        data = {}
        if operation:
            data["response"] = "Delete successful"
            return Response(data=data, status=status.HTTP_200_OK)
        else:
            data["error"] = "Delete failed"
            return Response(data=data, status=status.HTTP_400_BAD_REQUEST)