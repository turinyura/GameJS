import os
from pathlib import Path

def create_project_structure(base_path="."):
    """Создает структуру папок и файлов для проекта 'strannik-igra'"""
    
    # Основные директории
    directories = [
        "strannik-igra",
        "strannik-igra/modules",
        "strannik-igra/data/tables",
        "strannik-igra/data/descriptions",
        "strannik-igra/assets",
        "strannik-igra/gui",
        "strannik-igra/tests"
    ]
    
    # Файлы с путями
    files = {
        "strannik-igra/main.py": "# Точка входа в игру\n",
        
        "strannik-igra/modules/character.py": "# Класс персонажа (воин, вор и т.д.)\n",
        "strannik-igra/modules/battle.py": "# Логика боёв\n",
        "strannik-igra/modules/events.py": "# События, пробы, случайные происшествия\n",
        "strannik-igra/modules/locations.py": "# Локации, пути, таблицы событий\n",
        "strannik-igra/modules/game.py": "# Основной игровой цикл\n",
        "strannik-igra/modules/utils.py": "# Вспомогательные функции (броски кубиков, проверки)\n",
        
        "strannik-igra/data/tables/stats_table.json": "{}",
        "strannik-igra/data/tables/events_table.json": "{}",
        
        "strannik-igra/data/descriptions/intro.txt": "",
        "strannik-igra/data/descriptions/tavern_events.txt": "",
        
        "strannik-igra/gui/interface.py": "# GUI с использованием tkinter или pygame\n",
        "strannik-igra/gui/screens.py": "# Экраны: главное меню, создание персонажа, бой и т.д.\n",
        
        "strannik-igra/tests/test_character.py": "# Тесты для модуля character.py\n",
        "strannik-igra/tests/test_battle.py": "# Тесты для модуля battle.py\n"
    }
    
    # Создаем директории
    for directory in directories:
        dir_path = Path(base_path) / directory
        try:
            dir_path.mkdir(parents=True, exist_ok=True)
            print(f"Создана директория: {dir_path}")
        except OSError as e:
            print(f"Ошибка при создании директории {dir_path}: {e}")
    
    # Создаем файлы
    for file_path, content in files.items():
        full_path = Path(base_path) / file_path
        try:
            with open(full_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Создан файл: {full_path}")
        except OSError as e:
            print(f"Ошибка при создании файла {full_path}: {e}")

if __name__ == "__main__":
    print("Создание структуры проекта 'strannik-igra'...")
    create_project_structure()
    print("Готово!")