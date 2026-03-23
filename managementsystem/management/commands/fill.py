
from django.core.management import BaseCommand
from managementsystem.models import Banner, GymActivity

banners_data = [
    {
        "title": "Йога",
        "slogan": "Приобретай душевный покой и умиротворение",
        "button_text": "Присоединяйся к нам!",
        "link_url": "register",
        "image": "images/banners/001-training-yoga.jpg",
        "is_active": True
    },
    {
        "title": "Интенсивные тренировки в группах",
        "slogan": "Дай своему сердцу повод биться мощнее!",
        "button_text": "Узнай подробнее",
        "link_url": "activities",
        "image": "images/banners/002-training-step-aerobic.jpg",
        "is_active": True
    },
    {
        "title": "Зал силовых упражнений",
        "slogan": "Построй себя сам, закаляя характер и тело.",
        "button_text": "Фотогалерея",
        "link_url": "photogallery",
        "image": "images/banners/003-training-muscular-person.jpg",
        "is_active": True
    }
]

activities_data = [
    {
        "title": "Кардиотренировки",
        "slogan": "Дай своему сердцу повод биться мощнее.",
        "subtitle": "Кардиотренировки",
        "description": "Кардио и аэробика — это неиссякаемая энергия в каждом движении. Твое сердце — мощный мотор, который требует закалки. Укрепи выносливость, сожги лишнее и почувствуй прилив жизненных сил. Будь в ритме своего здоровья!",
        "image": "images/GymActivities/001-CardioWoman.jpg",
        "link_url": "cardio",
        "is_active": True
    },
    {
        "title": "Танцы",
        "slogan": "Раскрой свою истинную красоту в танце.",
        "subtitle": "Координация движений и ритм.",
        "description": "Бальные танцы — это совершенная координация движений и чистый драйв на паркете. Почувствуй ритм каждой клеткой, обрети грацию и уверенность. Наполни жизнь музыкой и страстью — начни танцевать прямо сейчас!",
        "image": "images/GymActivities/002-Dance.jpg",
        "link_url": "dance",
        "is_active": True
    },
    {
        "title": "Силовые упражнения",
        "slogan": "Построй себя сам, закаляя характер и тело.",
        "subtitle": "Работа над своим телом.",
        "description": "Бодибилдинг — это не просто мышцы, а триумф воли над ленью. Каждая тренировка кует характер и закаляет дух. Преврати боль в силу, а сомнения — в результат. Стань лучшей версией себя уже сегодня! Выбор за тобой.",
        "image": "images/GymActivities/003-AthleticMan.jpg",
        "link_url": "bodybuilding",
        "is_active": True
    },
    {
        "title": "Бассейн",
        "slogan": "Сила океана для твоих личных рекордов.",
        "subtitle": "Бассейн",
        "description": "Плавание в олимпийском 50-метровом бассейне — это максимум свободы для ваших достижений. Длинные дорожки позволяют держать темп без частых разворотов, развивая выносливость и силу. Укрепите спину и сбросьте лишнее в кристально чистой воде!",
        "image": "images/GymActivities/004-Swimmingpool.jpg",
        "link_url": "swimming",
        "is_active": True
    },
    {
    "title": "Единоборства",
    "slogan": "Используй энергию противника против него самого.",
    "subtitle": "Айкидо",
    "description": "Айкидо учит использовать энергию атакующего для защиты. Это путь самосовершенствования, где мягкость побеждает твердость, а контроль — агрессию. Развивайте гибкость, координацию и внутреннюю дисциплину в безопасной атмосфере.",
    "image": "images/GymActivities/005-Aikido.jpg",
    "link_url": "aikido",
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
        Banner.objects.all().delete()
        GymActivity.objects.all().delete()


    def handle_bulk_create(self, *args, **options):
        """
        заполнение с одним обращением в базу данных с
        записью множества строк одновременно
        """

        objects_for_creation = []
        for object_item in banners_data:
            objects_for_creation.append(Banner(**object_item))
        Banner.objects.bulk_create(objects_for_creation)

        objects_for_creation = []
        for object_item in activities_data:
            objects_for_creation.append(GymActivity(**object_item))
        GymActivity.objects.bulk_create(objects_for_creation)

