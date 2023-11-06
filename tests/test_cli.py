from pytest import mark
from typer.testing import CliRunner

from leitor_pdf.cli import app

runner = CliRunner()


def test_leitor_pdf_deve_retornar_0_ao_stdout():
    # command: str = 'read_file'
    arquivo = r'C:\Users\proc\GitHub\leitor_pdf\tests\file_test\helloworld.pdf'
    tipo_leitura: str = 'pdfminer'
    result = runner.invoke(app, [tipo_leitura, arquivo])
    assert result.exit_code == 2


@mark.parametrize('tipo_leitor', ['pdfminer', 'PyPDF2', 'pdf_plumber'])
def test_leitor_pdf_cli_leu_o_arquivo(tipo_leitor):
    command = 'read_file'
    path = r'C:\Users\proc\GitHub\leitor_pdf\tests\file_test\helloworld.pdf'
    result = runner.invoke(app, [tipo_leitor, path])
    assert result.stdout.strip()
