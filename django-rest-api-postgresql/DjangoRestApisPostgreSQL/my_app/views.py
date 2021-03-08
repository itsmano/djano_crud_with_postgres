import logging

from django.http.response import JsonResponse
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import JSONParser
from my_app.models import User
from my_app.serializers import UserSerializer
from django.views.decorators.cache import cache_page

# Get an instance of a logger
logger = logging.getLogger("user_view")


# Hands on for Django basic CRUD with postgres as DB

# @cache_page(60 * 5)
@api_view(['GET', 'POST', 'DELETE', 'PUT'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def user_list(request):
    if request.method == 'GET':
        print("inside the GET method")
        print(request.auth)
        users = User.objects.all()
        username = request.GET.get('username', None)
        if username is not None:
            logger.debug("*** User Object is not None **")
            logger.debug("The value of user name is  {}".format(username))
            users = users.filter(username=username)

        user_serializer = UserSerializer(users, many=True)
        return JsonResponse(user_serializer.data, safe=False)
        # 'safe=False' for objects serialization

    elif request.method == 'POST':
        user_data = JSONParser().parse(request)
        user_serializer = UserSerializer(data=user_data)
        if user_serializer.is_valid():
            user_serializer.save()
            return JsonResponse(user_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        username = request.GET.get('username', None)
        if username is not None:
            user = User.objects.filter(username=username)
            user.delete()
            return JsonResponse({'message': 'username {} deleted successfully'.format(username)})
        else:
            count = User.objects.all().delete()
            return JsonResponse({'message': '{} Tutorials were deleted successfully!'.format(count[0])},
                                status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        user_data = JSONParser().parse(request)
        username = user_data.get("username")
        print("******* username {} ******* \n".format(username))
        if username is not None:
            user = User.objects.filter(username=username)
            user.update(**user_data)
            update_user = User.objects.filter(username=username)
            user_serializer = UserSerializer(update_user, many=True)
            return JsonResponse(user_serializer.data, safe=False)
        else:
            return JsonResponse({'message': 'username must be given to update the records'},
                                status=status.HTTP_204_NO_CONTENT)
