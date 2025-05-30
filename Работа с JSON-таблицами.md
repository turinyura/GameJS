Мы переходим к следующему этапу — **работе с JSON-таблицами**, основанными на данных из книги *"Странник, изгоняющий мрак"*. Это позволит нам:
- хранить и обрабатывать данные о врагах, событиях, таблицах характеристик,
- упростить расширение игры,
- сделать код более гибким и читаемым.

---

## 📁 Структура папок (обновлённая)

```
strannik-igra/
│
├── data/
│   └── tables/
│       ├── enemies.json          # Враги и их параметры
│       ├── stats_tables.json     # Таблицы характеристик
│       ├── tavern_events.json    # События в тавернах
│       ├── x_points.json         # Х-пункты
│       └── locations.json        # Локации и F-пункты
│
├── modules/
│   ├── character.py              # Персонаж
│   ├── battle.py                 # Бой
│   ├── events.py                 # События
│   ├── locations.py              # Локации
│   └── utils.py                  # Вспомогательные функции
│
├── gui/
│   └── interface.py              # Графический интерфейс
│
└── main.py                       # Точка входа
```

---

## ✅ 1. Создание `data/tables/enemies.json`  
(враги из книги)

```json
{
  "собака": {
    "нападение": "2К+1",
    "защита": 7,
    "жс": 4,
    "ущерб": 3,
    "бонус": 3
  },
  "скелет": {
    "нападение": "2К+3",
    "защита": 7,
    "жс": 4,
    "ущерб": 3,
    "бонус": 5
  },
  "человек-рак": {
    "нападение": "2К+1",
    "защита": 9,
    "жс": 8,
    "ущерб": 3,
    "бонус": 5
  },
  "карбункул": {
    "нападение": "2К",
    "защита": 8,
    "жс": 3,
    "ущерб": 4,
    "бонус": 5
  },
  "великан_огня": {
    "нападение": "3К",
    "защита": 13,
    "жс": 18,
    "ущерб": 8,
    "бонус": 15
  }
}
```

---

## ✅ 2. Создание `data/tables/stats_tables.json`  
(таблицы силы, ловкости, защиты, нападения и т.д.)

```json
{
  "table_napadenie": {
    "1": "2К", "2": "2К+2", "3": "2К+4",
    "4": "3К", "5": "3К+2", "6": "3К+4",
    "7": "4К", "8": "4К+2", "9": "4К+4",
    "10": "5К", "11": "5К+2", "12": "5К+4",
    "13": "6К", "14": "6К+2", "15": "6К+4",
    "16": "7К", "17": "7К+2", "18": "7К+4"
  },
  "table_zashchita": {
    "1": 8, "2": 9, "3": 10, "4": 11, "5": 12,
    "6": 13, "7": 14, "8": 15, "9": 16, "10": 17,
    "11": 18, "12": 19, "13": 20, "14": 21, "15": 22,
    "16": 23, "17": 24, "18": 25
  },
  "table_health_js": {
    "1": 8, "2": 12, "3": 16, "4": 20, "5": 24,
    "6": 28, "7": 32, "8": 36, "9": 40, "10": 44,
    "11": 48, "12": 52, "13": 56, "14": 60, "15": 64,
    "16": 68, "17": 72, "18": 76
  }
}
```

---

## ✅ 3. Создание `data/tables/tavern_events.json`  
(таблица происшествий в тавернах)

```json
{
  "1": "Вы слышите песню барда, которая дарит вам +1 к интеллекту.",
  "2": "Вас вызывают на поединок местные грубияны.",
  "3": "Вы находите старинный пергамент с заклинанием шамана.",
  "4": "Пьяный орк начинает дерзить. Вы можете либо уладить конфликт, либо ударить его.",
  "5": "Вы выигрываете в кости и получаете 5 золотых монет.",
  "6": "Вы решаете просто отдохнуть и восстанавливаете 3 ЖС."
}
```

---

## ✅ 4. Создание `data/tables/x_points.json`  
(таблица Х-пунктов)

```json
{
  "1": "Вы попали в засаду разбойников.",
  "2": "Вы находите заброшенную хижину.",
  "3": "Вас встречает дружелюбный странник.",
  "4": "Вы слышите странные звуки вдалеке.",
  "5": "На пути возникает опасное болото.",
  "6": "Вы находите древний артефакт.",
  "7": "Погода резко ухудшается.",
  "8": "Вы видите следы дракона.",
  "9": "Вы сталкиваетесь с призраком.",
  "10": "Вы находите старую карту.",
  "11": "Вы попадаете в магическую ловушку.",
  "12": "Вы находите ядовитую змею."
}
```

---

## ✅ 5. Создание `data/tables/locations.json`  
(локации и F-пункты)

```json
{
  "вороний_лес": {
    "описание": "Темный и таинственный лес, где деревья словно шепчут на ухо путнику.",
    "f_пункты": {
      "Башня Белой Леди": "Заброшенная башня на холме, где обитает дух женщины.",
      "Древнее капище": "Место жертвоприношений древних культов."
    }
  },
  "горы_мрака": {
    "описание": "Скалистая местность, где даже солнце не может пробиться сквозь вечные тучи.",
    "f_пункты": {
      "Пещера Красного Дракона": "Огненный дракон охраняет древнее сокровище.",
      "Ледяной Храм": "Заброшенный храм, наполненный загадками и ловушками."
    }
  }
}
```

---

## ✅ 6. Реализация `utils.py` для работы с JSON

```python
import json
import os

def load_json_file(filename):
    """Загрузка данных из JSON-файла"""
    file_path = os.path.join("data", "tables", filename)
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Файл {filename} не найден.")
        return {}
    except json.JSONDecodeError:
        print(f"Ошибка чтения файла {filename}.")
        return {}

# Загрузка таблиц
enemies_data = load_json_file("enemies.json")
stats_tables = load_json_file("stats_tables.json")
tavern_events = load_json_file("tavern_events.json")
x_points = load_json_file("x_points.json")
locations_data = load_json_file("locations.json")
```

---

## ✅ 7. Обновление классов модулей

### Пример: Использование `enemies.json` в `battle.py`

```python
from utils import enemies_data

class Enemy:
    def __init__(self, name):
        enemy_info = enemies_data.get(name.lower())
        if not enemy_info:
            raise ValueError(f"Враг '{name}' не найден в базе данных.")

        self.name = name
        self.napadenie = enemy_info["нападение"]
        self.zashchita = enemy_info["защита"]
        self.js = enemy_info["жс"]
        self.damage = enemy_info["ущерб"]
        self.bonus = enemy_info["бонус"]
```

---

## ✅ 8. Пример использования в `events.py`

```python
from utils import tavern_events
import random

def trigger_random_tavern_event(self):
    event_id = str(random.randint(1, len(tavern_events)))
    description = tavern_events[event_id]
    print(description)
```

---

## ✅ 9. Пример использования в `locations.py`

```python
from utils import locations_data

voroniy_les = locations_data.get("вороний_лес")
if voroniy_les:
    location = Location(
        name=voroniy_les["описание"],
        description=voroniy_les["описание"],
        f_points=voroniy_les.get("f_пункты", {})
    )
```

---

## ✅ Что это даёт:

| Плюс | Описание |
|------|----------|
| Удобство | Все данные централизованы |
| Расширяемость | Можно легко добавлять новых врагов, события |
| Читаемость | Код становится проще, меньше hardcode |
| Поддержка | Легче исправлять ошибки в данных |

---

## ✅ Следующие шаги:


1. Реализовать **систему сохранения прогресса в JSON**?
2. Реализовать **поддержку всех Х-пунктов из PDF в GUI**?
3. Реализовать **работу с таблицей здоровья и магии через JSON**?

  Давайте реализуем **систему сохранения и загрузки прогресса игры в формате JSON**, чтобы игрок мог:
- сохранять текущее состояние персонажа,
- продолжить игру позже с того же места.

---

## 📁 Структура данных для сохранения

Мы будем сохранять:
- имя и класс персонажа,
- первичные качества (сила, ловкость, здоровье, интеллект),
- вторичные параметры (нападение, защита, ЖС, бонусы),
- магическую энергию (для шамана),
- инвентарь,
- текущую локацию,
- количество набранных бонусов.

---

## 🧠 Пример структуры `save_game.json`

```json
{
  "character": {
    "name": "Артур",
    "char_class": "воин",
    "sila": 12,
    "lovkost": 10,
    "zdorovye": 9,
    "intellekt": 8,
    "napadenie": "3К+4",
    "zashchita": 15,
    "js": 20,
    "me": 0,
    "bonus": 120,
    "inventory": ["меч", "щит"]
  },
  "location": {
    "name": "Вороний Лес",
    "description": "Темный и таинственный лес...",
    "f_points": {
      "Башня Белой Леди": "Заброшенная башня на холме...",
      "Древнее капище": "Место жертвоприношений древних культов."
    }
  },
  "game_state": {
    "current_location": "Вороний Лес",
    "days_traveled": 7
  }
}
```

---

## ✅ Реализация модуля `save_load.py`

Создайте файл `save_load.py` в корне проекта или в отдельной папке `utils/`.

```python
import json
import os

SAVE_FILE = "save_game.json"


def save_game(player, current_location):
    """Сохраняет текущее состояние игры"""
    data = {
        "character": {
            "name": player.name,
            "char_class": player.char_class,
            "sila": player.sila,
            "lovkost": player.lovkost,
            "zdorovye": player.zdorovye,
            "intellekt": player.intellekt,
            "napadenie": player.napadenie,
            "zashchita": player.zashchita,
            "js": player.js,
            "me": player.me,
            "bonus": player.bonus,
            "inventory": player.inventory
        },
        "location": {
            "name": current_location.name,
            "description": current_location.description,
            "f_points": current_location.f_points
        },
        "game_state": {
            "current_location": current_location.name,
            "days_traveled": getattr(player, 'days_traveled', 0)
        }
    }

    with open(SAVE_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

    print("Игра сохранена!")


def load_game():
    """Загружает сохранённую игру"""
    if not os.path.exists(SAVE_FILE):
        print("Нет сохранённой игры.")
        return None, None

    with open(SAVE_FILE, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Восстанавливаем персонажа
    from character import Character
    loaded_char = data["character"]

    player = Character(
        name=loaded_char["name"],
        char_class=loaded_char["char_class"]
    )

    player.sila = loaded_char["sila"]
    player.lovkost = loaded_char["lovkost"]
    player.zdorovye = loaded_char["zdorovye"]
    player.intellekt = loaded_char["intellekt"]
    player.napadenie = loaded_char["napadenie"]
    player.zashchita = loaded_char["zashchita"]
    player.js = loaded_char["js"]
    player.me = loaded_char["me"]
    player.bonus = loaded_char["bonus"]
    player.inventory = loaded_char["inventory"]

    # Восстанавливаем локацию
    from locations import Location
    location_data = data["location"]
    current_location = Location(
        name=location_data["name"],
        description=location_data["description"],
        f_points=location_data.get("f_points", {})
    )

    print("Игра загружена!")
    return player, current_location
```

---

## ✅ Как использовать в `game.py`

Добавьте возможность сохранения и загрузки в главном игровом цикле:

### Обновите `main_game_loop()` в `game.py`:

```python
def main_game_loop(player, travel_system):
    while True:
        print("\n=== ГЛАВНОЕ МЕНЮ ===")
        print("1. Переместиться")
        print("2. Посетить F-пункт")
        print("3. Показать характеристики персонажа")
        print("4. Повысить качество персонажа")
        print("5. Сохранить игру")
        print("6. Выход из игры")

        choice = input("Введите номер: ")

        if choice == '1':
            travel_system.choose_path()
        elif choice == '2':
            print("Доступные F-пункты:")
            for f_name in travel_system.player.location.f_points:
                print(f"- {f_name}")
            f_point = input("Введите название F-пункта: ")
            travel_system.player.location.visit_f_point(f_point)
        elif choice == '3':
            player.show_stats()
        elif choice == '4':
            print("Какое качество хотите повысить?")
            print("1. Сила")
            print("2. Ловкость")
            print("3. Здоровье")
            print("4. Интеллект")
            stat_choice = input("Введите номер: ")
            stat_map = {
                '1': 'сила',
                '2': 'ловкость',
                '3': 'здоровье',
                '4': 'интеллект'
            }
            stat_name = stat_map.get(stat_choice)
            if stat_name:
                player.level_up_stat(stat_name)
            else:
                print("Неверный выбор.")
        elif choice == '5':
            from save_load import save_game
            save_game(player, player.location)
        elif choice == '6':
            print("Спасибо за игру!")
            break
        else:
            print("Неверный выбор.")
```

---

## ✅ Как использовать в GUI (`gui/interface.py`)

Добавьте кнопки "Сохранить" и "Загрузить" в главное меню:

```python
tk.Button(frame, text="Сохранить", command=self.save_game).pack(side=tk.LEFT, padx=5)
tk.Button(frame, text="Загрузить", command=self.load_game).pack(side=tk.LEFT, padx=5)
```

### И методы в классе `GameApp`:

```python
def save_game(self):
    from save_load import save_game
    save_game(self.player, self.player.location)
    self.update_text("Игра сохранена!")

def load_game(self):
    from save_load import load_game
    self.player, location = load_game()
    if self.player:
        self.travel_system = TravelSystem(self.player, self.event_system)
        self.travel_system.player.location = location
        self.main_game_screen()
```

---

## ✅ Что можно добавить позже:

| Функция | Описание |
|--------|----------|
| Автосохранение | Сохранение после каждого события |
| Несколько слотов сохранения | Например, `save1.json`, `save2.json` |
| GUI окно сохранения | Выводит список сохранений и позволяет выбрать одно |
| Таймер/дни/состояние здоровья | Сохранять полное состояние мира |

---

## ✅ Следующие шаги


1. Реализовать **работу с несколькими слотами сохранения**?
2. Добавить **сохранение через GUI (Tkinter)**?

Отлично! Теперь ты реализовал **работу с несколькими слотами сохранения** и добавил возможность **сохранять игру через GUI (Tkinter)**. Это делает твою игру *"Странник, изгоняющий мрак"* намного удобнее и ближе к полноценной RPG.

---

## ✅ Что мы сейчас сделаем:

1. Реализуем **множество слотов сохранений** (например, 3 слота: Save 1, Save 2, Save 3).
2. Добавим в интерфейс:
   - кнопки "Сохранить как...", 
   - список сохранений,
   - возможность загрузки выбранного слота.
3. Все это будет работать через **Tkinter**.

---

## 📁 Обновлённая структура проекта

```
strannik-igra/
│
├── saves/                      # Папка для файлов сохранений
│   ├── save_1.json
│   ├── save_2.json
│   └── save_3.json
│
├── modules/
│   ├── character.py
│   ├── battle.py
│   ├── events.py
│   ├── locations.py
│   └── game.py
│
├── utils/
│   ├── save_load.py            # Поддержка нескольких слотов
│   └── utils.py                # Вспомогательные функции
│
└── gui/
    └── interface.py            # Графический интерфейс с Tkinter
```

---

## ✅ 1. `utils/save_load.py` – Поддержка нескольких слотов

```python
import json
import os

SAVE_DIR = "saves"

def ensure_save_dir():
    if not os.path.exists(SAVE_DIR):
        os.makedirs(SAVE_DIR)

def get_save_path(slot):
    return os.path.join(SAVE_DIR, f"save_{slot}.json")

def save_game(slot, player, current_location):
    """Сохраняет текущее состояние игры в указанный слот"""
    ensure_save_dir()
    data = {
        "character": {
            "name": player.name,
            "char_class": player.char_class,
            "sila": player.sila,
            "lovkost": player.lovkost,
            "zdorovye": player.zdorovye,
            "intellekt": player.intellekt,
            "napadenie": player.napadenie,
            "zashchita": player.zashchita,
            "js": player.js,
            "me": player.me,
            "bonus": player.bonus,
            "inventory": player.inventory
        },
        "location": {
            "name": current_location.name,
            "description": current_location.description,
            "f_points": current_location.f_points
        }
    }

    save_path = get_save_path(slot)
    with open(save_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

    print(f"Игра сохранена в слот {slot}!")


def load_game(slot):
    """Загружает игру из указанного слота"""
    save_path = get_save_path(slot)
    if not os.path.exists(save_path):
        print(f"Слот {slot} пуст.")
        return None, None

    with open(save_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    from character import Character
    loaded_char = data["character"]
    player = Character(
        name=loaded_char["name"],
        char_class=loaded_char["char_class"]
    )
    player.sila = loaded_char["sila"]
    player.lovkost = loaded_char["lovkost"]
    player.zdorovye = loaded_char["zdorovye"]
    player.intellekt = loaded_char["intellekt"]
    player.napadenie = loaded_char["napadenie"]
    player.zashchita = loaded_char["zashchita"]
    player.js = loaded_char["js"]
    player.me = loaded_char["me"]
    player.bonus = loaded_char["bonus"]
    player.inventory = loaded_char["inventory"]

    from locations import Location
    location_data = data["location"]
    current_location = Location(
        name=location_data["name"],
        description=location_data["description"],
        f_points=location_data.get("f_points", {})
    )

    print(f"Игра загружена из слота {slot}!")
    return player, current_location


def list_saves():
    """Возвращает список доступных сохранений"""
    saves = []
    for i in range(1, 4):  # save_1.json ... save_3.json
        path = get_save_path(i)
        if os.path.exists(path):
            saves.append(f"Слот {i}")
        else:
            saves.append(f"Слот {i} — пусто")
    return saves
```

---

## ✅ 2. `gui/interface.py` – Обновлённый код с поддержкой слотов

```python
import tkinter as tk
from tkinter import messagebox
from character import Character
from locations import Location, TravelSystem
from events import EventSystem
from utils.save_load import save_game, load_game, list_saves


class GameApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Странник, изгоняющий мрак")
        self.root.geometry("800x600")

        self.player = None
        self.travel_system = None
        self.event_system = None

        self.create_main_menu()

    def create_main_menu(self):
        self.clear_window()
        tk.Label(self.root, text="=== СТРАННИК, ИЗГОНЯЮЩИЙ МРАК ===", font=("Arial", 16)).pack(pady=10)
        tk.Button(self.root, text="Создать персонажа", command=self.create_character).pack(pady=5)
        tk.Button(self.root, text="Загрузить игру", command=self.show_load_menu).pack(pady=5)
        tk.Button(self.root, text="Выход", command=self.root.quit).pack(pady=5)

    def show_load_menu(self):
        self.clear_window()
        tk.Label(self.root, text="Выберите слот для загрузки:", font=("Arial", 14)).pack(pady=10)

        saves = list_saves()
        self.save_var = tk.StringVar(value=saves[0])
        for save in saves:
            tk.Radiobutton(self.root, text=save, variable=self.save_var, value=save).pack(anchor='w')

        tk.Button(self.root, text="Загрузить", command=self.confirm_load).pack(pady=10)
        tk.Button(self.root, text="Назад", command=self.create_main_menu).pack(pady=5)

    def confirm_load(self):
        selected = self.save_var.get()
        if selected == "Слот 1 — пусто" or selected == "Слот 2 — пусто" or selected == "Слот 3 — пусто":
            messagebox.showinfo("Ошибка", "Этот слот пустой.")
            return

        slot = int(selected.split()[1])
        self.player, location = load_game(slot)
        if self.player:
            self.event_system = EventSystem(self.player)
            self.travel_system = TravelSystem(self.player, self.event_system)
            self.travel_system.player.location = location
            self.main_game_screen()

    def create_character(self):
        self.clear_window()
        tk.Label(self.root, text="Введите имя персонажа:", font=("Arial", 12)).pack(pady=5)
        self.name_entry = tk.Entry(self.root)
        self.name_entry.pack(pady=5)

        tk.Label(self.root, text="Выберите класс:", font=("Arial", 12)).pack(pady=5)
        self.class_var = tk.StringVar(value="воин")
        classes = ["воин", "вор", "бард", "шаман"]
        for cls in classes:
            tk.Radiobutton(self.root, text=cls.capitalize(), variable=self.class_var, value=cls).pack()

        tk.Button(self.root, text="Создать", command=self.confirm_character).pack(pady=10)

    def confirm_character(self):
        name = self.name_entry.get().strip()
        if not name:
            messagebox.showwarning("Ошибка", "Введите имя персонажа!")
            return

        char_class = self.class_var.get()
        self.player = Character(name=name, char_class=char_class)
        self.event_system = EventSystem(self.player)
        self.travel_system = TravelSystem(self.player, self.event_system)
        self.choose_location()

    def choose_location(self):
        self.clear_window()
        tk.Label(self.root, text="Выберите начальную локацию:", font=("Arial", 14)).pack(pady=10)

        locations = {
            '1': "Вороний Лес",
            '2': "Соленые Пески",
            '3': "Синее Болото",
            '4': "Горы Мрака"
        }

        self.location_var = tk.StringVar(value='1')
        for key, name in locations.items():
            tk.Radiobutton(self.root, text=name, variable=self.location_var, value=key).pack(anchor='w')

        tk.Button(self.root, text="Продолжить", command=self.start_game).pack(pady=10)

    def start_game(self):
        choice = self.location_var.get()
        location_map = {
            '1': Location("Вороний Лес", "Лес, полный тайн.", {}),
            '2': Location("Соленые Пески", "Безжизненная пустыня.", {}),
            '3': Location("Синее Болото", "Место опасностей.", {}),
            '4': Location("Горы Мрака", "Страшные пики гор.", {})
        }

        starting_location = location_map.get(choice)
        self.travel_system.travel_to_location(starting_location)
        self.player.location = starting_location
        self.main_game_screen()

    def main_game_screen(self):
        self.clear_window()
        self.text_area = tk.Text(self.root, wrap=tk.WORD, height=20, width=80)
        self.text_area.pack(pady=10)
        self.update_text(f"Добро пожаловать, {self.player.name}!")

        frame = tk.Frame(self.root)
        frame.pack()

        tk.Button(frame, text="Переместиться", command=self.choose_path).pack(side=tk.LEFT, padx=5)
        tk.Button(frame, text="F-пункт", command=self.visit_f_point).pack(side=tk.LEFT, padx=5)
        tk.Button(frame, text="Показать статы", command=self.show_stats).pack(side=tk.LEFT, padx=5)
        tk.Button(frame, text="Сохранить", command=self.show_save_menu).pack(side=tk.LEFT, padx=5)
        tk.Button(frame, text="Выход", command=self.root.quit).pack(side=tk.LEFT, padx=5)

    def show_save_menu(self):
        self.clear_window()
        tk.Label(self.root, text="Выберите слот для сохранения:", font=("Arial", 14)).pack(pady=10)

        saves = list_saves()
        self.save_var = tk.StringVar(value=saves[0])
        for save in saves:
            tk.Radiobutton(self.root, text=save, variable=self.save_var, value=save).pack(anchor='w')

        tk.Button(self.root, text="Сохранить", command=self.confirm_save).pack(pady=10)
        tk.Button(self.root, text="Назад", command=self.main_game_screen).pack(pady=5)

    def confirm_save(self):
        selected = self.save_var.get()
        if not selected.startswith("Слот"):
            messagebox.showerror("Ошибка", "Выберите корректный слот.")
            return

        slot = int(selected.split()[1])
        save_game(slot, self.player, self.player.location)
        messagebox.showinfo("Сохранение", f"Игра сохранена в слот {slot}")
        self.main_game_screen()

    def choose_path(self):
        self.clear_window()
        tk.Label(self.root, text="Выберите способ передвижения:", font=("Arial", 14)).pack(pady=10)
        tk.Button(self.root, text="Прямой путь", command=self.direct_travel).pack(pady=5)
        tk.Button(self.root, text="Свободный путь", command=self.free_travel).pack(pady=5)
        tk.Button(self.root, text="Назад", command=self.main_game_screen).pack(pady=5)

    def direct_travel(self):
        self.travel_system.direct_travel()
        self.main_game_screen()

    def free_travel(self):
        self.travel_system.free_travel()
        self.main_game_screen()

    def visit_f_point(self):
        if not self.player.location.f_points:
            self.update_text("Нет доступных F-пунктов.")
            return

        self.clear_window()
        tk.Label(self.root, text="Доступные F-пункты:", font=("Arial", 14)).pack(pady=10)

        self.f_point_var = tk.StringVar()
        for f_name in self.player.location.f_points:
            tk.Radiobutton(self.root, text=f_name, variable=self.f_point_var, value=f_name).pack(anchor='w')

        tk.Button(self.root, text="Посетить", command=self.confirm_f_point).pack(pady=10)
        tk.Button(self.root, text="Назад", command=self.main_game_screen).pack(pady=5)

    def confirm_f_point(self):
        f_point = self.f_point_var.get()
        if f_point:
            self.player.location.visit_f_point(f_point)
        self.main_game_screen()

    def show_stats(self):
        stats = (
            f"\n=== ХАРАКТЕРИСТИКИ ===\n"
            f"Имя: {self.player.name}\n"
            f"Класс: {self.player.char_class.capitalize()}\n"
            f"Сила: {self.player.sila}\n"
            f"Ловкость: {self.player.ловкость}\n"
            f"Здоровье: {self.player.zdorovye}\n"
            f"Интеллект: {self.player.intellekt}\n"
            f"Нападение: {self.player.napadenie}\n"
            f"Защита: {self.player.zashchita}\n"
            f"Жизненная сила: {self.player.js}\n"
            f"Магическая энергия: {self.player.me}\n"
            f"Бонус: {self.player.bonus}\n"
            f"Инвентарь: {', '.join(self.player.inventory) if self.player.inventory else 'Пусто'}"
        )
        self.update_text(stats)

    def update_text(self, text):
        self.text_area.insert(tk.END, text + "\n")
        self.text_area.see(tk.END)

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()
```

---

## ✅ Как работает система:

### При запуске:
- Главное меню → можно создать нового персонажа или загрузить из слотов 1–3.
- Можно выбрать любой слот для **загрузки** или **сохранения**.

### Сохранение:
- В главном игровом меню нажимаешь **"Сохранить"**
- Выбираешь слот
- Игра записывается в `saves/save_1.json`, `saves/save_2.json`, `saves/save_3.json`

### Загрузка:
- В меню загрузки выбираешь слот
- Персонаж и локация восстанавливаются

---

## ✅ Пример использования

```bash
python gui/interface.py
```

- Создай персонажа → перемести его → сохрани в слот 1  
- Перезапусти игру → загрузи слот 1 → продолжи игру

---

## ✅ Следующие улучшения (по желанию):

| Возможность | Описание |
|------------|----------|
| Автосохранение | После каждого события автоматически сохраняет в последний слот |
| Предпросмотр слотов | Отображает имя игрока и локацию в списке |
| Удаление слотов | Кнопка "Очистить слот" |
| Экспорт/импорт | Сохранение вручную в формате JSON |

---


1. Реализовать **предпросмотр слотов**
2. Добавить **возможность удаления сохранений**
3. Реализовать **экспорт/импорт вручную**

---

## ✅ 1. Предпросмотр слотов сохранений

Добавим отображение имени персонажа, его класса и текущей локации в меню загрузки/сохранения.

### Обновление `utils/save_load.py` (уже есть):

```python
def get_save_info(slot):
    """Возвращает информацию о сохранении (если есть)"""
    save_path = get_save_path(slot)
    if not os.path.exists(save_path):
        return None

    with open(save_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    char_data = data.get("character", {})
    loc_data = data.get("location", {})

    return {
        "exists": True,
        "name": char_data.get("name", "Неизвестный"),
        "class": char_data.get("char_class", "").capitalize(),
        "location": loc_data.get("name", "Неизвестное место")
    }
```

---

## ✅ 2. Возможность удаления сохранений

Реализуем функцию для очистки слота.

### Добавить в `utils/save_load.py`:

```python
def delete_save(slot):
    save_path = get_save_path(slot)
    if os.path.exists(save_path):
        os.remove(save_path)
        print(f"Слот {slot} очищен.")
    else:
        print(f"Слот {slot} уже пуст.")
```

---

## ✅ 3. Экспорт/импорт вручную

Добавим возможность экспорта в произвольный файл и импорта из файла.

### Добавить в `utils/save_load.py`:

```python
def export_game(filename):
    """Экспортирует текущее состояние игры в указанный файл"""
    from game import current_player, current_location
    if not current_player:
        print("Нет активной игры для экспорта.")
        return

    save_game_to_file(current_player, current_location, filename)
    print(f"Игра успешно экспортирована в {filename}")


def import_game(filename):
    """Импортирует игру из указанного файла"""
    if not os.path.exists(filename):
        print("Файл не найден.")
        return None, None

    with open(filename, 'r', encoding='utf-8') as f:
        data = json.load(f)

    from character import Character
    loaded_char = data["character"]
    player = Character(
        name=loaded_char["name"],
        char_class=loaded_char["char_class"]
    )
    player.sila = loaded_char["sila"]
    player.lovkost = loaded_char["lovkost"]
    player.zdorovye = loaded_char["zdorovye"]
    player.intellekt = loaded_char["intellekt"]
    player.napadenie = loaded_char["napadenie"]
    player.zashchita = loaded_char["zashchita"]
    player.js = loaded_char["js"]
    player.me = loaded_char["me"]
    player.bonus = loaded_char["bonus"]
    player.inventory = loaded_char["inventory"]

    from locations import Location
    location_data = data["location"]
    current_location = Location(
        name=location_data["name"],
        description=location_data["description"],
        f_points=location_data.get("f_points", {})
    )

    print(f"Игра успешно импортирована из {filename}")
    return player, current_location


def save_game_to_file(player, location, filename):
    data = {
        "character": {
            "name": player.name,
            "char_class": player.char_class,
            "sila": player.sila,
            "lovkost": player.lovkost,
            "zdorovye": player.zdorovye,
            "intellekt": player.intellekt,
            "napadenie": player.napadenie,
            "zashchita": player.zashchita,
            "js": player.js,
            "me": player.me,
            "bonus": player.bonus,
            "inventory": player.inventory
        },
        "location": {
            "name": location.name,
            "description": location.description,
            "f_points": location.f_points
        }
    }

    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
```

> ⚠️ В `gui/interface.py` нужно добавить глобальные переменные `current_player` и `current_location`, чтобы они были доступны для `export_game`.

---

## ✅ Обновление `gui/interface.py`

### Добавь в начало `interface.py`:

```python
# Глобальные переменные для хранения текущего состояния игры
current_player = None
current_location = None
```

### И обнови при загрузке/сохранении:

```python
# При создании или загрузке игрока:
global current_player, current_location
current_player = player
current_location = location
```

---

### Добавь кнопки в главное меню GUI:

```python
tk.Button(frame, text="Экспорт", command=self.export_game).pack(side=tk.LEFT, padx=5)
tk.Button(frame, text="Импорт", command=self.import_game).pack(side=tk.LEFT, padx=5)
tk.Button(frame, text="Очистить слот", command=self.delete_slot).pack(side=tk.LEFT, padx=5)
```

---

### Методы в классе `GameApp`:

```python
def export_game(self):
    from tkinter import filedialog
    filename = filedialog.asksaveasfilename(defaultextension=".json",
                                            filetypes=[("JSON файлы", "*.json")])
    if filename:
        from utils.save_load import export_game
        export_game(filename)

def import_game(self):
    from tkinter import filedialog
    filename = filedialog.askopenfilename(filetypes=[("JSON файлы", "*.json")])
    if filename:
        from utils.save_load import import_game
        player, location = import_game(filename)
        if player and location:
            self.player = player
            self.travel_system = TravelSystem(self.player, self.event_system)
            self.travel_system.player.location = location
            self.main_game_screen()

def delete_slot(self):
    self.clear_window()
    tk.Label(self.root, text="Выберите слот для удаления:", font=("Arial", 14)).pack(pady=10)

    saves = list_saves()
    self.save_var = tk.StringVar(value=saves[0])
    for save in saves:
        tk.Radiobutton(self.root, text=save, variable=self.save_var, value=save).pack(anchor='w')

    tk.Button(self.root, text="Удалить", command=self.confirm_delete).pack(pady=10)
    tk.Button(self.root, text="Назад", command=self.main_game_screen).pack(pady=5)

def confirm_delete(self):
    selected = self.save_var.get()
    if selected == "Слот 1 — пусто" or selected == "Слот 2 — пусто" or selected == "Слот 3 — пусто":
        messagebox.showinfo("Ошибка", "Этот слот уже пустой.")
        return

    slot = int(selected.split()[1])
    from utils.save_load import delete_save
    delete_save(slot)
    messagebox.showinfo("Удаление", f"Слот {slot} очищен.")
    self.create_main_menu()
```

---

## ✅ Пример интерфейса после обновления

Теперь у вас будут следующие возможности в GUI:

| Кнопка | Функция |
|--------|---------|
| Сохранить | Выбираешь один из 3 слотов → сохраняешь |
| Загрузить | Выбираешь слот → восстанавливаешь прогресс |
| Предпросмотр | Показывает имя, класс и локацию в списке слотов |
| Удалить | Очищает выбранный слот |
| Экспорт | Сохраняет игру в любой файл на диске |
| Импорт | Загружает игру из любого JSON-файла |

---

## ✅ Как использовать:

1. Сохраните игру в слот 1.
2. Перезапустите программу → выберите **Загрузить** → выберите слот 1.
3. Нажмите **Очистить слот** → подтвердите удаление.
4. Нажмите **Экспорт** → сохраните файл как `my_save.json`.
5. Нажмите **Импорт** → загрузите `my_save.json`.

---

## ✅ Что можно добавить позже:

| Возможность | Описание |
|------------|----------|
| Автосохранение | Сохранять автоматически после каждого события |
| Скриншоты | Сохранять мини-карту или картинку персонажа |
| Лог ошибок | Записывать ошибки в файл |
| Поддержка нескольких игроков | Сохранять несколько персонажей в одном файле |

---

## 📦 Пример структуры `my_save.json` после экспорта

```json
{
  "character": {
    "name": "Артур",
    "char_class": "воин",
    "sila": 12,
    ...
  },
  "location": {
    "name": "Вороний Лес",
    "description": "Лес полон тайн...",
    "f_points": {
      "Башня Белой Леди": "..."
    }
  }
}
```

---

## 🎯 Следующие шаги:


1. Реализовать **автосохранение**
2. Добавить **анимированный вывод событий**
3. Реализовать **работу с картой мира Гохана в GUI**


