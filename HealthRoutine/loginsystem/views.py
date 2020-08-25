import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes

@api_view(["POST"])
@csrf_exempt
@permission_classes([permissions.AllowAny, ])
def signIn_view(request):
    payload = json.loads(request.body)
    try:
<<<<<<< HEAD
        userid = payload['userid']
=======
        userid = payload['id']
>>>>>>> 0321428de1bf8e11ac141d2a24a3ddb0758a5f01
        password = payload['password']
        user = authenticate(username=userid, password=password)
        if user is not None:
            login(request, user)
            return JsonResponse({'response_code': 'success'}, safe=False, status=status.HTTP_200_OK)
        else:
            return JsonResponse({'error': 'Wrong input'}, safe=False,
                                status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something terrible went wrong'}, safe=False,
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(["GET"])
@csrf_exempt
@permission_classes([permissions.AllowAny, ])
def logout_view(request):
    try:
        logout(request)
        return JsonResponse({'response_code': 'success'}, safe=False, status=status.HTTP_200_OK)
    except Exception:
        return JsonResponse({'error': 'Something terrible went wrong'}, safe=False,
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(["POST"])
@csrf_exempt
@permission_classes([permissions.AllowAny, ])
def signUp_view(request):
    payload = json.loads(request.body)
    try:
        user = User.objects.create_user(
            # first_name=request.POST.get('name'),
            # username=request.POST.get('id'),
            # email=request.POST.get('email'),
            # password=request.POST.get('password'),
            # is_active=False
            username=payload['id'],
            first_name=payload['name'],
            email=payload['email'],
            password=payload['password'],
            is_active=False
        )
        pk = urlsafe_base64_encode(force_bytes(user.pk))
        return JsonResponse({'pk': pk}, safe=False, status=status.HTTP_200_OK)
    except Exception:
        return JsonResponse({'error': 'Something terrible went wrong'}, safe=False,
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)