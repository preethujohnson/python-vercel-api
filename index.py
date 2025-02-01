import json
import urllib.parse
from http.server import BaseHTTPRequestHandler

# Sample data of student marks
STUDENT_MARKS = {
    "Alice": 10,
    "Bob": 20,
    "Charlie": 30,
    "David": 40
}

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')  # Enable CORS
        self.end_headers()

        # Parse query parameters
        query_string = self.path.split('?')[-1]
        params = urllib.parse.parse_qs(query_string)
        names = params.get("name", [])

        # Retrieve marks for the given names
        marks = [STUDENT_MARKS.get(name, 0) for name in names]

        # Send JSON response
        self.wfile.write(json.dumps({"marks": marks}).encode('utf-8'))
        return
        
