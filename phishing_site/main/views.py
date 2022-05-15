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
    predictionArray=[]
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
        predictionArray.append(f'The Site {urlArray[0]} is not a Phishing Site')
    elif prediction == 'bad':
        predictionArray.append(f'The Site {urlArray[0]} is a Phishing site')
    else:
        predictionArray.append("Error Occured")
    passPrediction= predictionArray[0]
    form = siteForm()
   
    return render(request, 'index.html',{'prediction':passPrediction,'form':form})