import requests
import argparse

parser = argparse.ArgumentParser(description='Find sites with a specific directory')
parser.add_argument('filename', type=str, help='filename with sites list')
parser.add_argument('directory', type=str, help='directory to check')

args = parser.parse_args()
filename = args.filename
dir_to_check = args.directory

with open(filename, "r") as file:
    for line in file:
        site = line.strip()  # удаляем символы новой строки и лишние пробелы
        
        # Добавляем директорию к URL сайта и делаем GET-запрос
        url_to_check = site + dir_to_check
        try:
            response = requests.get(url_to_check)
        except requests.exceptions.RequestException:
            # Если возникает ошибка, пропускаем сайт и переходим к следующему
            continue
        
        # Если ответ сервера имеет код 200, то директория существует
        if response.status_code == 200:
            print(f"Директория '{dir_to_check}' есть на сайте '{site}'")
            
            # Сохраняем информацию о сайте в файл
            with open('sitesthatyouspars.txt', 'a') as output_file:
                output_file.write(f"{url_to_check}: {response.status_code}\n")
                output_file.write(f"{site}\n")
