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

        content = "<h1>HELLOOOOO TEST2</h1>"

        self.wfile.write(content.encode('utf-8'))

        return
