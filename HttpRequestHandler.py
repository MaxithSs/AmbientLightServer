import http.server

import WallpaperManager


class HttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    # todo - send every response in json format
    def do_GET(self) -> None:
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes(WallpaperManager.get_current_wallpapers_color(), "utf8"))
        return
