Мы переходим к реализации **графического интерфейса (GUI)** для вашей игры *"Странник, изгоняющий мрак"*.  
Цель: создать простой, но функциональный графический интерфейс на Python, используя библиотеку `tkinter`.

---

## 🧰 Что мы будем использовать:

- `tkinter` — встроенная библиотека Python для GUI.
- Окна и кнопки вместо консольного ввода.
- Отображение текста событий, характеристик персонажа, боёв и выбора действий.

---

## 🎨 Возможности GUI:
1. Создание персонажа (имя, класс).
2. Отображение характеристик (`show_stats()`).
3. Выбор действия: перемещение, посещение F-пунктов, развитие качества.
4. Отображение событий, боя и результатов.
5. Простая стилизация текста и кнопок.

---

### 🔁 gui/interface.py – Полный код

```python
import tkinter as tk
from tkinter import messagebox
from character import Character
from game import choose_starting_location, main_game_loop
from locations import TravelSystem
from events import EventSystem


class GameApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Странник, изгоняющий мрак")
        self.root.geometry("800x600")

        # Персонаж
        self.player = None
        self.travel_system = None

        # Интерфейс
        self.create_main_menu()

    def create_main_menu(self):
        """Главное меню"""
        self.clear_window()
        tk.Label(self.root, text="=== СТРАННИК, ИЗГОНЯЮЩИЙ МРАК ===", font=("Arial", 16)).pack(pady=10)
        tk.Button(self.root, text="Создать персонажа", command=self.create_character).pack(pady=5)
        tk.Button(self.root, text="Выход", command=self.root.quit).pack(pady=5)

    def create_character(self):
        """Создание персонажа"""
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
        """Выбор начальной локации"""
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
            tk.Radiobutton(self.root, text=name, variable=self.location_var, value=key).pack()

        tk.Button(self.root, text="Продолжить", command=self.start_game).pack(pady=10)

    def start_game(self):
        """Начало игры"""
        choice = self.location_var.get()
        location_map = {
            '1': Location(
                name="Вороний Лес",
                description="Темный и таинственный лес, где деревья словно шепчут на ухо путнику.",
                f_points={
                    "Башня Белой Леди": "Заброшенная башня на холме, где обитает дух женщины.",
                    "Древнее капище": "Место жертвоприношений древних культов."
                }
            ),
            '2': Location(
                name="Соленые Пески",
                description="Безжизненная пустыня, где песок горит под ногами.",
                f_points={
                    "Крепость Лорда Гриза": "Зловещее место, где пребывает Рыцарь Смерти.",
                    "Оазис": "Укромное место, где можно отдохнуть и пополнить запасы воды."
                }
            ),
            '3': Location(
                name="Синее Болото",
                description="Страшное болото, полное ядовитых змей и призраков погибших странников.",
                f_points={
                    "Хижина ведьмы": "Место, где можно купить зелья или получить опасное задание.",
                    "Призрачный корабль": "Легендарное судно, затонувшее много лет назад."
                }
            ),
            '4': Location(
                name="Горы Мрака",
                description="Скалистая местность, где даже солнце не может пробиться сквозь вечные тучи.",
                f_points={
                    "Пещера Красного Дракона": "Огненный дракон охраняет древнее сокровище.",
                    "Ледяной Храм": "Заброшенный храм, наполненный загадками и ловушками."
                }
            )
        }

        starting_location = location_map.get(choice)
        self.travel_system.travel_to_location(starting_location)
        self.player.location = starting_location

        self.main_game_screen()

    def main_game_screen(self):
        """Основной экран игры"""
        self.clear_window()
        self.text_area = tk.Text(self.root, wrap=tk.WORD, height=20, width=80)
        self.text_area.pack(pady=10)

        self.update_text(f"Добро пожаловать, {self.player.name}!\n")
        self.update_text("Что вы хотите сделать?\n")

        frame = tk.Frame(self.root)
        frame.pack()

        tk.Button(frame, text="Переместиться", command=self.choose_path).pack(side=tk.LEFT, padx=5)
        tk.Button(frame, text="F-пункт", command=self.visit_f_point).pack(side=tk.LEFT, padx=5)
        tk.Button(frame, text="Показать статы", command=self.show_stats).pack(side=tk.LEFT, padx=5)
        tk.Button(frame, text="Развить качество", command=self.level_up_stat).pack(side=tk.LEFT, padx=5)
        tk.Button(frame, text="Выход", command=self.root.quit).pack(side=tk.LEFT, padx=5)

    def update_text(self, text):
        self.text_area.insert(tk.END, text + "\n")
        self.text_area.see(tk.END)

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

        self.f_point_var = tk.StringVar(value="")
        for f_name in self.player.location.f_points:
            tk.Radiobutton(self.root, text=f_name, variable=self.f_point_var, value=f_name).pack()

        tk.Button(self.root, text="Посетить", command=self.confirm_f_point).pack(pady=10)
        tk.Button(self.root, text="Назад", command=self.main_game_screen).pack(pady=5)

    def confirm_f_point(self):
        f_point = self.f_point_var.get()
        if f_point:
            self.player.location.visit_f_point(f_point)
        self.main_game_screen()

    def show_stats(self):
        stats = (
            f"\n=== ХАРАКТЕРИСТИКИ ПЕРСОНАЖА ===\n"
            f"Имя: {self.player.name}\n"
            f"Класс: {self.player.char_class.capitalize()}\n"
            f"Сила: {self.player.sila}\n"
            f"Ловкость: {self.player.lovkost}\n"
            f"Здоровье: {self.player.zdorovye}\n"
            f"Интеллект: {self.player.intellekt}\n"
            f"Нападение: {self.player.napadenie}\n"
            f"Защита: {self.player.zashchita}\n"
            f"Жизненная сила: {self.player.js}\n"
            f"Магическая энергия: {self.player.me}\n"
            f"Бонус: {self.player.bonus}\n"
            f"Инвентарь: {', '.join(self.player.inventory) if self.player.inventory else 'Пусто'}\n"
            f"==============================="
        )
        self.update_text(stats)

    def level_up_stat(self):
        self.clear_window()
        tk.Label(self.root, text="Какое качество хотите повысить?", font=("Arial", 14)).pack(pady=10)

        stats = ["сила", "ловкость", "здоровье", "интеллект"]
        self.stat_var = tk.StringVar(value="сила")

        for stat in stats:
            tk.Radiobutton(self.root, text=stat.capitalize(), variable=self.stat_var, value=stat).pack()

        tk.Button(self.root, text="Повысить", command=self.confirm_level_up).pack(pady=10)
        tk.Button(self.root, text="Назад", command=self.main_game_screen).pack(pady=5)

    def confirm_level_up(self):
        stat_name = self.stat_var.get()
        cost_map = {
            'сила': 80,
            'ловкость': 90,
            'здоровье': 90,
            'интеллект': 100
        }
        cost = cost_map[stat_name]
        if self.player.bonus >= cost:
            setattr(self.player, stat_name, getattr(self.player, stat_name) + 1)
            self.player.bonus -= cost
            self.player.calculate_secondary_stats()
            self.update_text(f"{stat_name.capitalize()} увеличен на 1. Осталось бонусов: {self.player.bonus}")
        else:
            self.update_text(f"Недостаточно бонусов для улучшения {stat_name}. Требуется: {cost}, у вас: {self.player.bonus}")

    def clear_window(self):
        """Очистка окна от всех виджетов"""
        for widget in self.root.winfo_children():
            widget.destroy()


# Запуск приложения
if __name__ == "__main__":
    root = tk.Tk()
    app = GameApp(root)
    root.mainloop()
```

---

## 📦 Не забудь подключить модули

Убедитесь, что у вас есть все файлы в проекте:

```
strannik-igra/
│
├── main.py                     # (необязательно, если запускаете через gui)
├── modules/
│   ├── character.py
│   ├── battle.py
│   ├── events.py
│   ├── locations.py
│   └── game.py
└── gui/
    └── interface.py             # наш GUI
```

---

## ✅ Что можно добавить позже:
- Сохранение/загрузка игры.
- Анимации и звуки.
- Поддержка нескольких игроков.
- Финальный экран с победой или проигрышем.
- Интеграция таблиц из PDF (JSON).

---

## 🚀 Как запустить игру:
```bash
cd gui
python interface.py
```

---

 Реализовать **сохранение прогресса**
 Добавить **звуковые эффекты и картинки**
 Реализовать **экспорт в .exe**

---
