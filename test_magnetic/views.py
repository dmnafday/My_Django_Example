from django.http import HttpResponse
from django.template import loader
from .models import System, Structure, MagGenInfo, MagBondData, MagExchangeData
# Create your views here.
#from django.shortcuts import render

def systems(request):
    mysystems = System.objects.all().values()
    template = loader.get_template('mysystems.html')
    context = {
        'mysystems': mysystems,
    }
    return HttpResponse(template.render(context, request))

def structure(request, id):
  mysystems = System.objects.get(id=id)
  mystructure = mysystems.structure_set.all().values() 
  template = loader.get_template('mystructures.html')
  context = {
    'mysystems': mysystems,      
    'mystructure': mystructure,
  }
  return HttpResponse(template.render(context, request))

def magnetic(request, id):
  mysystems = System.objects.get(id=id)
  mymaggeninfo = mysystems.maggeninfo_set.all().values()
  mymagbonddata = mysystems.magbonddata_set.all().values()
  template = loader.get_template('mymagdetails.html')
  context = {
    'mymaggeninfo': mymaggeninfo,
    'mymagbonddata': mymagbonddata,
    'mysystems': mysystems,
  }
  return HttpResponse(template.render(context, request))

def exchange(request, id):
  myexchangedata = MagExchangeData.objects.get(id=id)
  template = loader.get_template('myexchange.html')
  context = {
    'myexchangedata': myexchangedata,
  }
  return HttpResponse(template.render(context, request))
