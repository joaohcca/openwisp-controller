from django.shortcuts import render
import json
import requests

# Create your views here.
def portal(request):
    print("##############")
    request.bootstrap = 1
    return render(request,'portal.html',{'title':'Portal'})

def vagalume_status(request):
    request.bootstrap = 1
    if request.method == "POST":
        return render(request,'inventary.html',{'client' : request.POST['client'], 'title':'Vagalume Status'})
    if request.method == "GET":
        if('client' in request.GET and request.GET['client'] != ''):
            response = requests.get('http://discovery.controller.elcoma.com.br/v1/vagalume_status/v2/'+request.GET['client'])
            json_response = json.loads(response.content)
            return render(request,'vagalume_status.html',{'response' : json_response, 'client' : request.GET['client'], 'title':'Vagalume Status'})
    
    return render(request,'vagalume_status.html',{'title':'Vagalume Status'})
def vagalume_inventary(request):
    request.bootstrap = 1
    if request.method == "GET":
        if('client' in request.GET and request.GET['client'] != ''):
            response = requests.get('http://discovery.controller.elcoma.com.br/v1/clients/')
            if (response.status_code == 200):
                json_response = json.loads(response.content)
                if(request.GET['client'] in json_response['clients']):
                    macs = json_response['clients'][request.GET['client']]
                    return render(request,'inventory.html',{'macs' : macs, 'client_selected':request.GET['client'], 'title':'Inventory'})
    if request.method == "POST":
        if('client_receive' in request.POST and request.POST['client_receive'] != '' and 'macs' in request.POST):
            values = request.POST.getlist('macs')
            for mac in values:
                data = {
                    'mac' : mac
                }
                headers = {
                    'Content-Type': 'application/json'
                }
                datas = json.dumps(data)
                teste = requests.delete('http://discovery.controller.elcoma.com.br/v1/clients/',headers=headers, data = datas)
                data = {
                   'client.id' : request.POST['client_receive'],
                   'mac' : mac
                }
                response = requests.post('http://discovery.controller.elcoma.com.br/v1/clients/',data)
        elif('return' in request.POST):
            values = request.POST.getlist('macs')
            for mac in values:
                data = {
                    'mac' : mac
                }
                headers = {
                    'Content-Type': 'application/json'
                }
                datas = json.dumps(data)
                teste = requests.delete('http://discovery.controller.elcoma.com.br/v1/clients/',headers=headers, data = datas)            

    return render(request,'inventory.html',{ 'title':'Inventory'})

def vagalume_discovery(request):
    request.bootstrap = 1
    if request.method == "POST":
        if(request.POST['client'] != '' or request.POST['clientname'] != '' and 'macs' in request.POST):
            values = request.POST.getlist('macs')
            for mac in values:
                data = {
                   'client.id' : request.POST['client'] or request.POST['clientname'],
                   'mac' : mac
                }
                response = requests.post('http://discovery.controller.elcoma.com.br/v1/clients/',data)
                if(response.status_code == 200):
                    data = {
                        'mac' : mac
                    }
                    headers = {
                        'Content-Type': 'application/json'
                    }
                    datas = json.dumps(data)
                    teste = requests.delete('http://discovery.controller.elcoma.com.br/v1/discovery/',headers=headers, data = datas)
    response = requests.get('http://discovery.controller.elcoma.com.br/v1/discovery/')
    json_response = json.loads(response.content)
    return render(request,'vagalume_discovery.html',{'response' : json_response, 'title':'Discovery'})
