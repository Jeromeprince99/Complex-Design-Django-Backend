from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
import requests
import json
from django.http import StreamingHttpResponse, JsonResponse
from datetime import datetime
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .serializers import PostSerializer

#class PostStoryView(APIView):
 #   parser_class = (FileUploadParser,) 
def post_story(request):

        json_data= json.loads(request.body.decode("utf-8"))
        post_serializer = PostSerializer(data=json_data['image'])
        if post_serializer.is_valid():
                post_serializer.save()
        if("image" in json_data and "video" in json_data):
                newpost = Post(content=json_data['content'],image=post_serializer.data,video=json_data['video'])
        elif("image" in json_data):
                newpost = Post(content=json_data['content'],image=post_serializer.data)
        elif("video" in json_data):
                newpost = Post(content=json_data['content'],video=json_data['video'])
        else:
                newpost = Post(content=json_data['content'])
        newpost.save()
        return HttpResponse(newpost)

def get_story(request):
    all_post = Post.objects.all()
    #return JsonResponse( model_to_dict(all_post), safe=False)
    context = {
            "all_post":all_post
    }
    return render(request, "../templates/complex_design_backend/dbobjects.html" , context)


    
