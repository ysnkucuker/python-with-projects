from pdf2docx import Converter

# Path of the source PDF file
pdf_path = "sample.pdf"

# Path where the converted DOCX file will be saved
docx_path = "sample.docx"

# Create a Converter object with the PDF file
cv = Converter(pdf_path)

# Convert the PDF to DOCX format
cv.convert(docx_path)

# Close the converter and release resources
cv.close()
