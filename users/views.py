from users.functions import generate_otp
from users.models import UserOtp
from django.shortcuts import render
from datetime import datetime, timedelta
from django.http import JsonResponse
# Create your views here.
import random


def Test(request):
    generate_otp("9744567054")

    return JsonResponse("test", safe=False)
