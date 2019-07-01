# PDF Table to Markdown Converter

This is a wrapper around the [Python Camelot library](https://camelot-py.readthedocs.io/en/master/) which converts tables in PDF to markdown.

<br>

#### Convert one PDF file to markdown

`> python pdf-tables-to-markdown.py '<FILEPATH>/<FILENAME>.pdf'`

Markdown tables will be saved to `<FILEPATH>/<FILENAME>/tables/table_<TABLENUMBER>.md`

<br>

#### Convert all PDF files in directory to markdown

`> python pdf-tables-to-markdown.py '<FILEPATH>/<DIRECTORY>'`

Markdown tables will be saved to `<FILEPATH>/<FILENAME>/tables/table_<TABLENUMBER>.md`

<br>

To specify output location: 

`> python pdf-tables-to-markdown.py '<FILEPATH>/<DIRECTORY>' '<SECOND_FILEPATH>/<SECOND_DIRECTORY>'`

Markdown tables will be saved to `<SECOND_FILEPATH>/<SECOND_DIRECTORY>/<FILENAME>_table_<TABLENUMBER>.md`
