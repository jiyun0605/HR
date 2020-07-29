# import json
#
# from django.shortcuts import render
# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from rest_framework import status
# from rest_framework.decorators import api_view, permission_classes
# from rest_framework.permissions import IsAuthenticated
# from rest_framework.response import Response
# from time import timezone
# from .models import Post
# from .serializers import PostSerializer
#
# @api_view(["POST"])
# @csrf_exempt
# @permission_classes([IsAuthenticated])
# def create_view(request):
#     payload = json.loads(request.body)
#     user = request.user
#     try:
#         post = Post.objects.create(
#             title=payload["title"],
#             sports_name=payload["sports_name"],
#             routine=payload["routine"],
#             sets=payload["sets"],
#             created_date=payload["created_date"]
#
#
#         )

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
