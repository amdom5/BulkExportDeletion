import requests
import csv
import base64

# Placeholder for the Pod Number
elqPod = "your_pod_number"  # Update this with the actual pod number

# Eloqua API credentials and base URL
elqUrl = f"https://secure.p{elqPod}.eloqua.com/api/bulk/2.0/syncs/"
elqCompanyName = "your_company_name"
elqUsername = "your_username"
elqPassword = "your_password"

# Function to delete a sync by ID
def delete_sync(sync_id):
    url = f"{elqUrl}{sync_id}"
    headers = {
        "Authorization": f"Basic {base64.b64encode(f'{elqCompanyName}\\{elqUsername}:{elqPassword}'.encode()).decode()}",
        "Content-Type": "application/json",
    }

    response = requests.delete(url, headers=headers)

    if response.status_code == 204:
        print(f"Sync with ID {sync_id} deleted successfully.")
    else:
        print(f"Error deleting sync with ID {sync_id}. Status code: {response.status_code}, Response: {response.text}")

# Function to read IDs from CSV and delete each sync
def delete_bulk_syncs(csv_file_path):
    with open(csv_file_path, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row if exists

        for row in reader:
            sync_id = row[0]  # Assuming the ID is in the first column of your CSV
            delete_sync(sync_id)

# Example usage
if __name__ == "__main__":
    # Update the path to your CSV file
    csv_file_path = "path/to/your/csv/file.csv"
    
    # Update the pod number before running the script
    print("Before running the script, please update the 'elqPod' variable with your actual pod number.")
    
    # Uncomment the line below to execute the script
    # delete_bulk_syncs(csv_file_path)
