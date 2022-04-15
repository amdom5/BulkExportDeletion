# BulkSyncDeletion
Bulk Export dependencies can be a real pain when trying to clean up your instance. To make matters worse, there is no way to delete these dependencies through the UI. This Python script is designed to solve that problem and provide a way to delete bulk syncs.

The script takes input from a single column CSV file of Bulk Sync IDs. It iterates through each of the IDs and deletes the bulk export dependencies in Eloqua.

# Setup
Make sure you have Python installed on your system. As well, you must get the IDs of the bulk syncs you are trying to delete, and place them in a single column CSV file. Each sync ID must be in its own row.

# How to Use
Run the script from the command line and follow the prompts.
