
from django.core.management import BaseCommand
from managementsystem.models import Banner, GymActivity, PhotoAlbum, ImageGallery

photoalbom_data=[
    {
        "pk": "da5044d3-13e0-4e51-8ccc-cea9a11ce323",
        "title": "Природа",
        "cover_image": "images/PhotoAlbumCovers/001_collage_nature.jpg",
        "description": "Прикоснитесь к магии первозданной природы: от заснеженных горных пиков и таинственного леса до танцующего в небе северного сияния. Альбом о тишине, величии природы и моментах, когда захватывает дух. Настоящая сказка в каждом кадре.",
        "created_at": "2026-03-23T20:17:59.037Z",
        "is_active": True
    },
    {
        "pk": "aa34ec6e-3e8d-453d-bfdc-11c2524827f7",
        "title": "Наши работники",
        "cover_image": "images/PhotoAlbumCovers/002_cover_collage_team.jpg",
        "description": "Наша команда это эксперты с многолетним опытом, влюбленные в свое дело. Мы объединили лучших мастеров, чтобы гарантировать вам безупречное качество, индивидуальный подход и соблюдение сроков. Ваше доверие — наш главный стимул к совершенству!",
        "created_at": "2026-03-23T21:58:00.698Z",
        "is_active": True
    }

]

imagegallery_data=[
    {
        "album": "da5044d3-13e0-4e51-8ccc-cea9a11ce323",
        "title": "Горное озеро",
        "image": "images/ImageGallery/004_nature_mountains.jpg",
        "category": "горы",
        "description": "Горное озеро — природный бриллиант в оправе из древних скал. Чистота воды, свежесть воздуха и покой, который можно найти только здесь. Идеальный пейзаж для тех, кто ищет вдохновение в тишине.",
        "order": 1,
        "created_at": "2026-03-23T20:47:33.112Z",
        "is_active": True
    },
    {
        "album": "da5044d3-13e0-4e51-8ccc-cea9a11ce323",
        "title": "Северное сияние",
        "image": "images/ImageGallery/003_nature_northern_lights.jpg",
        "category": "полярные сияния",
        "description": "Яркие всполохи северного сияния превращают ночь в сказку, отражаясь в снегах и напоминая о невероятной красоте нашей планеты. Красота, которую невозможно забыть.",
        "order": 1,
        "created_at": "2026-03-23T20:39:10.804Z",
        "is_active": True
    },
    {
        "album": "da5044d3-13e0-4e51-8ccc-cea9a11ce323",
        "title": "Уютная бухта",
        "image": "images/ImageGallery/001_nature_5terre.jpg",
        "category": "Море",
        "description": "Вид с террасы на уютную бухту: разноцветные крыши домов и лодки на зеркальной глади. Идеальное утро в прибрежном раю, наполненное криком чаек и ароматом кофе. Здесь каждый уголок дышит спокойствием и летним теплом.",
        "order": 3,
        "created_at": "2026-03-23T20:45:39.366Z",
        "is_active": True
    },
    {
        "album": "da5044d3-13e0-4e51-8ccc-cea9a11ce323",
        "title": "Снежные вершины",
        "image": "images/ImageGallery/005_nature_snow.jpg",
        "category": "горы",
        "description": "Величественные горные пики, укрытые сияющим снежным покровом, безмолвно застыли под холодным зимним солнцем. Атмосфера первозданной тишины и кристальной чистоты природы, где небо встречается с землей в бесконечном танце льда и света.",
        "order": 0,
        "created_at": "2026-03-23T20:36:50.226Z",
        "is_active": True
    },
    {
        "album": "da5044d3-13e0-4e51-8ccc-cea9a11ce323",
        "title": "Дорога в лес",
        "image": "images/ImageGallery/002_nature_forest.jpg",
        "category": "Лес",
        "description": "Мост, ведущий в сердце дикого леса. Граница между суетой и спокойствием природы. Кажется, за этим поворотом начинается настоящая сказка. Идеальное место, чтобы оставить лишние мысли и просто идти вперед под шепот листвы.",
        "order": 2,
        "created_at": "2026-03-23T20:42:53.114Z",
        "is_active": True
    },
    {
        "album": "aa34ec6e-3e8d-453d-bfdc-11c2524827f7",
        "title": "Anna Doe",
        "image": "images/ImageGallery/001_team_AnnaDoe.jpg",
        "category": "Работники",
        "description": "Anna Doe — ведущий дизайнер нашей команды. Обладает тонким чувством стиля и уникальным взглядом на пространство. Анна создает эстетичные и функциональные интерьеры тренажерных залов, в которых продумана каждая деталь. Её проекты — это гармония уюта и современных трендов.",
        "order": 0,
        "created_at": "2026-03-23T22:00:01.950Z",
        "is_active": True
    },
    {
        "album": "aa34ec6e-3e8d-453d-bfdc-11c2524827f7",
        "title": "Katrin King",
        "image": "images/ImageGallery/004_team_KatrinKing.jpg",
        "category": "Работники",
        "description": "Katrin King — мудрая душа и совладелица нашей сети. Её жизненный опыт и верность традициям лежат в основе нашего гостеприимства. Катрин следит за тем, чтобы в каждом клубе сохранялась уютная атмосфера и семейные ценности, ставшие фундаментом бизнеса.",
        "order": 2,
        "created_at": "2026-03-23T22:03:52.429Z",
        "is_active": True
    },
    {
        "album": "aa34ec6e-3e8d-453d-bfdc-11c2524827f7",
        "title": "Eva Berg",
        "image": "images/ImageGallery/005_team_EvaBerg.jpg",
        "category": "Работники",
        "description": "Eva Berg — наш легендарный ведущий тренер, чьё присутствие ощущается в каждом результате, даже если её нет в зале. Она — дух нашей дисциплины и автор уникальных программ. Ева учит преодолевать границы возможного и находить гармонию в движении.",
        "order": 5,
        "created_at": "2026-03-23T22:05:03.991Z",
        "is_active": True
    },
    {
        "album": "aa34ec6e-3e8d-453d-bfdc-11c2524827f7",
        "title": "John Doe",
        "image": "images/ImageGallery/003_team_JohnDoe.jpg",
        "category": "Работники",
        "description": "John Doe — идейный вдохновитель и создатель нашей сети фитнес-центров. Сделал миссией своей жизни развитие доступного и профессионального спорта. Благодаря его опыту и видению, наши клубы стали эталоном качества, комфорта и здорового образа жизни.",
        "order": 2,
        "created_at": "2026-03-23T22:02:33.758Z",
        "is_active": True
    }

]

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
        PhotoAlbum.objects.all().delete()
        ImageGallery.objects.all().delete()



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

        objects_for_creation = []
        for object_item in photoalbom_data:
            objects_for_creation.append(PhotoAlbum(**object_item))
        PhotoAlbum.objects.bulk_create(objects_for_creation)

        objects_for_creation = []
        for object_item in imagegallery_data:
            id = object_item['album']
            object_item['album'] = PhotoAlbum.objects.get(id=id)
            objects_for_creation.append(ImageGallery(**object_item))
        ImageGallery.objects.bulk_create(objects_for_creation)
