from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import datetime, timedelta
from Users.models import *

class Command(BaseCommand):
    
    help="creates dummy user data"
    
    def handle(self, *args, **kwargs):
        user = User.objects.create(first_name='Donald', last_name='Trump', tz='Asia/kolkata')
        user.save()
        started_on = timezone.now()
        ended_on = started_on + timedelta(minutes=30)
        activity_period = ActivityPeriod.objects.create(session_key='f07b098b744f4fec973ff3110538c97d', started_on=started_on, ended_on=ended_on, user=user)
        activity_period.save()
