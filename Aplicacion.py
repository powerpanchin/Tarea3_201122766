from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer

PORT_NUMBER = 5555
class myHandler(BaseHTTPRequestHandler):
	def do_GET(self):
		self.send_response(200)
		self.send_header('Content-type','text/html')
		self.end_headers()
		self.wfile.write('<center><h1>Tarea 3 Sistemas Operativos 2, Creacion de Daemon</h1><br><br></center>');
		self.wfile.write('<center><h2>Francisco Alejandro Coloj Marroquin, 201122766</h2></center>');
		return

try:
	server = HTTPServer(('', PORT_NUMBER), myHandler)
	server.serve_forever()

except KeyboardInterrupt:
	server.socket.close()
	
