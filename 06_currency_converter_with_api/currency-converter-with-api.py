import requests


def convert():
    try:
        from_ = input("from: ")
        to = input("to: ")
        amount = input("enter amount: ")
        url = f"https://api.frankfurter.app/latest?amount={amount}&from={from_}&to={to}"
        response = requests.get(url)
        data = response.json()
        print(f"{amount} {data['base']} in {to} = {data['rates']['INR']}")
        # print(data['rates']['INR'])
        # print(data['rates'])
    except:
        print("error, please try again.")
        convert()

convert()
