import threading
import time
import webbrowser
import requests
import json
import sqlite3
import logging
from collections import Counter
from flask import Flask, render_template_string, jsonify, request, redirect, url_for
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

#DAHİLİ MODÜLLER
from modules.listener import LogListener
from modules.parser import LogParser
from modules.detector import ThreatDetector
from modules.database import DatabaseManager

#1.AYARLAR
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

app = Flask(__name__)
app.secret_key = '.267267' #->Session güvenliği için key

#2.LOGIN SİSTEMİ
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

class User(UserMixin):
    def __init__(self, id):
        self.id = id

ADMIN_USER = "admin"
ADMIN_PASS = "root"

@login_manager.user_loader
def load_user(user_id):
    return User(user_id) if user_id == ADMIN_USER else None

#3.HTML
#Giriş Sayfası Tasarım
LOGIN_HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>MicroSIEM - Giriş</title>
    <style>
        body { background-color: #0d1117; color: #c9d1d9; font-family: 'Segoe UI', monospace; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; }
        .login-box { background-color: #161b22; border: 1px solid #30363d; padding: 40px; border-radius: 10px; box-shadow: 0 4px 12px rgba(0,0,0,0.5); text-align: center; width: 300px; }
        input { width: 90%; padding: 10px; margin: 10px 0; background: #0d1117; border: 1px solid #30363d; color: white; border-radius: 5px; }
        button { width: 100%; padding: 10px; background-color: #238636; color: white; border: none; border-radius: 5px; cursor: pointer; font-weight: bold; }
        button:hover { background-color: #2ea043; }
        h2 { color: #58a6ff; }
        .error { color: #ff7b72; font-size: 12px; }
    </style>
</head>
<body>
    <div class="login-box">
        <h2>🔒 Güvenli Giriş</h2>
        <form method="POST">
            <input type="text" name="username" placeholder="Kullanıcı Adı" required>
            <input type="password" name="password" placeholder="Şifre" required>
            <button type="submit">Giriş Yap</button>
        </form>
        {% if error %}
            <p class="error">{{ error }}</p>
        {% endif %}
    </div>
</body>
</html>
"""

#Dashboard Tasarım
DASHBOARD_HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>MicroSIEM v3.0</title>
    <meta http-equiv="refresh" content="10">
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <style>
        body { background-color: #0d1117; color: #c9d1d9; font-family: 'Segoe UI', monospace; padding: 20px; }
        .container { max-width: 1200px; margin: 0 auto; }
        .card { background-color: #161b22; border: 1px solid #30363d; border-radius: 6px; padding: 20px; margin-bottom: 20px; }
        h1 { text-align: center; color: #58a6ff; border-bottom: 1px solid #30363d; padding-bottom: 15px; }
        table { width: 100%; border-collapse: collapse; margin-top: 10px; font-size: 14px; }
        th, td { border-bottom: 1px solid #21262d; padding: 12px; text-align: left; }
        th { color: #8b949e; }
        .risk-HIGH { color: #ff7b72; font-weight: bold; }
        .risk-INFO { color: #3fb950; }
        .location-tag { background-color: #1f6feb; color: white; padding: 2px 8px; border-radius: 12px; font-size: 12px; }
        .logout-btn { float: right; background-color: #da3633; color: white; text-decoration: none; padding: 5px 10px; border-radius: 5px; font-size: 14px; }
        .chart-container { position: relative; height: 300px; width: 100%; display: flex; justify-content: center; }
    </style>
</head>
<body>
    <div class="container">
        <a href="/logout" class="logout-btn">Çıkış Yap</a>
        <h1>🛡️ MicroSIEM - Yönetim Paneli</h1>

        <div class="card">
            <h3>📊 Tehdit Analizi</h3>
            <div class="chart-container"><canvas id="attackChart"></canvas></div>
        </div>

        <div class="card">
            <h3>📋 Canlı Loglar</h3>
            <table>
                <tr><th>Zaman</th><th>Kaynak IP</th><th>Konum</th><th>Olay</th><th>Mesaj</th></tr>
                {% for row in logs %}
                <tr>
                    <td>{{ row[3].split(' ')[1] }}</td>
                    <td style="font-weight:bold; color: #e1e4e8;">{{ row[1] }}</td>
                    <td><span class="location-tag">{{ ip_info(row[1]) }}</span></td>
                    <td class="{{ 'risk-HIGH' if 'AUTH_FAILURE' in row[2] else 'risk-INFO' }}">{{ row[2] }}</td>
                    <td style="font-size: 12px; color: #8b949e;">{{ row[4] }}</td>
                </tr>
                {% endfor %}
            </table>
        </div>
    </div>
    <script>
        fetch('/api/stats').then(r => r.json()).then(data => {
            new Chart(document.getElementById('attackChart'), {
                type: 'doughnut',
                data: { labels: data.labels, datasets: [{ data: data.values, backgroundColor: ['#ff7b72', '#d2a8ff', '#58a6ff', '#3fb950', '#f0883e'], borderWidth: 0 }] },
                options: { responsive: true, maintainAspectRatio: false, plugins: { legend: { position: 'right', labels: { color: '#c9d1d9' } } } }
            });
        });
    </script>
</body>
</html>
"""

#4.FLASK ROTALARI
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = request.form['username']
        pw = request.form['password']
        if user == ADMIN_USER and pw == ADMIN_PASS:
            login_user(User(user))
            return redirect(url_for('index'))
        else:
            return render_template_string(LOGIN_HTML, error="Hatalı Kullanıcı Adı veya Şifre!")
    return render_template_string(LOGIN_HTML)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

def get_ip_info(ip):
    if ip.startswith("192.168.") or ip.startswith("127.") or ip.startswith("10."): return "Yerel Ağ"
    try:
        data = requests.get(f"http://ip-api.com/json/{ip}", timeout=2).json()
        return f"{data['country']} - {data['isp']}" if data['status'] == 'success' else "Bilinmiyor"
    except: return "-"

def get_logs():
    try:
        conn = sqlite3.connect('siem.db')
        cur = conn.cursor()
        cur.execute("SELECT * FROM logs ORDER BY id DESC LIMIT 15")
        data = cur.fetchall()
        conn.close()
        return data
    except: return []

@app.route('/api/stats')
@login_required
def stats():
    try:
        conn = sqlite3.connect('siem.db')
        cur = conn.cursor()
        cur.execute("SELECT source_ip FROM logs")
        ips = [row[0] for row in cur.fetchall()]
        conn.close()
        common = Counter(ips).most_common(5)
        return jsonify({'labels': [i[0] for i in common], 'values': [i[1] for i in common]})
    except: return jsonify({'labels': [], 'values': []})

@app.route('/')
@login_required
def index():
    return render_template_string(DASHBOARD_HTML, logs=get_logs(), ip_info=get_ip_info)

def run_flask():
    app.run(host='0.0.0.0', port=5000, debug=False, use_reloader=False)

listener = LogListener(port=5140)
parser = LogParser()
detector = ThreatDetector()
db = DatabaseManager()

def process_log(ip, raw_message):
    parsed_data = parser.parse(ip, raw_message)
    db.insert_log(parsed_data)
    detector.analyze(parsed_data)
    print(".", end="", flush=True)

if __name__ == "__main__":
    print("[*] MicroSIEM v3.0 (Security Edition) Başlatılıyor...")
    
    # Web sitesini arka planda başlat
    t1 = threading.Thread(target=run_flask)
    t1.daemon = True
    t1.start()
    
    print("[*] Dashboard: http://127.0.0.1:5000")
    print(f"[*] Giriş Bilgileri: {ADMIN_USER} / {ADMIN_PASS}")
    
    time.sleep(1)
    # Tarayıcıyı aç
    webbrowser.open("http://127.0.0.1:5000")
    
    print("[*] Dinleniyor (UDP 5140)...")
    try:
        listener.start_listening(process_log)
    except KeyboardInterrupt:
        print("\n[!] Kapatılıyor.")