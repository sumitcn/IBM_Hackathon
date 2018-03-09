from django.http import HttpResponse , HttpResponseRedirect
from django.shortcuts import render , render_to_response
from django.template import RequestContext
import speech_recognition as sr
from time import ctime
import time
import os
import requests
import json
from os import path
from django.core.files.storage import FileSystemStorage


def home(request):
        context={}
        template='home.html'
        return render(request, template,context)


def analyze_tone(text):
    username = '449932af-87ee-4163-934b-846de18c0a02'
    password = 'l3hijfCcyebK'
    watsonUrl = 'https://gateway.watsonplatform.net/tone-analyzer/api/v3/tone?version=2017-09-21'
    headers = {"content-type": "text/plain"}
    data = text
    print (data)
    try:
        r = requests.post(watsonUrl, auth=(username,password),headers = headers,data=data)
        return r.text
    except:
        return False

 
def display_results(data):
    dict = json.loads(str(data))
  
    #print(json.dumps(data))
    return dict 

    #return render('home.html', {'dictionary': dict})
    #return HttpResponse(json.dumps(data))
    #return render(request,'home.html',{'datr':dict})


def main(data):
     
   
    if len(data) >= 1:
        if data == 'q'.lower():
            exit
        print(data)    
        results = analyze_tone(data)
        if results != False:
            dict=display_results(results)
            #print(dict)
            return dict
            exit
        else:
            print("Something went wrong")
           

def recordAudio(request):
  
    r = sr.Recognizer()    
# obtain audio from the microphone
    
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Say something!")
        audio = r.listen(source)
        
 
    
    IBM_USERNAME = "eb407541-3a15-49b0-97c1-f6ac052af6dd"
    IBM_PASSWORD = "te0bftui18JM"  
    try:
        
        data =  r.recognize_ibm(audio, username=IBM_USERNAME, password=IBM_PASSWORD)
        print("You said: " + data)
    except sr.UnknownValueError:
        print("Sorry, but, I could not understand what you said!")
        data="No data"
    except sr.RequestError as e:
        print("Could not request results from IBM Recognition service; {0}".format(e))
        data="No data"
    dic=main(data)
    lib={}
    for i in dic['document_tone']['tones']:
    	a=i['tone_name']
    	b=str(i['score'])
    	lib[a]=b



    print(dict)
    context={'datr':data,'dictio':lib}
    return render(request, 'home.html',context)
    html = "<html><body> %s.</body></html>" % data
    #return render(request,'home.html',{'datr':data})

   




