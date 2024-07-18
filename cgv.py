#!/usr/bin/env python3

import requests
from urllib.parse import urlparse
import os

class PDFDownloader:

    def __init__(self, base_url, download_directory):
        self.base_url = base_url
        self.download_directory = download_directory
        self.create_directory_if_not_exists()

    def download_pdf(self, pdf_url):
        if URLParser.is_valid_url(pdf_url) and URLParser.is_pdf_url(pdf_url):
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

class URLParser:
    @staticmethod
    def is_valid_url(url):
        try:
            result = urlparse(url)
            return all([result.scheme, result.netloc])
        except ValueError:
            return False

    @staticmethod
    def is_pdf_url(url):
        return url.lower().endswith('.pdf')
