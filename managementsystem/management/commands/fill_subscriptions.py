
from django.core.management import BaseCommand
from managementsystem.models import SubscriptionPlan


SubscriptionPlan_data=[
    {
        "name": "Базовый",
        "description": "Идеальный старт: 2 часа в зале 2 раза в неделю, раздевалка, душевая, сауна и хамам. Эффективные тренировки в комфортных условиях по лучшей цене. Гибкий график и готовый план спортивного питания для вас! Месячный абонемент.",
        "price": "8000.00",
        "duration_days": 30,
        "is_highlighted": False,
        "is_active": True
    },
    {
        "name": "Основной",
        "description": "Тренировки 3 раза в неделю без ограничений по времени. Включены услуги тренера, индивидуальный план тренировок и питание. К вашим услугам — раздевалка, душевая, сауна и хамам. Комфорт и результат в одном пакете! Абонемент на 3 месяца по выгодной цене.",
        "price": "34000.00",
        "duration_days": 90,
        "is_highlighted":False,
        "is_active": True
    },
    {
        "name": "Продвинутый",
        "description": "Тренировки в любые дни без ограничений по времени. Включены  персональный индивидуальны план тренировок и отслеживание прогресса. К вашим услугам — раздевалка, душевая, сауна и хамам. Максимальная свобода для достижения ваших целей! Абонемент на 6 месяцев.",
        "price": "70000.00",
        "duration_days": 180,
        "is_highlighted": True,
        "is_active": True
    }
]


class Command(BaseCommand):
    def handle(self, *args, **options):
        """
        запуск отдельной функции
        """
        self.clear_databases()
        self.handle_bulk_create(*args, **options)
        print("Success!!!")

    def clear_databases(self):
        SubscriptionPlan.objects.all().delete()

    def handle_bulk_create(self, *args, **options):
        """
        заполнение с одним обращением в базу данных с
        записью множества строк одновременно
        """

        objects_for_creation = []
        for object_item in SubscriptionPlan_data:
            objects_for_creation.append(SubscriptionPlan(**object_item))
        SubscriptionPlan.objects.bulk_create(objects_for_creation)
