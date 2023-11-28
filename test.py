from file_conversion import Docx2PdfConverter, Pdf2DocxConverter

# Convert DOCX to PDF
docx_path = "C:\\Users\\Pavun\\Desktop\\File_conversion\\input_folder\\input_file.docx"
pdf_path = "C:\\Users\\Pavun\\Desktop\\File_conversion\\output_folder\\output_file.pdf"

# Creating an instance of Docx2PdfConverter
converter = Docx2PdfConverter(docx_path, pdf_path)

# Performing the conversion from DOCX to PDF
converter.convert_docx_to_pdf()

# Convert PDF to DOCX
pdf_path = "C:\\Users\\Pavun\\Desktop\\File_conversion\\input_folder\\sample.pdf"
docx_path = "C:\\Users\\Pavun\\Desktop\\File_conversion\\output_folder\\sample.docx"

# Creating an instance of Pdf2DocxConverter
converter = Pdf2DocxConverter(pdf_path, docx_path)

# Performing the conversion from PDF to DOCX
converter.convert_pdf_to_docx()
