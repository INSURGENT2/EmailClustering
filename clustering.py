import pandas as pd

def jaccard_similarity(str1, str2):
    """Calculate Jaccard similarity between two strings."""
    set1 = set(str1.split())
    set2 = set(str2.split())
    intersection = len(set1.intersection(set2))
    union = len(set1.union(set2))
    return intersection / union if union != 0 else 0

def cluster_emails(emails, threshold=0.1):
    """Cluster emails based on Jaccard similarity."""
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

def main():
    # Load email data
    df = pd.read_csv('emails.csv')  # Read the generated CSV
    emails = df.to_dict('records')

    # Cluster emails
    clusters = cluster_emails(emails)
    
    # Save clustered results
    cluster_data = []
    for cluster_id, cluster in enumerate(clusters):
        for email in cluster:
            cluster_data.append({
                'Cluster': cluster_id, 
                'Subject': email['Subject'], 
                'Body': email['Body'],
                'Sender': email['Sender']
            })
    
    cluster_df = pd.DataFrame(cluster_data)
    cluster_df.to_csv('clustered_emails.csv', index=False)  # Save clusters to CSV

if __name__ == "__main__":
    main()
