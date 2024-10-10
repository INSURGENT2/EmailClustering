from flask import Flask, render_template
import pandas as pd
import random

app = Flask(__name__)

# Sample email data generator
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

# Generate random emails
def generate_emails(count=100):
    emails = []
    for _ in range(count):
        subject = random.choice(subjects)
        body = random.choice(bodies)
        sender = random.choice(senders)
        emails.append({
            "Subject": subject,
            "Body": body,
            "Sender": sender
        })
    return emails

# Jaccard Similarity Function
def jaccard_similarity(str1, str2):
    set1 = set(str1.split())
    set2 = set(str2.split())
    intersection = len(set1.intersection(set2))
    union = len(set1.union(set2))
    return intersection / union if union != 0 else 0

# Cluster emails based on subject similarity
def cluster_emails(emails, threshold=0.3):
    clusters = []
    visited = [False] * len(emails)
    
    for i in range(len(emails)):
        if visited[i]:
            continue
        
        current_cluster = [emails[i]]
        visited[i] = True
        
        for j in range(len(emails)):
            if i != j and not visited[j]:
                similarity = jaccard_similarity(emails[i]['Subject'], emails[j]['Subject'])
                if similarity > threshold:
                    current_cluster.append(emails[j])
                    visited[j] = True
                    
        clusters.append(current_cluster)
        
    return clusters

@app.route('/')
def index():
    emails = generate_emails()
    clusters = cluster_emails(emails)
    
    # Create cluster titles dynamically
    cluster_titles = {i: f"Cluster {i+1}" for i in range(len(clusters))}
    
    return render_template('index.html', clusters=clusters, cluster_titles=cluster_titles)

if __name__ == '__main__':
    app.run(debug=True)
