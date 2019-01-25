from flask import Flask, render_template, request, redirect, url_for, make_response
import socket

# Get server ip
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
server_ip = s.getsockname()[0]
s.close()

app = Flask(__name__) 

@app.route('/')
def index():

	return render_template('index.html', server_ip=server_ip)

app.run(debug=True, host='0.0.0.0', port=8000) 
