import logging
import json
import re
import datetime
import urllib
import csv
import hashlib
import os
from subprocess import call, check_output
from datetime import date, timedelta
log = logging.getLogger(__name__)

from django.db import transaction
from django.db.models import Count
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import View
from django.shortcuts import render
from django.contrib import messages
from django.utils.timezone import now
from django.conf import settings
from django.db import connection

from .models import Houses

HOME_VIEW = 'table_view'
LOGIN_VIEW = 'user_login'
LOGIN_TEMPLATE = 'login.html'
ERROR_TEMPLATE = 'error.html'
TABLE_VIEW_TEMPLATE = 'show.html'
CHART_VIEW_TEMPLATE = 'chart.html'

HOUSE_PER_PAGE = 25
TYPES = ('1 Single Family',
        '3 5-19 units',
        '5 50+ units',
        '4 20-49 units',
        '2 2-4 units',
        '6 Mobile Home')

class Login(View):

    def get(self, request):
        if request.user.is_authenticated():            
            return HttpResponseRedirect(reverse(HOME_VIEW))            
        return render(request, LOGIN_TEMPLATE)

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
        else:
            messages.error(request, 'Incorrect username/password.')

        return HttpResponseRedirect(reverse(LOGIN_VIEW))
    
    
class Logout(View):

    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse(LOGIN_VIEW))
    

class TableView(View):   
    def get(self, request): 
        if not request.user.is_authenticated():
            return not_authorized(request)
        
        houses = Houses.objects.all()[:700]
        paginator = Paginator(houses, HOUSE_PER_PAGE)

        page = request.GET.get('page')
        try:
            hs = paginator.page(page)
        except PageNotAnInteger:
            hs = paginator.page(1)
        except EmptyPage:
            hs = paginator.page(paginator.num_pages)
            
        return render(request, TABLE_VIEW_TEMPLATE, {
                                                     'houses': hs})
        
        
        
class ChartView(View):
    def get(self, request): 
        if not request.user.is_authenticated():
            return not_authorized(request)
        
        params = request.GET
        kwargs = {}
        if 'bedroom' in params:
            kwargs['bedrooms'] = int(params['bedroom'])
        if 'type' in params:
            kwargs['type'] = params['type']
   
        houses3 = Houses.objects.filter(region="3'", **kwargs)[:500]
        houses4 = Houses.objects.filter(region="4'", **kwargs)[:500]

        hs3 = [[int(h.built_year), int(h.value)] for h in houses3]
        hs4 = [[int(h.built_year), int(h.value)] for h in houses4]

        return render(request, CHART_VIEW_TEMPLATE, {
                                                    'houses3': hs3,
                                                    'houses4': hs4,
                                                    'choices1': range(8),
                                                    'choices2': TYPES,
                                                    'default1': kwargs.get('bedrooms'),
                                                    'default2': kwargs.get('type')})
    
    
def not_authorized(request):
    return error_response(request, 'You are not authorized to view this page.Please login.')    

def error_response(request, message):
    return render(request, ERROR_TEMPLATE, {'message': message})
