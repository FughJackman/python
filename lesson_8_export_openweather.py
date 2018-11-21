
""" OpenWeatherMap (экспорт)
Сделать скрипт, экспортирующий данные из базы данных погоды, 
созданной скриптом openweather.py. Экспорт происходит в формате CSV или JSON.
Скрипт запускается из командной строки и получает на входе:
    export_openweather.py --csv filename [<город>]
    export_openweather.py --json filename [<город>]
    export_openweather.py --html filename [<город>]
    
При выгрузке в html можно по коду погоды (weather.id) подтянуть 
соответствующие картинки отсюда:  http://openweathermap.org/weather-conditions
Экспорт происходит в файл filename.
Опционально можно задать в командной строке город. В этом случае 
экспортируются только данные по указанному городу. Если города нет в базе -
выводится соответствующее сообщение.
"""
# Реализована запись в csv и json для одного города(без проверки) и всех имеющихся.

import csv
import json
import sys
import os
import sqlite3

DIR = os.path.dirname(__file__)


try:
    file_type = sys.argv[1][2:]
    file_name = sys.argv[2]
    city = sys.argv[3]
except:
    city = None
    

def make_json(file_name, city, cur):
    with open(os.path.join(DIR, '{}.json'.format(file_name)), 'w', encoding='utf8') as f:
        data = []
        for row in cur.fetchall():
            city_id, city_name, date, temp, weather_id = row
            if city_name == city or city == None:
                data.append({'city_id':city_id, 'city_name':city_name, 'date':date, 'temp':temp, "weather_id":weather_id})
                
        json.dump(data, f, ensure_ascii=False, sort_keys=True, indent=4)
        f.close()

def make_csv(file_name, city, cur):
    with open(os.path.join(DIR, '{}.csv'.format(file_name)), 'w', encoding='utf8') as csvfile:
        writer = csv.writer(csvfile, delimiter=' ',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(('city_id', 'city_name', 'date', 'temp', 'weather_id'))
        for row in cur.fetchall():
            city_id, city_name, date, temp, weather_id = row
            if city_name == city or city == None:
                writer.writerow([city_id, city_name, date, temp, weather_id])
        csvfile.close()

db_filename = os.path.join(DIR, 'weather.db')
with sqlite3.connect(db_filename) as conn:   
    conn.row_factory = sqlite3.Row

    cur = conn.cursor()
    cur.execute("select * from t_weather")

    if file_type == "json":
        make_json(file_name, city, cur)
    elif file_type == "csv":
        make_csv(file_name, city, cur)
    else:
        print("Формат указан неверно")