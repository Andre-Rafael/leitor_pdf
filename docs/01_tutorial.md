# Tutorial

{% include "templates/instalacao.md" %}

Se voce chegou até aqui, significa que quer aprender mais sobre o `leitor_pdf`

O objetivo desse projeto é unir diversas extrações de texto em um modulo unico

## Instalação

{% include "templates/instalacao.md" %}


## Comandos
Para extrair texto da primeira pagina do pdf
````bash
{{ commands.run }} [nome_lib] [path_do_pdf]
````

Lista as lib disponiveis para extração de texto
````bash
{{ commands.run }} list_options
'1 - pdfminer
2 - PyPDF2
3 - pdf_plumber'
````