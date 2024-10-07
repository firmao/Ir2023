import subprocess
import time

def fetch_pubmed_records(query, retmax=1000, batch_size=500, output_file='results.txt'):
    with open(output_file, 'w') as outfile:
        retstart = 0
        while True:
            try:
                # Construct the EDirect search command
                command = f'esearch -db pubmed -query "{query}[TIAB]" | efetch -format uid'
                
                # Execute the command
                result = subprocess.run(command, shell=True, capture_output=True, text=True)
                
                # Check if there are no more records or an error occurred
                if not result.stdout.strip() or "No items found" in result.stdout:
                    print("No more records found. Completed fetching.")
                    break
                
                # Write the results to file
                outfile.write(result.stdout)
                print(f"Fetched records {retstart} to {retstart + batch_size}")
                
                # Move to the next batch
                retstart += batch_size
                
                # Pause to avoid overwhelming PubMed's servers
                time.sleep(1)
                
            except Exception as e:
                print(f"Error occurred: {e}. Retrying in 5 seconds...")
                time.sleep(5)
                continue

# Example usage
fetch_pubmed_records("emotion", retmax=10000, batch_size=500)
