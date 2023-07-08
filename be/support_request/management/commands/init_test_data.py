import random
from django.core.management.base import BaseCommand, CommandError
from django.utils import timezone
from support_request.models import SupportRequest


class Command(BaseCommand):
    help = "Creating test data in DB."

    def handle(self, *args, **options):
        # SupportRequest.objects.all().delete()
        for i in range(200):
            sr = SupportRequest.objects.create(
                number=f"{random.choice(['SD', 'SX', 'KL'])}{random.randint(1000000, 9999999)}",
                status=random.choice(SupportRequest.STATUSES)[0],
                author=random.choice(['Светлана Пустокартриджова', 'Олег Ничегонеработайлов', 'Виктор Дуб']),
                contact=random.choice(['Валерий Починийло', 'Маргаритта Решайлова', None]),
                short_description='краткое описание проблемы',
                description='полное описание проблемы',
                decision=random.choice(['Решение такое', 'Решение сякое', None]),
                state=random.choice(['Состояние 1', 'Состояние 2', 'Состояние 0']),
                closed=random.choice([True, False]),
                deadline=timezone.now() + timezone.timedelta(days=random.randint(3, 7))
            )
            self.stdout.write(self.style.SUCCESS('Created "%s"' % sr))
