import csv
from datetime import datetime

from django.core.management.base import BaseCommand
from core.models import UVIndexRecord


class Command(BaseCommand):
    help = "Import YEARLY UV index data into UVIndexRecord"

    def add_arguments(self, parser):
        parser.add_argument("csv_path", type=str, help="Path to the yearly CSV file")

    def handle(self, *args, **options):
        csv_path = options["csv_path"]

        created = 0
        with open(csv_path, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)

            for row in reader:
                # CSV columns: year, avg_uv_index, location
                year = int(row["year"])
                uv_value = float(row["avg_uv_index"])
                location = row.get("location", "Melbourne")

                # Use a synthetic timestamp: 1 Jan of that year at noon
                timestamp = datetime(year, 1, 1, 12, 0, 0)

                UVIndexRecord.objects.create(
                    location=location,
                    uv_level_index=uv_value,
                    timestamp=timestamp,
                )
                created += 1

        self.stdout.write(self.style.SUCCESS(f"Imported {created} yearly UV records from {csv_path}"))
