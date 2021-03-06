# This file handles routing and serving requests made to the application.

import BaseHTTPServer
import SimpleHTTPServer
import json
import State
import os

from Utilities import log_debug
import GETRequests
import POSTRequests

def send_html_headers(s):
	s.send_response(200)
	s.send_header("Content-type","text/html")
	s.end_headers()

def send_json_headers(s):
	s.send_response(200)
	s.send_header("Content-type","application/json")
	s.end_headers()

def send_headers_for_file_in_path(s):
	s.send_response(200)
	s.send_header('Content-type', s.guess_type(s.path))
	s.end_headers()

def send_failure_headers(s):
	s.send_response(404)
	s.send_header("Content-type","text/html")
	s.end_headers()

class RequestHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
	blinky_interface = None

	def do_HEAD(s):
		send_html_headers(s)

	def do_GET(s):
		if s.path.startswith('/site'):
			try:
				f = open(os.curdir + os.sep + s.path)
				send_headers_for_file_in_path(s)
				s.wfile.write(f.read())
				f.close()
			except IOError:
				s.send_error(404, 'File Not Found: %s' % s.path)
		elif GETRequests.is_valid_route(s.path):
			if GETRequests.is_json_route(s.path):
				send_json_headers(s)
			else:
				send_html_headers(s)
			s.wfile.write(GETRequests.page_for_route(s.path))
		else:
			send_failure_headers(s)
			s.wfile.write(GETRequests.page_not_found(s.path))


	def do_POST(s):
		if POSTRequests.is_valid_route(s.path):
			raw_data = s.rfile.read(int(s.headers['Content-Length']))
			post_data = json.loads(raw_data)
			success = POSTRequests.process_route_with_data(s.path, post_data, s.blinky_interface)			

			send_json_headers(s)
			s.wfile.write('{ "success": "%s" }' % str(success))
		else:
			send_failure_headers(s)
			s.wfile.write(POSTRequests.invalid_request(s.path))


class Server(BaseHTTPServer.HTTPServer):
	def serve_forever(self, blinky_interface):
		self.RequestHandlerClass.blinky_interface = blinky_interface
		BaseHTTPServer.HTTPServer.serve_forever(self)


class BlinkyServer(object):
	def read_network_info(self):
		host = "localhost" # default
		port = 9001 # default
		with open(os.path.join(os.path.dirname(__file__), 'NetworkInfo.txt')) as netInfo:
			lines = netInfo.readlines()
			for line in lines:
				comps = line.rstrip().split('=')
				if len(comps) != 2:
					print("Error in NetworkInfo.txt: %s" % line)
				else:
					if comps[0] == "HOST_NAME":
						host = comps[1]
					elif comps[0] == "PORT_NUMBER":
						port = int(comps[1])
		return (host, port)

	def start_server(self, blinky_interface):
		netinfo = self.read_network_info()
		server_class = Server
		httpd = server_class(netinfo, RequestHandler)
		log_debug("Server started on %s:%s" % netinfo)
		try:
			httpd.serve_forever(blinky_interface)
		except KeyboardInterrupt:
			pass
		httpd.server_close()
		log_debug("Server stopped on %s:%s" % netinfo)
