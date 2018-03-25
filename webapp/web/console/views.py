from django.shortcuts import render
from django.core import serializers
from django.http import JsonResponse
from django.forms.models import model_to_dict
from console.models import Data
import json
# Create your views here.
def home(request):
    string =u"the string from the views"
    #return render(request,'home.html',{'string':string})
    return render(request, 'index.html')

def help(request):
    return render(request,'help.html')


def retrieve(request):
    data_list = Data.objects.all()
    #data_dict = serializers.serialize("",data_list)
    data_dict = model_to_dict(data_list)
    data_json = json.dumps(data_dict)
    return render(request,'retrieve.html',{'data_list':data_list,'data_json': data_json})

def analyze(request):
    data_list = Data.objects.all()
    return render(request,'analyze.html',{'data_list':data_list})

def ajax_data(request):
    data_list = Data.objects.all()
    data_json = serializers.serialize("json",data_list)
    return JsonResponse(data_json,safe=False)