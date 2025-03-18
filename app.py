from flask import Flask, render_template, jsonify, Response
import cv2
import mysql.connector
from datetime import datetime

app = Flask(__name__)

# Configurações do banco de dados MySQL
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="cimatec",
        database="visualshield"
    )

# Função para pegar os logs do banco de dados
def get_alerts():
    db = get_db_connection()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT data_hora, erro, epi_faltando FROM logs_camera WHERE erro IS NOT NULL ORDER BY data_hora DESC LIMIT 10")
    logs = cursor.fetchall()
    cursor.close()
    db.close()
    return logs

# Função para gerar gráfico (método simplificado para JSON)
@app.route('/get_logs')
def get_logs():
    db = get_db_connection()
    cursor = db.cursor()
    cursor.execute("SELECT COUNT(*), MONTH(data_hora) FROM logs_camera WHERE erro IS NOT NULL GROUP BY MONTH(data_hora)")
    logs = cursor.fetchall()
    cursor.close()
    db.close()
    return jsonify(logs)

# Captura da câmera (usando OpenCV)
def gen_camera():
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        ret, jpeg = cv2.imencode('.jpg', frame)
        if ret:
            frame = jpeg.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/camera')
def camera():
    return Response(gen_camera(), mimetype='multipart/x-mixed-replace; boundary=frame')

# Rota para a página principal do dashboard
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, threaded=True)
