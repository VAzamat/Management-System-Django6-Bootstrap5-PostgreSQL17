
from django.core.management import BaseCommand
from managementsystem.models import SubscriptionPlan, SubscriptionPlanFeature

SubscriptionPlanFeatures_data=[
    {
        "pk": 1,
        "name": "Гибкий график"
    },
    {
        "pk": 2,
        "name": "Рекомендации по спортивной диете"
    },
    {
        "pk": 3,
        "name": "Индивидуальный тренер"
    },
    {
        "pk": 4,
        "name": "Тренировки без ограничения по времени"
    },
    {
        "pk": 5,
        "name": "Отслеживанием вашего прогресса"
    },
    {
        "pk": 6,
        "name": "Ежедневные тренировки"
    }
]

SubscriptionPlan_data=[
    {
        "name": "Базовый",
        "description": "Идеальный старт: 2 часа в зале 2 раза в неделю, раздевалка, душевая, сауна и хамам. Эффективные тренировки в комфортных условиях по лучшей цене. Гибкий график и готовый план спортивного питания для вас! Месячный абонемент.",
        "price": "8000.00",
        "duration_days": 30,
        "is_highlighted": False,
        "is_active": True,
        "features": [
            1,
            2
        ]

    },
    {
        "name": "Основной",
        "description": "Тренировки 3 раза в неделю без ограничений по времени. Включены услуги тренера, индивидуальный план тренировок и питание. К вашим услугам — раздевалка, душевая, сауна и хамам. Комфорт и результат в одном пакете! Абонемент на 3 месяца по выгодной цене.",
        "price": "34000.00",
        "duration_days": 90,
        "is_highlighted":False,
        "is_active": True,
        "features": [
            1,
            2,
            3,
            4
        ]

    },
    {
        "name": "Продвинутый",
        "description": "Тренировки в любые дни без ограничений по времени. Включены  персональный индивидуальны план тренировок с индивидуальным тренером и отслеживание прогресса. К вашим услугам — раздевалка, душевая, сауна и хамам. Максимальная свобода для достижения ваших целей! Абонемент на 6 месяцев.",
        "price": "70000.00",
        "duration_days": 180,
        "is_highlighted": True,
        "is_active": True,
        "features": [
            1,
            2,
            3,
            4,
            5,
            6
        ]

    }
]


class Command(BaseCommand):
    def handle(self, *args, **options):
        """
        запуск отдельной функции
        """
        self.clear_databases()
        self.handle_bulk_individual_create(*args, **options)
        print("Success!!!")

    def clear_databases(self):
        SubscriptionPlan.objects.all().delete()
        SubscriptionPlanFeature.objects.all().delete()

    def handle_bulk_individual_create(self, *args, **options):
        """
        заполнение с одним обращением в базу данных с
        записью множества строк одновременно
        """

        objects_for_creation_features = []
        for object_item in SubscriptionPlanFeatures_data:
            objects_for_creation_features.append(SubscriptionPlanFeature(**object_item))
        SubscriptionPlanFeature.objects.bulk_create(objects_for_creation_features)

        """
        заполнение с обращением в базу данных по 
        каждой записи, чтобы features со связью ManyToManyField заполнить 
        """

        for object_item in SubscriptionPlan_data:
            features = list(object_item['features'])
            del object_item['features']
            tarif, created = SubscriptionPlan.objects.get_or_create(**object_item)
            tarif.features.set( features )
