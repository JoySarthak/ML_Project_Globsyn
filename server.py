#!/usr/bin/env python3
import http.server
import socketserver
import os

PORT = 5000

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        super().end_headers()

if __name__ == "__main__":
    # Change to the directory containing the HTML files
    web_dir = os.path.dirname(os.path.realpath(__file__))
    os.chdir(web_dir)
    
    with socketserver.TCPServer(("0.0.0.0", PORT), MyHTTPRequestHandler) as httpd:
        print(f"🌐 Mobile Sales Analytics Dashboard running at:")
        print(f"   http://localhost:{PORT}")
        print(f"   http://0.0.0.0:{PORT}")
        print("\n📊 Features:")
        print("   ✅ Interactive Plotly charts")
        print("   ✅ Colorful visualizations from your notebook") 
        print("   ✅ All insights and analytics preserved")
        print("   ✅ Beautiful gradient backgrounds")
        print("   ✅ Mobile-responsive design")
        print("\nPress Ctrl+C to stop the server")
        httpd.serve_forever()