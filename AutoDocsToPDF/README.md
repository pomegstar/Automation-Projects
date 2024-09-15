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

### 4. Set Up Triggers
- To automatically save the document as a PDF, you can set a time-based trigger:
  1. In the Apps Script Editor, click the clock icon (Triggers).
  2. Click **+ Add Trigger** in the lower right.
  3. Set the following options:
     - **Choose which function to run**: `autoSaveToPDF`
     - **Choose which deployment should run**: `Head`
     - **Select event source**: `Time-driven`
     - **Select type of time-based trigger**: Select the frequency you want (e.g., every 5 minutes, hourly, etc.)
  4. Save the trigger.

### 5. Testing the Script
- Make changes to the Google Docs file and wait for the trigger to run based on your chosen schedule.
- The PDF file will automatically be saved/updated in the same folder as the Google Docs file.

## Customization

If you want to add more features or modify the script, you can:
- Customize the naming convention of the generated PDF.
- Add other metadata (such as date or versioning) to the PDF file name.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Feel free to contribute or submit issues if you encounter any problems or have ideas for improvements.
