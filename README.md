# BulkSyncDeletion
 This Python script is designed to solve that problem and provide a way to delete a bunch of bulk syncs.

The script takes input from a single column CSV file of Bulk Sync IDs. It iterates through each of the IDs and deletes the bulk export dependencies in Eloqua.

# Setup
Make sure you have Python installed on your system. As well, you must get the IDs of the bulk syncs you are trying to delete, and place them in a single column CSV file. Each sync ID must be in its own row.

# How to Use
Run the script from the command line and follow the prompts.


# Eloqua Bulk Sync Deletion Script

Bulk Sync dependencies can be a real pain when trying to clean up your Eloqua instance. To make matters worse, there is no way to delete these dependencies through the UI. 
This Python script allows you to delete multiple syncs in Eloqua using the Eloqua Bulk API. The script takes a CSV file containing a list of sync IDs and makes DELETE requests to the Eloqua API for each ID.

## Prerequisites

- Python 3.x
- `requests` library (`pip install requests`)

## Configuration

1. Open the script (`eloqua_bulk_sync_deletion.py`) in a text editor.
2. Replace the following placeholders with your actual Eloqua credentials and information:
   - `your_pod_number`: Update with your Eloqua pod number.
   - `your_company_name`: Update with your Eloqua company name.
   - `your_username`: Update with your Eloqua username.
   - `your_password`: Update with your Eloqua password.
   - `path/to/your/csv/file.csv`: Update with the path to your CSV file.

## Usage

1. Ensure the Eloqua account has the necessary permissions access the API and delete syncs.
1. Ensure Python and the `requests` library are installed.
2. Update the script with your Eloqua configuration.
3. Open a terminal and navigate to the script's directory.
4. Run the script by uncommenting the line `# delete_bulk_syncs(csv_file_path)` and executing the script.

   Note: Before running the script, make sure to update the 'elqPod' variable with your actual pod number.
   
```bash
python eloqua_bulk_sync_deletion.py
