from __future__ import unicode_literals
import uuid
from django.db import models



class UserObjectsManager(models.Manager):
    """
    Only Those User objects which have is_active=True
    """
    def get_queryset(self):
        return super(UserObjectsManager, self).get_queryset().filter(is_active=True)


class AllUsersObjectManager(models.Manager):
    """
    To Give all users regardless of is_active
    """
    pass


class User(models.Model):
    """
    class holds all the details of the users
    """

    import pytz
    TIMEZONES = tuple(zip(pytz.all_timezones, pytz.all_timezones))

    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created = models.DateTimeField(auto_now_add=True, editable=False, help_text="The date at which user was created")
    first_name = models.CharField(max_length=30, help_text="first name of theu user")
    last_name = models.CharField(max_length=30, help_text="last name of the user")
    tz = models.CharField(max_length=200, choices=TIMEZONES, default='UTC', help_text="The timezone of the user")
    is_active = models.BooleanField(default=True)
    objects = UserObjectsManager() # Gives out only those objects with is_active=True
    all_users = AllUsersObjectManager() # Gives out all objects

    class Meta:
        get_latest_by = 'created'
        ordering = ['-created']
        verbose_name = 'User'

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class ActivityPeriod(models.Model):
    session_key = models.UUIDField(default=uuid.uuid4, editable=False)
    started_on = models.DateTimeField(null=True, blank=True, help_text="when users activity period starts")
    ended_on = models.DateTimeField(null=True, blank=True, help_text="when users activity period ends")
    user = models.ForeignKey(User, related_name="activity_timings", blank=True, help_text="Timings within which user is active")

    class Meta:
        get_latest_by = 'started_on'
        ordering = ['-started_on']
        verbose_name = 'Activity Period'

