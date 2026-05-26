import os

def convert_value(value: str) -> str | int | float:
    """Преобразует строку в int, float или оставляет str."""
    if not value or value.strip() == "":
        return ""
    
    val_clean = value.strip()
    
    #убираем кавычки
    if val_clean.startswith('"') and val_clean.endswith('"'):
        val_clean = val_clean[1:-1].strip()
    
    has_minus = val_clean.startswith("-")
    check_str = val_clean[1:] if has_minus else val_clean

    #проверка на int
    if check_str.isdigit() and len(check_str) > 0:
        return int(val_clean)
        
    #проверка на float
    if val_clean.count(".") == 1:
        str_without_dot = check_str.replace(".", "", 1)
        if str_without_dot.isdigit() and len(str_without_dot) > 0:
            return float(val_clean)
            
    return val_clean


def read_table_file(filepath: str, delimiter: str = ',', has_header: bool = True) -> dict:
    """Читает таблицу и определяет типы данных по первой строке."""
    with open(filepath, 'r', encoding='utf-8') as f:
        #игнорируем пустые строки в файле
        lines = [line.strip() for line in f if line.strip()]

    if not lines:
        return {'header': [], 'data': [], 'types': []}

    start_data_idx = 0
    header_list = []

    # обработка заголовка
    if has_header:
        
        if delimiter == ' ':
            header_list = [col.strip() for col in lines[0].split()]
        else:
            header_list = [col.strip() for col in lines[0].split(delimiter)]
        start_data_idx = 1

    if start_data_idx >= len(lines):
        return {'header': header_list, 'data': [], 'types': []}

    #считываем сырые данные строк
    raw_data = []
    for line in lines[start_data_idx:]:
        if delimiter == ' ':
            row = [col.strip() for col in line.split()]
        else:
            row = [col.strip() for col in line.split(delimiter)]
        raw_data.append(row)

    #определение типов столбцов
    first_data_row = raw_data[0]
    column_types = []
    for val in first_data_row:
        converted = convert_value(val)
        column_types.append(type(converted).__name__)

    #преобразования ко всем строкам таблицы
    final_data = []
    for row in raw_data:
        converted_row = []
        for idx, val in enumerate(row):
            if idx < len(column_types):
                col_type = column_types[idx]
                if col_type == 'int':
                    try:
                        clean_val = val.strip().strip('"')
                        converted_row.append(int(clean_val))
                    except ValueError:
                        converted_row.append(val)
                elif col_type == 'float':
                    try:
                        clean_val = val.strip().strip('"')
                        converted_row.append(float(clean_val))
                    except ValueError:
                        converted_row.append(val)
                else:
                    converted_row.append(val.strip().strip('"'))
            else:
                converted_row.append(convert_value(val))
        final_data.append(converted_row)

    return {
        'header': header_list if has_header else None,
        'data': final_data,
        'types': column_types
    }


#исходные файлы

files_content = {
    "file1.txt": (
        "Name,Age,Salary,FullTime,Department\n"
        "Ivan Petrov,28,75000.50,True,IT\n"
        "Mariya Sidorova,35,82000.75,True,HR\n"
        "Aleksej Ivanov,22,45000.00,False,Sales\n"
        "Olga Smirnova,41,95000.25,True,Management\n"
        "Dmitrij Kuznecov,19,35000.50,False,IT"
    ),
    "file2.txt": (
        "ID Name Category Price InStock Rating Weight\n"
        "001 Noutbuk Elektronika 899.99 True 4.5 2.3\n"
        "002 Stul Mebel 150.00 True 4.2 7.8\n"
        "003 Kniga Kancelyariya 25.50 False 4.8 0.5\n"
        "004 Telefon Elektronika 599.99 True 4.1 0.3\n"
        "005 Stol Mebel 32.23 False 4.7 15.2"
    ),
    "file3.txt": (
        "Yabloki;100;85.50;Frukty;2024-01-20\n"
        "Banany;150;65.30;Frukty;2024-01-18\n"
        "Moloko;50;89.90;Molochnye;2024-01-19\n"
        "Hleb;200;45.00;Vypechka;2024-01-20\n"
        "Syr;75;350.00;Molochnye;2024-01-17"
    ),
    "file4.txt": (
        'Date|Product|Quantity|Price|Discount|"Customer Name"\n'
        '2024-01-15|Laptop|5|999.99|0.10|"Ivanov I.I."\n'
        '2024-01-16|Mouse|20|25.50|0.05|"Petrova M.S."\n'
        '2024-01-17|Keyboard|15|45.00|null|"Sidorov A.V."\n'
        '2024-01-18|Monitor|3|299.99|0.15|"Kuznecova E.P."\n'
        '2024-01-19|Tablet|8|399.50|0.00|"Smirnov D.K."'
    )
}

#чтение каждого файла
file_settings = {
    "file1.txt": {"delimiter": ",", "has_header": True},
    "file2.txt": {"delimiter": " ", "has_header": True},
    "file3.txt": {"delimiter": ";", "has_header": False}, 
    "file4.txt": {"delimiter": "|", "has_header": True}
}

#тестирование и удаление файлов
for filename, content in files_content.items():
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)
    
    settings = file_settings[filename]
    result = read_table_file(filename, delimiter=settings["delimiter"], has_header=settings["has_header"])
    
    print(f"\n==================== ПРОВЕРКА: {filename} ====================")
    print(f"Параметры: разделитель='{settings['delimiter']}', заголовок={settings['has_header']}")
    print(f"Определенные типы ('types'): {result['types']}")
    print(f"Заголовки ('header'): {result['header']}")
    print("Данные ('data'):")
    for row in result['data']:
        row_with_types = [f"{val} ({type(val).__name__})" for val in row]
        print(f"  {row_with_types}")
        
    if os.path.exists(filename):
        os.remove(filename)
