#!/usr/bin/python3
"""HTTP Server Module
"""
import http.server
import socketserver
import json


class RequestHandler(http.server.BaseHTTPRequestHandler):
    """RequestHandlerSubClass

    Args:
        http (HTTPClass): handler
    """
    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            msj = "Hello, this is a simple API!"
            self.wfile.write(msj.encode())

        elif self.path == "/data":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            dataset = {"name": "John", "age": 30, "city": "New York"}
            self.wfile.write(json.dumps(dataset).encode())

        elif self.path == "/status":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            msj = "OK"
            self.wfile.write(msj.encode())

        else:
            self.send_error(404, "Endpoint not found")


PORT = 8000

Handler = RequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()
