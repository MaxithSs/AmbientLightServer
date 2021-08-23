import socketserver

from HttpRequestHandler import HttpRequestHandler
PORT = 8000


def start_server():
    handler_object = HttpRequestHandler
    server = socketserver.TCPServer(("", PORT), handler_object)
    server.serve_forever()