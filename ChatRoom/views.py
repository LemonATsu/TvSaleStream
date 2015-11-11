from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse

# Create your views here.


def openChatRoom(request):
	
	return render_to_response('chatroom.html',RequestContext(request,locals()))
