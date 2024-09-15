# Google Docs to PDF Auto-Save Script

This folder contains a Google Apps Script that automatically converts a Google Docs file to PDF and saves it to the same Google Drive folder. The script can be set to run on a periodic trigger, ensuring that the PDF version is always updated when changes are made to the Google Docs file.

## Features

- Automatically exports Google Docs files as PDFs.
- Saves the converted PDF in the same folder as the original Google Docs file.
- Replaces the old PDF file with the new version to ensure the latest changes are reflected.
- Can be configured to run at specific intervals (e.g., every 5 minutes, hourly, etc.).

## Setup Instructions

Follow these steps to set up and run the auto-save Google Docs to PDF script:

### 1. Open the Google Docs File
- Open the Google Docs file you want to automatically save as a PDF in your Google Drive.

### 2. Open the Apps Script Editor
- In the Google Docs file, go to **Extensions > Apps Script**.

### 3. Add the Script
- Copy AutoDocsToPDF.gs file's script and paste it in the editor. Remove any code from the editor before pasting (if any).
