import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_email():
    # Variáveis de ambiente (definidas nos Secrets do GitHub Actions)
    sender_email = os.getenv("EMAIL_USER")
    sender_pass = os.getenv("EMAIL_PASS")
    receiver_email = os.getenv("EMAIL_TO")

    if not sender_email or not sender_pass or not receiver_email:
        raise ValueError("Variáveis de ambiente EMAIL_USER, EMAIL_PASS e EMAIL_TO são obrigatórias.")

    # Monta a mensagem
    subject = "CI/CD Pipeline - Campo Minado"
    body = "O pipeline foi executado com sucesso!"

    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))

    # Conexão SMTP (exemplo: Gmail)
    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(sender_email, sender_pass)
            server.sendmail(sender_email, receiver_email, msg.as_string())
        print("Email enviado com sucesso!")
    except Exception as e:
        print(f"Erro ao enviar email: {e}")


if __name__ == "__main__":
    send_email()
