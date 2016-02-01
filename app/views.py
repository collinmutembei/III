from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from django.shortcuts import render


@api_view(('GET',))
def root_route(request, format=None):
    return Response({
        'bucketlists': reverse('bucketlist-list', request=request, format=format),
    })

def index(request):
    return render(request, 'blst/landing.html')
