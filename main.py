import datetime

import requests

import time

API_URL = 'https://sholiday.faboul.se/dagar/v2.1/'


def request_new_data():
    return requests.get(API_URL).json()


def get_data(api_data) -> []:
    use_full_data = []
    name_day = api_data['dagar'][0]['namnsdag']
    date = api_data['dagar'][0]['datum']
    day_of_week = api_data['dagar'][0]['veckodag']
    week = api_data['dagar'][0]['vecka']

    use_full_data.append(name_day)
    use_full_data.append(date)
    use_full_data.append(day_of_week)
    use_full_data.append(week)

    return use_full_data


def formatted_data(content_list):
    end = ', '
    text = ''

    for name in content_list[0]:
        text += name + end
    text += content_list[1] + end
    text += content_list[2] + end
    text += 'Vecka ' + content_list[3] + '\n'

    return text


def run_program():
    api_get = request_new_data()
    use_full_data_list = get_data(api_get)
    data_string = formatted_data(use_full_data_list)
    with open('name_day', 'a') as name_file:
        name_file.write(data_string)


check_time_hour = 0
for_one_hour = 3600

while True:
    hour = datetime.datetime.now().hour

    if hour == check_time_hour:
        run_program()

    time.sleep(for_one_hour)