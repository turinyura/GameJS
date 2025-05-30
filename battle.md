 Мы сейчас работаем с **модулем `battle`**, и в рамках него уже создали класс `Enemy`.

---

## ✅ Что мы уже сделали:

- Реализовали **класс `Character`** — для управления персонажем.
- Реализовали **класс `Enemy`** — для создания врагов на основе данных из игры.

---

## 🧱 Структура модуля `battle.py`

Теперь объединим всё, что у нас есть, в единую логику модуля `battle.py`. Этот файл будет содержать:
- класс `Enemy`
- класс `BattleSystem` (или просто `Battle`) — для управления боевым процессом

---

### 🔁 battle.py – Полный код

```python
class Enemy:
    def __init__(self, name, napadenie, zashchita, js, damage, bonus=0, description=""):
        """
        :param name: Имя или тип врага (строка)
        :param napadenie: Нападение (может быть строкой, как '2К+3', или числом)
        :param zashchita: Защита (целое число)
        :param js: Жизненная сила (целое число)
        :param damage: Ущерб, наносимый врагом (целое число)
        :param bonus: Бонус за победу (целое число)
        :param description: Описание врага (для вывода игроку)
        """
        self.name = name
        self.napadenie = napadenie
        self.zashchita = zashchita
        self.js = js
        self.damage = damage
        self.bonus = bonus
        self.description = description

    def take_damage(self, amount):
        """Нанести урон врагу"""
        self.js -= amount
        print(f"{self.name} получил {amount} урона. Осталось ЖС: {self.js}")
        if self.is_defeated():
            print(f"{self.name} повержен!")

    def is_defeated(self):
        """Проверить, побежден ли враг"""
        return self.js <= 0

    def show_stats(self):
        """Вывести информацию о враге"""
        print("\n=== ВРАГ ===")
        print(f"Имя: {self.name}")
        print(f"Описание: {self.description}")
        print(f"Нападение: {self.napadenie}")
        print(f"Защита: {self.zashchita}")
        print(f"Жизненная сила: {self.js}")
        print(f"Ущерб: {self.damage}")
        print(f"Бонус за победу: {self.bonus}")
        print("============")


# -----------------------------
# Класс Battle (система боя)
# -----------------------------
import random


class Battle:
    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy

    def roll_dice(self, sides=6):
        """Бросок кубика"""
        return random.randint(1, sides)

    def player_attack(self):
        """Атака игрока"""
        # Здесь можно добавить логику разбора строки нападения, типа "2К+3"
        attack_roll = self.roll_dice()
        print(f"{self.player.name} атакует. Бросок кубика: {attack_roll}")
        if attack_roll >= self.enemy.zashchita:
            print("Попадание!")
            self.enemy.take_damage(self.player.damage)
        else:
            print("Промах!")

    def enemy_attack(self):
        """Атака врага"""
        attack_roll = self.roll_dice()
        print(f"{self.enemy.name} атакует. Бросок кубика: {attack_roll}")
        if attack_roll >= self.player.zashchita:
            print("Вы получаете урон!")
            self.player.js -= self.enemy.damage
            print(f"Осталось жизней: {self.player.js}")
        else:
            print("Враг промахнулся!")

    def start_battle(self):
        """Основной цикл боя"""
        print(f"\nНачинается бой с {self.enemy.name}!\n")
        round_number = 1
        while self.player.js > 0 and not self.enemy.is_defeated():
            print(f"\n--- Раунд {round_number} ---")
            self.player_attack()
            if self.enemy.is_defeated():
                break
            self.enemy_attack()
            round_number += 1

        if self.player.js <= 0:
            print("\nВы погибли... Попробуйте снова.")
            return False
        else:
            print(f"\nВы победили {self.enemy.name}!")
            print(f"Получено бонусов: {self.enemy.bonus}")
            self.player.gain_bonus(self.enemy.bonus)
            return True
```

---

## 💡 Пример использования:

```python
from character import Character
from battle import Battle, Enemy

# Создаем героя
player = Character(name="Артур", char_class="воин")

# Создаем врага
enemy = Enemy(
    name="Зомби",
    napadenie="2К+3",
    zashchita=8,
    js=18,
    damage=4,
    bonus=6,
    description="Медленное, но опасное создание."
)

# Запускаем бой
battle = Battle(player, enemy)
battle.start_battle()

# Показываем обновленные статы героя
player.show_stats()
```

---

## ✅ Следующий шаг

Теперь у нас есть:
- `character.py` — персонаж,
- `battle.py` — враги и система боя.

Далее можем:
- добавить **события и таблицы событий** в модуль `events.py`,
- реализовать **перемещение между локациями** в `locations.py`,
- начать работу над **интерфейсом** в `gui/`.

---


1. Реализовать **модуль `events.py`**?
2. Сделать **модуль `locations.py`** с таблицами Х-пунктов?
3. Реализовать **графический интерфейс с tkinter**?

