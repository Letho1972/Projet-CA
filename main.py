#!/usr/bin/env python3

import requests
from urllib.parse import urlparse
import os
import cgv

class PDFDownloader:
    def __init__(self, base_url, download_directory):
        self.base_url = base_url
        self.download_directory = download_directory
        self.create_directory_if_not_exists()

    def download_pdf(self, pdf_url):
        if cgv.URLParser.is_valid_url(pdf_url) and cgv.URLParser.is_pdf_url(pdf_url):
            response = requests.get(pdf_url)
            if response.status_code == 200:
                filename = self.get_filename_from_url(pdf_url)
                filepath = os.path.join(self.download_directory, filename)
                with open(filepath, 'wb') as f:
                    f.write(response.content)
                print(f'Téléchargé: {filepath}')
            else:
                print(f'Échec du téléchargement: {pdf_url}')
        else:
            print(f'URL invalide ou ce n\'est pas un PDF: {pdf_url}')

    def download_multiple_pdfs(self, pdf_urls):
        for url in pdf_urls:
            self.download_pdf(url)

    def create_directory_if_not_exists(self):
        if not os.path.exists(self.download_directory):
            os.makedirs(self.download_directory)

    def get_filename_from_url(self, url):
        parsed_url = urlparse(url)
        return os.path.basename(parsed_url.path)

def main():
    base_url = "https://example.com/pdfs/"
    download_dir = "download_pdfs"

    downloader = PDFDownloader(base_url, download_dir)

    # Exemple d'utilisation
    pdf_url = "https://portail-lcl-web.cdn.prismic.io/portail-lcl-web/69f061a4-8d2c-4b48-9639-be9079d2feb5_LCL_+Document+Information+Tarifaire_01+01+2024+.pdf"
    downloader.download_pdf(pdf_url)

    # Exemple avec plusieurs PDFs
    pdf_urls = [
        "https://example.com/pdfs/doc1.pdf",
        "https://example.com/pdfs/doc2.pdf",
        "https://example.com/pdfs/doc3.pdf"
    ]
    downloader.download_multiple_pdfs(pdf_urls)

if __name__ == "__main__":
    main()
