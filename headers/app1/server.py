from http.server import BaseHTTPRequestHandler, HTTPServer


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Headers received:")
        header_string = ""
        for name, value in self.headers.items():
            header_string += f"{name}: {value}\n"

        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"APP1 header string:\n" + header_string.encode())


HTTPServer(("0.0.0.0", 8000), Handler).serve_forever()
