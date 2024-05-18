from django.shortcuts import render
import logging
from django.http import HttpResponse

logger = logging.getLogger(__name__)

# Create your views here.

def index(request):
    logger.info('Index page accessed')
    return HttpResponse('Hello, wolrd!')

def about(request):
    return HttpResponse('About us')