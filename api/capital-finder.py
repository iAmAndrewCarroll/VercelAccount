import requests
from http.server import BaseHTTPRequestHandler, HTTPServer

def get_capital(country):
    url = f'https://restcountries.com/v3.1/name/{country}'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        capital = data[0]['capital'][0]
        return f"The capital of {country} is {capital}."
    else:
        return f'Request failed. Status: {response.status_code}'
    
class handler(BaseHTTPRequestHandler):
    
    def do_GET(self):
        if self.path.startswitch('/capital-finder'):
            query_params = self.path.split('?')[1]
            params = dict(param.split('=') for param in query_params.split('&'))
            country_name = params.get('country', '')
            if country_name:
                capital_info = get_capital(country_name)
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(capital_info.encode())
            else: 
                self.send_response(400)
                self.send_header('Content-type', 'text/plain')
                self.end_headers()
                self.wfile.write(b'Invalid request. Please provide a country name.')
        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'Not found.')

def main():
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, handler)  
    print('Started on http://localhost:8000/capital-finder')

    while True: 
        country_name = input("Enter a country name or 'exit' to quit: ")
        if country_name.lower() == 'exit':
            break
        capital_info = get_capital(country_name)
        print(capital_info)

    httpd.serve_forever()   


if __name__ == '__main__':
  main()

# Path: api/capital-finder.py
# http://localhost:8000/capital-finder?country=germany