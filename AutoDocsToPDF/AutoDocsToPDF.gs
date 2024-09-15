function autoSaveToPDF() {
  // If you wanna change active documents into PDF then use this line: 'var doc = DocumentApp.getActiveDocument();'
  
  // else if you wanna change a specific documents then use this: 
  var docId = 'Your-google-docs-document-ID'; //you can find 'document Id' from the document url
  var doc = DocumentApp.openById(docId);
  var docName = doc.getName();
  
  // Convert Google Docs file to PDF
  var pdf = DriveApp.getFileById(docId).getAs('application/pdf');
  
  // Get the folder where the document is saved
  var folder = DriveApp.getFileById(docId).getParents().next();
  
  // Save the PDF in the same folder with a new name (or replace existing)
  var files = folder.getFilesByName(docName + ".pdf");
  
  // Delete old PDF if it exists
  while (files.hasNext()) {
    var oldPdf = files.next();
    oldPdf.setTrashed(true);
  }
  
  // Save the new PDF
  folder.createFile(pdf).setName(docName + ".pdf");
}
