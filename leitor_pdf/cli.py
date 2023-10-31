from rich.console import Console
from typer import Argument, Typer

from leitor_pdf.main import LeitorPdf

console = Console()
app = Typer()


leitor = LeitorPdf()


@app.command()
def leitor_pdf(
    tipo_leitor: str = Argument(
        'pdfminer', help='Lib usada para extrair texto'
    ),
    path: str = Argument(
        '/helloworld.pdf', help='path do pdf que terá o texto extraído'
    ),
):
    print(leitor.extract_text_from_file(path, True, tipo_leitor, 0))


@app.command('list_options')
def leitor_pdf():
    for index, opcao in enumerate(leitor.opcoes_de_extracao, 1):
        print('{} - {}'.format(index, opcao))
