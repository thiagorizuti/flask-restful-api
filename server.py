from flask import Flask, abort, request, jsonify, redirect, send_from_directory
from werkzeug.utils import secure_filename
import os
import psutil
import platform

UPLOAD_FOLDER = 'uploads/'
ALLOWED_EXTENSIONS = set(['zip'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 2 * 1024 * 1024
app.config['MIN_CONTENT_LENGTH'] = 1024



@app.route('/', methods=['GET','POST'])
def index():
	if request.method == 'GET':
		return 'Bem-vindo.'
	elif request.method == 'POST':
		return 'Este endpoint não aceita pedidos.'
	else:
		abort(403)

@app.route('/info', methods=['GET','POST'])
def info():
	if request.method == 'GET':
		return 'Retorna informacoes do sistema.  METODO: post  JSON: {"cpu":bool,"memory":bool,"hostname":bool,"os":bool} CONTENT-TYPE: application/json'
	elif request.method == 'POST':
		if not request.json:
			abort(400)
		if not 'cpu' in request.json or type(request.json['cpu']) is not bool:
			abort(400)
		if not 'memory' in request.json or type(request.json['memory']) is not bool: 
			abort(400)
		if not 'hostname' in request.json:
			abort(400)
		if not 'os' in request.json:
			abort(400)
		response = {	
			'cpu': str(psutil.cpu_percent())+'%' if request.json['cpu'] else '',
			'memory': str(psutil.virtual_memory().free)+'bytes' if request.json['memory'] else '',
			'hostname': str(request.host) if request.json['hostname'] else '',
			'os': platform.platform() if request.json['os'] else ''
		}
		return jsonify({'response':response})
	else:
		abort(403)

def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/arquivo', methods=['GET', 'POST'])
def arquivo():
	if request.method == 'GET':
		return 'Armazena arquivos no servidor.  METODO: post ARQUIVO: .zip NOME_DO_CAMPO: file '
	if request.method == 'POST':
		file = request.files['file']
		if file and allowed_file(file.filename):
			filename = secure_filename(file.filename)
			file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
			return 'Arquivo enviado com sucesso.'
		else:
			abort(400)
	else:
		abort(403)
		
@app.route('/arquivo/<filename>', methods=['GET'])
def download(filename):
	return send_from_directory(os.path.join(app.config['UPLOAD_FOLDER']), filename=filename)

@app.route('/arquivos', methods=['GET'])
def arquivos():
	return ', '.join(os.listdir(os.path.join(app.config['UPLOAD_FOLDER'])))
			
if __name__ == '__main__':
   app.run(port=7654)
