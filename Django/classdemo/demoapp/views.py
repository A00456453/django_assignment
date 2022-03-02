from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Hotels
from .serializers import HotelSerializers


def home(request):
    return HttpResponse("<h1> Hello SMU </h1>")


@api_view(['GET', 'POST'])
def Hotels_list(request):
    if request.method == "GET":
        hotel_list = Hotels.objects.all()
        hotelSerializer = HotelSerializers(hotel_list, many=True)
        return Response(hotelSerializer.data)
    if request.method == "POST":
        hotel_request = request.data
        serialize_request_data = HotelSerializers(data=hotel_request)
        if serialize_request_data.is_valid():
            serialize_request_data.save()

        return Response({"Message": "Added Successfully"}) 
