from  datetime import datetime
from .models import UserOtp
from django.contrib.auth import get_user_model
import random
User = get_user_model()

def generate_otp(phone):
    user,_ =UserOtp.objects.get_or_create(user__phone = phone)
    user.otp = random.randint(99999, 999999)
    user.save()
    print(user.otp)
    return user.otp


def genKey(phone):
    return str(phone) + str(datetime.date(datetime.now())) + "deepsense"