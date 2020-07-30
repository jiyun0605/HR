import json
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
from rest_framework.response import Response
from django.utils import timezone

from .models import Post
from .serializers import PostSerializer

@api_view(["POST"])
@csrf_exempt
@permission_classes([permissions.AllowAny, ])
def create_view(request):
    payload = json.loads(request.body)
    user = request.user
    try:
        post = Post.objects.create(
            title=payload["title"],
            sports_name=payload["sports_name"],
            routine=payload["routine"],
            sets=payload["sets"],
            created_date=payload["created_date"],
            updated_date=payload["updated_date"]
        )
        serializer = PostSerializer(post)
        return JsonResponse({'post': serializer.data}, safe=False, status=status.HTTP_201_CREATED)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    #safe=False 는 dict type check.
    except Exception:
        return JsonResponse({'error': 'Something terrible went wrong'}, safe=False,
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(["GET"])
@csrf_exempt
@permission_classes([permissions.AllowAny, ])
def list_view(request):
    user = request.user.id
    posts = Post.objects.all()
    serializer = PostSerializer(posts, many=True)
    return JsonResponse({'posts': serializer.data}, safe=False,
                        status=status.HTTP_200_OK)

@api_view(['DELETE'])
@csrf_exempt
@permission_classes([permissions.AllowAny, ])
def delete_view(request, post_id):
    user = request.user.id
    try:
        post = Post.objects.get(id=post_id)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False,
                            status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something went wrong'}, safe=False,
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(["PUT"])
@csrf_exempt
@permission_classes([permissions.AllowAny, ])
def update_view(request, post_id):
    user = request.user.id
    payload = json.loads(request.body)
    print(payload)  
    try:
        post = Post.objects.get(id=post_id)
        print("test")
        post.title = payload['title']
        print("test2")
        post.sports_name = payload['sports_name']
        print("test3")
        post.routine = payload['routine']
        print("test4")
        post.sets = payload['sets']
        print("test5")
        post.updated_date = timezone.localtime()
        print("test6")
        serializer = PostSerializer(post)
        return JsonResponse({'post': serializer.data}, safe=False,
            status=status.HTTP_200_OK)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something terrible went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)