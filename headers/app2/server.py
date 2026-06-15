from http.server import BaseHTTPRequestHandler, HTTPServer


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Headers received:")
        for name, value in self.headers.items():
            print(f"{name}: {value}")

        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"APP2 - OK")


HTTPServer(("0.0.0.0", 8000), Handler).serve_forever()
