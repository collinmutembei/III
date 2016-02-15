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
    return render(request, 'landing.html')


def dashboard(request):
    return render(request, 'dashboard.html')


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("/")
