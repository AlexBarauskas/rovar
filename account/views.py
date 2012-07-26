# -*- coding: utf-8 -*-
 
from django.conf import settings

from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from django.utils import simplejson

from django.db.models import Max, Min

from account.models import Account
import base64
from datetime import datetime
import time


def main_page(request):
    return HttpResponse('Account_index')
    #return render_to_response('html/accounts.html',
    #                          context,
    #                          context_instance=RequestContext(request))

