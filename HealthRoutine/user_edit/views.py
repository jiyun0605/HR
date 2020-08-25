import json

from django.contrib.auth import authenticate
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from django.db.models.query_utils import Q
from .serializers import UserSerializer

@api_view(["GET"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def profile_view(request):
    user_profile = User.objects.filter(username=str(request.user))
    serializer = UserSerializer(user_profile, many=True)
    return JsonResponse({'user': serializer.data}, safe=False,
                        status=status.HTTP_200_OK)

@api_view(["PUT"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def profile_update(request):
    payload = json.loads(request.body)
    try:
        user_profile = User.objects.filter(username=str(request.user))
        user_profile.first_name = payload['first_name'],
        user_profile.username = payload['username'],
        user_profile.email = payload['email'],
        user_profile.password = payload['password'],
        serializer = UserSerializer(user_profile)
        return JsonResponse({'user': serializer.data}, safe=False,
                            status=status.HTTP_200_OK)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something terrible went wrong'}, safe=False,
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(["DELETE"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def profile_delete(request):
    payload = json.loads(request.body)
    try:
        password = payload['password']
        user = authenticate(password=password)
        if user is not None:
            User.is_active=False
            return JsonResponse({'response_code': 'success'}, safe=False, status=status.HTTP_204_NO_CONTENT)
        else:
            return JsonResponse({'error': 'Wrong input'}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something terrible went wrong'}, safe=False,
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)
