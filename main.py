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
from xhtml2pdf import pisa

def send_email_with_pdf(sender_email, receiver_email, subject, message, html_text):
    
    if not isinstance(html_text, (str, bytes)):
        raise TypeError("html_content must be a string or bytes object.")

    #file = open("output.pdf", "wb")  # Open in binary write mode
    pdf_buffer = io.BytesIO()

    if isinstance(html_text, str):
        html_bytes = html_text.encode('utf-8')  # Encode string to bytes

    pisa.CreatePDF(html_bytes, pdf_buffer)

    
    # Get the generated PDF content as bytes
    #pdf_bytes = pdf.output(dest='S').encode()  # Save to string and encode


    #pdf_buffer = io.BytesIO()

    #pdf_buffer.write(pdf_bytes)
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


