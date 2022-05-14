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
    form = siteForm()
    return render(request, 'index.html',{'prediction':prediction,'form':form})