import streamlit as st 

st.write ('welcome Home')

#username = "walid.hamad89@gmail.com"

import io
from pdfkit import from_string
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import smtplib

def send_email_with_pdf(sender_email, receiver_email, subject, message, html_text):
    # Convert HTML to PDF in memory
    pdf_buffer = io.BytesIO()
    pdf_file = from_string(html_text)
    pdf_buffer.write(pdf_file)
    pdf_data = pdf_buffer.getvalue()

    # Create email components
    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg["Subject"] = subject

    # Add text body
    body = MIMEText(message, "plain")
    msg.attach(body)

    # Attach PDF from memory
    attachment = MIMEBase("application", "octet-stream")
    attachment.set_payload(pdf_data)
    encoders.encode_base64(attachment)
    attachment.add_header("Content-Disposition", f"attachment; filename=output.pdf")
    msg.attach(attachment)

    # Send email
    smtp_server = "smtp.gmail.com"  # Replace with your SMTP server
    port = 587
    username = "walid.hamad89@gmail.com"
    password = st.secrets["password"]

    with smtplib.SMTP(smtp_server, port) as server:
        server.starttls()
        server.login(username, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())

# Example usage
sender_email = "walid.hamad89@gmail.com"
receiver_email = "eduforests@gmail.com"
subject = "Example Email with PDF Attachment"
message = "This is the body of the email."
html_text = """
<h1>My Example Title</h1>
<p>This is some paragraph content.</p>
<ul>
  <li>List item 1</li>
  <li>List item 2</li>
</ul>
"""

send_email_with_pdf(sender_email, receiver_email, subject, message, html_text)
st.write ("email sent")


