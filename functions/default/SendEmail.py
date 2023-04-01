"""
This code defines a class SendEmail that provides functionality to send an email with an attachment. The SendEmail class has three methods:

__init__: initializes the host, port, login credentials, email recipient, and attachment name for the email.
connect: connects to the SMTP server specified by the host and port, and starts a TLS session.
setEmail: creates a MIME message and attaches the specified file to it.
send: sends the email with the attached file.

The main function parses the command-line arguments to get the email recipient and attachment name, creates an instance of SendEmail 
with the appropriate parameters, and calls the connect, setEmail, and send methods to send the email.

This file is not called as a module inside the code, but as a separated file.
"""

# Import required modules for sending email
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import smtplib
import ssl


import sys
sys.path.append('./serverConfig/')
sys.path.append('./database/')
sys.path.append('./functions/default')

# Import custom modules
from Config import HOST, PORT, LOGIN, PASSWORD
from Database import DatabaseFunctions
from SearchFiles import SearchFiles


# IMPORTANT -> FIX THE PATH
class SendEmail:
    """A class to send an email with an attachment"""

    def __init__(self, host: str, port: str, login: str, password: str, emailTo: str, bookID: int) -> None:
        """Initialize the email object with the given parameters"""
        self.host = host
        self.port = port
        self.login = login
        self.password = password
        self.emailTo = emailTo
        self.bookID = bookID

    def connect(self) -> None:
        """Connect to the SMTP server"""
        try:
            self.server = smtplib.SMTP(self.host, self.port)
            self.server.ehlo()
            context = ssl.create_default_context()
            self.server.starttls(context=context)
            self.server.login(self.login, self.password)
        except Exception as e:
            raise RuntimeError(f"SendEmail.py: Couldn't connect to the Server! Error: {e}")

    def setEmail(self) -> None:
        """Create the email message with the attachment"""
        try:
            path = SearchFiles().searchFileByID(self.bookID, "txt")
            bookName = DatabaseFunctions().getBookName(self.bookID)
            self.email_msg = MIMEMultipart()
            self.email_msg["From"] = self.login
            self.email_msg["To"] = self.emailTo
            self.email_msg["Subject"] = ""

            path = open(path, "rb")
            epub = MIMEApplication(path.read())
            epub.add_header("Content-Disposition",
                            "attachment", filename=f"{bookName}.txt")
            self.email_msg.attach(epub)
        except Exception as e:
            raise RuntimeError(f"SendEmail.py: Couldn't set email configuration! Error: {e}")

    def send(self) -> None:
        """Send the email with the attachment"""
        try:
            self.server.sendmail(
                self.email_msg["From"], self.email_msg['To'], self.email_msg.as_string())
            self.server.quit()
        except Exception as e:
            raise RuntimeError(f"SendEmail.py: Couldn't send email! Error: {e}")

def main() -> None:
    """Main function that sends the email with attachment"""
    # Check if command line arguments are valid
    if len(sys.argv) != 3:
        print("Usage: python program.py <email_to> <book_name>")
        return

    # Get the email recipient and attachment name from command line arguments
    emailTo = sys.argv[1]
    bookID = sys.argv[2]

    # Create an instance of SendEmail class with the given parameters
    sendMail = SendEmail(
        host=HOST,
        port=PORT,
        login=LOGIN,
        password=PASSWORD,
        emailTo=emailTo,
        bookID=int(bookID)
    )

    # Connect to the SMTP server, create the email message with the attachment, and send the email
    sendMail.connect()
    sendMail.setEmail()
    sendMail.send()


if __name__ == "__main__":
    try:
        main()
    except RuntimeError as e:
        print(f"Error Message: --> {e}")
