import logging
from math import log
from django.http import HttpResponse

from .tasks import add

logger = logging.getLogger(__name__)


def az(request):
    for x in range(1000):
        add.delay(x, x + 1)
    return HttpResponse("OK")


def ping(request):
    return HttpResponse("pong")
