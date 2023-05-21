config = {
    "base_url": "https://example.com/api",
    "timeout": 3,
}

def update_config(**kwargs):
    for key, value in kwargs.items():
        if key in {"api_key", "base_url", "timeout"}:
            config[key] = value
        else:
            raise KeyError(key)

update_config(api_key="111222333")
config

update_config(timeout=5)
config


conf = {
    "database": {
      "host": "localhost",
      "port": 5432,
      "name": "database.db",
      "user": "username",
      "password": "secret"
    },
    "api_key": "111222333",
    "base_url": "https://example.com/api",
    "timeout": 60
}


def set_config_key(key, value):
    globals()[key] = value

for key, value in conf.items():
    set_config_key(key, value)

api_key
database
timeout


import webbrowser

import requests

API_KEY = "DEMO_KEY"
BASE_URL = "https://api.nasa.gov/planetary"
TIMEOUT = 3

def load_earth_image(date):
    endpoint = f"{BASE_URL}/apod"
    try:
        response = requests.get(
            endpoint,
            params={
                "api_key": API_KEY,
                "date": date,
            },
            timeout=TIMEOUT,
        )
    except requests.exceptions.RequestException as e:
        print(f"Error connecting to API: {e}")
        return

    try:
        url = response.json()["url"]
    except KeyError:
        print(f"No image available on {date}")
        return

    webbrowser.open(url)
    

load_earth_image("2023-02-12")


class Account:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Successful deposit: +${amount:,.2f}")

    def withdraw(self, amount):
        if self.balance - amount > 0:
            self.balance -= amount
            print(f"Successful withdrawal: -${amount:,.2f}")
        else:
            print("Not enough funds for this transaction")

def main():
    account = Account()
    while True:
        operation = input(
            "What would you like to do?\n"
            " d) deposit  "
            " w) withdraw  "
            " b) balance  "
            " q) quit\n"
            "> "
        )
        if operation in "dD":
            amount = float(input("Enter the deposit amount: "))
            account.deposit(amount)
        elif operation in "wW":
            amount = float(input("Enter the withdrawal amount: "))
            account.withdraw(amount)
        elif operation in "bB":
            print(f"Current balance: ${account.balance:,.2f}")
        elif operation in "qQ":
            print("Goodbye!")
            break
        else:
            print("Invalid operation. Please try again.")

main()

