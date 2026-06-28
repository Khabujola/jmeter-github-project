from http.server import BaseHTTPRequestHandler, HTTPServer

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Send response status code
        self.send_response(200)

        # Send headers
        self.send_header("Content-type", "text/plain")
        self.end_headers()

        # Send message
        self.wfile.write(b"Hello from Python server!")

def run():
    server_address = ('', 3000)
    httpd = HTTPServer(server_address, SimpleHandler)
    print("Server running on port 3000...")
    httpd.serve_forever()

if __name__ == "__main__":
    run()
``
