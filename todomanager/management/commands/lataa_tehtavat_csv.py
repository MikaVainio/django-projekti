import csv

from django.core.management.base import BaseCommand

from ...models import Tehtava


class Command(BaseCommand):
    help = 'Lataa tehtäviä CSV-tiedostosta'

    def add_arguments(self, parser):
        parser.add_argument('csv_tiedosto', type=str)

    def handle(self, csv_tiedosto, *args, **options):
        with open(csv_tiedosto, encoding='utf-8') as tiedosto:
            lukija = csv.DictReader(tiedosto)
            for rivi in lukija:
                print(f"Tehtävä {rivi['otsikko']}")
                kannassa = Tehtava.objects.filter(otsikko=rivi['otsikko'])
                if kannassa.exists():
                    print("    oli jo kannassa")
                    continue
                print("    lisätään")
                Tehtava.objects.create(
                    otsikko=rivi['otsikko'],
                    kuvaus=rivi['kuvaus'],
                )
