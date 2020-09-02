import datetime, random, names, string, pytz
from randomtimestamp import randomtimestamp

from django.core.management.base import BaseCommand
from get_data.models import User, ActivityPeriod


class Command(BaseCommand):

    def get_name(self):
        name = names.get_full_name()
        return name

    def get_id(self):
        #string must start with "W0" + "number" + "char / number" ...... & must be 9 digit long
        final_id = "W0"+ random.choice(string.digits) +''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(6))
        return final_id
        
    def get_timezone(self):
        timezone = random.choice(pytz.all_timezones)
        return timezone

    def get_timestamp(self):
        time1 = randomtimestamp(text=False)
        time2 = randomtimestamp(text=False)

        #time_format = "%d-%m-%Y %H:%M:%S"

        #temp = datetime.datetime.strptime(time1, time_format)
        #time1 = datetime.datetime.timestamp(temp)

        #temp = datetime.datetime.strptime(time2, time_format)
        #time2 = datetime.datetime.timestamp(temp)

        if time1 >= time2:
            end_time = time1
            start_time = time2

        else:
            end_time = time2
            start_time = time1

        return (start_time, end_time)


    def handle(self, *args, **options):
        records1 = []
        records2 = []
        
        for _ in range(20):

            userid = self.get_id()
            time = self.get_timestamp()
            
            kwargs1 = {
                'u_id': userid,
                'u_name': self.get_name(),
                'u_tz': self.get_timezone()
            }

            kwargs2 = {
                'u_id': userid,
                'start_timestamp': time[0],
                'end_timestamp': time[1]
            }

            record1 = User(**kwargs1)
            record2 = ActivityPeriod(**kwargs2)

            records1.append(record1)
            records2.append(record2)


        User.objects.bulk_create(records1)
        ActivityPeriod.objects.bulk_create(records2)
        
