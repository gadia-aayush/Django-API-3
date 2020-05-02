from .models import User, ActivityPeriod
from django.http import HttpResponse
from django.db import connection

from pytz import timezone
import json, time, datetime


def json_format(request):
	output_dict = {}
	cursor = connection.cursor()
	cursor.execute('''SELECT u_id, u_name, u_tz FROM user''')
	ids, names, tzs = [], [], []
	
	for each in cursor:
		ids.append(each[0])
		names.append(each[1])
		tzs.append(each[2])

	if len(ids) > 0:
		output_dict["ok"] = True
		output_dict["members"] = []
		for i in range(len(ids)):
			member_dict = {}
			member_dict["id"] = ids[i]
			member_dict["real_name"] = names[i]
			member_dict["tz"] = tzs[i]
			member_dict["activity_periods"] = []
			cursor.execute("SELECT start_timestamp, end_timestamp FROM activityperiod WHERE u_id=:id ORDER BY start_timestamp ASC", {"id" : ids[i]})
			for each in cursor:
				time_dict = {}
				
				s_localtime = datetime.datetime.fromtimestamp(float(each[0]), timezone(str(tzs[i])))
				e_localtime = datetime.datetime.fromtimestamp(float(each[1]), timezone(str(tzs[i])))

				time_dict["start_time"] = s_localtime.strftime("%b %-d %Y %-I:%M%p")
				time_dict["end_time"] = e_localtime.strftime("%b %-d %Y %-I:%M%p")
				member_dict["activity_periods"].append(time_dict)
				
			output_dict["members"].append(member_dict)

	else:
		output_dict["ok"] = False
		output_dict["members"] = []		

	output_json = json.dumps(output_dict)
	return HttpResponse(output_json)

	