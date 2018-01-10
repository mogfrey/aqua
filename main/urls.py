from django.conf.urls import include ,url
import rest_framework
from . import views
from .controllers import datacontroller, usercontroller, messagingcontroller

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^search_data/', datacontroller.search_data),
    url(r'^store_values/', datacontroller.store_values),
    url(r'^fetch_values/', datacontroller.fetch_values),
    url(r'^clear_data/', datacontroller.clear_data),
    url(r'^current_temperature/', datacontroller.current_temperature),

    #user management methods
    url(r'^new_user/', usercontroller.user_manage),
    url(r'^create_session/', usercontroller.pass_check),
    url(r'^all_users/', usercontroller.all_users),

    #chats
    url(r'^load_chat/', messagingcontroller.load_chat),
    url(r'^send_message/', messagingcontroller.send_message),
    url(r'^get_messages/', messagingcontroller.get_messages),

    


    
    


    

]