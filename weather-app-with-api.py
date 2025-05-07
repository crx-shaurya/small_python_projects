import requests

def current():
    location = input("enter your location, ")
    api = "38b0b76da94a431b866113458251904"
    url = f"http://api.weatherapi.com/v1/current.json?key={api}&q={location}&aqi=no"

    response = requests.get(url)
    data = response.json()


    print("location =",data['location']['name'])
    print("time =",data['location']['localtime'])
    print("temperature('c) =",data['current']['temp_c'])
    print("time zone =",data['location']['tz_id'])
    print("humidity =",data['current']['humidity'])
    print("uv index =",data['current']['uv'])
    print("heatindex =",data['current']['heatindex_f'])

def forecast():
    location = input("enter your location, ")
    api = "38b0b76da94a431b866113458251904"
    url = f"http://api.weatherapi.com/v1/forecast.json?key={api}&q={location}&aqi=no"

    response = requests.get(url)
    data = response.json()

    print(data)
    print("location =",data['location']['name'])
    print("time =",data['location']['localtime'])
    print("temperature('c) =",data['current']['temp_c'])
    print("time zone =",data['location']['tz_id'])
    print("humidity =",data['current']['humidity'])
    print("uv index =",data['current']['uv'])
    print("heatindex =",data['current']['heatindex_f'])

def run():
    a= input("enter your choice: ")
    if a=="1":
        current()
    elif a == "2":
        forecast()
    else:
        print("invalid input. \nPlease try again")
        run()

print("welcome")
print("choose 1 for current weather & 2 for forecast")

run()