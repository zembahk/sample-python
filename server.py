import os
import http.server
import socketserver
import requests
from http import HTTPStatus



class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path.lower() == '/img':
            self.path = '/index.html'
            return http.server.SimpleHTTPRequestHandler.do_GET(self)
        else:
            msg = 'Hello! you requested %s' % (self.path)
        self.wfile.write(msg.encode())


port = int(os.getenv('PORT', 80))
print('Listening on port %s' % (port))
httpd = socketserver.TCPServer(('', port), Handler)
httpd.serve_forever()
