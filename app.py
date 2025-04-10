from flask import Flask, render_template, request, jsonify
import requests
import json

app = Flask(__name__)

# List of available APIs
AVAILABLE_APIS = {
    'cep': {
        'name': 'Consulta de CEP',
        'description': 'Busca informações de endereço pelo CEP brasileiro',
        'url': 'https://viacep.com.br/ws/{cep}/json/'
    },
    'ip': {
        'name': 'Consulta de IP',
        'description': 'Mostra informações sobre o IP público',
        'url': 'https://api.ipify.org?format=json'
    },
    'jokes': {
        'name': 'Piadas Aleatórias',
        'description': 'Retorna uma piada aleatória em inglês',
        'url': 'https://official-joke-api.appspot.com/random_joke'
    }
}

@app.route('/')
def index():
    return render_template('index.html', apis=AVAILABLE_APIS)

@app.route('/api/<api_name>', methods=['GET', 'POST'])
def api_endpoint(api_name):
    if api_name not in AVAILABLE_APIS:
        return jsonify({'error': 'API não encontrada'}), 404

    api_info = AVAILABLE_APIS[api_name]
    
    if api_name == 'cep':
        cep = request.args.get('cep', '')
        if not cep:
            return jsonify({'error': 'CEP não fornecido'}), 400
        
        try:
            response = requests.get(api_info['url'].format(cep=cep))
            return jsonify(response.json())
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    
    elif api_name == 'ip':
        try:
            response = requests.get(api_info['url'])
            return jsonify(response.json())
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    
    elif api_name == 'jokes':
        try:
            response = requests.get(api_info['url'])
            return jsonify(response.json())
        except Exception as e:
            return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True) 