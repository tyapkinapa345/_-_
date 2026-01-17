from flask import Flask, request, jsonify
import ssl
from cryptography.fernet import Fernet
 
app = Flask(__name__)
 
@app.route('/api/data', methods=['POST'])
def get_data():
    try:
        json_data = request.get_json()
        print(f"Received JSON: {json_data}")
 
        if not json_data:
            return jsonify({'error': 'No JSON data'}), 400
 
        # Проверяем наличие данных
        if 'data' not in json_data:
            return jsonify({'error': 'No "data" field'}), 400
 
        # Пытаемся расшифровать если есть ключ
        try:
            with open('encryption_key.txt', 'rb') as f:
                key = f.read()
            cipher = Fernet(key)
            decrypted = cipher.decrypt(json_data['data'].encode()).decode()
            print(f"Decrypted data: {decrypted}")
        except FileNotFoundError:
            print("No encryption key, using raw data")
            decrypted = json_data['data']
        except Exception as e:
            print(f"Decryption failed: {e}")
            decrypted = json_data['data']
 
        return jsonify({
            'result': 'ok',
            'received': json_data.get('data'),
            'decrypted': decrypted
        })
 
    except Exception as e:
        print(f"Server error: {e}")
        return jsonify({'error': str(e)}), 500
 
if __name__ == '__main__':
    # Создаем ключ если его нет
    try:
        with open('encryption_key.txt', 'rb') as f:
            pass
    except FileNotFoundError:
        key = Fernet.generate_key()
        with open('encryption_key.txt', 'wb') as f:
            f.write(key)
        print("Encryption key created")
 
    # SSL контекст
    context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    context.load_cert_chain('server_cert.pem', 'server_key.pem')
    context.verify_mode = ssl.CERT_REQUIRED
    context.load_verify_locations('ca_cert.pem')
 
    app.run(host='0.0.0.0', port=5000, ssl_context=context, debug=True)
