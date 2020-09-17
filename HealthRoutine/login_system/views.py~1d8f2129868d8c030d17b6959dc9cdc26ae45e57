from django.core.exceptions import ObjectDoesNotExist
from django.core.mail import EmailMessage
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny,IsAuthenticated
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from .models import User
from django.http import JsonResponse
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_text
from six import text_type
from django.contrib import messages
from django.contrib.sites.shortcuts import get_current_site
import json
import bcrypt
import jwt
from django.conf import settings
from django.contrib.auth import login,logout,authenticate

@api_view(["GET"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def sign_out(request):
    try:
        logout(request)
        return JsonResponse({'success': 'success_code'}, safe=False, status=status.HTTP_201_CREATED)
    except Exception as e:
        return JsonResponse({'error': str(e)}, safe=False,
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

def send_mail(request, pk):
    current_site = get_current_site(request)
    pk = force_text(urlsafe_base64_decode(pk))
    user = User.objects.get(id=pk)
    token = AccountActivationTokenGenerator()
    token = token.make_token(user)
    content = 'HR 인증 주소.\n\n{}/user/{}/verify/{}/'.format(current_site.domain, urlsafe_base64_encode(force_bytes(user.pk)), token)
    email = EmailMessage('HR 인증', content, to=[user.email])
    EmailMessage()
    email.send()
    return JsonResponse({'success': '성공!'})


@api_view(["POST"])
@csrf_exempt
@permission_classes([AllowAny])
def sign_up(request):
    payload = json.loads(request.body)
    try:
        user = User.objects.create(
            username=payload["username"],
            name=payload["name"],
            email=payload["email"],
            password=bcrypt.hashpw(payload["password"].encode("UTF-8"),
                                   bcrypt.gensalt()).decode("UTF-8")
        )
        pk = urlsafe_base64_encode(force_bytes(user.id))
        send_mail(request._request, pk)
        return JsonResponse({'success': user.id}, safe=False, status=status.HTTP_201_CREATED)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return JsonResponse({'error': str(e)}, safe=False,
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(["POST"])
@csrf_exempt
@permission_classes([AllowAny])
def sign_in(request):
    payload = json.loads(request.body)
    try:
        user=User.objects.get(username = payload["username"])
        if user is not None:
            login(request,user)
            return JsonResponse( {'success':user.id}, safe=False,
                                status=status.HTTP_200_OK)
        return JsonResponse({'error': 'wrong input'}, safe=False,
                            status=status.HTTP_401_UNAUTHORIZED)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False,
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    except KeyError as e:
        return JsonResponse({'error': str(e)}, safe=False,
                            status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return JsonResponse({'error': str(e)}, safe=False,
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)



class AccountActivationTokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return (text_type(user.pk)) + text_type(timestamp)


@api_view(["GET"])
@csrf_exempt
@permission_classes([AllowAny])
def verify(request, pk, token, mail=None):
    uid = force_text(urlsafe_base64_decode(pk))
    try:
        user = User.objects.get(id=uid)
        is_valid = AccountActivationTokenGenerator().check_token(user, token)
        if is_valid and not user.is_valid:
            user.is_valid = True
            user.save()
        else:
            return JsonResponse({'error': 'wrong access'}, safe=False,
                                status=status.HTTP_400_BAD_REQUEST)
        if mail is not None:
            mail = force_text(urlsafe_base64_decode(mail))
            user.email = mail
            user.save()
        return JsonResponse({'success': user.id}, safe=False, status=status.HTTP_200_OK)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False,
                            status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return JsonResponse({'error': str(e)}, safe=False,
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)
# git test