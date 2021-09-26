from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
import json
# It is a sample Html example.
def showindex(request):
    html_text="<html><body bgcolor='yellow'>Sample Example</body></html>"
    return HttpResponse(html_text)

# passing a json data through HttpResponse
def showjson1index(request):
    d1={'idno':101,'name':"Bhabani","status":True}
    # dumbs function is converting dict data to json
    json_data=json.dumps(d1)
    return HttpResponse(json_data,content_type='application/json')

# passing a json data through JsonResponse
def showjson2index(request):
    d1 = {'idno': 102, 'name': "Bhabani Shankar", "status": True}
    return JsonResponse(d1)


def showjson3index(request):
    d1=[{'idno':101,'name':"Bhabani","status":True},
        {'idno': 102, 'name': "Bhabani Shankar", "status": False},
        {'idno': 103, 'name': "Bhabani Shankar Swain", "status": None}
        ]
    #return JsonResponse(d1)#(We can't send nested dict through JsonResponse)
    json_data=json.dumps(d1)
    return HttpResponse(json_data,content_type='application/json')