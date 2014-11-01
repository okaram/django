from django.shortcuts import render,redirect
from abads.models import ABExperiment,ExperimentAd
from random import randint

# Create your views here.

def index(request):
    return render(request, 'abads/index.html')

def test(request):
    return render(request, 'abads/test.html')
def get_ad(request,exp_id):
    exp=ABExperiment.objects.get(id=exp_id)
    ads=exp.experimentad_set.all()
    place=randint(1,len(ads))-1
    url=ads[place].src_url
    ads[place].visits=ads[place].visits+1;
    ads[place].save()
    resp=redirect(url)
    resp.set_cookie('abexperiment_'+str(exp_id),str(place))
    return resp

def record_click(request,exp_id):
    exp=ABExperiment.objects.get(id=exp_id)
    ad_id=request.COOKIES.get('abexperiment_'+str(exp_id))
    ad=ExperimentAd.objects.get(id=ad_id)
    ad.clicks=ad.clicks+1
    ad.save()
    return redirect(exp.action_url)
    
    

