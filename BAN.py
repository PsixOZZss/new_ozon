BAN_WORD = [
    'аналог',
    'подделка',
    'копия',
    'copy',
    'реплика',
    ' оригинал ',
    'original',
    'подлинный']

BAN_CHEMIST = [
    'индийская лакрица',
    'аконит',
    'воронец',
    'горицвет',
    'собачья петрушка',
    'корейская мята',
    'верблюжья колючка обыкновенная',
    'очный цвет полевой',
    'рыбная ягода',
    'печеночница',
    'ветреница',
    'водосбор',
    'чертово дерево',
    'шип-дерево',
    'пальма катеху',
    'роза гавайская',
    'полынь',
    'arum',
    'копытень',
    'белладонна',
    'барбарис',
    'переступень',
    'осока',
    'арабский чай',
    'кат съедобный',
    'мирт болотный',
    'чистотел',
    'цикута',
    'грудника',
    'маточные рожки',
    'спорынья',
    'ломонос',
    'безвременник',
    'вьюнок',
    'золотая нить',
    'многоцвет',
    'чахоточная трава',
    'хохлатка',
    'covid',
    'ковид',
    'кротон слабительный',
    'цикламен',
    'цикломен аджарский',
    'золотой дождь',
    'волчник',
    'дурман',
    'живокость',
    'дицентра',
    'мужской папоротник',
    'кактус сан педро',
    'мордовник',
    'синяк обыкновенный',
    'чертов куст',
    'хвойник',
    'хвойник хвощевой',
    'желтушник',
    'молочай',
    'рябчик уссурийский',
    'гайлардия красивая',
    'подснежник воронова',
    'пикульник',
    'женьшень',
    'мачек',
    'харг',
    'кровник',
    'перекати поле',
    'цельнолистник',
    'морозник',
    'золотая печать',
    'розмарин лесной',
    'кактус пейот',
    'магнолия',
    'пролесник',
    'хренное дерево',
    'мускатный орех',
    'олеандр',
    'табак',
    'лотос голубой',
    'омежник',
    'пион уклоняющийся',
    'мак армянский',
    'мак голостебельный',
    'мак прицветниковый',
    'мак снотворный',
    'мак сомнительный',
    'вороний глаз',
    'мытник',
    'могильник',
    'гармала обыкновенная',
    'собачье зелье',
    'пеларгония',
    'герань',
    'тростник южный',
    'пузырница',
    'лаконос',
    'лаконос американский',
    'перец бетель',
    'перец кава-кава',
    'перец опьяняющий',
    'подофил',
    'соломонова печать',
    'прострел',
    'африканская слива',
    'лютик',
    'погремок',
    'золотой корень',
    'солянка русская',
    'солянка южная',
    'мыльный корень',
    'мыльная трава',
    'лавр американский',
    'хохоба',
    'стефания',
    'строфант',
    'рвотный орех',
    'окопник',
    'муравьиное дерево',
    'василистник',
    'мышатник',
    'пьяная трава',
    'термопсис',
    'ололиуки',
    'ололюки',
    'крапива шариконосная',
    'пузырчатая головня кукурузы',
    'пузырчатка вздутая',
    'валериана',
    'птичий клей',
    'дурнишник',
    'юкка нитевидная',
    'парнолистник',
    'тгк',
    'thc',
    'кбд',
    'cbn',
    'cbd',
    '2-ag',
    '2-age',
    'aea',
    'cbc',
    'cbl',
    'cbdv',
    'cbg',
    'cbv',
    'thvc',
    'am-2201',
    'cp-55940',
    'hu-210',
    'hu-331',
    'jwh-018',
    'jwh-073',
    'jwh-133',
    'sr144528',
    'win 55,212-2',
    'автоцветы',
    'киеф',
    'keef',
    'дмгп',
    'бмк',
    '2c-t-7',
    '2ct7',
    '2-apb',
    '2apb',
    '2с-в',
    '2св',
    '2c-b',
    '3-caf',
    '3-f-iso-mc',
    '3-meo-mpc',
    '3-meo-pcmo',
    '4-mmc',
    '6-mam',
    'cp 47,497',
    'cp-47,497',
    'cp-47497',
    'cp 47497',
    'cp 47,497-c6',
    'cp 47497-c6-homolog',
    'cp 47,497-c8',
    'cp 47497-c8-homolog',
    'cp 47,497-c9',
    'cp 47497-c9-homolog',
    'cp 50,5561',
    'lsd',
    'лсд',
    'лсд-25',
    'катин',
    'flea',
    'hot-7',
    'hu-210',
    'jb-336',
    'jp104',
    'jwh-007',
    'jwh007',
    'jwh-018',
    'jwh018',
    'jwh-073',
    'jwh073',
    'jwh-081',
    'jwh081',
    'jwh-098',
    'jwh098',
    'jwh-116',
    'jwh116',
    'jwh-122',
    'jwh122',
    'jwh-149',
    'jwh149',
    'jwh-175',
    'jwh175',
    'jwh-176',
    'jwh176',
    'jwh-184',
    'jwh184',
    'jwh-185',
    'jwh185',
    'jwh-192',
    'jwh192',
    'jwh-193',
    'jwh193',
    'jwh-194',
    'jwh194',
    'jwh-195',
    'jwh195',
    'jwh-196',
    'jwh196',
    'jwh-197',
    'jwh197',
    'jwh-198',
    'jwh198',
    'jwh-199',
    'jwh199',
    'jwh-200',
    'jwh200',
    'm-alpha',
    'm alpha',
    'mmb-022',
    'mmb022',
    'mtta',
    'tcm',
    'org 27569',
    'org27569',
    'карбоновая кислота',
    'org 29647',
    'org29647',
    'pf-03550096',
    'pf03550096',
    'pf 03550096',
    'pre-084',
    '(2-морфолин-4-илэтил)-1-фенилциклогексан-1-карбоксилат',
    'pre084',
    'pre 084',
    'psb-sb-1202',
    'psb sb 1202',
    'r-31826',
    'r31826',
    'r 31826',
    'rh-34',
    'rh34',
    'rti-126',
    'rti126',
    'sch-5472',
    'sch5472',
    '2-(дифенилметил)-1-метилпиперидин-3-ол',
    'tfmpp',
    '1-(3-трифлюорометилфенил) пиперазин',
    'trifluoromethylphenyl',
    'tfmpp',
    'u-47700',
    'u47700',
    'u 47700',
    'u-48800',
    'u48800',
    'u 48800',
    'u-51754',
    'u51754',
    'u 51754',
    'urb602',
    'lt-290',
    'фенамин',
    'mhh',
    'a-3331',
    'доб',
    'дмгп',
    'dmhp',
    'дмт',
    'd2pm',
    'hydrochloride',
    'doc',
    'доэт',
    'диэтилтриптамин',
    'мбдб',
    'mbdb',
    'мдма',
    'mdma',
    'мдпв',
    'mdpv',
    'mmda',
    'мппп',
    'мфпп',
    'пепап',
    'стп (дом)',
    'stp',
    'dom',
    '2,5-диметокси-4-метиламфетамин',
    'mda',
    'тцп',
    'thc',
    'тма',
    'tma',
    'фцп',
    'pcp',
    'mcpp',
    '3-ho-pcp',
    '3-oh-pce',
    '4-mta',
    'bzp',
    'hu-308',
    'hu-331',
    'jwh-133',
    'jwh133',
    'mda-19',
    'urb-597',
    'papp',
    'тарен',
    'Abrus precatorius L.',
    'Aconitum L.',
    'Actaea L.',
    'Adinis L.',
    'Aethusa Cynapium L.',
    'Agastache rugosa O.Kuntze',
    'Alhagi pseudalhagi Fisch.',
    'Anagallis arvensis L.',
    'Anamirta cocculus Wight et Arn.',
    'Anemone sp.',
    'Anemone L.',
    'Aquilegia L.',
    'Arali elata',
    'Arali elata',
    'Areca catechu L.',
    'Argyreia nervosa',
    'Artemisia L.',
    'Arum L.',
    'Asarum L.',
    'Atropa belladonna L.',
    'Berberis L.',
    'Bryonia L.',
    'Carex L.',
    'Catha edulis Forsk.',
    'Catha edulis Forsk.',
    'Chamaedaphne calyculata Moench',
    'Chelidonium L.',
    'Cicuta L.',
    'Cida L.',
    'Claviceps sp.',
    'Claviceps sp.',
    'Clematis sp.',
    'Colchicum sp.',
    'Convolvulus L.',
    'Coptis L.',
    'Coronilla L.',
    'Coronilla L.',
    'Corydalis sp.',
    'Covid',
    'Covid',
    'Croton tiglium L.',
    'Cyclamen L.',
    'Cyclamen L.',
    'Laburnum anagyroides',
    'Daphne sp.',
    'Datura L.',
    'Delphinium L.',
    'Dicentra',
    'Dryopteris filix mas Schott.',
    'Echinopsis pachanoi',
    'Echinopsis L.',
    'Echium vulgaris L.',
    'Eleutherococcus senticosus',
    'Ephedra sp.',
    'Ephedra sp.',
    'Erysimum L.',
    'Euphorbia sp.',
    'Fritillaria ussuriensis Maxim.',
    'Gaillardia pulchella Foug.',
    'Galanthus woronowii Lozinsk.',
    'Galeopsis sp.',
    'Ginseng',
    'Glaucium L.',
    'Gomphocarpus L.',
    'Gratiola officinalis L.',
    'Gypsophila L.',
    'Haplophyllum',
    'Helleborus L.',
    'Hydrastis L.',
    'Ledum L.',
    'Lophophora williamsii',
    'Magnolia L.',
    'Mercurialis L.',
    'Moringa oleifera Lam.',
    'Myristica fragrans Hjuft',
    'Nerium L.',
    'Nicotiana L.',
    'Nymphaea Caerulea',
    'Oenanthe sp.',
    'Paeonia anomalae L.',
    'Papaver L.',
    'Papaver L.',
    'Papaver L.',
    'Papaver L.',
    'Papaver L.',
    'Paris L.',
    'Pedicularis sp.',
    'Peganum L.',
    'Peganum L.',
    'Peganum L.',
    'Pelargonium Willd.',
    'Pelargonium Willd.',
    'Phragmites Australia Trin. ex Steud.',
    'Physochlaina L.',
    'Phytolacca L.',
    'Phytolacca L.',
    'Piper betle L.',
    'Piper methysticum (kava-kava)',
    'Piper methysticum (kava-kava)',
    'Podophyllum L.',
    'Polygonatum L.',
    'Pulsatilla sp.',
    'Pygeum africanum',
    'Ranunculus L.',
    'Rhinanthus L.',
    'Rhodiola rosea L.',
    'Salsola australis R.Br.',
    'Salsola australis R.Br.',
    'Saponaria officinalis L.',
    'Saponaria officinalis L.',
    'Sassafras officinale albium',
    'Simmondsia californica Nutt.',
    'Stephania L.',
    'Strophanthus DC',
    'Strychnos L.',
    'Symphytum L.',
    'Tabebuia heptaphylla',
    'Thalictrum L.',
    'Thermopsis L.',
    'Thermopsis L.',
    'Thermopsis L.',
    'Turbina corymbosa',
    'Turbina corymbosa',
    'Urtica pilulifera L.',
    'Ustilago maydis DC.',
    'Utricularia physalis',
    'Valeriana L.',
    'Viscum L.',
    'Xanthium L.',
    'Yucca filamentosa',
    'Zygophyllum L.',
]

BAN_VAPE = [
    'HQD',
    'CUVIE',
    'Hqd',
    'RYSE',
    'Puff Bar',
    '2KAN',
    'PUFF BAR PLUS',
    'Megalink, MASKKING',
    'Puff Plus',
    'KADO',
    'Puff',
    'Bang',
    'Fizzy',
    'City',
    'Kingtons',
    'Jomotech',
    'easysmoke',
    'SKYI',
    'VOZOL',
    'JOOK',
    'FUEGOSTIX',
    'R&M'
]

BAN_OTHER = [
    'бита',
    'Бита',
    'Попперсы',
    'Бонг',
    'Конопля',
    'конопля',
    'Конопли',
    'конопли',
    'электрошокер',
    'электрошокером',
    'стики',
    'Оружие огнестрельное',
    'Оружие сигнальное',
    'Оружие газовое',
    'Боеприпасы',
    'Вооружение, боеприпасы к нему',
    'Взрывчатые вещества',
    'Средства взрывания',
    'Порох',
    'сабли',
    'шашки',
    'кинжалы',
    'финский нож',
    'кортик',
    'кастеты',
    'стилеты',
    'Перцовый баллончик',
    'anti-dog',
    'Прекурсоры',
    'Ртуть',
    'Ртутный термометр',
    'Ртутная лампа',
    'Жидкости для электронных парителей',
    'Раколовка',
    'Верша рыболовная',
    'Коробчатые',
    'штоковые',
    'Сети погружения',
    'Сеть подъема',
    'Тралы',
    'Зонтичная сеть',
    'Сеть для выуживания',
    'Л. Рон Хаббард',
    'нацизм',
    'война на украине',
    'иноагент',
    'Цифровая книга',
    'онлайн книга',
    'Нацизм',
    'Фашист',
    'Фюрер',
    'Нацист',
    'Национализм',
    'Вермахт',
    'Концлагерь',
    'Гитлеровец',
    'Нация',
    'Оккупация,',
    'Оккупант',
    'Антисемитизм',
    'Война',
    'Идеология',
    'Эсэсовец',
    'Националист',
    'Холокост',
    'Наклейка на номер',
    'Золотые слитки'
]

BAN_SEED =[
'Мухомор',
'2-cd',
'Альфапвп',
'Амф',
'амфетамин',
'Аяваска',
'Бошки',
'Бупренорфин',
'Гашиш',
'анаша',
'смола каннабиса',
'Героин',
'диацетилморфин',
'Дезоморфин',
'Диоксафетил бутират',
'ДМТ',
'DMT',
'Каннабис',
'каннабинол',
'марихуана',
'Кетамин',
'Кодеин',
'Кокаин',
'Крек',
'Крокодил',
'Лизергиновая кислота',
'Лист кока',
'ЛСД',
'Lcd',
'Маковая солома',
'Марки',
'Масло каннабиса',
'гашишное масло',
'МДА',
'тенамфетамин',
'ММДА',
'МДМА',
'MDMA',
'MDA',
'molly',
'мадам',
'Мескалин',
'Метадон',
'фенадон',
'долофин',
'Метаквало',
'Мефедрон',
'Мирофин',
'Морфин, морфий',
'Мяу',
'Опий',
'Опийсырец',
'Опиаты',
'опиум',
'Орипавин',
'Первитин',
'Псилоцибин, псилоцин',
'Сибирь',
'спиды',
'Фентанил',
'Фенциклидин',
'Экстази',
'Экстракт маковой соломы',
'концентрат маковой соломы',
'Эскодол',
'Этилморфин',
'Эфедрин',
'Эфедрон',
'меткатинон',
'Marihuana',
'Марихуана',
'Марихуанна',
'трава',
'Wax',
'Каннабидиол',
'cbd',
'Закладки',
'наркотиков',
]
