import requests
import pendulum

def load_attempts():
    start_parse = 1
    end_parse = 11
    url = "https://devman.org/api/challenges/solution_attempts"
    for page in range(start_parse, end_parse):
        payload = {"page" : page}
        records = requests.get(url, params = payload).json()["records"]
        for record in records:
            timestamp = record["timestamp"]
            if timestamp is not None:
                yield {
                    'username': record["username"],
                    'timestamp': timestamp,
                }

def get_midnighters(attempts):
    moscow_timezone = 'Europe/Moscow'
    today_midnight = pendulum.today(moscow_timezone)
    for attempt in attempts:
        timestamp = attempt['timestamp']
        if pendulum.from_timestamp(timestamp, moscow_timezone) > today_midnight:
            yield {
                'username': attempt['username'],
                'time': pendulum.fromtimestamp(timestamp, moscow_timezone).to_datetime_string(),
            }

if __name__ == '__main__':
    counter = 0
    for idx, midnighter in enumerate(get_midnighters(load_attempts()), 1):
        print("{}) {} submitted last task for review at {}\n".format(idx, 
            midnighter['username'], midnighter['time']))
