import requests
from datetime import date, datetime


def currency_converter(FROM, TO):
    url = "https://api.frankfurter.dev/v2/rates"
    today = date.today().strftime("%Y-%m-%d")

    try:
        params = {
            "date": today,
            "base": FROM,
            "quotes": TO
        }

        response = requests.get(
            url,
            timeout=10,
            params=params
        )

        response.raise_for_status()
        data = response.json()

        return data[0]["rate"]

    except requests.RequestException as e:
        return {"error": f"API request failed: {e}"}


url = "https://api.frankfurter.dev/v2/currencies"

response = requests.get(
    url,
    timeout=10
)

response.raise_for_status()
data = response.json()


def currencies():
    currencies_list = []

    for i in data:
        if datetime.strptime(i["end_date"], "%Y-%m-%d").date() == date.today():
            currencies_list.append(i["iso_code"])

    return currencies_list