import csv
import requests
from fake_useragent import UserAgent
from http import HTTPStatus

def get_websites(csv_path: str) -> list[str]:
    websites: list[str] = []
    with open(csv_path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if len(row) > 1:  # Check if the row has at least 2 elements
                if 'http://' not in row[1]:
                    websites.append(f'https://{row[1]}')
                else:
                    websites.append(row[1])
    return websites

print(get_websites("websitess.csv"))
