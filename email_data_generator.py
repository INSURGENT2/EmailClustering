import random
import pandas as pd

subjects = [
    "Meeting Reminder", "Project Update", "Invoice Attached", 
    "Your Subscription", "Happy Birthday!", "Follow Up", 
    "Newsletter", "Weekly Report", "Holiday Greetings", "Discount Offer"
]

bodies = [
    "This is a reminder for our upcoming meeting.", 
    "Please find the project update attached.", 
    "Your invoice is attached to this email.", 
    "Your subscription has been renewed.", 
    "Wishing you a very happy birthday!", 
    "Just following up on our last conversation.", 
    "Here is the latest newsletter for you.", 
    "Attached is the weekly report.", "Happy holidays!", 
    "Don't miss this limited-time discount offer!"
]

senders = ["alice@example.com", "bob@example.com", "carol@example.com", "dave@example.com"]

def generate_emails(count=100):
    emails = []
    for _ in range(count):
        subject = random.choice(subjects)
        body = random.choice(bodies)
        sender = random.choice(senders)
        email = {
            "Subject": subject,
            "Body": body,
            "Sender": sender
        }
        emails.append(email)
    
    df = pd.DataFrame(emails)
    df.to_csv('emails.csv', index=False)  # Save as a CSV

if __name__ == "__main__":
    generate_emails()
    print("Generated 100 emails and saved to 'emails.csv'.")
