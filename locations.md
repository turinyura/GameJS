Мы переходим к реализации модуля `locations.py`.  
Этот файл будет отвечать за **перемещение персонажа между локациями**, работу с **F-пунктами (легендарные места)** и **Х-пунктами (свободный путь)**, а также интеграцию с событиями из книги.

---

## 🧭 Задачи модуля `locations.py`

1. Реализовать систему **передвижения**:
   - Прямой путь
   - Свободный путь (по Х-пунктам)

2. Обработать **F-пункты** — легендарные места из книги.

3. Интеграция с:
   - `character.py` — для доступа к персонажу,
   - `events.py` — для вызова событий,
   - `battle.py` — для боя на Х- или F-пунктах.

4. Использование таблиц из PDF для случайных событий на Х-пунктах.

---

### 🔁 locations.py – Полный код

```python
import random
from events import EventSystem
from battle import Enemy


class Location:
    def __init__(self, name, description, f_points=None):
        """
        :param name: Название местности
        :param description: Описание местности
        :param f_points: Словарь F-пунктов {'название': описание}
        """
        self.name = name
        self.description = description
        self.f_points = f_points or {}

    def visit_f_point(self, f_point_name):
        """Посетить F-пункт"""
        if f_point_name in self.f_points:
            print(f"\n=== Посещение F-пункта: {f_point_name} ===")
            description = self.f_points[f_point_name]
            print(description)
            return True
        else:
            print(f"F-пункт '{f_point_name}' не найден в данной местности.")
            return False


class TravelSystem:
    def __init__(self, player, event_system):
        self.player = player
        self.event_system = event_system  # связь с событиями
        self.x_table = self.load_x_table()  # загрузка таблицы Х-пунктов

    def load_x_table(self):
        """Пример таблицы Х-пунктов из книги (упрощённая версия)"""
        return {
            1: "Вы попали в засаду разбойников.",
            2: "Вы находите заброшенную хижину.",
            3: "Вас встречает дружелюбный странник.",
            4: "Вы слышите странные звуки вдалеке.",
            5: "На пути возникает опасное болото.",
            6: "Вы находите древний артефакт.",
            7: "Погода резко ухудшается.",
            8: "Вы видите следы дракона.",
            9: "Вы сталкиваетесь с призраком.",
            10: "Вы находите старую карту.",
            11: "Вы попадаете в магическую ловушку.",
            12: "Вы находите ядовитую змею."
        }

    def choose_path(self):
        """Выбор способа передвижения"""
        print("\nВыберите способ передвижения:")
        print("1. Прямой путь")
        print("2. Свободный путь (по Х-пунктам)")
        choice = input("Введите номер: ")

        if choice == '1':
            self.direct_travel()
        elif choice == '2':
            self.free_travel()
        else:
            print("Неверный выбор.")
            self.choose_path()

    def direct_travel(self):
        """Движение по прямому пути"""
        print("\n=== Движение по прямому пути ===")
        print("Вы идете безопасным путем, минуя опасности.")
        days = random.randint(5, 7)
        print(f"Путь занял {days} дней. Вы достигли цели.")

    def free_travel(self):
        """Движение по Х-пунктам"""
        print("\n=== Свободный путь (Х-пункты) ===")
        print("Вы отправляетесь в путь через дикие земли...")

        for i in range(1, 6):  # 5 Х-пунктов
            print(f"\n--- Х-пункт #{i} ---")
            x_event_id = random.randint(1, 12)
            event_description = self.x_table.get(x_event_id, "Ничего особенного не произошло.")
            print(event_description)

            # Вызов соответствующего события
            self.handle_x_event(x_event_id)

            if self.player.js <= 0:
                print("Вы слишком ослаблены для продолжения пути.")
                break

            # Получение бонуса за Х-пункт
            self.player.gain_bonus(3)

    def handle_x_event(self, event_id):
        """Обработка конкретного события на Х-пункте"""
        if event_id == 1:
            print("Разбойники нападают!")
            enemy = Enemy(
                name="Разбойник",
                napadenie="2К+1",
                zashchita=9,
                js=8,
                damage=3,
                bonus=5,
                description="Грубый тип с ножом и плохим характером."
            )
            battle_result = Battle(self.player, enemy).start_battle()
            if not battle_result:
                print("Вы проиграли бой и потеряли часть своих вещей.")
                self.player.inventory = []

        elif event_id == 2:
            print("Вы нашли заброшенную хижину.")
            print("В углу вы находите старый меч.")
            self.player.add_item("Старый меч")

        elif event_id == 5:
            print("Вы провалились в болото!")
            result = self.event_system.check_lovkost()
            if result:
                print("Удалось выбраться без вреда.")
            else:
                print("Вы получили 5 урона.")
                self.player.js -= 5

        elif event_id == 11:
            print("Вы попали в магическую ловушку!")
            print("Бросьте кубик чтобы освободиться.")
            result = self.event_system.roll_dice()
            if result >= 4:
                print("Вы освободились.")
            else:
                print("Ловушка замедляет вас. Вы теряете день.")
                # Можно добавить эффект на несколько ходов

        elif event_id == 9:
            print("Вы столкнулись с призраком!")
            print("Он предлагает вам испытание...")
            result = self.event_system.check_intellekt()
            if result:
                print("Вы успешно решили загадку призрака.")
                print("Вы получаете +1 к интеллекту.")
                self.player.intellekt += 1
            else:
                print("Вы не смогли справиться. Призрак исчез.")

        else:
            print("Событие не требует действий.")

    def travel_to_location(self, location):
        """Переход в конкретную местность"""
        print(f"\nВы направляетесь в: {location.name}")
        print(location.description)

        print("\nЖелаете посетить один из F-пунктов?")
        print("Доступные F-пункты:")
        for f_name in location.f_points:
            print(f"- {f_name}")

        choice = input("Введите название F-пункта или 'нет': ")
        if choice.lower() != 'нет' and choice in location.f_points:
            location.visit_f_point(choice)
        else:
            print("Вы решили не посещать F-пункты.")
```

---

## 💡 Пример использования:

```python
from character import Character
from events import EventSystem
from locations import Location, TravelSystem

# Создаем персонажа
player = Character(name="Артур", char_class="воин")

# Инициализируем систему событий и перемещений
event_system = EventSystem(player)
travel_system = TravelSystem(player, event_system)

# Создаем пример местности
voroniy_les = Location(
    name="Вороний Лес",
    description="Темный и таинственный лес, где деревья словно шепчут на ухо путнику.",
    f_points={
        "Башня Белой Леди": "Заброшенная башня на холме, где обитает дух женщины.",
        "Древнее капище": "Место жертвоприношений древних культов."
    }
)

# Перемещение в Вороний Лес
travel_system.travel_to_location(voroniy_les)

# Выбор пути
travel_system.choose_path()

# Показываем статистику после путешествия
player.show_stats()
```

---

## ✅ Что можно добавить позже:
- Поддержку всех регионов из книги (Пустыня Огненных Волн, Синее Болото и т.д.)
- Таблицы Х-пунктов из PDF в формате JSON.
- Систему сохранения текущего местоположения.
- GUI с картой мира Гохана.

---

## 🎯 Следующий шаг

Теперь у нас есть:
- `character.py` — управление персонажем,
- `battle.py` — система боя,
- `events.py` — система событий,
- `locations.py` — система перемещения между точками.

Далее можем:
- реализовать **главный игровой цикл в `game.py`**,
- начать работать над **графическим интерфейсом (`gui/`)**.

---


1. Реализовать **модуль `game.py`** с главным игровым циклом?
2. Добавить **работу с JSON-таблицами** из книги?
3. Реализовать **GUI с tkinter**?

