from http.server import BaseHTTPRequestHandler


class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        content = "<h1>HELLOOOOO</h1>"

        self.wfile.write(content.encode('utf-8'))

        return
