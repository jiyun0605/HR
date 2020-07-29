import json
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import Post
from .serializers import PostSerializer

@api_view(["POST"])
@csrf_exempt
@permission_classes([IsAuthenticated])
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
    except Exception:
        return JsonResponse({'error':'Something terrible went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# def createView(request):
#     if request.method == 'POST':
#         contents = Post(
#             title=request.POST['title'],
#             sports_name=request.POST['sports_name'],
#             routine=request.POST['routine'],
#             sets=request.POST['sets'],
#             created_date=timezone.now(),
#             updated_date=timezone.now()
#         )
#     contents.save()
#     return Response(status=status.HTTP_201_CREATED)
