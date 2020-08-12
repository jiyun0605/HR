import json
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
from django.contrib.auth.models import User
from .serializers import UserSerializer

@api_view(["GET"])
@csrf_exempt
@permission_classes([permissions.AllowAny, ])
def profile_view(request, user_id):
    user_profile = User.objects.all(id=user_id)
    serializer = UserSerializer(user_profile, many=True)
    return JsonResponse({'posts': serializer.data}, safe=False,
                        status=status.HTTP_200_OK)

@api_view(["PUT"])
@csrf_exempt
@permission_classes([permissions.AllowAny, ])
def profile_update(request, user_id):

    permission_func(request)

    payload = json.loads(request.body)
    print(payload)
    try:
        user_profile = User.objects.get(id=user_id)
        user_profile.first_name = payload['first_name'],
        user_profile.username = payload['username'],
        user_profile.email = payload['email'],
        user_profile.password = payload['password'],
        user_profile.is_active = False
        serializer = UserSerializer(user_profile)
        return JsonResponse({'user': serializer.data}, safe=False,
            status=status.HTTP_200_OK)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something terrible went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


def permission_func(request):
    if not request.user.username.is_authenticated:
        return JsonResponse({'error': 'Failed authentication'}, safe=False, status=status.HTTP_401_UNAUTHORIZED)