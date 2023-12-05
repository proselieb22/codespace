import sys
import requests

def get_bitcoin_price(bitcoin_amount):
    try:
        bitcoin_amount = float(bitcoin_amount)
    except ValueError:
        sys.exit("Command-line argument is not a number")

    try:
        response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
        response.raise_for_status()
        bitcoin_data = response.json()
        usd_rate = bitcoin_data['bpi']['USD']['rate_float']
        cost_in_usd = bitcoin_amount * usd_rate
        print(f"${cost_in_usd:,.4f}")
    except requests.RequestException:
        sys.exit("Error: Unable to fetch Bitcoin price data")

def main():
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")

    bitcoin_amount = sys.argv[1]
    get_bitcoin_price(bitcoin_amount)

if __name__ == "__main__":
    main()
