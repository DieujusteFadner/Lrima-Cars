from flask import Flask,render_template,Response
import cv2
from picamera2 import Picamera2
import time
import socket
import ssl


class Stream:
	def __init__(self):
		self.camera = Picamera2()
		self.camera.configure(self.camera.create_preview_configuration(main={"format":"XRGB8888","size":(640,480)}))
		self.camera.start()
		self.app = Flask(__name__)
		self.streamOpen = True
		
		


	def generate_frames(self):
		while True:
			frame=self.camera.capture_array()
			ret,buffer=cv2.imencode('.jpg',frame)
			frame= buffer.tobytes()
			yield(b'--frame\r\n'
				b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

		
	def creerStream(self):
		@self.app.route('/video')
		def video():
			return Response(self.generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')
		context = ssl.SSLContext(ssl.PROTOCOL_TLS)
		context.load_cert_chain('cert.pem', 'key.pem')
		self.app.run(host='0.0.0.0', debug=False, port=8080,ssl_context=context)
	

		
	

	def get_ip_address():

		try:
			# Create a socket object
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			
			# Connect to a remote server (doesn't have to be reachable)
			s.connect(('8.8.8.8', 80))
			
			# Get the local IP address
			local_ip = s.getsockname()[0]
			
			s.close()
			
			return local_ip
		except socket.error:
			return None
	
	def allumerStream(self):
		# création de l'obejet stream
		try:
			# appelle de la fonction pour creer un stream
			self.creerStream()
			print("Stream en marche")
		except:
			print("erreur est survenue")
			
		finally:
			print("Merci d'utiliser notre service")
		

	def eteindreStream(self):
		# changement du state du stream a false
		sstreamOpen = False
		return
		
