import subprocess

def fetch_pubmed_ids(search_term):
    
    retrieve_per_query = 10000
    # Construct the EDirect command
    #command = f'esearch -db pubmed -query "{search_term}[TIAB]" | efetch -format uid'
    command = f'esearch -db pubmed -query "{search_term}[TIAB]" -retmax {retrieve_per_query} | efetch -format uid'

    # Execute the command using subprocess
    try:
        # Run the command and capture the output
        result = subprocess.run(command, shell=True, check=True, text=True, capture_output=True)
        
        # Split the output into a list of IDs
        pubmed_ids = result.stdout.strip().split('\n')
        
        return pubmed_ids
    
    except subprocess.CalledProcessError as e:
        print("An error occurred while fetching PubMed IDs:", e)
        return []

# Example usage
search_term = "emotion"
pubmed_ids = fetch_pubmed_ids(search_term)

print(f"Fetched {len(pubmed_ids)} PubMed IDs:")
print(pubmed_ids)
