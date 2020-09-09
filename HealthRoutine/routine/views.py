import json
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.utils import timezone

from .models import Post
from .serializers import PostSerializer

@api_view(["POST"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def create_view(request):
    payload = json.loads(request.body)
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
@permission_classes([IsAuthenticated])
def list_view(request):
    posts = Post.objects.all()
    serializer = PostSerializer(posts, many=True)
    return JsonResponse({'posts': serializer.data}, safe=False,
                        status=status.HTTP_200_OK)

@api_view(['DELETE'])
@csrf_exempt
@permission_classes([IsAuthenticated])
def delete_view(request, post_id):
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
@permission_classes([IsAuthenticated])
def update_view(request, post_id):
    payload = json.loads(request.body) 
    try:
        post = Post.objects.get(id=post_id)
        post.title = payload['title']
        post.sports_name = payload['sports_name']
        post.routine = payload['routine']
        post.sets = payload['sets']
        post.updated_date = timezone.localtime()
        serializer = PostSerializer(post)
        return JsonResponse({'post': serializer.data}, safe=False,
            status=status.HTTP_200_OK)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something terrible went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)