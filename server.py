import SimpleHTTPServer
import SocketServer
import os

PORT = int(os.getenv('PORT', 5555))

Handler = SimpleHTTPServer.SimpleHTTPRequestHandler

httpd = SocketServer.TCPServer(("", PORT), Handler)

print "serving at port", PORT
httpd.serve_forever()
