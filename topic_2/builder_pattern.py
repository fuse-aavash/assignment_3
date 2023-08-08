from abc import ABC, abstractmethod

# Base class for documents
class Document(ABC):
    """Abstract Base Class for representing different types of documents."""

    def __init__(self):
        self.content = ""

    @abstractmethod
    def add_heading(self, heading: str):
        """Add a heading to the document."""
        pass

    @abstractmethod
    def add_paragraph(self, paragraph: str):
        """Add a paragraph to the document."""
        pass

    def __str__(self):
        return f"{self.__class__.__name__}:\n{self.content}"


class PDFDocument(Document):
    """Represents a PDF document."""

    def add_heading(self, heading: str):
        self.content += f"<h1>{heading}</h1>\n"

    def add_paragraph(self, paragraph: str):
        self.content += f"<p>{paragraph}</p>\n"


class HTMLDocument(Document):
    """Represents an HTML document."""

    def add_heading(self, heading: str):
        self.content += f"<h1>{heading}</h1>\n"

    def add_paragraph(self, paragraph: str):
        self.content += f"<p>{paragraph}</p>\n"


class PlainTextDocument(Document):
    """Represents a plain text document."""

    def add_heading(self, heading: str):
        self.content += f"{heading}\n"

    def add_paragraph(self, paragraph: str):
        self.content += f"{paragraph}\n"


class DocumentGenerator:
    """Generates different types of documents using a given builder."""

    def __init__(self, builder: Document):
        self.builder = builder

    def generate_document(self):
        """Generate the document using the provided builder."""
        self.builder.add_heading("Sample Document")
        self.builder.add_paragraph("This is a paragraph in the document.")
        self.builder.add_heading("Another Heading")
        self.builder.add_paragraph("Another paragraph here.")
        return self.builder


def main():
    """ Main function """
    pdf_builder = PDFDocument()
    pdf_generator = DocumentGenerator(pdf_builder)
    pdf_document = pdf_generator.generate_document()
    print(pdf_document)

    print("\n")

    html_builder = HTMLDocument()
    html_generator = DocumentGenerator(html_builder)
    html_document = html_generator.generate_document()
    print(html_document)

    print("\n")

    plain_text_builder = PlainTextDocument()
    plain_text_generator = DocumentGenerator(plain_text_builder)
    plain_text_document = plain_text_generator.generate_document()
    print(plain_text_document)


if __name__ == "__main__":
    main()
