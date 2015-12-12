from django.core.management.base import BaseCommand, CommandError
from humanbot.health.models import (Measurement, MeasurementFor,
        MeasurementType)
from humanbot.core.models import Human
import csv

class Command(BaseCommand):
    help = 'Import CSV Health Data'

    def add_arguments(self, parser):
        parser.add_argument('file', nargs=1, type=str)

    def handle(self, *args, **options):
        pk = raw_input('Measurement For (pk): ')
        measurement_for = MeasurementFor.objects.get(pk=pk)
        print measurement_for

        pk = raw_input('Measurement Type (pk): ')
        measurment_type = MeasurementType.objects.get(pk=pk)
        print measurment_type

        pk = raw_input('Human (pk): ')
        human = Human.objects.get(pk=pk)
        print human

        with open(options['file'][0]) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                # TODO: At some point make this work with more files
                measurment = Measurement(
                    human=human,
                    source_name='csv',
                    source_id=options['file'][0],
                    measurement_for=measurement_for,
                    measurement_type=measurment_type,
                    value=row['Lengths'],
                    created=row['Session'])
                measurment.save()
