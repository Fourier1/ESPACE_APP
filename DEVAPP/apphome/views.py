# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render


# Create your views here.

def base(request):
    """
    page template de home des applications
    :param request: 
    :return: 
    """
    return render(request, 'apphome/base.html')
