import requests
import pendulum


def load_attempts():
    start_parse = 1
    end_parse = 11
    url = 'https://devman.org/api/challenges/solution_attempts'
    for page in range(start_parse, end_parse):
        payload = {'page': page}
        records = requests.get(url, params=payload).json()['records']
        for record in records:
            timestamp = record['timestamp']
            if timestamp is not None:
                yield {
                    'username': record['username'],
                    'timestamp': timestamp,
                }


def get_midnighters(attempts):
    moscow_timezone = 'Europe/Moscow'
    today_midnight = pendulum.today(moscow_timezone)
    for attempt in attempts:
        timestamp = attempt['timestamp']
        current_date = pendulum.from_timestamp(timestamp, moscow_timezone)
        if current_date > today_midnight:
            time = pendulum.fromtimestamp(timestamp, moscow_timezone)
            time_human_view = time.to_datetime_string()
            yield {
                'username': attempt['username'],
                'time': time_human_view,
            }


if __name__ == '__main__':
    counter = 0
    for idx, midnighter in enumerate(get_midnighters(load_attempts()), 1):
        attempt_print = '{}) {} submitted task for review at {}\n'
        print(attempt_print.format(idx, midnighter['username'],
                                   midnighter['time']))
