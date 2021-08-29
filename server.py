import os
import http.server
import socketserver

from http import HTTPStatus
import requests




class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(HTTPStatus.OK)
        self.end_headers()
        if self.path.lower() == '/img':
            # msg = '<img src="/img/QRhoge.png"></img>'
            url = 'http://google.com/favicon.ico'
            r = requests.get(url, allow_redirects=True)
            open('google.ico', 'wb').write(r.content)
        else:
            msg = 'Hello! you requested %s' % (self.path)
        self.wfile.write(msg.encode())


port = int(os.getenv('PORT', 80))
print('Listening on port %s' % (port))
httpd = socketserver.TCPServer(('', port), Handler)
httpd.serve_forever()
