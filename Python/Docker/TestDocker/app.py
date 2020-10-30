# imports

import http.server
import socketserver

print(" Starting simple http server ")
handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("",8000), handler) as httpd:
    print(" Serving at 8000 ")
    httpd.serve_forever()