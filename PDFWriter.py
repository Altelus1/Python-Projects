#PDFWriter v1.0

"""
Can Only write texts in an existing PDF using reportlab and PyPDF2
"""

#PyPDFeditor.py v1.0

from reportlab.pdfgen import canvas
import io
from PyPDF2 import PdfFileWriter, PdfFileReader

class PDF_Plate:
	
	def __init__(self, existing_pdf_filename, saving_pdf_filename):
		self.existing_pdf_filename = existing_pdf_filename
		self.saving_pdf_filename = saving_pdf_filename
		self.io_plate = io.BytesIO()
		self.canv_plate = canvas.Canvas(self.io_plate)
		
	def write_to_plate(self, pos_x, pos_y, string):
		self.canv_plate.drawString(pos_x, pos_y, string)
		
	def set_font_style(self, font_name):
		pass
		
	def save_plate(self):
		self.canv_plate.save()
		self.io_plate.seek(0)
		self.output_pdf = PdfFileReader(self.io_plate)
		self.input_pdf = PdfFileReader(open(self.existing_pdf_filename,"rb"))
		self.writer = PdfFileWriter()
		self.page = self.output_pdf.getPage(0)
		self.page.mergePage(self.input_pdf.getPage(0))
		self.writer.addPage(self.page)
		self.outputStream = open(self.saving_pdf_filename,"wb")
		self.writer.write(self.outputStream)
		self.outputStream.close()
		
















