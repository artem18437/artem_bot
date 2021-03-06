
import random

A_cities = ['Абакан', 'Азов', 'Александров', 'Алексин', 'Альметьевск', 'Анапа', 'Ангарск', 'Анжеро-Судженск', 'Апатиты',
            'Арзамас', 'Армавир', 'Арсеньев', 'Артем', 'Архангельск', 'Асбест', 'Астрахань', 'Ачинск']
B_cities = ['Балаково', 'Балахна', 'Балашиха', 'Балашов', 'Барнаул', 'Батайск', 'Белгород', 'Белебей', 'Белово',
            'Белогорск', 'Белорецк', 'Белореченск', 'Бердск', 'Березники', 'Березовский', 'Бийск', 'Биробиджан',
            'Благовещенск', 'Бор', 'Борисоглебск', 'Боровичи', 'Братск', 'Брянск', 'Бугульма', 'Буденновск', 'Бузулук',
            'Буйнакск']
V_cities = ['Видное', 'Владивосток', 'Владикавказ', 'Владимир', 'Волгоград', 'Волгодонск', 'Волжск', 'Волжский',
            'Вологда', 'Вольск', 'Воркута', 'Воронеж', 'Воскресенск', 'Воткинск', 'Всеволожск', 'Выборг', 'Выкса',
            'Вязьма']
G_cities = ['Гатчина', 'Геленджик', 'Георгиевск', 'Глазов', 'Горно-Алтайск', 'Грозный', 'Губкин', 'Гудермес', 'Гуково',
            'Гусь-Хрустальный']
D_cities = ['Дербент', 'Дзержинск', 'Димитровград', 'Дмитров', 'Долгопрудный', 'Домодедово', 'Донской', 'Дубна']
E_cities = ['Евпатория', 'Егорьевск', 'Ейск', 'Екатеринбург', 'Елабуга', 'Елец', 'Ессентуки']
ZH_cities = ['Железногорск', 'Железногорск', 'Жигулевск', 'Жуковский']
Z_cities = ['Заречный', 'Зеленогорск', 'Зеленодольск', 'Златоуст']
I_cities = ['Иваново', 'Ивантеевка', 'Ижевск', 'Избербаш', 'Иркутск', 'Искитим', 'Ишим', 'Ишимбай']
K_cities = ['Казань', 'Калининград', 'Калуга', 'Каменск-Уральский', 'Каменск-Шахтинский', 'Камышин', 'Канск',
            'Каспийск', 'Кемерово', 'Керчь', 'Кинешма', 'Кириши', 'Киров', 'Кирово-Чепецк', 'Киселевск', 'Кисловодск',
            'Клин', 'Клинцы', 'Ковров', 'Когалым', 'Коломна', 'Комсомольск-на-Амуре', 'Копейск', 'Королев', 'Кострома',
            'Котлас', 'Красногорск', 'Краснодар', 'Краснокаменск', 'Краснокамск', 'Краснотурьинск', 'Красноярск',
            'Кропоткин', 'Крымск', 'Кстово', 'Кузнецк', 'Кумертау', 'Кунгур', 'Курган', 'Курск', 'Кызыл']
L_cities = ['Лабинск', 'Лениногорск', 'Ленинск-Кузнецкий', 'Лесосибирск', 'Липецк', 'Лиски', 'Лобня', 'Лысьва',
            'Лыткарино', 'Люберцы']
M_cities = ['Магадан', 'Магнитогорск', 'Майкоп', 'Махачкала', 'Междуреченск', 'Мелеуз', 'Миасс', 'Минеральные-Воды',
            'Минусинск', 'Михайловка', 'Мичуринск', 'Москва', 'Мурманск', 'Муром', 'Мытищи', ]
N_cities = ['Набережные-Челны', 'Назарово', 'Назрань', 'Нальчик', 'Наро-Фоминск', 'Находка', 'Невинномысск', 'Нерюнгри',
            'Нефтекамск', 'Нефтеюганск', 'Нижневартовск', 'Нижнекамск', 'Нижний-Новгород', 'Нижний-Тагил',
            'Новоалтайск', 'Новокузнецк', 'Новокуйбышевск', 'Новомосковск', 'Новороссийск', 'Новосибирск', 'Новотроицк',
            'Новоуральск', 'Новочебоксарск', 'Новочеркасск', 'Новошахтинск', 'Новый-Уренгой', 'Ногинск', 'Норильск',
            'Ноябрьск', 'Нягань']
O_cities = ['Обнинск', 'Одинцово', 'Октябрьский', 'Омск', 'Орел', 'Оренбург', 'Орехово-Зуево', 'Орск']
P_cities = ['Павлово', 'Павловский-Посад', 'Пенза', 'Первоуральск', 'Пермь', 'Петрозаводск', 'Петропавловск-Камчатский',
            'Подольск', 'Полевской', 'Прокопьевск', 'Прохладный', 'Псков', 'Пушкино', 'Пятигорск']
R_cities = ['Раменское', 'Ревда', 'Реутов', 'Ржев', 'Рославль', 'Россошь', 'Ростов-на-Дону', 'Рубцовск', 'Рыбинск',
            'Рязань']
S_cities = ['Салават', 'Сальск', 'Самара', 'Санкт-Петербург', 'Саранск', 'Сарапул', 'Саратов', 'Саров', 'Свободный',
            'Севастополь', 'Северодвинск', 'Северск', 'Сергиев-Посад', 'Серов', 'Серпухов', 'Сертолово', 'Сибай',
            'Симферополь', 'Славянск-на-Кубани', 'Смоленск', 'Соликамск', 'Солнечногорск', 'Сосновый-Бор', 'Сочи',
            'Ставрополь', 'Оскол', 'Стерлитамак', 'Ступино', 'Сургут', 'Сызрань', 'Сыктывкар']
T_cities = ['Таганрог', 'Тамбов', 'Тверь', 'Тимашевск', 'Тихвин', 'Тихорецк', 'Тобольск', 'Тольятти', 'Томск', 'Троицк',
            'Туапсе', 'Туймазы', 'Тула', 'Тюмень']
U_cities = ['Узловая', 'Улан-Удэ', 'Ульяновск', 'Урус-Мартан', 'Усолье-Сибирское', 'Уссурийск', 'Усть-Илимск', 'Уфа',
            'Ухта']
F_cities = ['Феодосия', 'Фрязино']
H_cities = ['Хабаровск', 'Хадыженск', 'Ханты-Мансийск', 'Харабали', 'Харовск', 'Хасавюрт', 'Хвалынск', 'Хилок', 'Химки',
            'Холм', 'Холмск', 'Хотьково']
C_cities = ['Цивильск', 'Цимлянск', 'Циолковский']
CH_cities = ['Чайковский', 'Чапаевск', 'Чебоксары', 'Челябинск', 'Черемхово', 'Череповец', 'Черкесск', 'Черногорск',
             'Чехов', 'Чистополь', 'Чита']
SH_cities = ['Шадринск', 'Шали', 'Шахты', 'Шуя']
SH2_cities = ['Щекино', 'Щелково']
E2_cities = ['Электросталь', 'Элиста', 'Энгельс']
YU_cities = ['Южно-Сахалинск', 'Юрга']
YA_cities = ['Якутск', 'Ялта', 'Ярославль']

all_cities = []
all_cities.extend(A_cities)
all_cities.extend(B_cities)
all_cities.extend(V_cities)
all_cities.extend(G_cities)
all_cities.extend(D_cities)
all_cities.extend(E_cities)
all_cities.extend(ZH_cities)
all_cities.extend(Z_cities)
all_cities.extend(I_cities)
all_cities.extend(K_cities)
all_cities.extend(L_cities)
all_cities.extend(M_cities)
all_cities.extend(N_cities)
all_cities.extend(O_cities)
all_cities.extend(P_cities)
all_cities.extend(R_cities)
all_cities.extend(S_cities)
all_cities.extend(T_cities)
all_cities.extend(U_cities)
all_cities.extend(F_cities)
all_cities.extend(C_cities)
all_cities.extend(CH_cities)
all_cities.extend(SH_cities)
all_cities.extend(SH2_cities)
all_cities.extend(H_cities)
all_cities.extend(E2_cities)
all_cities.extend(YU_cities)
all_cities.extend(YA_cities)
print(YA_cities)
A_cities = ['Абакан', 'Азов', 'Александров', 'Алексин', 'Альметьевск', 'Анапа', 'Ангарск', 'Анжеро-Судженск', 'Апатиты',
            'Арзамас', 'Армавир', 'Арсеньев', 'Артем', 'Архангельск', 'Асбест', 'Астрахань', 'Ачинск']
B_cities = ['Балаково', 'Балахна', 'Балашиха', 'Балашов', 'Барнаул', 'Батайск', 'Белгород', 'Белебей', 'Белово',
            'Белогорск', 'Белорецк', 'Белореченск', 'Бердск', 'Березники', 'Березовский', 'Бийск', 'Биробиджан',
            'Благовещенск', 'Бор', 'Борисоглебск', 'Боровичи', 'Братск', 'Брянск', 'Бугульма', 'Буденновск', 'Бузулук',
            'Буйнакск']
V_cities = ['Видное', 'Владивосток', 'Владикавказ', 'Владимир', 'Волгоград', 'Волгодонск', 'Волжск', 'Волжский',
            'Вологда', 'Вольск', 'Воркута', 'Воронеж', 'Воскресенск', 'Воткинск', 'Всеволожск', 'Выборг', 'Выкса',
            'Вязьма']
G_cities = ['Гатчина', 'Геленджик', 'Георгиевск', 'Глазов', 'Горно-Алтайск', 'Грозный', 'Губкин', 'Гудермес', 'Гуково',
            'Гусь-Хрустальный']
D_cities = ['Дербент', 'Дзержинск', 'Димитровград', 'Дмитров', 'Долгопрудный', 'Домодедово', 'Донской', 'Дубна']
E_cities = ['Евпатория', 'Егорьевск', 'Ейск', 'Екатеринбург', 'Елабуга', 'Елец', 'Ессентуки']
ZH_cities = ['Железногорск', 'Железногорск', 'Жигулевск', 'Жуковский']
Z_cities = ['Заречный', 'Зеленогорск', 'Зеленодольск', 'Златоуст']
I_cities = ['Иваново', 'Ивантеевка', 'Ижевск', 'Избербаш', 'Иркутск', 'Искитим', 'Ишим', 'Ишимбай']
K_cities = ['Казань', 'Калининград', 'Калуга', 'Каменск-Уральский', 'Каменск-Шахтинский', 'Камышин', 'Канск',
            'Каспийск', 'Кемерово', 'Керчь', 'Кинешма', 'Кириши', 'Киров', 'Кирово-Чепецк', 'Киселевск', 'Кисловодск',
            'Клин', 'Клинцы', 'Ковров', 'Когалым', 'Коломна', 'Комсомольск-на-Амуре', 'Копейск', 'Королев', 'Кострома',
            'Котлас', 'Красногорск', 'Краснодар', 'Краснокаменск', 'Краснокамск', 'Краснотурьинск', 'Красноярск',
            'Кропоткин', 'Крымск', 'Кстово', 'Кузнецк', 'Кумертау', 'Кунгур', 'Курган', 'Курск', 'Кызыл']
L_cities = ['Лабинск', 'Лениногорск', 'Ленинск-Кузнецкий', 'Лесосибирск', 'Липецк', 'Лиски', 'Лобня', 'Лысьва',
            'Лыткарино', 'Люберцы']
M_cities = ['Магадан', 'Магнитогорск', 'Майкоп', 'Махачкала', 'Междуреченск', 'Мелеуз', 'Миасс', 'Минеральные-Воды',
            'Минусинск', 'Михайловка', 'Мичуринск', 'Москва', 'Мурманск', 'Муром', 'Мытищи', ]
N_cities = ['Набережные-Челны', 'Назарово', 'Назрань', 'Нальчик', 'Наро-Фоминск', 'Находка', 'Невинномысск', 'Нерюнгри',
            'Нефтекамск', 'Нефтеюганск', 'Нижневартовск', 'Нижнекамск', 'Нижний-Новгород', 'Нижний-Тагил',
            'Новоалтайск', 'Новокузнецк', 'Новокуйбышевск', 'Новомосковск', 'Новороссийск', 'Новосибирск', 'Новотроицк',
            'Новоуральск', 'Новочебоксарск', 'Новочеркасск', 'Новошахтинск', 'Новый-Уренгой', 'Ногинск', 'Норильск',
            'Ноябрьск', 'Нягань']
O_cities = ['Обнинск', 'Одинцово', 'Октябрьский', 'Омск', 'Орел', 'Оренбург', 'Орехово-Зуево', 'Орск']
P_cities = ['Павлово', 'Павловский-Посад', 'Пенза', 'Первоуральск', 'Пермь', 'Петрозаводск', 'Петропавловск-Камчатский',
            'Подольск', 'Полевской', 'Прокопьевск', 'Прохладный', 'Псков', 'Пушкино', 'Пятигорск']
R_cities = ['Раменское', 'Ревда', 'Реутов', 'Ржев', 'Рославль', 'Россошь', 'Ростов-на-Дону', 'Рубцовск', 'Рыбинск',
            'Рязань']
S_cities = ['Салават', 'Сальск', 'Самара', 'Санкт-Петербург', 'Саранск', 'Сарапул', 'Саратов', 'Саров', 'Свободный',
            'Севастополь', 'Северодвинск', 'Северск', 'Сергиев-Посад', 'Серов', 'Серпухов', 'Сертолово', 'Сибай',
            'Симферополь', 'Славянск-на-Кубани', 'Смоленск', 'Соликамск', 'Солнечногорск', 'Сосновый-Бор', 'Сочи',
            'Ставрополь', 'Оскол', 'Стерлитамак', 'Ступино', 'Сургут', 'Сызрань', 'Сыктывкар']
T_cities = ['Таганрог', 'Тамбов', 'Тверь', 'Тимашевск', 'Тихвин', 'Тихорецк', 'Тобольск', 'Тольятти', 'Томск', 'Троицк',
            'Туапсе', 'Туймазы', 'Тула', 'Тюмень']
U_cities = ['Узловая', 'Улан-Удэ', 'Ульяновск', 'Урус-Мартан', 'Усолье-Сибирское', 'Уссурийск', 'Усть-Илимск', 'Уфа',
            'Ухта']
F_cities = ['Феодосия', 'Фрязино']
H_cities = ['Хабаровск', 'Хадыженск', 'Ханты-Мансийск', 'Харабали', 'Харовск', 'Хасавюрт', 'Хвалынск', 'Хилок', 'Химки',
            'Холм', 'Холмск', 'Хотьково']
C_cities = ['Цивильск', 'Цимлянск', 'Циолковский']
CH_cities = ['Чайковский', 'Чапаевск', 'Чебоксары', 'Челябинск', 'Черемхово', 'Череповец', 'Черкесск', 'Черногорск',
             'Чехов', 'Чистополь', 'Чита']
SH_cities = ['Шадринск', 'Шали', 'Шахты', 'Шуя']
SH2_cities = ['Щекино', 'Щелково']
E2_cities = ['Электросталь', 'Элиста', 'Энгельс']
YU_cities = ['Южно-Сахалинск', 'Юрга']
YA_cities = ['Якутск', 'Ялта', 'Ярославль']
print(A_cities)
start = random.choice(all_cities)
print(start)

inp = str(input())
end_symbol = (inp[-1::])
while inp not in all_cities:
    print('Нужно ввести название города!')
    inp = str(input())
Eend_symbol = (start[-1::])
if Eend_symbol == 'ь' or Eend_symbol == 'ъ' or Eend_symbol == 'ы' or Eend_symbol == 'ё' or Eend_symbol == 'й':
    Eend_symbol =(start[-2:-1:])
if end_symbol == 'ь' or end_symbol == 'ъ' or end_symbol == 'ы' or end_symbol == 'ё' or end_symbol == 'й':
    end_symbol = (inp[-2:-1:])
if inp[0:1:] != start[-1::]:

    while inp[0:1:] != start[-1::]:

        if inp[0:1:] != start[-1::]:
            print('Введите город ещё раз')
            inp = str(input())
            inp = inp.lower()
inp = inp[0:1:].upper() + inp[1::]
first_simbol = (inp[0:1:])
Efirst_simbol = (start[0:1:])

if inp in all_cities and start in all_cities:
    while inp != 'стоп':
        if end_symbol == 'ь' or end_symbol == 'ъ' or end_symbol == 'ы' or end_symbol == 'ё' or end_symbol == 'й':
            end_symbol = (inp[-2:-1:])
        if Eend_symbol == 'ь' or Eend_symbol == 'ъ' or Eend_symbol == 'ы' or Eend_symbol == 'ё' or Eend_symbol == 'й':
            Eend_symbol = (start[-2:-1:])

        if Efirst_simbol == 'А':
            all_cities.remove(start)
            A_cities.remove(start)
        elif Efirst_simbol == 'Б':
            all_cities.remove(start)
            B_cities.remove(start)
        elif Efirst_simbol == 'В':
            print(all_cities)
            all_cities.remove(start)
            V_cities.remove(start)
        elif Efirst_simbol == 'Г':
            all_cities.remove(start)
            G_cities.remove(start)
        elif Efirst_simbol == 'Д':
            all_cities.remove(start)
            D_cities.remove(start)
        elif Efirst_simbol == 'Е':
            all_cities.remove(start)
            E_cities.remove(start)
        elif Efirst_simbol == 'Ж':
            all_cities.remove(start)
            ZH_cities.remove(start)
        elif Efirst_simbol == 'З':
            all_cities.remove(start)
            Z_cities.remove(start)
        elif Efirst_simbol == 'И':
            all_cities.remove(start)
            I_cities.remove(start)
        elif Efirst_simbol == 'К':
            print(all_cities)
            all_cities.remove(start)
            K_cities.remove(start)
        elif Efirst_simbol == 'Л':
            all_cities.remove(start)
            L_cities.remove(start)
        elif Efirst_simbol == 'М':
            all_cities.remove(start)
            M_cities.remove(start)
        elif Efirst_simbol == 'Н':
            print(all_cities)
            all_cities.remove(start)
            N_cities.remove(start)
        elif Efirst_simbol == 'О':
            print(all_cities)
            all_cities.remove(start)
            O_cities.remove(start)
        elif Efirst_simbol == 'П':
            print(all_cities)
            all_cities.remove(start)
            P_cities.remove(start)
        elif Efirst_simbol == 'Р':
            print(all_cities)
            all_cities.remove(start)
            R_cities.remove(start)
        elif Efirst_simbol == 'С':
            all_cities.remove(start)
            S_cities.remove(start)
        elif Efirst_simbol == 'Т':
            all_cities.remove(start)
            T_cities.remove(start)
        elif Efirst_simbol == 'У':
            print(all_cities)
            all_cities.remove(start)
            U_cities.remove(start)
        elif Efirst_simbol == 'Ф':
            all_cities.remove(start)
            F_cities.remove(start)
        elif Efirst_simbol == 'Х':
            all_cities.remove(start)
            H_cities.remove(start)
        elif Efirst_simbol == 'Ц':
            all_cities.remove(start)
            C_cities.remove(start)
        elif Efirst_simbol == 'Ч':
            all_cities.remove(start)
            CH_cities.remove(start)
        elif Efirst_simbol == 'Ш':
            all_cities.remove(start)
            SH_cities.remove(start)
        elif Efirst_simbol == 'Щ':
            all_cities.remove(start)
            SH2_cities.remove(start)
        elif Efirst_simbol == 'Э':
            all_cities.remove(start)
            E2_cities.remove(start)
        elif Efirst_simbol == 'Ю':
            all_cities.remove(start)
            YU_cities.remove(start)
        elif Efirst_simbol == 'Я':
            all_cities.remove(start)
            YA_cities.remove(start)

        if inp in all_cities:
            if first_simbol == 'А':
                all_cities.remove(inp)
                A_cities.remove(inp)
            elif first_simbol == 'Б':
                all_cities.remove(inp)
                B_cities.remove(inp)
            elif first_simbol == 'В':
                all_cities.remove(inp)
                V_cities.remove(inp)
            elif first_simbol == 'Г':
                all_cities.remove(inp)
                G_cities.remove(inp)
            elif first_simbol == 'Д':
                all_cities.remove(inp)
                D_cities.remove(inp)
            elif first_simbol == 'Е':
                all_cities.remove(inp)
                E_cities.remove(inp)
            elif first_simbol == 'Ж':
                all_cities.remove(inp)
                ZH_cities.remove(inp)
            elif first_simbol == 'З':
                all_cities.remove(inp)
                Z_cities.remove(inp)
            elif first_simbol == 'И':
                all_cities.remove(inp)
                I_cities.remove(inp)
            elif first_simbol == 'К':
                all_cities.remove(inp)
                K_cities.remove(inp)
            elif first_simbol == 'Л':
                all_cities.remove(inp)
                L_cities.remove(inp)
            elif first_simbol == 'М':
                all_cities.remove(inp)
                M_cities.remove(inp)
            elif first_simbol == 'Н':
                all_cities.remove(inp)
                N_cities.remove(inp)
            elif first_simbol == 'О':
                all_cities.remove(inp)
                O_cities.remove(inp)
            elif first_simbol == 'П':
                all_cities.remove(inp)
                P_cities.remove(inp)
            elif first_simbol == 'Р':
                all_cities.remove(inp)
                R_cities.remove(inp)
            elif first_simbol == 'С':
                all_cities.remove(inp)
                S_cities.remove(inp)
            elif first_simbol == 'Т':
                all_cities.remove(inp)
                T_cities.remove(inp)
            elif first_simbol == 'У':
                all_cities.remove(inp)
                U_cities.remove(inp)
            elif first_simbol == 'Ф':
                all_cities.remove(inp)
                F_cities.remove(inp)
            elif first_simbol == 'Х':
                all_cities.remove(inp)
                H_cities.remove(inp)
            elif first_simbol == 'Ц':
                all_cities.remove(inp)
                C_cities.remove(inp)
            elif first_simbol == 'Ч':
                all_cities.remove(inp)
                CH_cities.remove(inp)
            elif first_simbol == 'Ш':
                all_cities.remove(inp)
                SH_cities.remove(inp)
            elif first_simbol == 'Щ':
                all_cities.remove(inp)
                SH2_cities.remove(inp)
            elif first_simbol == 'Э':
                all_cities.remove(inp)
                E2_cities.remove(inp)
            elif first_simbol == 'Ю':
                all_cities.remove(inp)
                YU_cities.remove(inp)
            elif first_simbol == 'Я':
                all_cities.remove(inp)
                YA_cities.remove(inp)

        end_symbol = (inp[-1::])
        Eend_symbol = (start[-1::])
        if end_symbol == 'ь' or end_symbol == 'ъ' or end_symbol == 'ы' or end_symbol == 'ё' or end_symbol == 'й':
            end_symbol == (inp[-2:-1:])
        if Eend_symbol == 'ь' or Eend_symbol == 'ъ' or Eend_symbol == 'ы' or Eend_symbol == 'ё' or Eend_symbol == 'й':
            Eend_symbol == (start[-2:-1:])
        #
        if inp[0:1:].lower() == Eend_symbol:
            if end_symbol == 'а':
                A = random.choice(A_cities)
                print(A)
            elif end_symbol == 'б':
                B = random.choice(B_cities)
                print(B)
            elif end_symbol == 'в':
                V = random.choice(V_cities)
                print(V)
            elif end_symbol == 'г':
                G = random.choice(G_cities)
                print(G)
            elif end_symbol == 'д':
                D = random.choice(D_cities)
                print(D)
            elif end_symbol == 'е':
                E = random.choice(E_cities)
                print(E)
            elif end_symbol == 'ж':
                ZH = random.choice(ZH_cities)
                print(ZH)
            elif end_symbol == 'з':
                Z = random.choice(Z_cities)
                print(Z)
            elif end_symbol == 'и':
                I = random.choice(I_cities)
                print(I)
            elif end_symbol == 'к':
                K = random.choice(K_cities)
                print(K)
            elif end_symbol == 'л':
                L = random.choice(L_cities)
                print(L)
            elif end_symbol == 'м':
                M = random.choice(M_cities)
                print(M)
            elif end_symbol == 'н':
                N = random.choice(N_cities)
                print(N)
            elif end_symbol == 'о':
                O = random.choice(O_cities)
                print(O)
            elif end_symbol == 'п':
                P = random.choice(P_cities)
                print(P)
            elif end_symbol == 'р':
                R = random.choice(R_cities)
                print(R)
            elif end_symbol == 'с':
                S = random.choice(S_cities)
                print(S)
            elif end_symbol == 'т':
                T = random.choice(T_cities)
                print(T)
            elif end_symbol == 'у':
                U = random.choice(U_cities)
                print(U)
            elif end_symbol == 'ф':
                F = random.choice(F_cities)
                pint(F)
            elif end_symbol == 'х':
                H = random.choice(H_cities)
                print(H)
            elif end_symbol == 'ц':
                C = random.choice(C_cities)
                print(C)
            elif end_symbol == 'ч':
                CH = random.choice(CH_cities)
                print(CH)
            elif end_symbol == 'ш':
                SH = random.choice(SH_cities)
                print(SH)
            elif end_symbol == 'щ':
                SH2 = random.choice(SH2_cities)
                print(SH2)
            elif end_symbol == 'э':
                E2 = random.choice(E2_cities)
                print(E2)
            elif end_symbol == 'ю':
                YU = random.choice(YU_cities)
                print(YU)
            elif end_symbol == 'я':
                YA = random.choice(YA_cities)
                print(YA)