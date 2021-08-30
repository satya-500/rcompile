import os
import json
import uuid
import subprocess
from flask import Flask
from flask import request
from flask_cors import CORS

app = Flask(__name__)

WERKZEUG_OPTS = {'host': '127.0.0.1', 'port': 8080}


@app.route('/api/v1/compiler', methods=['POST'])
def compiler():
    language = request.form.get('language', '')
    answer = request.form.get('answer', '')
    return docker(language, answer)


def docker(language_name, answer):
	print(language_name)
	f = open('languages.json',)
	languages = json.load(f)
	f.close()
	
	language = languages[language_name]
	
	ext = language['extension']
	docker_image = language['image_name']
	
	cwd = os.getcwd()
	file_name = f'/tmp/{str(uuid.uuid1())}.{ext}'
	file = open(cwd+file_name, 'w')
	file.write(answer)
	file.close()

	if language['is_executable']:
		os.system(f'chmod +x {cwd+file_name}')

	docker_cmd = f'docker run --rm -v {cwd}/tmp:/tmp {docker_image} '
	if language_name == 'java':
		cmd = f'bash -c "cd /tmp/; javac {file_name}; java Test"'
	elif(language_name == 'go'):
		cmd =  f'{language_name} run {file_name}'
	else:
		cmd =  f'{language_name} {file_name}'
	
	docker_cmd = docker_cmd + cmd
	

	print(docker_cmd)



	output = subprocess.getoutput(docker_cmd)
	os.remove(cwd+file_name)

	response = {
		'output': output
	}
	
	return response



CORS(app)
app.run(**WERKZEUG_OPTS)