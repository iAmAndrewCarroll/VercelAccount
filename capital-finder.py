# from http.server import BaseHTTPRequestHandler
import requests

# class handler(BaseHTTPRequestHandler):
    
#     def do_GET(self):
#         self.send_response(200)
#         self.send_header('Content-type', 'text/plain')
#         self.end_headers()

#         country_name = input("Enter a country name: ")

#         url = f'https://restcountries.com/v3.1/name/{country_name}'
#         response = requests.get(url)

#         if response.status_code == 200:
#             data = response.json()
#             capital = data[0]['capital']
#             response_text = f"The capital of {country_name} is {capital}."
#         else:
#             response_text = 'Request failed. Status Code: ', + str(response.status_code)

#         self.wfile.write(response_text.encode())
#         return

def get_capital(country):
    url = f'https://restcountries.com/v3.1/name/{country}'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        capital = data[0]['capital']
        return "The capital of " + country + " is " + capital + "."
    else: 
        print('Request failed. Status Code: ', response.status_code)

def handler(request):
    if request.method == 'GET':
        country_name = request.query.get('country')
        if country_name:
            return get_capital(country_name)
        else:
            return 'Invalid request. Please provide a country name.'
        
def main():
    while True:
      country_name = input("Enter a country name or 'exit' to quit: ")
      if country_name.lower() == 'exit':
          break
      result = get_capital(country_name)
      if result is not None:
        print(result)

if __name__ == '__main__':
    main()
