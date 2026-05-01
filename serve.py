import http.server, os
port = int(os.environ.get("PORT", 8080))
handler = http.server.SimpleHTTPRequestHandler
httpd = http.server.HTTPServer(("0.0.0.0", port), handler)
print(f"Serving on port {port}", flush=True)
httpd.serve_forever()
