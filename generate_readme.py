import csv
from pathlib import Path
import re

# Пути
homeworks_dir = Path("homeworks")
lessons_file = Path("lessons.csv")
readme_file = Path("README.md")

# Чтение структуры занятий
lessons = []
with open(lessons_file, encoding="utf-8-sig") as f:
    reader = csv.DictReader(f, delimiter=';')
    current_section = ""
    current_topic = ""
    for row in reader:
        section = row["section"].strip() if row["section"] else current_section
        topic = row["topic"].strip() if row["topic"] else current_topic
        code = row["code"].strip()
        title = row["title"].strip()
        date = row["date"].strip()
        lessons.append({
            "section": section,
            "topic": topic,
            "code": code,
            "title": title,
            "date": date
        })
        current_section, current_topic = section, topic

# Сканирование файлов в папке homeworks/
files = sorted(homeworks_dir.glob("*"))
homework_map = {}

for file in files:
    match = re.match(r"(OP\d{2}_HW_\d{2})", file.stem)
    if match:
        base = match.group(1)
        homework_map.setdefault(base, {"main": None, "extras": []})
        if file.suffix == ".py":
            homework_map[base]["main"] = file
        else:
            homework_map[base]["extras"].append(file)

# Генерация README.md
with open(readme_file, "w", encoding="utf-8") as readme:
    readme.write("# Python 2025\n\n")
    readme.write("## Домашние задания по занятиям\n\n")

    last_section = ""
    last_topic = ""

    for lesson in lessons:
        code = lesson["code"]
        lesson_key_prefix = code.replace("OP", "OP") + "_HW_"
        matching_keys = [k for k in homework_map.keys() if k.startswith(lesson_key_prefix)]

        if not matching_keys:
            continue  # Пропускаем, если нет домашних заданий

        # Раздел
        if lesson["section"] != last_section:
            readme.write(f"## {lesson['section']}\n\n")
            last_section = lesson["section"]

        # Тема
        if lesson["topic"] != last_topic:
            readme.write(f"### {lesson['topic']}\n\n")
            last_topic = lesson["topic"]

        # Занятие
        readme.write(f"#### Занятие {code[2:]} — {lesson['date']}\n")
        readme.write(f"📘 *{lesson['title']}*\n\n")

        for key in sorted(matching_keys):
            data = homework_map[key]
            hw_num = key.split("_HW_")[1]

            # Описание из docstring
            description = ""
            if data["main"]:
                with open(data["main"], "r", encoding="utf-8") as f:
                    first_line = f.readline().strip()
                    if first_line.startswith(("'''", '"""')):
                        description = first_line.strip('"""').strip("'''").strip()

            # Основной файл
            readme.write(f"- **Домашка {hw_num}** — [{data['main'].name}](homeworks/{data['main'].name})\n")
            if description:
                readme.write(f"  \U0001F4DD *Описание*: {description}\n")

            # Дополнительные файлы
            for extra in data["extras"]:
                readme.write(f"  \U0001F4CE Доп. файл: [{extra.name}](homeworks/{extra.name})\n")

            readme.write("\n")
