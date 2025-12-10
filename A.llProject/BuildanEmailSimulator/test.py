class Email:
    def __init__(self,sender,receiver,subject,body):
        self.sender=sender
        self.receiver=receiver
        self.subject=subject
        self.body=body
        self.is_read=False

    def mark_is_read (self):
        self.is_read=True

    def display_full_email(self):
        self.mark_is_read()
        print('\n--- Email ---')
        print(f'From: {self.sender.name}')
        print(f'To: {self.receiver.name}')
        print(f'Subject: {self.subject}')
        print(f"Received: {self.timestamp.strftime('%Y-%m-%d %H:%M')}")
        print(f'Body: {self.body}')
        print('------------\n')

class Inbox:
    def __init__(self,email):
        self.email=[]


tory=Email("tory","123",'Hello', 'Hi Ramy, just saying hello!')

email=[]

email.append(tory)

print(email[0].sender)


