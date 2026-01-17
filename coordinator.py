from flask import Flask, request, jsonify  # добавить jsonify
import requests
import traceback  # для отладки
 
app = Flask(__name__)
server_urls = ['https://127.0.0.1:5000', 'https://192.168.0.137:5000']
 
@app.route('/api/data', methods=['POST'])
def handle_request():
    try:
        data = request.get_json()
        print(f"Coordinator received: {data}")
 
        for url in server_urls:
            try:
                print(f"Trying server: {url}")
                # Отключаем SSL проверку для тестирования
                response = requests.post(f"{url}/api/data", 
                                       json=data, 
                                       verify=False,
                                       timeout=5)
 
                print(f"Server response: {response.status_code}")
 
                if response.status_code == 200:
                    return jsonify(response.json())
 
            except Exception as e:
                print(f"Error contacting {url}: {e}")
                continue
 
        return jsonify({'error': 'All servers are down'}), 503
 
    except Exception as e:
        print(f"Coordinator error: {e}")
        print(traceback.format_exc())
        return jsonify({'error': 'Internal server error'}), 500
 
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
