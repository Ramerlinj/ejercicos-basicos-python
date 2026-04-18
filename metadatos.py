from PyPDF2 import PdfReader

reader = PdfReader("archivo.pdf")
metadata = reader.metadata

print(metadata) 