import http.server
import os

class CleanURLHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Support clean URLs: /teetimes -> /teetimes.html
        path = self.path.split('?')[0].split('#')[0]
        if path != '/' and '.' not in os.path.basename(path):
            html_path = path.rstrip('/') + '.html'
            full_path = os.path.join(os.getcwd(), html_path.lstrip('/'))
            if os.path.isfile(full_path):
                self.path = html_path
        super().do_GET()

if __name__ == '__main__':
    server = http.server.HTTPServer(('', 3000), CleanURLHandler)
    print('Serving on http://localhost:3000')
    server.serve_forever()
