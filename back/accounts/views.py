from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST, require_http_methods

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .seralizers import UserDetailSerializer


# Create your views here.
@api_view(('get',))
def profile(request, user_pk):
    person = get_user_model().objects.get(pk=user_pk)
    serializer = UserDetailSerializer(person)
    print('person',serializer)
    return Response(serializer.data)



# @require_POST
# def follow(request, user_pk):
#     person = get_object_or_404(get_user_model(), pk=user_pk)
#     user = request.user
#     if person != user:
#         if person.followers.filter(pk=user.pk).exists():
#             person.followers.remove(user)
#             is_followed = False
#         else:
#             person.followers.add(user)
#             is_followed = True
#         context = {
#             'is_followed': is_followed,
#             'followersnum': person.followers.count(),
#             'followingnum': person.followings.count(),
#         }
#         return JsonResponse(context)
