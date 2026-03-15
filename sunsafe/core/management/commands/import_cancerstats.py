import csv
from pathlib import Path
from django.core.management.base import BaseCommand
from core.models import CancerYearlyStat

class Command(BaseCommand):
    help = "Import cancer stats from a CSV file"

    def add_arguments(self, parser):
        parser.add_argument("csv_path", type=str, help="Path to cancer stats CSV")

    def handle(self, *args, **options):
        path = Path(options["csv_path"])
        if not path.exists():
            self.stderr.write(self.style.ERROR(f"File not found: {path}"))
            return

        objs = []

        with path.open() as f:
            reader = csv.DictReader(f)
            for row in reader:
                objs.append(
                    CancerYearlyStat(
                        year=int(row["year"]),
                        region=row["region"],
                        cancer_type=row["cancer_type"],
                        cases=int(row["cases"]),
                    )
                )

        CancerYearlyStat.objects.bulk_create(objs, ignore_conflicts=True)
        self.stdout.write(self.style.SUCCESS(f"Imported {len(objs)} rows"))
