from django.core.management.base import BaseCommand
import datetime


class Command(BaseCommand):
    help = 'Create random users'

    def add_arguments(self, parser):
        parser.add_argument('year', type=int, help='Year')
        parser.add_argument('quarter', type=int, help='Quarter')

    def handle(self, *args, **kwargs):
        year = kwargs['year']
        quarter = kwargs['quarter']
        start_time = 0
        end_time = 0
        if quarter == 1:
            start_time = datetime.datetime(year, 1, 1, 0, 0, 0)
            end_time = datetime.datetime(year, 3, 31, 23, 59, 59)
            print("First quarter!")
            print(start_time, end_time)
        elif quarter == 2:
            print("Second quarter!")
        else:
            print("Wrong")

        time_stamp = end_time -start_time
        print(time_stamp)
