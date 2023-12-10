from http.server import BaseHTTPRequestHandler

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        # Add headers for htmx compatibility
        self.send_header('HX-Request', 'true')
        self.send_header('HX-Trigger', 'true')
        self.send_header('HX-Swap', 'true')
        self.end_headers()

        content = "<h1>HELLOOOOO</h1>"

        self.wfile.write(content.encode('utf-8'))

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()

if __name__ == '__main__':
    from http.server import HTTPServer
    server = HTTPServer(('0.0.0.0', 8000), handler)
    print('Starting server on port 8000...')
    server.serve_forever()

