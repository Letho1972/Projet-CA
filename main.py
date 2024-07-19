#!/usr/bin/env python3

import requests
from urllib.parse import urlparse
import os
from cgv import PDFDownloader


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
