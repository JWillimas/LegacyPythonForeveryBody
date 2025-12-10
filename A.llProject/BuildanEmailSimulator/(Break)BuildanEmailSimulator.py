print("-"*50)#--------------------------------------------------------->

#Question1: Nesting Class Using
    #Question1.1: Magic method Using
        #Using" .name function" , print variable as string :
            #email01=Email(tory,"123",'Hello', 'Hi Ramy, just saying hello!')
                #print(f{email01.sender.name}')

#Question2: Using list to store the objects
    #class Inbox--->def __init__(self):----> self.emails=[]
       

#Question3: Creat a other class object in the current class 
    #def __init__(self,name):-->self.inbox=Inbox()

        #def send_email(self,receiver,subject,body):--->
            #email=Email(sender=self,receiver=receiver,
                #subject=subject,body=body)
                    
        


print("-"*50)#--------------------------------------------------------->


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
        # print(f"Received: {self.timestamp.strftime('%Y-%m-%d %H:%M')}")
        print(f'Body: {self.body}')
        print('------------\n')

    def __str__(self):
        status='Unread' if self.is_read==False else 'Read'
        return f"[{status}]From: {self.sender.name} | Subject:{self.subject}"

class Inbox:
    def __init__(self):
        self.emails=[]
        #emails=[
                #Email01(in __str__ form:)
                #Email02
                #Email03
                #.......
            #]


    def receive_email(self,email):
        self.emails.append(email)
        #return the __str__ in email to store

    def list_emails(self):
        if not self.emails:
            print("\nYour box is empty\n")
            return
        print("\nYour emails:\n")

        for i,email in enumerate(self.emails ,start=1):
            print(f'{i}.{email}')
    
    def read_email(self,index):
        if not self.emails:
            print("\n Your inbox is empty\n")
            return 
        ac_index=index-1
        if ac_index<0 or ac_index>=len(self.emails):
            print("Your index is unavalible")

        self.emails[ac_index].display_full_email()

    def delete_email(self,index):
        if not self.emails:
            print("\n Your inbox is empty\n")
            return
        ac_index=index-1
        if ac_index<0 or ac_index>=len(self.emails):
            print("Your index is not avaliable")
        del self.emails[ac_index]
        

class User:
    def __init__(self,name):
        self.name=name
        self.inbox=Inbox()
    
    def send_email(self,receiver,subject,body):

        email=Email(sender=self,receiver=receiver,
                    subject=subject,body=body)
        #define body
        
        receiver.inbox.receive_email(email)
        #send the meassage to receiver

        print(f'Email sent from {self.name} to {receiver.name}!\n')

    def check_inbox(self):
        print(f"{self.name}'s Email")
        self.inbox.list_emails()

    def read_email(self,index):
        self.inbox.read_email(index)
    
    def delete_email(self,index):
        self.inbox.delete_email(index)
    

#tory-'Tory'-'Hello', 'Hi Ramy, just saying hello!'
#ramy-'Ramy'-'Re: Hello', 'Hi Tory, hope you are fine.'


def main():
    tory = User('Tory')
    ramy = User('Ramy')        
    
    tory.send_email(ramy, 'Hello', 'Hi Ramy, just saying hello!')
    ramy.send_email(tory, 'Re: Hello', 'Hi Tory, hope you are fine.')

    ramy.check_inbox()
    ramy.read_email(1)
    ramy.delete_email(1)
    ramy.check_inbox()

if __name__ == '__main__':
    main()

#Output:

# Email sent from Tory to Ramy!

# Email sent from Ramy to Tory!

# Ramy's Email

# Your emails:

# 1.[Unread]From: Tory | Subject:Hello

# --- Email ---
# From: Tory
# To: Ramy
# Subject: Hello
# Body: Hi Ramy, just saying hello!
# ------------

# Ramy's Email

# Your box is empty

    