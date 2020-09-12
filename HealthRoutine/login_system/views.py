from django.core.exceptions import ObjectDoesNotExist
from django.core.mail import EmailMessage
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from .models import Account
from django.http import JsonResponse, HttpResponse
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_text
from six import text_type
from django.contrib import messages
from django.contrib.sites.shortcuts import get_current_site
import json
import bcrypt
import jwt
from django.conf import settings


@api_view(["POST"])
@csrf_exempt
@permission_classes([AllowAny])
def sign_up(request):
    payload = json.loads(request.body)
    try:
        user = Account.objects.create(
            id=payload["id"],
            name=payload["name"],
            email=payload["email"],
            password=bcrypt.hashpw(payload["password"].encode("UTF-8"),
                                   bcrypt.gensalt()).decode("UTF-8")
        )
        pk = urlsafe_base64_encode(force_bytes(user.id))
        send_mail(request, pk)
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
    id = payload["id"]
    password = payload["password"]
    try:
        if Account.objects.filter(id=payload.id).exists():
            print("test")
            check_user = Account.objects.get(id=payload.id)
            if bcrypt.checkpw(payload.password.encode('UTF-8'), check_user.password.encode('UTF-8')):
                token = jwt.encode({'user': check_user.id}, settings.SECRET_KEY, algorithm='HS256').decode('UTF-8')
                return JsonResponse({'token': token}, safe=False,
                                    status=status.HTTP_200_OK)
            return JsonResponse({'error': 'wrong input'}, safe=False,
                                status=status.HTTP_401_UNAUTHORIZED)
        return JsonResponse({'error': 'wrong input'}, safe=False,
                            status=status.HTTP_400_BAD_REQUEST)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False,
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    except KeyError as e:
        return JsonResponse({'error': str(e)}, safe=False,
                            status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return JsonResponse({'error': str(e)}, safe=False,
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)


def send_mail(request, pk):
    current_site = get_current_site(request)
    pk = force_text(urlsafe_base64_decode(pk))
    user = Account.objects.get(pk=pk)
    token = AccountActivationTokenGenerator()
    token = token.make_token(user)
    content = 'HR 인증 주소.\n\n{}/user/{}/verify/{}/'.format(current_site.domain,
                                                               urlsafe_base64_encode(force_bytes(user.pk)), token)
    email = EmailMessage('HR 인증', content, to=[user.email])
    EmailMessage()
    email.send()
    return JsonResponse({'success': '성공!'})


class AccountActivationTokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return (text_type(user.pk)) + text_type(timestamp)


@api_view(["GET"])
@csrf_exempt
@permission_classes([AllowAny])
def verify(request, pk, token, mail="0"):
    uid = force_text(urlsafe_base64_decode(pk))
    user = Account.objects.get(pk=uid)
    is_valid = AccountActivationTokenGenerator().check_token(user, token)
    if is_valid:
        user.is_valid = True
        user.save()
        messages.info(request, '인증이 완료되었습니다.')
    else:
        messages.error(request, '인증에 실패했습니다.')
    if mail != "0":
        mail = force_text(urlsafe_base64_decode(mail))
        user.email = mail
        user.save()
    return JsonResponse({'success': user.id}, safe=False, status=status.HTTP_200_OK)