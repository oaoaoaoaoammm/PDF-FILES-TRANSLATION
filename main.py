import os
import fitz  # PyMuPDF
from deep_translator import GoogleTranslator

def translate_text(text, dest_language):
    """
    Translate the given text to the specified language.
    :param text: The text to be translated.
    :param dest_language: The target language for translation.
    :return: Translated text.
    """
    try:
        translator = GoogleTranslator(source='auto', target=dest_language)
        translated =  translator.translate(text)
        print(translated)
        return translated
    except Exception as e:
        print(f"\n\nError translating text '{text}': {e}\n\n")
        return text

def is_numeric(text):
    """
    Check if the given text is numeric.
    :param text: The text to check.
    :return: True if the text is numeric, False otherwise.
    """
    return text.replace('.', '', 1).isdigit()

def translate_pdf_text(pdf_path, output_path, dest_language, font_path):
    """
    Translate the text in the PDF file while preserving the structure and layout.
    :param pdf_path: Path to the original PDF file.
    :param output_path: Path to save the translated PDF file.
    :param dest_language: Target language for translation.
    """
    doc = fitz.open(pdf_path)
    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        blocks = page.get_text("dict")["blocks"]

        for block in blocks:
            if block["type"] == 0:  # Check if it's a text block
                for line in block["lines"]:
                    for span in line["spans"]:
                        original_text = span["text"].strip()
                        if is_numeric(original_text):
                            continue  # Skip numeric text blocks

                        translated_text = translate_text(original_text, dest_language)
                        rect = fitz.Rect(span["bbox"])  # Get the coordinates of the text span
                        font_size = span["size"]

                        # Draw a white rectangle to cover the old text
                        page.draw_rect(rect, color=(1, 1, 1), fill=(1, 1, 1))

                        # Insert the new text at the same coordinates
                        try:
                            if font_path:
                                page.insert_text(rect.tl, translated_text, fontsize=font_size, fontfile=font_path, fontname="china-ss")
                            else:
                                page.insert_text(rect.tl, translated_text, fontsize=font_size, fontname="helv")
                        except Exception as e:
                            print(f"\n\nError inserting text '{translated_text}': {e}\n\n")

    doc.save(output_path, garbage=3, deflate=True)
    doc.close()

def translate_pdf_files_in_folder(folder_path, dest_language, font_path):
    """
    Translate all PDF files in the specified folder.
    :param folder_path: Path to the folder containing PDF files.
    :param dest_language: Target language for translation.
    """
    output_folder = os.path.join(folder_path, "translated_pdfs")
    os.makedirs(output_folder, exist_ok=True)

    for filename in os.listdir(folder_path):
        if filename.endswith(".pdf"):
            pdf_path = os.path.join(folder_path, filename)
            translated_filename = translate_text(filename.replace(".pdf", ""), dest_language) + ".pdf"
            output_path = os.path.join(output_folder, translated_filename)

            translate_pdf_text(pdf_path, output_path, dest_language, font_path)
            print(f"\n\n Translated {filename} to {translated_filename} \n\n")

# Example usage
folder_path = "./pdf_files"
translate_pdf_files_in_folder(folder_path, dest_language="zh-CN", font_path="./fonts/NotoSansSC-Light.ttf")