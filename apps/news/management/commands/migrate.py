from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = "Override default migrate command to bypass SQL database migration for MongoDB setup."

    def handle(self, *args, **kwargs):
        self.stdout.write("MongoDB setup doesn't use migrations. No action taken for 'migrate'.")