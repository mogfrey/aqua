from googleapiclient.discovery import build
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from main.models import Farmers, Farms, Temperatures
from json_tricks import dumps, loads
from pusher import Pusher
import datetime


pusher_client = Pusher(
  app_id='229305',
  key='36e3e7ba8b06e8d25a84',
  secret='3f372f653e795cb5123f',
  ssl=True
)

_DEVLOPER_KEY_="AIzaSyDJsKwHikseUohUcvNu-CIJDIqA_yopnKo"

@api_view(['GET'])
def search_data(request):
   
    try:
        service = build("customsearch", "v1",
                developerKey=_DEVLOPER_KEY_)

        res = service.cse().list(
            q='fish farming techniques',
            cx='017576662512468239146:omuauf_lfve',
        ).execute()

        snippets={
            'message': res,
            'status_code':200
        }
        return Response(snippets)

    except:
        
        snippets={
            'message':'error encountered',
            'status_code':500
        }
        return Response(snippets)

@api_view(['POST'])
def store_values(request):
    null = None
    _input = loads(request.POST['data'], preserve_order=True)

    data = _input[0]['date']
    error = {
            'message':'error',
            'status_code':500
    }

    
    temperature = Temperatures(
            farm_id = 'LX580WAF5',
            year = data.year,
            month = data.month,
            day = data.day,
            hour = data.hour,
            minute = data.minute,
            second = data.second,
            microsecond = data.microsecond,
            value = _input[0]['temp']
        )

    success = {
            'message':'success',
            'data':temperature.save(),
            'status_code':200
        }

    push_values()   
    current_temperature()
   
    return Response(success)


@api_view(['GET'])
def fetch_values(request):
    
    temperatures = Temperatures.objects.filter(month=10).order_by('day')[:120]
    details=[]

    for temperature in temperatures:
        values={
            'year': temperature.year,
            'month': temperature.month,
            'day': temperature.day,
            'hour': temperature.hour ,
            'minute': temperature.minute,
            'second': temperature.second,
            'microsecond': temperature.microsecond,
            'value': temperature.value
        }
        details.append(values)

    pusher_client.trigger('graph-channel', 'graph-temp-event', {'values': details})
    
    success = {
            'message':'success',
            'data':details,
            'status_code':200
            }

    return Response(success)   

@api_view(['GET'])
def clear_data(request):
    delete= Temperatures.objects.all().delete()
    success = {
            'message':'success',
            'data':delete,
            'status_code':200
            }

    return Response(success)

    


def push_values():
    temperatures = Temperatures.objects.filter(month=10).order_by('day')[:300]
    details=[]

    for temperature in temperatures:
        values={
            'year': temperature.year,
            'month': temperature.month,
            'day': temperature.day,
            'hour': temperature.hour ,
            'minute': temperature.minute,
            'second': temperature.second,
            'microsecond': temperature.microsecond,
            'value': temperature.value
        }
        details.append(values)

    pusher_client.trigger('graph-channel', 'graph-temp-event', {'values': details})
    success = {
            'message':'success',
            'data':details,
            'status_code':200
            }

    return success 


def current_temperature():
    temperatures = Temperatures.objects.filter(farm_id = 'LX580WAF5').order_by('-id')[:1]
    pusher_client.trigger('temp-channel', 'new-temp-event', {'value': temperatures[0].value})
    success = {
                'message':'success',
                'data':[],
                'status_code':200
            } 
    return success






    

   

        



    


    #+211 259 542 134


