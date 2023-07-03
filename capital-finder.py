import requests

def get_capital(country):
    url = f'https://restcountries.com/v3.1/name/{country}'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        capital = data[0]['capital']
        print(f"The capital of {country} is {capital}.")
    else: 
        print('Request failed. Status Code: ', response.status_code)

def handler(request):
    if request.method == 'GET':
        country_name = request.query.get('country')
        if country_name:
            return get_capital(country)
        else:
            return 'Invalid request. Please provide a country name.'
        
def main():
    country_name = input("Enter a country name: ")
    result = get_capital(country_name)
    print(result)

if __name__ == '__main__':
    main()
