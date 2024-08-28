# Import necessary libraries
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Define function to send email
def send_email(subject, message, from_addr, to_addr, password):
    msg = MIMEMultipart()
    msg['From'] = from_addr
    msg['To'] = to_addr
    msg['Subject'] = subject
    msg.attach(MIMEText(message, 'plain'))
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(from_addr, password)
    text = msg.as_string()
    server.sendmail(from_addr, to_addr, text)
    server.quit()

# Define function to calculate NPS score
def calculate_nps(score):
    if score >= 9:
        return "Promotor"
    elif score >= 7:
        return "Passivo"
    else:
        return "Detrator"

# Define function to handle form submission
def handle_form_submission(form_data):
    # Extract data from form
    name = form_data['name']
    email = form_data['email']
    experience = form_data['experience']
    improvements = form_data['improvements']
    features = form_data['features']
    usability = form_data['usability']
    comments = form_data['comments']
    
    # Calculate NPS category based on experience
    nps_category = calculate_nps(int(experience))
    
    # Prepare email content
    subject = "Nova Submissão de Feedback"
    message = f"Nome: {name}\\nEmail: {email}\\nExperiência: {experience}\\nMelhorias: {improvements}\\nRecursos: {features}\\nFacilidade de uso: {usability}\\nComentários: {comments}\\nCategoria NPS: {nps_category}"
    
    # Send email to a list of employees
    employees = ["funcionario1@exemplo.com", "funcionario2@exemplo.com", "funcionario3@exemplo.com"]
    for employee in employees:
        send_email(subject, message, "seu_email@exemplo.com", employee, "sua_senha")

# Nota: Substitua "seu_email@exemplo.com" e "sua_senha" pelo seu e-mail e senha reais
