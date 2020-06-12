from datetime import timedelta, time, datetime

from django.core.mail import mail_admins
from django.core.management import BaseCommand
from django.utils import timezone
from django.utils.timezone import make_aware

today = timezone.now()
tomorrow = today + timedelta(1)
today_start = make_aware(datetime.combine(today, time()))
today_end = make_aware(datetime.combine(tomorrow, time()))


class Command(BaseCommand):
    help = "Send email reports to admins"

    def handle(self, *args, **options):
        # orders = Order.objects.filter(confirmed_date__range=(today_start, today_end))

        message = "Test Message"

        subject = (
            f"Order report for {today_start.strftime('%Y-%m-%d')} "
            f"to {today_end.strftime('%Y-%m-%d')}"
        )

        mail_admins(subject=subject, message=message, html_message=None)

        self.stdout.write("The email reports were sent.")
