from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from django.shortcuts import render
from django.contrib import auth
from django.http import HttpResponseRedirect


@api_view(('GET',))
def root_route(request, format=None):
    return Response({
        'bucketlists': reverse(
            'bucketlist-list',
            request=request,
            format=format
        ),
    })


def custom_404(request):
    return render(request, '404.html')


def landing(request):
    if request.user.is_authenticated():
        return render(request, 'dashboard.html')
    return render(request, 'landing.html')


def dashboard(request):
    if request.user.is_authenticated():
        return render(request, 'dashboard.html')
    return HttpResponseRedirect("/")


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("/")
