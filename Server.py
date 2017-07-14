# This file handles routing and serving requests made to the application.

import BaseHTTPServer
import json
import State

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

def send_failure_headers(s):
	s.send_response(404)
	s.send_header("Content-type","text/html")
	s.end_headers()

class RequestHandler(BaseHTTPServer.BaseHTTPRequestHandler):
	def do_HEAD(s):
		send_html_headers(s)

	def do_GET(s):
		if GETRequests.is_valid_route(s.path):
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
			success = POSTRequests.process_route_with_data(s.path, post_data)			

			send_json_headers(s)
			s.wfile.write('{ "success": "%s" }' % str(success))
		else:
			send_failure_headers(s)
			s.wfile.write(POSTRequests.invalid_request(s.path))

def read_network_info():
	host = "localhost" # default
	port = 9001 # default
	with open('NetworkInfo.txt') as netInfo:
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

def start_server():
	netinfo = read_network_info()
	server_class = BaseHTTPServer.HTTPServer
	httpd = server_class(netinfo, RequestHandler)
	log_debug("Server started on %s:%s" % netinfo)
	try:
		httpd.serve_forever()
	except KeyboardInterrupt:
		pass
	httpd.server_close()
	log_debug("Server stopped on %s:%s" % netinfo)
