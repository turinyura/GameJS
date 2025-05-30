Мы переходим к реализации модуля `events.py`, который будет содержать **систему событий и пробы** для вашей игры на основе книги *"Странник, изгоняющий мрак"*.

---

## 🧭 Задача модуля `events.py`

Этот модуль будет отвечать за:
- обработку случайных событий (например, в лесу, болоте, таверне),
- систему **проб** (на силу, ловкость, интеллект),
- взаимодействие с игроком при выборе действий,
- вызов боя или других реакций в зависимости от события.

---

## ✅ Содержание `events.py`

Мы создадим:
1. Класс `EventSystem` — основной класс для управления событиями.
2. Функции для проб: `check_sila()`, `check_lovkost()`, `check_intellekt()`.
3. Обработчики случайных событий: например, `handle_swamp_event()` или `handle_tavern_event()`.
4. Используем таблицы из PDF (например, *Таблица происшествий в тавернах*).

---

### 🔁 events.py – Полный код

```python
import random
from battle import Battle, Enemy


class EventSystem:
    def __init__(self, player):
        self.player = player

    def roll_dice(self, sides=6):
        """Бросок кубика"""
        return random.randint(1, sides)

    def check_sila(self, difficulty=4):
        """Проба на силу"""
        result = self.roll_dice()
        print(f"Вы бросили кубик на силу: {result}")
        return result >= difficulty

    def check_lovkost(self, difficulty=4):
        """Проба на ловкость"""
        result = self.roll_dice()
        print(f"Вы бросили кубик на ловкость: {result}")
        return result >= difficulty

    def check_intellekt(self, difficulty=4):
        """Проба на интеллект"""
        result = self.roll_dice()
        print(f"Вы бросили кубик на интеллект: {result}")
        return result >= difficulty

    def trigger_random_tavern_event(self):
        """Случайное происшествие в таверне (по таблице)"""
        print("\n=== ПОСЕЩЕНИЕ ТАВЕРНЫ ===")
        print("Вы заходите в уютную таверну, чтобы немного отдохнуть...")
        event_id = self.roll_dice(6)
        print(f"Выпавший номер события: {event_id}")

        tavern_events = {
            1: "Вы слышите песню барда, которая дарит вам +1 к интеллекту.",
            2: "Вас вызывают на поединок местные грубияны. Хотите принять вызов?",
            3: "Вы находите старинный пергамент с заклинанием шамана.",
            4: "Пьяный орк начинает дерзить. Вы можете либо уладить конфликт, либо ударить его.",
            5: "Вы выигрываете в кости и получаете 5 золотых монет.",
            6: "Вы решаете просто отдохнуть и восстанавливаете 3 ЖС."
        }

        description = tavern_events.get(event_id, "Ничего особенного не произошло.")
        print(description)

        # Логика для каждого события
        if event_id == 1:
            self.player.intellekt += 1
            print("+1 к интеллекту.")
        elif event_id == 2:
            fight = input("Принять поединок? (да/нет): ").lower()
            if fight == 'да':
                enemy = Enemy(name="Грубиян", napadenie="2К+1", zashchita=9, js=8, damage=3, bonus=5)
                battle = Battle(self.player, enemy)
                battle.start_battle()
        elif event_id == 3:
            print("Вы нашли заклинание. Если вы шаман — это может быть полезно!")
            self.player.add_item("Заклинание: Огненный сгусток")
        elif event_id == 4:
            print("Орк пьян и агрессивен. Вы можете попробовать его успокоить или ударить.")
        elif event_id == 5:
            print("Вы получили 5 золотых.")
        elif event_id == 6:
            self.player.js += 3
            print("Вы отдыхаете и восстанавливаете 3 ЖС.")

    def handle_swamp_event(self):
        """Событие на болоте — человек-ящерица нападает"""
        print("\n=== БОЛОТО ===")
        print("Страшная жара, москиты не дают покоя ни секунды... Вдруг из болотной ряски выныривают два человека-ящерицы!")
        print("Они метают в вас деревянные копья!")

        if "щит" in self.player.inventory:
            print("У вас есть щит — вы защищены от копий.")
        else:
            result = self.roll_dice()
            print(f"Вы бросили кубик: {result}")
            if result in [1, 2]:
                print("Оба копья пролетели мимо.")
            elif result in [3, 4]:
                print("Вы получили урон в 5 ЖС.")
                self.player.js -= 5
            elif result in [5, 6]:
                print("Вы получили урон в 10 ЖС.")
                self.player.js -= 10

        # После копий начинается рукопашная
        print("Человеки-ящерицы достают мечи и бросаются в атаку!")
        enemy = Enemy(name="Человек-ящерица", napadenie="2К+2", zashchita=10, js=12, damage=4, bonus=7)
        battle = Battle(self.player, enemy)
        battle.start_battle()

    def handle_cave_event(self):
        """Событие в пещере — встреча с Красным Драконом"""
        print("\n=== ПЕЩЕРА ===")
        print("Вы входите в темную пещеру. Груды костей и следы когтей говорят о её опасности...")
        print("Из темноты выходит Красный Дракон!")

        enemy = Enemy(
            name="Красный Дракон",
            napadenie="4К+4",
            zashchita=20,
            js=30,
            damage=8,
            bonus=50,
            description="Гигантский огнедышащий дракон. Его кожа раскалена, как уголь."
        )
        battle = Battle(self.player, enemy)
        battle.start_battle()

    def handle_desert_event(self):
        """Событие в пустыне — яма-ловушка"""
        print("\n=== ПУСТЫНЯ ===")
        print("Вы шагаете по песчаной равнине, как вдруг земля проваливается под вами...")
        print("Вы падаете в яму-ловушку, дно которой утыкано кольями.")

        result = self.roll_dice()
        if result <= 3:
            print("Древесина истлела. Вы отделались легким испугом.")
        else:
            damage = 10
            print(f"Вы получили {damage} урона.")
            self.player.js -= damage

        if self.player.js <= 0:
            print("Вы слишком ослаблены, чтобы продолжать путь.")
            return False
        return True

    def choose_event(self, location):
        """Выбор события в зависимости от локации"""
        if location == "таверна":
            self.trigger_random_tavern_event()
        elif location == "болото":
            self.handle_swamp_event()
        elif location == "пещера":
            self.handle_cave_event()
        elif location == "пустыня":
            self.handle_desert_event()
        else:
            print("Ничего интересного не происходит.")
```

---

## 💡 Пример использования

```python
from character import Character
from events import EventSystem

# Создаем героя
player = Character(name="Артур", char_class="воин")

# Инициализируем систему событий
event_system = EventSystem(player)

# Выбираем событие (например, в таверне)
event_system.choose_event("таверна")

# Показываем статистику после события
player.show_stats()
```

---

## 📚 Как использовать данные из PDF:

Мы можем добавить в `data/tables/tavern_events.json` события из таблицы таверн, чтобы сделать их более разнообразными и соответствующими книге.

Пример JSON:
```json
{
  "tavern_events": [
    "Вы слышите песню барда, которая дарит вам +1 к интеллекту.",
    "Вас вызывают на поединок местные грубияны.",
    "Вы находите старинный пергамент с заклинанием шамана.",
    "Пьяный орк начинает дерзить. Вы можете либо уладить конфликт, либо ударить его.",
    "Вы выигрываете в кости и получаете 5 золотых монет.",
    "Вы решаете просто отдохнуть и восстанавливаете 3 ЖС."
  ]
}
```

И загружать события из файла, если хотите.

---

## ✅ Что можно добавить позже:
- Поддержку всех типов локаций из книги (горы, лес, дорога).
- Систему случайного выбора события на Х-пункте.
- Работу с таблицами из PDF (например, Х-пункты, F-пункты).
- Сохранение прогресса игрока.
- GUI интерфейс с выбором действия.

---

## 🎯 Следующий шаг

Теперь у нас есть:
- `character.py` — управление персонажем,
- `battle.py` — система боя,
- `events.py` — система событий и пробы.

Следующая логическая часть — **модуль `locations.py`**, где мы будем реализовывать:
- перемещение между точками (F-пункты, Х-пункты),
- выбор пути (прямой / свободный),
- работу с таблицами событий.

---


1. Реализовать **модуль `locations.py`**
2. Добавить **работу с JSON-таблицами** событий из книги
3. Реализовать **GUI с tkinter**
