# Product classes
class PDFDocument:
    def __init__(self):
        self.content = ""

    def add_heading(self, heading):
        self.content += f"<h1>{heading}</h1>\n"

    def add_paragraph(self, paragraph):
        self.content += f"<p>{paragraph}</p>\n"

    def __str__(self):
        return f"PDF Document:\n{self.content}"


class HTMLDocument:
    def __init__(self):
        self.content = ""

    def add_heading(self, heading):
        self.content += f"<h1>{heading}</h1>\n"

    def add_paragraph(self, paragraph):
        self.content += f"<p>{paragraph}</p>\n"

    def __str__(self):
        return f"HTML Document:\n{self.content}"


class PlainTextDocument:
    def __init__(self):
        self.content = ""

    def add_heading(self, heading):
        self.content += f"{heading}\n"

    def add_paragraph(self, paragraph):
        self.content += f"{paragraph}\n"

    def __str__(self):
        return f"Plain Text Document:\n{self.content}"



class DocumentBuilder:
    def add_heading(self, heading):
        pass

    def add_paragraph(self, paragraph):
        pass

    def get_document(self):
        pass


# Concrete Builder for PDF Document
class PDFDocumentBuilder(DocumentBuilder):
    def __init__(self):
        self.document = PDFDocument()

    def add_heading(self, heading):
        self.document.add_heading(heading)

    def add_paragraph(self, paragraph):
        self.document.add_paragraph(paragraph)

    def get_document(self):
        return self.document


class HTMLDocumentBuilder(DocumentBuilder):
    def __init__(self):
        self.document = HTMLDocument()

    def add_heading(self, heading):
        self.document.add_heading(heading)

    def add_paragraph(self, paragraph):
        self.document.add_paragraph(paragraph)

    def get_document(self):
        return self.document


class PlainTextDocumentBuilder(DocumentBuilder):
    def __init__(self):
        self.document = PlainTextDocument()

    def add_heading(self, heading):
        self.document.add_heading(heading)

    def add_paragraph(self, paragraph):
        self.document.add_paragraph(paragraph)

    def get_document(self):
        return self.document



class DocumentGenerator:
    def __init__(self, builder):
        self.builder = builder

    def generate_document(self):
        self.builder.add_heading("Sample Document")
        self.builder.add_paragraph("This is a paragraph in the document.")
        self.builder.add_heading("Another Heading")
        self.builder.add_paragraph("Another paragraph here.")
        return self.builder.get_document()

def main():
    
    pdf_builder = PDFDocumentBuilder()
    pdf_generator = DocumentGenerator(pdf_builder)
    pdf_document = pdf_generator.generate_document()
    print(pdf_document)

    print("\n")

    
    html_builder = HTMLDocumentBuilder()
    html_generator = DocumentGenerator(html_builder)
    html_document = html_generator.generate_document()
    print(html_document)

    print("\n")

    
    plain_text_builder = PlainTextDocumentBuilder()
    plain_text_generator = DocumentGenerator(plain_text_builder)
    plain_text_document = plain_text_generator.generate_document()
    print(plain_text_document)


if __name__ == "__main__":
    main()
