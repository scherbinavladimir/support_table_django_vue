import random

from django.utils import timezone

from support_request.models import SupportRequest


def init_data():
    for i in range(200):
        SupportRequest.objects.create(
            status=random.choice(SupportRequest.STATUSES),
            author=random.choice(['Светлана Пустокартриджова', 'Олег Ничегонеработайлов', 'Виктор Дуб']),
            contact=random.choice(['Валерий Починийло', 'Маргаритта Решайлова', None]),
            short_description='краткое описание проблемы',
            description='полное описание проблемы',
            decision=random.choice(['Решение такое', 'Решение сякое', None]),
            state=random.choice(['Состояние 1', 'Состояние 2', 'Состояние 0']),
            closed=random.choice([True, False]),
            deadline=timezone.now() + timezone.timedelta(days=random.randint(3, 7))
        )


if __name__ == '__main__':
    init_data()