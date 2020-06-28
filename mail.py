import smtplib
import urllib.request as urllib
# Senders email
sender_email = "arorasuhani1511@gmail.com"
# Receivers email
rec_email = "arorasuhani1511@gmail.com"

message = "Kuberenetes cluster not running.......Do the required changes."
# Initialize the server variable
server = smtplib.SMTP('smtp.gmail.com', 587)
# Start the server connection
server.starttls()
# Login
server.login("arorasuhani1511@gmail.com", "Password#12345")
print("Login Success!")
# Send Email
server.sendmail("Suhani Arora", "arorasuhani1511@gmail.com", message)