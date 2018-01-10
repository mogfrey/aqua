from googleapiclient.discovery import build
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from main.models import Farmers, Farms, Temperatures, Chats, Messages
from json_tricks import dumps, loads
from pusher import Pusher
from django.contrib.auth.hashers import make_password
from passlib.hash import django_pbkdf2_sha256 as password_handler

import random
import string
import datetime

pusher_client = Pusher(
  app_id='229305',
  key='36e3e7ba8b06e8d25a84',
  secret='3f372f653e795cb5123f',
  ssl=True
)

@api_view(['POST'])
def send_message(request):
    try:
        sender=request.POST['sender']
        receiver=request.POST['receiver']
        chat_id=request.POST['chat_id']
        message=request.POST['message']
        create=Messages(sender=sender, receiver=receiver, chat_id=chat_id, message=message, created_at = datetime.date.today(),updated_at= datetime.date.today())
        create.save()
        
        pusher_client.trigger(chat_id, 'new-message-text',{'values':{
            'sender':sender,
            'receiver':receiver,
            'message':message
        }})
        return Response({
            'message':'success',
            'status_code':200
        }) 

    except BaseException as e:   
        error = {
                'message':'error:'+ str(e),
                'status_code':500
                }
            
        return Response(error) 

@api_view(['POST'])
def get_messages(request):
    try:
        details=[]
        messages=Messages.objects.filter(chat_id=request.POST['chat_id']).order_by('-id')
        for ch in messages:
            values={
                'id':ch.id,
                'chat_id':ch.chat_id,
                'sender':ch.sender,
                'receiver':ch.receiver,
                'message':ch.message,
                'created_at': ch.created_at,
                'updated_at': ch.updated_at
            }
            details.append(values)
        return Response({
            'data':details,
            'status_code':200,
            'message':'success'
        }) 
    except BaseException as e:   
        error = {
                'message':'error:'+ str(e),
                'status_code':500
                }
            
        return Response(error)





@api_view(['POST'])
def load_chat(request):
    try:
        member_1=request.POST['member_1']
        member_2=request.POST['member_2']

        chat= Chats.objects.filter(member_1=member_1, member_2=member_2)
        chat_2= Chats.objects.filter(member_1=member_2, member_2=member_1)
        details=[]
        if not chat:
            if not chat_2:
                random=random_string()
                create=Chats(member_1=member_1, member_2=member_2, chat_id=random, created_at = datetime.date.today(),updated_at= datetime.date.today())
                create.save()
                for ch in Chats.objects.filter(member_1=member_1, member_2=member_2):
                    values={
                        'id':ch.id,
                        'chat_id':ch.chat_id,
                        'member_1':ch.member_1,
                        'member_2':ch.member_2,
                        'created_at': ch.created_at,
                        'updated_at': ch.updated_at
                    }
                details.append(values)
                return Response({
                    'data':details,
                    'status_code':200,
                    'message':'attempt 2'
                }) 
            else:
                for ch in chat_2:
                    values={
                        'id':ch.id,
                        'chat_id':ch.chat_id,
                        'member_1':ch.member_1,
                        'member_2':ch.member_2,
                        'created_at': ch.created_at,
                        'updated_at': ch.updated_at
                    }
                details.append(values)
                return Response({
                    'data':details,
                    'status_code':200,
                    'message':'attempt 3'
                })     
        else:      
            for ch in chat:
                    values={
                        'id':ch.id,
                        'chat_id':ch.chat_id,
                        'member_1':ch.member_1,
                        'member_2':ch.member_2,
                        'created_at': ch.created_at,
                        'updated_at': ch.updated_at
                    }
            details.append(values)
            return Response({
                'data':details,
                'status_code':200,
                'message':'attempt 1'
            })   

    except BaseException as e:   

        error = {
                'message':'error:'+ str(e),
                'status_code':500
                }
            
        return Response(error)           


def random_string():
    char_set = string.ascii_uppercase + string.digits
    return ''.join(random.sample(char_set*6, 6))