import requests
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib import parse

class handler(BaseHTTPRequestHandler):
    
    def do_GET(self):
        BASE_URL = 'https://restcountries.com/v3.1/'
        s = self.path
        url_components = parse.urlsplit(s)
        query_string_list = parse.parse_qsl(url_components.query)
        dic = dict(query_string_list)
        country = dic.get('country')
        capital = dic.get('capital')
        if country and capital:
            message = f'Country: {country} Capital: {capital}'
        elif country:
            url = f'{BASE_URL}name/{country}'
            r = requests.get(url)
            data = r.json()
            capitals = data[0]['capital']
            join_capitals = ' and '.join(capitals)
            message = f'The capital of {country} is {join_capitals}.'
        elif capital:
            url = f'{BASE_URL}capital/{capital}'
            r = requests.get(url)
            data = r.json()
            message = str(data)
        else:
            message = 'Invalid request. Please provide a country name or capital.'
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(message.encode())
        return
    
if __name__ == "__main__":
    server_address = ("", 5500)
    httpd = HTTPServer(server_address, handler)
    print(f"Started on http://localhost:{server_address[1]}/capital-finder")
    httpd.serve_forever()

    
# def get_capital(country):
#     url = f'https://restcountries.com/v3.1/name/{country}'
#     response = requests.get(url)

#     if response.status_code == 200:
#         data = response.json()
#         capital = data[0]['capital'][0]
#         return f"The capital of {country} is {capital}."
#     else:
#         return f'Request failed. Status: {response.status_code}'
    
# class handler(BaseHTTPRequestHandler):
    
#     def do_GET(self):
#         if self.path.startswith('/capital-finder'):
#             query_params = self.path.split('?')[1]
#             params = dict(param.split('=') for param in query_params.split('&'))
#             country_name = params.get('country', '')
#             if country_name:
#                 capital_info = get_capital(country_name)
#                 self.send_response(200)
#                 self.send_header('Content-type', 'text/plain')
#                 self.end_headers()
#                 self.wfile.write(capital_info.encode('utf-8'))
#             else: 
#                 self.send_response(400)
#                 self.send_header('Content-type', 'text/plain')
#                 self.end_headers()
#                 self.wfile.write(b'Invalid request. Please provide a country name.')
#         else:
#             self.send_response(404)
#             self.send_header('Content-type', 'text/plain')
#             self.end_headers()
#             self.wfile.write(b'Not found.')
#         return

# def main():
#     server_address = ('', 5500)
#     httpd = HTTPServer(server_address, handler)  
#     print(f'Started on http://localhost:{server_address[1]}/capital-finder')

#     while True: 
#         country_name = input("Enter a country name or 'exit' to quit: ")
#         if country_name.lower() == 'exit':
#             break
#         capital_info = get_capital(country_name)
#         print(capital_info)

#     httpd.serve_forever()   


# if __name__ == '__main__':
#     main()

# import requests
# from http.server import BaseHTTPRequestHandler, HTTPServer

# def get_capital(country):
#     url = f'https://restcountries.com/v3.1/name/{country}'
#     response = requests.get(url)

#     if response.status_code == 200:
#         data = response.json()
#         capital = data[0]['capital'][0]
#         return f"The capital of {country} is {capital}."
#     else:
#         return f'Request failed. Status: {response.status_code}'
    
# class handler(BaseHTTPRequestHandler):
    
#     def do_GET(self):
#         if self.path.startswitch('/capital-finder'):
#             query_params = self.path.split('?')[1]
#             params = dict(param.split('=') for param in query_params.split('&'))
#             country_name = params.get('country', '')
#             if country_name:
#                 capital_info = get_capital(country_name)
#                 self.send_response(200)
#                 # self.send_header('Content-type', 'application/json')
#                 self.send_header('Content-type', 'text/plain')
#                 self.end_headers()
#                 self.wfile.write(capital_info.encode())
#             else: 
#                 self.send_response(400)
#                 self.send_header('Content-type', 'text/plain')
#                 self.end_headers()
#                 self.wfile.write(b'Invalid request. Please provide a country name.')
#         else:
#             self.send_response(404)
#             self.send_header('Content-type', 'text/plain')
#             self.end_headers()
#             self.wfile.write(b'Not found.')
#         return

# def main():
#     server_address = ('', 8000)
#     httpd = HTTPServer(server_address, handler)  
#     print(f'Started on ${httpd.server_address}')

#     while True: 
#         country_name = input("Enter a country name or 'exit' to quit: ")
#         if country_name.lower() == 'exit':
#             break
#         capital_info = get_capital(country_name)
#         print(capital_info)

#     httpd.serve_forever()   


# if __name__ == '__main__':
#   main()

# Path: api/capital-finder.py
# http://localhost:8000/capital-finder?country=germany

# def main():
#     server_address = ('', 8000)
#     httpd = HTTPServer(server_address, handler)  
#     print(f'Started on ${httpd.server_address}')

#     while True: 
#         country_name = input("Enter a country name or 'exit' to quit: ")
#         if country_name.lower() == 'exit':
#             break
#         capital_info = get_capital(country_name)
#         print(capital_info)

#     httpd.serve_forever()   


# if __name__ == '__main__':
#   main()

# Path: api/capital-finder.py
# http://localhost:8000/capital-finder?country=germany