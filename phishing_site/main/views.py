from traceback import print_tb
from django.shortcuts import render
from .form import siteForm
from .models import siteModel
import pickle 
import os
from pathlib import Path


def index(request):
    form = siteForm()
    return render(request, 'index.html',{'form':form})


def CheckURL(request):
    TheSite=[]
    end=[]
    urlArray=[]
    BASE_DIR = Path(__file__).resolve().parent.parent
    form = siteForm(request.POST)
    url = request.POST.get("url")
    print(url)
    urlArray.append(url)
    modelPath = os.path.join(BASE_DIR,'main/model.pkl')
    with open(modelPath, 'rb') as pred:
        lr = pickle.load(pred)
    prediction=lr.predict(urlArray) 
    print(prediction[0])
    prediction=prediction[0]
    if prediction =='good':
        TheSite.append('The Site')
        end.append('is not a Phishing Site')
    elif prediction == 'bad':
        TheSite.append('The Site')
        end.append('is a Phishing Site')

    else:
        TheSite.append("Error Occured")
    passPrediction= TheSite[0]
    form = siteForm()
    link= urlArray[0]
    end=end[0]
    context={
    'prediction':passPrediction,
    'form':form,
    'pred':prediction,
    'link':link,
    'end':end
    }
    return render(request, 'index.html',context)
    #The Site {urlArray[0]} is not a Phishing Site'
    #The Site {urlArray[0]} is a Phishing site'