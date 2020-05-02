from django.db import models

# Create your models here.

class User(models.Model):
	u_id = models.CharField(primary_key=True, max_length=255)
	u_name = models.CharField(max_length=255)
	u_tz = models.CharField(max_length=255)

	class Meta:
		managed = True
		db_table = 'user'


class ActivityPeriod(models.Model):
	u_id = models.CharField(max_length=255)
	start_timestamp = models.CharField(max_length=255)
	end_timestamp = models.CharField(max_length=255)

	class Meta:
		managed = True
		db_table = 'activityperiod'
