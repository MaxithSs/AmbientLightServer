import http.server

import WallpaperManager


class HttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    # todo - send every response in json format
    def do_GET(self) -> None:
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        html = f"<html><head></head><body>{ WallpaperManager.get_current_wallpapers_color() }</body></html>"
        self.wfile.write(bytes(html, "utf8"))
        return
