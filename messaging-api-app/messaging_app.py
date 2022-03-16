import smtplib
import ssl
from tkinter import *
from tkinter import simpledialog

def get_message():
    root = Tk()
    root.withdraw()
    root.size
    message = simpledialog.askstring(title="SMS", prompt="What is your message?")
    return message
# def submit():
#     message = entry.get()
#     return message

# def delete():
#     entry.delete(0,END) # This deletes the entire line of text.
    
# window = Tk()

# submit = Button(window,text="submit",command=submit)
# submit.pack(side = RIGHT)
# delete = Button(window,text="delete",command=delete)
# delete.pack(side = RIGHT)

# entry = Entry()
# entry.config(font=('Ink Free', 50))
# entry.config(bg='black')
# entry.config(fg='green')
# # entry.insert(0,'Spongebob')
# # entry.config(state=DISABLED) #ACTIVE/DISABLED
# entry.config(width=10)
# entry.config(show='$')
# entry.pack()
# window.mainloop()

    # window.title("Python SMS app")
    # window.configure(width=500, height=300)
    # window.configure(bg = 'lightblue')

    # winWidth = window.winfo_reqwidth()
    # winHeight = window.winfo_reqheight()
    # posRight = int(window.winfo_screenwidth() / 2 - winWidth / 2)
    # posDown = int(window.winfo_screenheight() / 2 - winHeight /2)
    # window.geometry("+{}+{}".format(posRight, posDown))
        
    # return(message)

def send_sms_via_email(number: str, message: str, provider: str, sender_credentials: tuple, subject: str = "sent using python", smtp_server: str = "smtp.gmail.com", smtp_port: int = 465):
    sender_email, email_password = sender_credentials

    receiver_email = f"{number}@txt.att.net"
    message = f"Subject:{subject}\nTo:{receiver_email}\n{message}"

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(smtp_server, smtp_port, context=context) as server:
        server.login(sender_email, email_password)
        server.sendmail(sender_email, receiver_email, message)


def main():
    number = "8435405406"
    provider = "AT&T"
    sender_credentials = ("jalaimo86@gmail.com", "azrltidhiuskmzeh")
    message = get_message()
    send_sms_via_email(number, message, provider, sender_credentials)
    

main()