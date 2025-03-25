from flask import Flask, render_template, jsonify, Response
import cv2
import mysql.connector
import io
import matplotlib.pyplot as plt

app = Flask(__name__)

# Configurações do banco de dados
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="12345678",
        database="visualshield"
    )

# Obtém logs do banco de dados para o gráfico
@app.route('/get_logs')
def get_logs():
    db = get_db_connection()
    cursor = db.cursor()
    cursor.execute("SELECT COUNT(*), MONTH(data_hora) FROM logs_camera WHERE erro IS NOT NULL GROUP BY MONTH(data_hora)")
    logs = cursor.fetchall()
    cursor.close()
    db.close()
    return jsonify(logs)

# Captura de câmera
def gen_camera():
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frame = cv2.flip(frame, 1)
        ret, jpeg = cv2.imencode('.jpg', frame)
        if ret:
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + jpeg.tobytes() + b'\r\n\r\n')

@app.route('/camera')
def camera():
    return Response(gen_camera(), mimetype='multipart/x-mixed-replace; boundary=frame')

# Gerar gráfico usando Matplotlib
@app.route('/grafico.png')
def grafico():
    db = get_db_connection()
    cursor = db.cursor()
    cursor.execute("SELECT COUNT(*), MONTH(data_hora) FROM logs_camera WHERE erro IS NOT NULL GROUP BY MONTH(data_hora)")
    logs = cursor.fetchall()
    cursor.close()
    db.close()

    # Verifica se há dados no banco
    if not logs:
        logs = [(0, 1)]  # Adiciona um valor fictício para evitar erro

    # Preparando os dados para o gráfico
    meses = [f"Mês {item[1]}" for item in logs]
    valores = [item[0] for item in logs]

    fig, ax = plt.subplots(figsize=(6, 3))
    ax.bar(meses, valores, color='blue', alpha=0.7, label="Número de Alertas")

    ax.set_title("Número de Alertas por Mês")
    ax.set_xlabel("Mês")
    ax.set_ylabel("Quantidade")
    ax.legend()
    ax.grid(axis='y', linestyle='--', alpha=0.7)

    # Ajusta os rótulos do eixo X para evitar sobreposição
    plt.xticks(rotation=45)

    # Salvar o gráfico na memória
    

# Rota para obter alertas com log
@app.route('/get_alerts')
def get_alerts():
    db = get_db_connection()
    cursor = db.cursor()
    cursor.execute("SELECT data_hora, erro, epi_faltando FROM logs_camera WHERE erro IS NOT NULL")
    alerts = cursor.fetchall()
    print("Fetched alerts:", alerts)  # Log fetched alerts for debugging
    cursor.close()
    db.close()
    return jsonify([{'data_hora': alert[0], 'erro': alert[1], 'epi_faltando': alert[2]} for alert in alerts])


# Página principal

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, threaded=True)
