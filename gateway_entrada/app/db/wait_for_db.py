import time

from psycopg2 import OperationalError as Psycopg2Error


class Command():
    """Django command to wait for database."""

    def handle(self, *args, **options):
        """Entrypoint for command."""
        self.stdout.write('Esperando database...')
        db_up = False
        while db_up is False:
            try:
                self.check(databases=['default'])
                db_up = True
            except (Psycopg2Error):
                self.stdout.write('Database indisponível, esperando 1 segundo...')
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS('Database disponível!'))
