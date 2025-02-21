import http.server
import json
"""Set up a web server using the http.server module."""


class SimpleAPI(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")

        elif self.path == "/data":
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            in_data = {
                "name": "John", "age": 30, "city": "New York"
            }
            self.wfile.write(json.dumps(in_data).encode('utf-8'))

        elif self.path == "/status":
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps("OK").encode('utf-8'))

        elif self.path == "/info":
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            in_info = {
                "version": "1.0",
                "description": "A simple API built with http.server"
            }
            self.wfile.write(json.dumps(in_info).encode('utf-8'))
        else:
            self.send_response(404)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(b"Endpoint not found")


def run_server(port=8000):

    server_address = ('', port)
    httpd = http.server.HTTPServer(server_address, SimpleAPI)
    print(f"Server running on port {port}")
    httpd.serve_forever()


if __name__ == "__main__":
    run_server()
