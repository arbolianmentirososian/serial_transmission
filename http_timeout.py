import http.server
import socketserver
import json
import time

PORT = 8000
json_file = '{"parse_time_nanoseconds": 23413}'
json_test = json_test = {
    "results": [
        {
            "series": [
                {
                    "name": "DVBS2",
                    "columns": [
                        "time",
                        "board",
                        "host",
                        "port",
                        "type",
                        "value"
                    ],
                    "values": [
                        [
                            "2018-11-22T17:34:02.408636495Z",
                            "4",
                            "DCM_192_168_29_57",
                            "3",
                            "CN_Margin",
                            9.7
                        ]
                    ]
                }
            ]
        }
    ]
}

print(type(json_file))

class OwnHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        print("request detected")
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        #time.sleep(1)
        self.wfile.write(json.dumps(json_test).encode())
        return




Handler = OwnHandler


with socketserver.TCPServer(("", PORT), Handler) as httpd:
    try:
        print("serving at port", PORT)
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("^C pressed - stopping server")
