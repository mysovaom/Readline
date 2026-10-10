import json




# ПЕРЕМЕННЫЕ
onegins_pages=0
all_pages=0

#-------------
def start_giver(filename):
    if filename == "Onegin.json":
        global onegins_pages
        return onegins_pages * 20
    return None


def get_lines(filename, start, count=20):
    """Получить count строк из файла начиная с start."""
    start = start_giver(filename)
    with open(filename, "r", encoding="utf-8") as f:
        text = json.load(f)

    while isinstance(text, str):
        try:
            text = json.loads(text)
        except json.JSONDecodeError:
            break

    if isinstance(text, list):
        lines = text
    elif isinstance(text, str):
        lines = text.split("\n")
    else:
        lines = str(text).split("\n")

    return lines[start:start + count]


def print_page(filename, start, count=20):
    """Напечатать count строк каждая на своей строке."""
    for line in get_lines(filename, start, count):
        # strip() убирает пробелы и \n
        # strip('"') убирает кавычки
        clean = line.strip().strip('"')
        print(clean)

def flip_onegin():
    global onegins_pages
    global all_pages
    onegins_pages += 1
    all_pages += 1
    print_page("Onegin.json", onegins_pages)

def mark_date():
    key_ivent = input("Введите название события:")
    ivent_data = input("Введите дату в формате дд.мм.гггг:")
    with open("ivents.json", "r", encoding="utf-8") as f:
        ivents = json.load(f)
    ivents[key_ivent] = ivent_data
    with open("ivents.json", "w", encoding="utf-8") as f:
        json.dump(ivents, f, ensure_ascii=False, indent=4)

def show_ivents():
    with open("ivents.json", "r", encoding="utf-8") as f:
        ivents = json.load(f)
    for key in ivents:
        print(f"{key}: {ivents[key]}")

def exit():
    with open("variables.json", "w", encoding="utf-8") as f:
        json.dump({"onegins_pages": onegins_pages}, f, indent=4, ensure_ascii=False)
        json.dump({"all_pages": all_pages}, f, indent=4, ensure_ascii=False)





# print('Вас приветствует программа Readline!\n Моя программа для чтения электронных книг и для контроля дедлайнов\n Сейчас в наличии только книга Александра Сергеевича Пушкина "Евгений Онегин"')
# print('Вы можете:\n1.Начать читать "Евгений Онегин"\n2.Выйти\n3.Отметить в электронном календаре событие\n4.Просмотреть все события')
flip_onegin()
flip_onegin()
flip_onegin()
print(onegins_pages, all_pages)
exit()