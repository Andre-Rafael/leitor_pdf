"""
AAA - 3A - A3

Arrange - Act - Assets!
Arrumar - Agir - Garantir!
"""
from pathlib import Path

from pytest import raises

from leitor_pdf.exceptions import InvalidOptionException, TheFileIsnPdf
from leitor_pdf.main import LeitorPdf

leitor = LeitorPdf()


def test_leitor_pdfplumber():
    # Arrumar
    BASE_DIR = Path(__file__).resolve().parent.parent
    file = Path(BASE_DIR, 'tests', 'file_test', 'helloworld.pdf')

    # Act - Chamo o que testar
    with open(file, 'rb') as file_opened:
        result = leitor._extract_text_with_pdfminer_high_level(
            file_opened, [0]
        )

    # Assets
    assert result


def test_arq_nao_pdf():
    BASE_DIR = Path(__file__).resolve().parent.parent
    file = Path(BASE_DIR, 'tests', 'file_test', 'helloworld.txt')

    with raises(TheFileIsnPdf) as error:
        text = leitor.extract_text_from_file(file, True, 'PyPDF2', 0)

    message_error = 'O arquivo enviado nao é um pdf'
    assert error.value.args[0] == message_error


def test_opcao_invalida():
    BASE_DIR = Path(__file__).resolve().parent.parent
    file = Path(BASE_DIR, 'tests', 'file_test', 'helloworld.pdf')

    with raises(InvalidOptionException) as error:
        text = leitor.extract_text_from_file(file, True, 'PyPDF5', 0)

    error_message = 'Opção invalida'
    assert error.value.args[0] == error_message
