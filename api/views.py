from rest_framework.response import Response
from rest_framework.decorators import api_view
from api.models import city,event
from api.serializers import citySerializer,eventSerializer

@api_view(['GET'])
def getCity(request):
    cities = city.objects.all()
    serializer = citySerializer(cities, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def addCity(request):
    serializer = citySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['GET'])
def viewCity(request):
    id = request.query_params["id"]
    if id != None:
        response_obj = city.objects.get(id=id)
        response = citySerializer(response_obj)
        return Response(response.data)


@api_view(['DELETE'])
def deleteCity(request):
    id = request.query_params["id"]
    if id != None:
        city_obj = city.objects.filter(id=id)
        city_obj.delete()
        return Response("Deleted")


#### event API view starts here #####

##Author: Aswin Soman ##

@api_view(['GET'])
def getEvents(request):
    events = event.objects.all()
    serializedEvents = eventSerializer(events, many=True)
    return Response(serializedEvents.data)
    
@api_view(['POST'])
def addEvent(request):
    serializer = eventSerializer(data= request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)

@api_view(['GET'])
def viewEvent(request):
    event_id = request.query_params["id"]
    if event_id != None:
        event_response = event.objects.get(id=event_id)
        serializer = eventSerializer(event_response)
        return Response(serializer.data)
    return Response("event Id != null")

@api_view(['DELETE'])
def deleteEvent(request):
    event_id = request.query_params['event_id']
    if event_id != None:
        event_obj = event.objects.filter(id=event_id)
        event_obj.delete()
        return Response("event deleted")
    return Response("Error")