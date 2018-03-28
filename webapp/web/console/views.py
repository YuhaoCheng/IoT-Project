from django.shortcuts import render
from django.core import serializers
from django.http import JsonResponse
from django.forms.models import model_to_dict
from django.forms import modelformset_factory
from console.models import Data
from console.models import Device
from console.models import Manager
import json
# Create your views here.
def home(request):
    string =u"the string from the views"
    #return render(request,'home.html',{'string':string})
    return render(request, 'index.html')

def help(request):
    return render(request,'help.html')


def retrieve(request):
    devices = Device.objects.all().values_list('deviceID', 'location', 'type', 'description')
    return render(request,'retrieve.html',{'devices': devices})

def analyze(request):
    #data_list = Data.objects.all()
    devices = Device.objects.all().values_list('deviceID', 'location', 'type', 'description')
    return render(request, 'analyze.html', {'devices': devices})

def manage_login(request):
    return render(request, 'manage_login.html')

def manage(request):
    #data_list = Data.objects.all()
    devices = Device.objects.all().values_list('deviceID', 'location', 'type', 'description')
    return render(request, 'manage.html', {'devices': devices})

def ajax_data_retrieve(request):
    id = request.GET['deviceID']
    #data = Data.objects.values_list('deviceID','temperature','humidity','light','time','day')
    data = Data.objects.filter(deviceID=id).values_list('deviceID','temperature','humidity','light','time','day')
    data_list = list(data)
    if data_list:
        return JsonResponse(data_list, safe=False)
    else:
        return JsonResponse("false", safe=False)

def ajax_devices(request):
    devices = Device.objects.all().values_list('deviceID','location','type','description')
    devices_list = list(devices)
    return JsonResponse(devices_list,safe=False)

def ajax_data_analyze(request):
    id = request.GET['deviceID']
    data = Data.objects.filter(deviceID=id).values_list('temperature', 'humidity', 'light', 'time')
    data_list = list(data)
    return JsonResponse(data_list, safe=False)

def check(request):
    manager = Manager.objects.all().values_list('managerID','password')
    manager_list = list(manager)
    return JsonResponse(manager_list,safe=False)

def add_new_device(request):
    deviceID = request.GET['deviceID']
    location = request.GET['location']
    type = request.GET['type']
    description = request.GET['description']

    id_list = Device.objects.all().values_list('deviceID')
    check_list = list(id_list)
    check_flag = True
    flag = True

    for temp in check_list:
        if temp[0] == deviceID:
            check_flag = False
            break

    if check_flag:
        result, flag = Device.objects.get_or_create(deviceID=deviceID, location=location, type=type,description=description)
        result.save()
        print(flag)

    send_flag = "false"
    if(flag and check_flag):
        send_flag = "true"
    else:
        send_flag = "false"

    return JsonResponse(send_flag, safe=False)

def delete_device(request):
    deviceID = request.GET['deviceID']

    id_list = Device.objects.all().values_list('deviceID')
    check_list = list(id_list)
    check_flag = False
    send_flag = "false"

    for temp in check_list:
        if temp[0] == deviceID:
            check_flag = True
            break

    if check_flag:
        Device.objects.filter(deviceID=deviceID).delete()
        send_flag = "true"

    return JsonResponse(send_flag, safe=False)