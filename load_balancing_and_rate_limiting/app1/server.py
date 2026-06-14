from http.server import BaseHTTPRequestHandler, HTTPServer
import time


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        time.sleep(1)

        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(b"Response from APP1")


HTTPServer(("0.0.0.0", 8000), Handler).serve_forever()
