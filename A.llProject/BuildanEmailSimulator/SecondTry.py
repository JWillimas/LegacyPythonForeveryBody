class Email:
    def __init__(self,sender,receiver,subject,body):
        self.sender=sender
        self.receiver=receiver
        self.subject=subject
        self.body=body
        self.read_email=False

    def mark_as_read(self):
        self.read_email=True

    def display_whole_list(self):
        print("\n --- Email ---\n")
        print(f"From:{self.sender.name}")
        print(f"To:{self.receiver.name}")
        print(f"Subject:{self.subject}")
        print(f"Body:{self.body}")
        print("--------------------")
    
    def __str__(self):
        status="Read" if self.read_email==True else "Unread"
        return f"[{status}From: {self.sender.name} |Subject:{self.subject} ]"

class Inbox:
    def __init__(self):
        self.emails=[]
    
    def receive_email(self,email):
        self.emails.append(email)

    def list_email(self):
        if not self.emails:
            print("There are not email in box")
            return
        
        for i ,email in enumerate(self.emails,start=1):
            print(f"{i}.{email}")

    def read_email(self,index):
        if not self.emails:
             print("There are not email in box")
             return
        ac_index=index-1
        
        if ac_index<0 or ac_index>=len(self.emails):
            print("The index is unavaliable")
            return
        
        self.emails[ac_index].display_whole_list()

    def delete_email(self,index):
        if not self.emails:
             print("There are not email in box")
             return
        ac_index=index-1
        
        if ac_index<0 or ac_index>=len(self.emails):
            print("The index is unavaliable")
            return
        
        del self.emails[ac_index]
        print("delete sucessful")
    

 




class User:
    def __init__ (self,name):
        self.name=name
        self.inbox=Inbox()

    def send_email(self,receiver,subject,body):
        email=Email(sender=self,receiver=receiver,
                subject=subject,body=body) 

        receiver.inbox.receive_email(email)

        print(f"Email sent from {self.name} to {receiver.name}!")

    def check_inbox(self):
        print(f"{self.name}'s Email")
        self.inbox.list_email()

    def read_email(self,index):
        self.inbox.read_email(index)

    def delete_email(self,index):
        self.inbox.delete_email(index)



tory =User('Tory')
ramy =User('Ramy')        

tory.send_email(ramy, 'Hello', 'Hi Ramy, just saying hello!')
ramy.send_email(tory, 'Re: Hello', 'Hi Tory, hope you are fine.')

ramy.check_inbox()
ramy.read_email(1)
ramy.delete_email(1)
ramy.check_inbox()