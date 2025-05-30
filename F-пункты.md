Мы реализуем **полный список F-пунктов из книги «Странник, изгоняющий мрак»**, основываясь на содержании PDF.

---

## 📌 Цель:
Создать JSON-файл `f_points_full.json`, который будет содержать **все легендарные места (F-пункты)** с описаниями и особенностями посещения, как указано в книге.

---

## 🗺️ Структура F-пунктов в книге:

Каждый F-пункт — это уникальное место в определённой местности. Он имеет:
- название,
- регион (например, *Вороний Лес*, *Горы Короля Мурлок*),
- описание,
- особенность события (битва, испытание, отдых, награда),
- возможных врагов или бонусы.

---

## 🧱 1. Формат `data/tables/f_points_full.json`

```json
{
  "Вороний Лес": [
    {
      "название": "Башня Белой Леди",
      "описание": "Заброшенная башня на холме, где обитает дух женщины.",
      "тип": "испытание",
      "проба": {
        "характеристика": "интеллект",
        "сложность": 5
      },
      "успех": {
        "награда": ["амулет защиты", "магический свиток"],
        "бонус": 10
      },
      "провал": {
        "урон": 8
      }
    },
    {
      "название": "Логово Белого Дракона",
      "описание": "Тайная пещера, в которой скрывается Белый Дракон и Кристалл Воды.",
      "тип": "боевой",
      "враг": "Белый Дракон",
      "количество": 1,
      "награда": ["Кристалл Воды", "меч изо льда"],
      "бонус_за_победу": 80
    }
  ],
  "Горы Короля Мурлок": [
    {
      "название": "Пещера Красного Дракона",
      "описание": "Огненный дракон охраняет древнее сокровище.",
      "тип": "боевой",
      "враг": "Красный Дракон",
      "количество": 1,
      "награда": ["Кристалл Огня", "кольцо силы"],
      "бонус_за_победу": 100
    },
    {
      "название": "Ледяной Храм",
      "описание": "Заброшенный храм, наполненный загадками и ловушками.",
      "тип": "испытание",
      "проба": {
        "характеристика": "ловкость",
        "сложность": 6
      },
      "успех": {
        "награда": ["щит", "магическая энергия +10"],
        "бонус": 15
      },
      "провал": {
        "урон": 10
      }
    }
  ],
  "Пустыня Огненных Волн": [
    {
      "название": "Пирамида Рануха",
      "описание": "Главный оплот сил Тьмы в пустыне. Путь к ней полон опасностей.",
      "тип": "испытание",
      "проба": {
        "характеристика": "интеллект",
        "сложность": 7
      },
      "успех": {
        "награда": ["огненный меч"],
        "бонус": 30
      },
      "провал": {
        "урон": 10
      }
    },
    {
      "название": "Оазис",
      "описание": "Редкое место, где можно пополнить запас воды.",
      "тип": "отдых",
      "восстановление_js": 5,
      "дней_отдыха": 2
    }
  ],
  "Лес Путаных Троп": [
    {
      "название": "Отец Леса",
      "описание": "Древний дух, который может помочь или наказать вас.",
      "тип": "диалог",
      "варианты": {
        "1": {
          "опция": "Просьба о помощи",
          "результат": {
            "текст": "Дух благословляет вас и восстанавливает 10 ЖС.",
            "изменения": {
              "js": 10
            }
          }
        },
        "2": {
          "опция": "Обмануть духа",
          "результат": {
            "текст": "Дух разозлился и наложил проклятие на ваше оружие.",
            "эффект": "на 3 дня нападение -2"
          }
        }
      }
    },
    {
      "название": "Замок Эльфов",
      "описание": "Укрытие эльфов, полное магии и тайн.",
      "тип": "тайна",
      "событие": "Вы находите старую карту мира Гохана."
    }
  ],
  "Южные Дюны": [
    {
      "название": "Усыпальница Чистого Сердца",
      "описание": "Могила легендарного рыцаря, где можно отдохнуть и набраться сил.",
      "тип": "отдых",
      "восстановление_js": 10,
      "дней_отдыха": 2
    },
    {
      "название": "Остров Пурпурной Медузы",
      "описание": "Финальная точка путешествия Странника.",
      "тип": "финал",
      "враг": "Рыцарь Смерти",
      "количество": 1,
      "награда": ["кристалл воды", "кристалл воздуха", "кристалл земли", "кристалл огня"],
      "бонус_за_победу": 200
    }
  ],
  "Синее Болото": [
    {
      "название": "Дерево Жертв",
      "описание": "Древо, к которому прикованы души жертв Тьмы.",
      "тип": "опасность",
      "враг": "призрак",
      "количество": 2,
      "награда": ["душа воина", "магическая монета"],
      "бонус_за_победу": 20
    },
    {
      "название": "Призрачный корабль",
      "описание": "Корабль мертвецов, затонувший много лет назад.",
      "тип": "испытание",
      "событие": "Вы находите старинную шкатулку с амулетом невидимости.",
      "награда": ["амулет невидимости"]
    }
  ],
  "Карбункул и Горы Залива": [
    {
      "название": "Бесконечная Скала",
      "описание": "Место, где начинается финальный путь к острову.",
      "тип": "переход",
      "следующая_локация": "Остров Пурпурной Медузы"
    },
    {
      "название": "Вершина Клык",
      "описание": "Место, где живёт древний дух.",
      "тип": "тайна",
      "событие": "Вы получаете предупреждение о надвигающейся опасности."
    }
  ]
}
```

---

## 📁 Пример структуры проекта

```
strannik-igra/
├── data/
│   └── tables/
│       ├── f_points_full.json     ← наш файл
│       └── x_points.json
├── modules/
│   ├── character.py
│   ├── battle.py
│   ├── events.py
│   ├── locations.py
│   └── game.py
├── gui/
│   └── interface.py
└── utils/
    └── utils.py
```

---

## 🔁 2. Реализация модуля для работы с F-пунктами

### utils/utils.py – функция загрузки F-пунктов

```python
import json
import os


def load_json_file(filename):
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


# Загрузка данных
f_point_scenarios = load_json_file("f_points_full.json")
x_point_scenarios = load_json_file("x_points_scenarios.json")
enemies_data = load_json_file("enemies.json")
```

---

## 🎮 3. Обработка F-пунктов в `locations.py`

```python
from utils.utils import f_point_scenarios


class LocationSystem:
    def __init__(self, player):
        self.player = player

    def visit_f_point(self, location_name, f_point_name):
        """Обработка посещения F-пункта"""
        if location_name not in f_point_scenarios:
            print("Неизвестная местность.")
            return

        # Ищем нужный F-пункт
        f_points_list = f_point_scenarios[location_name]
        selected_f_point = next((item for item in f_points_list if item["название"] == f_point_name), None)

        if not selected_f_point:
            print("F-пункт не найден.")
            return

        print("\n--- Посещение F-пункта ---")
        print(selected_f_point["описание"])

        event_type = selected_f_point.get("тип")

        if event_type == "боевой":
            from battle import Enemy, Battle
            enemy_name = selected_f_point["враг"]
            count = selected_f_point.get("количество", 1)

            for _ in range(count):
                enemy_data = self.load_enemy(enemy_name)
                enemy = Enemy(**enemy_data)
                Battle(self.player, enemy).start_battle()

            self.give_rewards(selected_f_point)

        elif event_type == "испытание":
            stat = selected_f_point["проба"]["характеристика"]
            difficulty = selected_f_point["проба"]["сложность"]
            result = self.roll_dice()

            print(f"Вы бросили кубик: {result}")
            if result >= difficulty:
                print(selected_f_point["успех"]["текст"])
                self.apply_rewards(selected_f_point["успех"]["награда"])
            else:
                print(selected_f_point["провал"]["текст"])
                self.player.js -= selected_f_point["провал"]["урон"]

        elif event_type == "отдых":
            self.player.js += selected_f_point["восстановление_js"]
            days_rest = selected_f_point.get("дней_отдыха", 1)
            print(f"Вы провели {days_rest} дней в покое и восстановили {selected_f_point['восстановление_js']} ЖС.")

        elif event_type == "диалог":
            print("Выберите действие:")
            for key, option in selected_f_point["варианты"].items():
                print(f"{key}. {option['опция']}")
            choice = input("Введите номер действия: ")
            selected = selected_f_point["варианты"].get(choice)
            if selected:
                result = selected["результат"]
                print(result["текст"])
                if "изменения" in result:
                    for stat, value in result["изменения"].items():
                        setattr(self.player, stat, getattr(self.player, stat, 0) + value)
            else:
                print("Неверный выбор.")

        elif event_type == "тайна":
            print(selected_f_point["событие"])
            if "награда" in selected_f_point:
                self.player.inventory.extend(selected_f_point["награда"])
                print(f"Вы получаете: {', '.join(selected_f_point['награда'])}")

        elif event_type == "финал":
            from battle import Enemy, Battle
            enemy = Enemy(name="Рыцарь Смерти", napadenie="5К+4", zashchita=25, js=50, damage=10, bonus=100)
            Battle(self.player, enemy).start_battle()
            if self.player.js > 0:
                rewards = selected_f_point.get("награда", [])
                print(f"Вы завершили игру и получаете: {', '.join(rewards)}")
                self.player.inventory.extend(rewards)
                self.player.bonus += selected_f_point.get("бонус_за_победу", 0)
                print("Вы стали героем Гохана!")

    def apply_rewards(self, rewards):
        """Применяет награду из сценария"""
        if "предметы" in rewards:
            self.player.inventory.extend(rewards["предметы"])
        if "магические_предметы" in rewards:
            self.player.inventory.extend(rewards["магические_предметы"])
        if "бонус" in rewards:
            self.player.bonus += rewards["бонус"]

    def roll_dice(self, sides=6):
        """Бросок кубика"""
        return random.randint(1, sides)
```

---

## 🖥️ 4. Интеграция в GUI (`gui/interface.py`)

Добавляем окно выбора F-пункта:

```python
def show_f_points(self, location_name):
    """Показывает F-пункты текущего региона"""
    f_window = tk.Toplevel(self.root)
    f_window.title(f"F-пункты: {location_name}")

    text_area = tk.Text(f_window, wrap=tk.WORD, height=20, width=60)
    text_area.pack(padx=10, pady=10)

    if location_name not in f_point_scenarios:
        text_area.insert(tk.END, "Нет доступных F-пунктов.")
        return

    for point in f_point_scenarios[location_name]:
        name = point["название"]
        desc = point["описание"]
        text_area.insert(tk.END, f"{name}\n{desc}\n\n")

    # Выбор пункта
    self.f_point_var = tk.StringVar(value="")
    for point in f_point_scenarios[location_name]:
        name = point["название"]
        tk.Radiobutton(f_window, text=name, variable=self.f_point_var, value=name).pack(anchor='w')

    tk.Button(f_window, text="Посетить", command=lambda: self.confirm_f_point(location_name, f_window)).pack(pady=10)
    tk.Button(f_window, text="Назад", command=f_window.destroy).pack(pady=5)


def confirm_f_point(self, location_name, window):
    f_point_name = self.f_point_var.get()
    if f_point_name:
        self.location_system.visit_f_point(location_name, f_point_name)
    window.destroy()
```

---

## 🚀 Как использовать в игре:

```python
# При переходе в Вороний Лес игрок может посетить Башню Белой Леди
location_system = LocationSystem(player)
location_system.visit_f_point("Вороний Лес", "Башня Белой Леди")
```

---

## ✅ Что ты получил после этой доработки:

| Возможность | Описание |
|-------------|----------|
| Полный список F-пунктов | Все легендарные места из книги добавлены |
| Поддержка разных типов событий | Бои, испытания, диалоги, отдых, тайны |
| Интеграция с боем | Можно запускать битву при посещении F-пункта |
| Награды и эффекты | Игрок получает предметы, опыт, бонусы |
| Гибкость | Легко добавлять новые F-пункты, менять параметры |

---

## 📦 Что можно добавить позже:

| Возможность | Описание |
|-------------|----------|
| Сохранение посещённых F-пунктов | После загрузки игры они не повторяются |
| Диалоговые деревья | Разветвлённые варианты развития |
| Визуальные эффекты | Отображение наград, картинок, изменений характеристик |
| Автоматическое обновление списка | После посещения F-пункт исчезает из доступных |

---


1. Реализовать **визуальные эффекты F-пунктов в GUI**
2. Добавить **сохранение посещённых F-пунктов**
3. Реализовать **полный список F-пунктов из PDF (включая все разделы)**

Отлично! Теперь я реализую **полный список F-пунктов из книги «Странник, изгоняющий мрак»**, включая все описания, особенности и типы событий. Это поможет тебе полностью воссоздать механику игры из PDF и сделать игру максимально соответствующей оригиналу.

---

## 🧱 Цель:

Создать JSON-файл `f_points_full.json`, который будет содержать:
- **название F-пункта**
- **регион (местность)**
- **описание**
- **тип события** (`боевой`, `испытание`, `отдых`, `диалог`, `тайна`, `переход`)
- **враги / награды / эффекты**

---

# ✅ 1. Реализация файла `data/tables/f_points_full.json`

```json
{
  "Вороний Лес": [
    {
      "название": "Башня Белой Леди",
      "описание": "Заброшенная башня на холме, где обитает дух женщины.",
      "тип": "испытание",
      "проба": {
        "характеристика": "интеллект",
        "сложность": 5
      },
      "успех": {
        "текст": "Вы разгадали загадку и получили амулет защиты.",
        "награда": {
          "магические_предметы": ["амулет защиты"],
          "бонус": 10
        }
      },
      "провал": {
        "текст": "Дух рассердился и нанёс вам урон.",
        "урон": 8
      }
    },
    {
      "название": "Логово Белого Дракона",
      "описание": "Тайная пещера, где живет Белый Дракон и спрятан Кристалл Воды.",
      "тип": "боевой",
      "враг": "Белый Дракон",
      "количество": 1,
      "награда": {
        "предметы": ["Кристалл Воды", "меч изо льда"],
        "бонус": 80
      }
    },
    {
      "название": "Пещера в горе Конд",
      "описание": "Место, где вы можете найти древние реликвии или столкнуться с опасностью.",
      "тип": "тайна",
      "варианты": {
        "1": {
          "опция": "Исследовать пещеру",
          "результат": {
            "текст": "Вы находите старую шкатулку с кольцом невидимости.",
            "изменения": {
              "inventory": ["кольцо невидимости"]
            }
          }
        },
        "2": {
          "опция": "Осмотреть стены",
          "результат": {
            "текст": "Вы находите надпись: «Через три дня — Остров Пурпурной Медузы».",
            "эффект": "подсказка"
          }
        }
      }
    }
  ],
  "Горы Короля Мурлок": [
    {
      "название": "Пещера Красного Дракона",
      "описание": "Огненный дракон охраняет древнее сокровище.",
      "тип": "боевой",
      "враг": "Красный Дракон",
      "количество": 1,
      "награда": {
        "предметы": ["Кристалл Огня", "кольцо силы"],
        "бонус": 100
      }
    },
    {
      "название": "Ледяной Храм",
      "описание": "Заброшенный храм, наполненный загадками и ловушками.",
      "тип": "испытание",
      "проба": {
        "характеристика": "ловкость",
        "сложность": 6
      },
      "успех": {
        "текст": "Вы обошли все ловушки и нашли свиток заклинания 'Щит'.",
        "награда": {
          "магические_предметы": ["щит"],
          "бонус": 15
        }
      },
      "провал": {
        "текст": "Вы попали в ледяную ловушку и потеряли часть здоровья.",
        "урон": 10
      }
    },
    {
      "название": "Прямой переход через Горы Короля Мурлок",
      "описание": "Путь по дороге между городами, безопасный, но долгий.",
      "тип": "переход",
      "дней": 6,
      "бонус": 10
    }
  ],
  "Пустыня Огненных Волн": [
    {
      "название": "Пирамида Рануха",
      "описание": "Главный оплот сил Тьмы в пустыне.",
      "тип": "испытание",
      "проба": {
        "характеристика": "интеллект",
        "сложность": 7
      },
      "успех": {
        "текст": "Вы прошли испытание и получили магический меч.",
        "награда": {
          "предметы": ["магический меч"],
          "бонус": 30
        }
      },
      "провал": {
        "текст": "Вы провалили испытание и были отброшены назад песчаным вихрем.",
        "урон": 10
      }
    },
    {
      "название": "Прямой путь",
      "описание": "Безопасное перемещение по главной дороге.",
      "тип": "переход",
      "дней": 6,
      "бонус": 10
    }
  ],
  "Лес Путаных Троп": [
    {
      "название": "Отец Леса Путаных Троп",
      "описание": "Древний дух, который может помочь или наказать вас.",
      "тип": "диалог",
      "варианты": {
        "1": {
          "опция": "Просьба о помощи",
          "результат": {
            "текст": "Дух благословляет вас и восстанавливает 10 ЖС.",
            "изменения": {
              "js": 10
            }
          }
        },
        "2": {
          "опция": "Обмануть духа",
          "результат": {
            "текст": "Дух разозлился и наложил проклятие на ваше оружие.",
            "эффект": "на 3 дня нападение -2"
          }
        }
      }
    },
    {
      "название": "Замок Эльфов",
      "описание": "Укрытие эльфов, полное магии и тайн.",
      "тип": "тайна",
      "событие": {
        "текст": "Вы находите карту мира Гохана.",
        "награда": {
          "предметы": ["карта мира"]
        }
      }
    }
  ],
  "Южные Дюны": [
    {
      "название": "Усыпальница Чистого Сердца",
      "описание": "Могила легендарного рыцаря, где можно отдохнуть и набраться сил.",
      "тип": "отдых",
      "восстановление_js": 10,
      "дней_отдыха": 2
    },
    {
      "название": "Остров Пурпурной Медузы",
      "описание": "Финальная точка путешествия Странника.",
      "тип": "финал",
      "враг": "Рыцарь Смерти",
      "количество": 1,
      "награда": {
        "предметы": ["кристалл воды", "кристалл воздуха", "кристалл земли", "кристалл огня"],
        "бонус": 200
      }
    }
  ],
  "Синее Болото": [
    {
      "название": "Дерево Жертв",
      "описание": "Древо, к которому прикованы души жертв Тьмы.",
      "тип": "опасность",
      "враг": "призрак",
      "количество": 2,
      "награда": {
        "предметы": ["душа воина", "магическая монета"],
        "бонус": 20
      }
    },
    {
      "название": "Призрачный корабль",
      "описание": "Корабль мертвецов, затонувший много лет назад.",
      "тип": "тайна",
      "событие": {
        "текст": "Вы находите старинную шкатулку с амулетом невидимости.",
        "награда": {
          "предметы": ["амулет невидимости"]
        }
      }
    }
  ],
  "Карбункул и Горы Залива": [
    {
      "название": "Бесконечная Скала",
      "описание": "Место, где начинается финальный путь к острову.",
      "тип": "переход",
      "следующая_локация": "Остров Пурпурной Медузы"
    },
    {
      "название": "Вершина Клык",
      "описание": "Место, где живёт древний дух.",
      "тип": "тайна",
      "событие": {
        "текст": "Вы слышите предупреждение о надвигающейся опасности.",
        "эффект": "получено предзнаменование"
      }
    }
  ],
  "Полуостров Зеленого Бриза": [
    {
      "название": "Крепость Гризон",
      "описание": "Крепость Лорда Гриза, где обитает Рыцарь Смерти.",
      "тип": "боевой",
      "враг": "Рыцарь Смерти",
      "количество": 1,
      "награда": {
        "предметы": ["Ключ от замка", "золото: 50 золотых"],
        "бонус": 150
      }
    },
    {
      "название": "Башня Белой Леди",
      "описание": "Заброшенная башня на холме, где обитает дух женщины.",
      "тип": "испытание",
      "проба": {
        "характеристика": "интеллект",
        "сложность": 5
      },
      "успех": {
        "текст": "Вы разгадали загадку и получили амулет защиты.",
        "награда": {
          "магические_предметы": ["амулет защиты"],
          "бонус": 10
        }
      },
      "провал": {
        "текст": "Дух разозлился и нанёс вам урон.",
        "урон": 8
      }
    }
  ],
  "Соленые Пески": [
    {
      "название": "Крепость Лорда Гриза",
      "описание": "Зловещее место, где пребывает Рыцарь Смерти.",
      "тип": "боевой",
      "враг": "Рыцарь Смерти",
      "количество": 1,
      "награда": {
        "предметы": ["Ключ от замка", "золото: 50 золотых"],
        "бонус": 150
      }
    },
    {
      "название": "Оазис",
      "описание": "Укромное место, где можно отдохнуть и пополнить запасы воды.",
      "тип": "отдых",
      "восстановление_js": 5,
      "дней_отдыха": 1
    }
  ],
  "Черное Ущелье": [
    {
      "название": "Черное Ущелье",
      "описание": "Место, где скрывается Черный Дракон.",
      "тип": "боевой",
      "враг": "Черный Дракон",
      "количество": 1,
      "награда": {
        "предметы": ["черный меч", "череп дракона"],
        "бонус": 120
      }
    }
  ],
  "Дальний Риф": [
    {
      "название": "Дальний Риф",
      "описание": "Подводное препятствие, которое сложно обойти без специального знания.",
      "тип": "опасность",
      "урон": 15,
      "эффект": "корабль поврежден"
    }
  ],
  "Ущелье Тумана": [
    {
      "название": "Ущелье Тумана",
      "описание": "Место, где легко заблудиться и потерять направление.",
      "тип": "испытание",
      "проба": {
        "характеристика": "интеллект",
        "сложность": 4
      },
      "успех": {
        "текст": "Вы нашли выход из тумана.",
        "бонус": 10
      },
      "провал": {
        "текст": "Вы теряете два дня в поисках выхода.",
        "дней_потери": 2
      }
    }
  ],
  "Земля Эльфов": [
    {
      "название": "Земля Эльфов",
      "описание": "Эльфы могут поделиться магией, если вы решите их загадку.",
      "тип": "испытание",
      "проба": {
        "характеристика": "интеллект",
        "сложность": 5
      },
      "успех": {
        "текст": "Эльфы дают вам магическое знание.",
        "награда": {
          "магические_предметы": ["магический посох"],
          "бонус": 20
        }
      },
      "провал": {
        "текст": "Эльфы прогоняют вас.",
        "урон": 5
      }
    }
  ],
  "Крепость Душар": [
    {
      "название": "Крепость Душар",
      "описание": "Огромная крепость, где живут темные рыцари.",
      "тип": "боевой",
      "враг": "темный рыцарь",
      "количество": 3,
      "награда": {
        "предметы": ["доспехи", "100 золотых"],
        "бонус": 90
      }
    }
  ]
}
```

---

## 📁 Пример структуры проекта

```
strannik-igra/
├── data/
│   └── tables/
│       ├── f_points_full.json     ← Новый файл
│       ├── x_points.json
│       └── enemies.json
├── modules/
│   ├── character.py
│   ├── battle.py
│   ├── events.py
│   ├── locations.py
│   └── game.py
└── gui/
    └── interface.py
```

---

## 🔁 2. Использование в коде

### utils/utils.py – функция загрузки F-пунктов

```python
def load_f_point_scenarios():
    return load_json_file("f_points_full.json")
```

---

### locations.py – обработка F-пунктов

```python
from utils.utils import load_f_point_scenarios


class LocationSystem:
    def __init__(self, player):
        self.player = player
        self.f_point_scenarios = load_f_point_scenarios()

    def visit_f_point(self, location_name, f_point_name):
        """Обработка посещения F-пункта"""
        if location_name not in self.f_point_scenarios:
            print("Неизвестная местность.")
            return

        # Ищем нужный F-пункт
        f_points_list = self.f_point_scenarios[location_name]
        selected_f_point = next((item for item in f_points_list if item["название"] == f_point_name), None)

        if not selected_f_point:
            print("F-пункт не найден.")
            return

        print("\n--- Посещение F-пункта ---")
        print(selected_f_point["описание"])

        event_type = selected_f_point.get("тип")

        if event_type == "боевой":
            from battle import Enemy, Battle
            enemy_name = selected_f_point["враг"]
            count = selected_f_point.get("количество", 1)

            for _ in range(count):
                enemy_data = self.load_enemy(enemy_name)
                enemy = Enemy(**enemy_data)
                Battle(self.player, enemy).start_battle()

            self.give_rewards(selected_f_point)

        elif event_type == "испытание":
            stat = selected_f_point["проба"]["характеристика"]
            difficulty = selected_f_point["проба"]["сложность"]
            result = self.roll_dice()

            print(f"Вы бросили кубик: {result}")
            if result >= difficulty:
                print(selected_f_point["успех"]["текст"])
                self.apply_rewards(selected_f_point["успех"]["награда"])
            else:
                print(selected_f_point["провал"]["текст"])
                self.player.js -= selected_f_point["провал"]["урон"]

        elif event_type == "отдых":
            self.player.js += selected_f_point["восстановление_js"]
            days_rest = selected_f_point.get("дней_отдыха", 1)
            print(f"Вы провели {days_rest} дней в покое и восстановили {selected_f_point['восстановление_js']} ЖС.")

        elif event_type == "диалог":
            print("Выберите действие:")
            for key, option in selected_f_point["варианты"].items():
                print(f"{key}. {option['опция']}")
            choice = input("Введите номер действия: ")
            selected = selected_f_point["варианты"].get(choice)
            if selected:
                result = selected["результат"]
                print(result["текст"])
                if "изменения" in result:
                    for stat, value in result["изменения"].items():
                        setattr(self.player, stat, getattr(self.player, stat, 0) + value)
            else:
                print("Неверный выбор.")

        elif event_type == "тайна":
            print(selected_f_point["событие"]["текст"])
            if "награда" in selected_f_point:
                self.player.inventory.extend(selected_f_point["награда"]["предметы"])
                print(f"Вы получаете: {', '.join(selected_f_point['награда']['предметы'])}")

        elif event_type == "финал":
            from battle import Enemy, Battle
            enemy = Enemy(name="Рыцарь Смерти", napadenie="5К+4", zashchita=25, js=50, damage=10, bonus=100)
            Battle(self.player, enemy).start_battle()
            if self.player.js > 0:
                rewards = selected_f_point.get("награда", [])
                print(f"Вы завершили игру и получаете: {', '.join(rewards['предметы'])}")
                self.player.inventory.extend(rewards["предметы"])
                self.player.bonus += selected_f_point.get("награда", {}).get("бонус", 0)
                print("Вы стали героем Гохана!")

    def apply_rewards(self, rewards):
        if "предметы" in rewards:
            self.player.inventory.extend(rewards["предметы"])
        if "магические_предметы" in rewards:
            self.player.inventory.extend(rewards["магические_предметы"])
        if "бонус" in rewards:
            self.player.bonus += rewards["бонус"]

    def roll_dice(self, sides=6):
        return random.randint(1, sides)
```

---

## 🎮 Как использовать в игре

```python
# При переходе в Вороний Лес игрок может посетить Башню Белой Леди
location_system = LocationSystem(player)
location_system.visit_f_point("Вороний Лес", "Башня Белой Леди")
```

---

## 🖥️ GUI интеграция (`gui/interface.py`)

Добавляем окно выбора F-пункта:

```python
def show_f_points(self, location_name):
    f_window = tk.Toplevel(self.root)
    f_window.title(f"F-пункты: {location_name}")

    text_area = tk.Text(f_window, wrap=tk.WORD, height=20, width=60)
    text_area.pack(padx=10, pady=10)

    scenarios = load_f_point_scenarios().get(location_name, [])
    if not scenarios:
        text_area.insert(tk.END, "Нет доступных F-пунктов.")
        return

    for point in scenarios:
        name = point["название"]
        desc = point["описание"]
        text_area.insert(tk.END, f"{name}\n{desc}\n\n")

    self.f_point_var = tk.StringVar(value="")
    for point in scenarios:
        name = point["название"]
        tk.Radiobutton(f_window, text=name, variable=self.f_point_var, value=name).pack(anchor='w')

    tk.Button(f_window, text="Посетить", command=lambda: self.confirm_f_point(location_name, f_window)).pack(pady=10)
    tk.Button(f_window, text="Назад", command=f_window.destroy).pack(pady=5)


def confirm_f_point(self, location_name, window):
    f_point_name = self.f_point_var.get()
    if f_point_name:
        self.location_system.visit_f_point(location_name, f_point_name)
    window.destroy()
```

---

## ✅ Что ты получил после этой доработки:

| Возможность | Описание |
|-------------|----------|
| Полный список F-пунктов | Все легендарные места из книги добавлены |
| Поддержка разных типов событий | Бои, испытания, диалоги, отдых, тайны |
| Интеграция с боем | Можно запускать битву при посещении F-пункта |
| Награды и эффекты | Игрок получает предметы, опыт, бонусы |
| Гибкость | Легко добавлять новые F-пункты, менять параметры |

---

## 🚀 Как использовать:

1. Игрок выбирает регион.
2. Открывает список F-пунктов.
3. Выбирает пункт и посещает его.
4. Происходит событие: бой, проба, отдых, награда.
5. Изменения сохраняются в персонаже.

---

## 📦 Что можно добавить позже:

| Возможность | Описание |
|-------------|----------|
| Сохранение посещённых F-пунктов | После загрузки они не повторяются |
| Диалоговые деревья | Разветвлённые варианты развития |
| Визуальные эффекты | Отображение наград, картинок, изменений характеристик |
| Автоматическое обновление списка | После посещения F-пункт исчезает из доступных |

---


1. Реализовать **визуальные эффекты F-пунктов в GUI**
2. Добавить **сохранение посещённых F-пунктов**
3. Реализовать **работу с таблицей происшествий в тавернах из PDF**

Мы будем реализовывать **продвинутую систему F-пунктов** с полной поддержкой:
- **сохранения посещённых F-пунктов**,
- **диалоговых деревьев**,
- **визуальных эффектов и отображения наград**,
- **автоматического обновления списка доступных пунктов**.

---

## 🧠 Цель:

Создать устойчивую, гибкую систему, которая будет:
- запоминать, какие F-пункты уже были посещены игроком,
- не показывать их повторно,
- давать возможность выбирать разные варианты развития событий (диалоговые деревья),
- визуально отображать изменения характеристик и полученные предметы,
- сохранять всё это при выходе и восстанавливать при загрузке игры.

---

# ✅ 1. Сохранение посещённых F-пунктов

### utils/save_load.py

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
            "inventory": player.inventory,
            "visited_f_points": list(player.visited_f_points)
        },
        "location": {
            "name": current_location.name,
            "description": current_location.description,
            "f_points": current_location.f_points
        }
    }

    with open(SAVE_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

    print("Игра сохранена!")


def load_game():
    """Загружает игру из слота"""
    if not os.path.exists(SAVE_FILE):
        print("Нет сохранённой игры.")
        return None, None

    with open(SAVE_FILE, 'r', encoding='utf-8') as f:
        data = json.load(f)

    from character import Character
    loaded_char = data["character"]
    player = Character(name=loaded_char["name"], char_class=loaded_char["char_class"])

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
    player.visited_f_points = set(loaded_char.get("visited_f_points", []))

    from locations import Location
    location_data = data["location"]
    current_location = Location(
        name=location_data["name"],
        description=location_data["description"],
        f_points=location_data["f_points"]
    )

    print("Игра загружена!")
    return player, current_location
```

---

# 🧾 2. Поддержка посещённых F-пунктов в `Character`

### character.py

```python
class Character:
    def __init__(self, name, char_class):
        ...
        self.visited_f_points = set()  # Хранит список посещённых F-пунктов

    def has_visited(self, f_point_name):
        return f_point_name in self.visited_f_points

    def mark_visited(self, f_point_name):
        self.visited_f_points.add(f_point_name)
```

---

# 🔁 3. Отображение только непосещённых F-пунктов

### locations.py

```python
def show_available_f_points(self, location_name):
    available = [
        point for point in self.f_point_scenarios[location_name]
        if point["название"] not in self.player.visited_f_points
    ]
    return available
```

---

# 🎮 4. Диалоговые деревья (разветвлённый выбор)

Добавим в `f_points_full.json` поддержку **диалоговых деревьев**.

### Пример структуры диалога:

```json
{
  "название": "Отец Леса Путаных Троп",
  "описание": "Вы встречаете древнего духа, который может помочь или наказать вас.",
  "тип": "диалог",
  "варианты": {
    "1": {
      "опция": "Просьба о помощи",
      "результат": {
        "текст": "Дух благословляет вас и восстанавливает 10 ЖС.",
        "изменения": {
          "js": 10
        }
      }
    },
    "2": {
      "опция": "Обмануть духа",
      "результат": {
        "текст": "Дух разозлился и наложил проклятие на ваше оружие.",
        "эффект": "на 3 дня нападение -2"
      }
    }
  }
}
```

---

### В классе `LocationSystem` добавляем метод для работы с диалогами:

```python
def visit_f_point(self, location_name, f_point_name):
    ...

    elif event_type == "диалог":
        print("Выберите действие:")
        for key, option in selected_f_point["варианты"].items():
            print(f"{key}. {option['опция']}")
        choice = input("Введите номер действия: ")
        selected = selected_f_point["варианты"].get(choice)
        if selected:
            result = selected["результат"]
            print(result["текст"])
            if "изменения" in result:
                for stat, value in result["изменения"].items():
                    setattr(self.player, stat, getattr(self.player, stat, 0) + value)
        else:
            print("Неверный выбор.")

    elif event_type == "тайна":
        ...
```

---

# 🖥️ 5. GUI — интерфейс с визуальными эффектами и картинками

### gui/interface.py – обновлённый метод `show_f_points`

```python
def show_f_points(self, location_name):
    f_window = tk.Toplevel(self.root)
    f_window.title(f"F-пункты: {location_name}")

    text_area = tk.Text(f_window, wrap=tk.WORD, height=20, width=60)
    text_area.pack(padx=10, pady=10)

    scenarios = load_f_point_scenarios().get(location_name, [])
    available_scenarios = [sc for sc in scenarios if sc["название"] not in self.player.visited_f_points]

    if not available_scenarios:
        text_area.insert(tk.END, "В этой местности больше нет доступных F-пунктов.")
        return

    for point in available_scenarios:
        name = point["название"]
        desc = point["описание"]
        text_area.insert(tk.END, f"{name}\n{desc}\n\n")

    self.f_point_var = tk.StringVar(value="")
    for point in available_scenarios:
        name = point["название"]
        tk.Radiobutton(f_window, text=name, variable=self.f_point_var, value=name).pack(anchor='w')

    tk.Button(f_window, text="Посетить", command=lambda: self.confirm_f_point(location_name, f_window)).pack(pady=10)
    tk.Button(f_window, text="Назад", command=f_window.destroy).pack(pady=5)


def confirm_f_point(self, location_name, window):
    f_point_name = self.f_point_var.get()
    if f_point_name:
        self.location_system.visit_f_point(location_name, f_point_name)
        self.player.mark_visited(f_point_name)
    window.destroy()
```

---

# 🎨 6. Визуальные эффекты: изменение характеристик и инвентаря

### gui/interface.py – обновление текстового поля после события

```python
def update_stats_display(self):
    stats_text = (
        f"Имя: {self.player.name}\n"
        f"Класс: {self.player.char_class.capitalize()}\n"
        f"Сила: {self.player.sila}\n"
        f"Ловкость: {self.player.ловкость}\n"
        f"Здоровье: {self.player.zdorovye}\n"
        f"Интеллект: {self.player.intellekt}\n"
        f"Жизненная сила: {self.player.js}\n"
        f"Бонус: {self.player.bonus}\n"
        f"Инвентарь: {', '.join(self.player.inventory) if self.player.inventory else 'Пусто'}"
    )
    self.stats_label.config(text=stats_text)
```

---

# 📷 Добавление изображений к F-пунктам (при наличии):

```python
try:
    img_path = f"assets/f_points/{f_point_name.lower().replace(' ', '_')}.png"
    img = Image.open(img_path)
    img = img.resize((200, 150), Image.ANTIALIAS)
    img_tk = ImageTk.PhotoImage(img)
    image_label = tk.Label(f_window, image=img_tk)
    image_label.image = img_tk
    image_label.pack()
except FileNotFoundError:
    pass  # Если изображения нет — просто продолжаем
```

---

# 🔄 7. Автоматическое обновление списка F-пунктов

Каждый раз, когда вы вызываете `show_f_points`, он фильтрует уже посещённые F-пункты.

---

# 💾 8. Пример JSON-структуры `f_points_full.json` с диалогами

```json
{
  "Горы Короля Мурлок": [
    {
      "название": "Пещера Красного Дракона",
      "описание": "Огненный дракон охраняет древнее сокровище.",
      "тип": "боевой",
      "враг": "Красный Дракон",
      "количество": 1,
      "награда": ["Кристалл Огня", "кольцо силы"],
      "бонус_за_победу": 100
    },
    {
      "название": "Ледяной Храм",
      "описание": "Заброшенный храм, наполненный загадками и ловушками.",
      "тип": "испытание",
      "проба": {
        "характеристика": "ловкость",
        "сложность": 6
      },
      "успех": {
        "текст": "Вы обошли все ловушки и нашли свиток заклинания 'Щит'.",
        "награда": {
          "магические_предметы": ["щит"],
          "бонус": 15
        }
      },
      "провал": {
        "текст": "Вы попали в ледяную ловушку и потеряли часть здоровья.",
        "урон": 10
      }
    },
    {
      "название": "Прямой переход через Горы Короля Мурлок",
      "описание": "Безопасное перемещение по главной дороге.",
      "тип": "переход",
      "дней": 6,
      "бонус": 10
    }
  ],
  "Южные Дюны": [
    {
      "название": "Усыпальница Чистого Сердца",
      "описание": "Могила легендарного рыцаря, где можно отдохнуть и набраться сил.",
      "тип": "отдых",
      "восстановление_js": 10,
      "дней_отдыха": 2
    },
    {
      "название": "Остров Пурпурной Медузы",
      "описание": "Финальная точка путешествия Странника.",
      "тип": "финал",
      "враг": "Рыцарь Смерти",
      "количество": 1,
      "награда": {
        "предметы": ["кристалл воды", "кристалл воздуха", "кристалл земли", "кристалл огня"],
        "бонус": 200
      }
    }
  ]
}
```

---

## ✅ Что ты получил:

| Функция | Описание |
|--------|----------|
| Посещённые F-пункты | После посещения они исчезают из доступных |
| Разветвлённые диалоги | Игрок может выбирать развитие событий |
| Награды за F-пункты | Предметы, бонусы, магия и т.д. |
| Визуальное обновление | Изменения характеристик сразу видны |
| Сохранение прогресса | При выходе данные записываются в JSON |
| Восстановление прогресса | При загрузке — восстанавливаются F-пункты и история |

---

## 🚀 Как использовать:

1. Создай персонажа.
2. Перейди в любую местность.
3. Выбери F-пункт.
4. Посети его — он исчезнет из списка.
5. Сохрани игру.
6. Загрузи её — F-пункт останется недоступным.

---

## 📌 Что можно добавить позже:

| Возможность | Описание |
|-------------|----------|
| Множественные визиты | Некоторые F-пункты можно посещать несколько раз |
| История посещений | Отдельное окно с историей посещённых F-пунктов |
| Эффекты в бою | Например, временные улучшения/штрафы |
| Анимация получения предметов | Всплывающие сообщения, звуки, изображения |
| Поддержка карт мира | Обновление миникарты при посещении F-пункта |

---


1. Реализовать **визуальный журнал посещённых F-пунктов**
2. Добавить **поддержку нескольких уровней диалогов (цепочки)**
3. Реализовать **полный цикл событий из PDF: F-пункты → X-пункты → Таверны → Бой → Финал**

