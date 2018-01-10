from googleapiclient.discovery import build
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from main.models import Farmers, Farms, Temperatures
from json_tricks import dumps, loads
from pusher import Pusher
from django.contrib.auth.hashers import make_password
from passlib.hash import django_pbkdf2_sha256 as password_handler

import datetime



@api_view(['POST'])
def user_manage(request):
    try:
        if request.method == 'GET':
            snippets='success'
            return Response(snippets, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'POST':
            customer = Farmers(fname=request.POST['fname'], lname=request.POST['lname'], email=request.POST['email'], password=make_password(request.POST['password']), status='1', phone=request.POST['phone'],created_at = datetime.date.today(),updated_at= datetime.date.today())
            customer.save()
                
            success={
                'message':'success',
                'status_code':200
                }
                
            return Response(success)
    except BaseException as e:  

        error = {
                'message':'error:' + str(e),
                'status_code':500
                }
            
        return Response(error)            

    
@api_view(['POST'])
def pass_check(request):
    try:
        if request.method == 'GET':
            snippets='success'
            return Response(snippets, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'POST':
            user_id=request.POST['email']
            user_input_pass=request.POST['password']

            customer=Farmers.objects.get(email=user_id)
            if password_handler.verify(user_input_pass, customer.password):
                success={
                    'message':'success',
                    'session':{
                        'id':customer.id,
                        'fname':customer.fname,
                        'lname':customer.lname,
                        'email':customer.email,
                        'phone':customer.phone
                     },
                    'status_code':200
                    }
            
                return Response(success)

            else:
                success={
                    'message':'success',
                    'status_code':500
                }
            
                return Response(success)
    except BaseException as e:   

        error = {
                'message':'error:'+ str(e),
                'status_code':500
                }
            
        return Response(error)   


@api_view(['GET'])
def all_users(request): 
    farmers= Farmers.objects.all()
    details=[]
    for customer in farmers:
        values={
            'id':customer.id,
            'fname': customer.fname,
            'lname': customer.lname,
            'email ': customer.email,
            'status': customer.status,
            'phone': customer.phone,
            'created_at': customer.created_at,
            'updated_at': customer.updated_at
        }
        details.append(values)

    data={'data':details,'message':'success','status_code':200}
    return Response(data) 


             

