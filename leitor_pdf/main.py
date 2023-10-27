from typing import List, Union, Tuple
from re import sub
from io import BufferedReader
from pathlib import Path

import PyPDF2
from PyPDF2 import PageObject
from pdfminer.high_level import extract_text
from unidecode import unidecode
import pdfplumber


class LeitorPdf:
    

    @property.getter
    def opcoes_de_extracao(self) -> Tuple[str]:
        """str: Opções de biblioteca para extrair o texto."""
        return ('PyPDF2', 'pdfminer', 'pdf_plumber',)


    def __clean_text(self, text: str) -> str:
        """
        Remove caracteres especiais do texto, acentuação, quebra de linha, cifrão, reduz espaçamento para um e deixa o texto minusculo

        Args:
            text: Texto que terá os caracteres removido.

        Returns:
            texto limpo
        """
        sem_acento: str = unidecode(text)
        sem_quebra_de_linha: str = sem_acento.replace('\n', '')
        tudo_minusculo: str = sem_quebra_de_linha.lower()
        unico_espacamento: str = sub(r'\s+', ' ', tudo_minusculo)
        sem_cifrao: str = sub(r'r\$', '', unico_espacamento)
        return sem_cifrao
    

    def extract_text_with_pypdf2(self, file_opened: BufferedReader, page_number: int = None) -> str:
        """
        Extrai texto do PDF usando o lib PyPDF2

        Args:
            file_opened: path do pdf que terá o texto extraido
            page_number: caso deseje extrair uma pagina especifica, informar o numero, caso contrario o texto do PDF o texto do pdf todo

        Returns:
            texto do PDF

        Examples:
            >>> leitor = LeitorPdf()
            >>> leitor.extract_text_with_pypdf2('/bar/foo/test.pdf', 0)
            "O texto presente no PDF"
        """
        text_in_document: List[str] = []
        pdf_reader = PyPDF2.PdfFileReader(file_opened)
        if not page_number:
            page_number = pdf_reader.numPages

        for i in range(page_number):
            page_obj: PageObject = pdf_reader.getPage(i)
            text_in_document.append(page_obj.extractText())
        all_text = ' '.join(text_in_document)

        return all_text
    

    def extract_text_with_pdfminer_high_level(self, file_opened: BufferedReader, page_number: List[int] = None) -> str:
        """
        Extrai texto do PDF usando a lib pdfminer

        Args:
            file_opened: path do pdf que terá o texto extraido
            page_number: caso deseje extrair uma pagina especifica, informar o numero, caso contrario o texto do PDF o texto do pdf todo

        Returns:
            texto do PDF

        Examples:
            >>> leitor = LeitorPdf()
            >>> leitor.extract_text_with_pdfminer_high_level('/bar/foo/test.pdf', [0])
            "o texto presente no pdf"
        """
        return extract_text(file_opened, page_numbers=page_number)

    
    def extract_text_with_pdfplumber(self, file_opened: BufferedReader, page_number: List[int] = None) -> str:
        """
        Extrai texto do PDF usando a lib pdfplumber

        Args:
            file_opened: path do pdf que terá o texto extraido
            page_number: caso deseje extrair uma pagina especifica, informar o numero, caso contrario o texto do PDF o texto do pdf todo

        Returns:
            texto do PDF

        Examples:
            >>> leitor = LeitorPdf()
            >>> leitor.extract_text_with_pdfplumber('/bar/foo/test.pdf', [0])
            "o texto presente no pdf"
        """
        text = ''
        with pdfplumber.open(path_or_fp=file_opened, pages=page_number) as pdf:
            for page in pdf.pages:
                text += page.extract_text()
        return text
    
    
    def extract_text(self, file: BufferedReader, clean_text: bool, lib: str, page_number: int = None) -> str:
        """
        Extrai texto do PDF

        Args:
            file: arquivo que terá o texto extraído
            clean_text: se o texto sairá limpo (sem acento, espaco unico, texto em minusculo)
            lib: modo de extração de texto do PDF
            page_number: caso deseje extrair uma pagina especifica, informar o numero, caso contrario o texto do PDF o texto do pdf todo

        Returns:
            texto do PDF

        Examples:
            >>> leitor = LeitorPdf()
            >>> leitor.extract_text('/bar/foo/test.pdf', True, 'PyPDF2', 0)
            "o texto presente no pdf"
            >>> leitor.extract_text('/bar/foo/test.pdf', False, 'pdfminer')
            "O texto presente no PDF"
        """
        if lib == 'PyPDF2':
            text: str = self.extract_text_with_pypdf2(file, page_number)
        elif lib == 'pdfminer':
            text: str = self.extract_text_with_pdfminer_high_level(file, [page_number])
        elif lib == 'pdf_plumber':
            text: str = self.extract_text_with_pdfplumber(file, [page_number])
        else:
            raise Exception('Nenhuma opção válida foi escolhida')

        return self.__clean_text(text) if clean_text else text