# Класс персонажа (воин, вор и т.д.)
import random

class Character:
    def __init__(self, name, char_class):
        # Основные данные
        self.name = name
        self.char_class = char_class.lower()  # 'воин', 'вор', 'бард', 'шаман'
        
        # Первичные качества (очки)
        self.sila = 0     # Сила
        self.lovkost = 0  # Ловкость
        self.zdorovye = 0  # Здоровье
        self.intellekt = 0  # Интеллект
        
        # Вторичные показатели
        self.napadenie = 0  # Нападение
        self.zashchita = 0  # Защита
        self.js = 0         # Жизненная сила
        self.me = 0         # Магическая энергия (только для шамана)
        self.bonus = 0      # Бонус за победы
        
        # Инвентарь
        self.inventory = []

        # Таблицы для вычисления нападения и защиты
        self.table_napadenie = {
            1: "2К", 2: "2К+2", 3: "2К+4",
            4: "3К", 5: "3К+2", 6: "3К+4",
            7: "4К", 8: "4К+2", 9: "4К+4",
            10: "5К", 11: "5К+2", 12: "5К+4",
            13: "6К", 14: "6К+2", 15: "6К+4",
            16: "7К", 17: "7К+2", 18: "7К+4"
        }

        self.table_zashchita = {
            1: 8, 2: 9, 3: 10, 4: 11, 5: 12,
            6: 13, 7: 14, 8: 15, 9: 16, 10: 17,
            11: 18, 12: 19, 13: 20, 14: 21, 15: 22,
            16: 23, 17: 24, 18: 25
        }

        # Инициализируем начальные параметры
        self.roll_stats()
        self.calculate_secondary_stats()

    def roll_stat(self):
        """Бросок кубика для одной характеристики"""
        return random.randint(1, 6)

    def roll_stats(self):
        """Генерация случайных значений для всех первичных качеств"""
        rolls = [self.roll_stat() for _ in range(4)]
        print(f"Выпавшие значения при генерации: {rolls}")
        print("Распределите очки на следующие качества:")
        print("1. Сила")
        print("2. Ловкость")
        print("3. Здоровье")
        print("4. Интеллект")

        # Простое распределение через ввод (можно заменить на автоматическое позже)
        self.sila = int(input("Введите значение силы (одно из выпавших): "))
        self.lovkost = int(input("Введите значение ловкости (оставшееся): "))
        self.zdorovye = int(input("Введите значение здоровья (оставшееся): "))
        self.intellekt = int(input("Введите значение интеллекта (оставшееся): "))

    def calculate_secondary_stats(self):
        """Вычисление вторичных параметров по таблицам"""
        # Нападение зависит от силы
        self.napadenie = self.table_napadenie.get(self.sila, "0К")

        # Защита зависит от ловкости
        self.zashchita = self.table_zashchita.get(self.lovkost, 0)

        # ЖС (жизненная сила) зависит от здоровья
        self.js = self.zdorovye * 2  # Примерная формула

        # Магическая энергия — только для шамана
        if self.char_class == 'шаман':
            self.me = self.intellekt * 2
        else:
            self.me = 0

    def show_stats(self):
        """Вывод характеристик персонажа"""
        print("\n=== ХАРАКТЕРИСТИКИ ПЕРСОНАЖА ===")
        print(f"Имя: {self.name}")
        print(f"Класс: {self.char_class.capitalize()}")
        print(f"Сила: {self.sila}")
        print(f"Ловкость: {self.ловкость}")
        print(f"Здоровье: {self.zdorovye}")
        print(f"Интеллект: {self.intellekt}")
        print(f"Нападение: {self.napadenie}")
        print(f"Защита: {self.zashchita}")
        print(f"Жизненная сила: {self.js}")
        print(f"Магическая энергия: {self.me}")
        print(f"Бонус: {self.bonus}")
        print(f"Инвентарь: {', '.join(self.inventory) if self.inventory else 'Пусто'}")
        print("===============================")

    def add_item(self, item):
        """Добавление предмета в инвентарь"""
        self.inventory.append(item)
        print(f"{item} добавлен в инвентарь.")

    def use_magic(self, spell_name):
        """Применение магии (пример)"""
        if self.char_class != 'шаман':
            print("Только шаман может использовать магию.")
            return False
        if self.me >= 5:
            self.me -= 5
            print(f"{self.name} использует заклинание '{spell_name}'. Осталось магической энергии: {self.me}")
            return True
        else:
            print("Недостаточно магической энергии!")
            return False

    def gain_bonus(self, amount):
        """Получение бонуса за победы"""
        self.bonus += amount
        print(f"{self.name} получил {amount} бонусов. Всего: {self.bonus}")

    def level_up_stat(self, stat_name):
        """Улучшение одного из качеств за бонусы"""
        cost_map = {
            'сила': 80,
            'ловкость': 90,
            'здоровье': 90,
            'интеллект': 100
        }
        if stat_name not in cost_map:
            print("Неизвестное качество.")
            return

        cost = cost_map[stat_name]
        if self.bonus >= cost:
            setattr(self, stat_name, getattr(self, stat_name) + 1)
            self.bonus -= cost
            print(f"{stat_name.capitalize()} увеличен на 1. Осталось бонусов: {self.bonus}")
            self.calculate_secondary_stats()
        else:
            print(f"Недостаточно бонусов для улучшения {stat_name}. Требуется: {cost}, у вас: {self.bonus}")