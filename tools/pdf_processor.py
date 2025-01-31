from pdfminer.high_level import extract_text
import pymupdf
import os
import uuid


def extract_text_from_pdf_using_pdfminer(pdf_path: str) -> str:
    """Use this function to convert a PDF to text.

    Args:
        pdf_path (str): The path to the PDF file.

    Returns:
        str: The text contained in the PDF.
    """
    return extract_text(pdf_path)


def extract_text_from_pdf_using_pymupdf(pdf_path: str) -> str:
    """Use this function to convert a PDF to text.

    Args:
        pdf_path (str): The path to the PDF file.

    Returns:
        str: The text contained in the PDF.
    """
    doc = pymupdf.open(pdf_path)
    text = "\n".join(page.get_text() for page in doc)
    doc.close()
    return text


def create_temporary_file_from_text(pdf_content_text: str):
    """Use this function to create a randomly temporary file from text.

    Args:
        pdf_content_text (str): The text to write to the file.

    Returns:
        str: The path to the temporary file.
    """
    # Generate a random file name
    file_name = f"./text_files/{uuid.uuid4().hex}.txt"
    pdf_content_text = pdf_content_text.replace("●", "-").replace("•", "-")
    # Create and write to the file
    with open(file_name, "w", encoding="utf-8") as file:
        file.write(pdf_content_text)
    return file_name


def delete_temporary_file(file_name: str):
    """Use this function to delete a temporary file.

    Args:
        file_name (str): The path to the file.
    """
    if os.path.exists(file_name):
        os.remove(file_name)
        print(f"File '{file_name}' deleted.")
    else:
        print("File does not exist.")

