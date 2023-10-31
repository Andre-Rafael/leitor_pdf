from pytest import mark
from typer.testing import CliRunner

from leitor_pdf.cli import app

runner = CliRunner()


def test_leitor_pdf_deve_retornar_0_ao_stdout():
    arquivo = r'C:\Users\proc\GitHub\leitor_pdf\tests\file_test\helloworld.pdf'
    tipo_leitura = 'pdfminer'
    result = runner.invoke(app, [tipo_leitura, arquivo])
    assert result.exit_code == 0


@mark.parametrize('tipo_leitor', ['pdfminer', 'PyPDF2', 'pdf_plumber'])
def test_leitor_pdf_cli_leu_o_arquivo(tipo_leitor):
    arquivo = r'C:\Users\proc\GitHub\leitor_pdf\tests\file_test\helloworld.pdf'
    result = runner.invoke(app, [tipo_leitor, arquivo])
    assert result.stdout
