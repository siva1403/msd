from flask import Flask, request, jsonify
import smtplib
from email.mime.text import MIMEText

app = Flask(__name__)

# Email config (use environment variables in real use)
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
EMAIL_USER = "your_email@gmail.com"
EMAIL_PASS = "your_app_password"
TO_EMAIL = "receiver@gmail.com"


def send_email(subject, body):
    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = EMAIL_USER
    msg["To"] = TO_EMAIL

    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(EMAIL_USER, EMAIL_PASS)
        server.send_message(msg)
        server.quit()
        print("Email sent successfully")
    except Exception as e:
        print("Email failed:", str(e))


@app.route("/cleanup", methods=["POST"])
def cleanup():
    data = request.json

    repo = data.get("repository")
    branch = data.get("branch")
    action = data.get("action")

    print(f"Cleanup triggered for {repo}:{branch}")

    # 🔧 Example cleanup logic
    # (replace with real logic like deleting temp branches, logs, etc.)
    cleanup_status = f"Cleaned resources for {branch}"

    # 📧 Send email
    send_email(
        subject="Cleanup Completed",
        body=f"""
Repository: {repo}
Branch: {branch}
Action: {action}

Status: {cleanup_status}
"""
    )

    return jsonify({"status": "cleanup done"}), 200


if __name__ == "__main__":
    app.run(port=5000)
