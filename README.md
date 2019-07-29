# PDF Table to Markdown Converter

This is a wrapper around the [Python Camelot library](https://camelot-py.readthedocs.io/en/master/) which converts tables in PDF to markdown.

Please install [Ghostscript](https://camelot-py.readthedocs.io/en/master/user/install-deps.html#for-ghostscript), 
a Camelot dependency.

<br>

#### Convert one PDF file to markdown

`> python table_to_markdown.py '<FILEPATH>/<FILENAME>.pdf'`

Markdown tables will be saved to `<FILEPATH>/<FILENAME>_table_<TABLENUMBER>.md`

<br>

#### Convert all PDF files in directory to markdown

`> python table_to_markdown.py '<FILEPATH>/<DIRECTORY_NAME>'`

Markdown tables will be saved to `<FILEPATH>/<DIRECTORY_NAME>/<FILENAME>_table_<TABLENUMBER>.md`

<br>

#### Convert all PDF files in directory to markdown and save to specific location: 

`> python table_to_markdown.py '<FILEPATH>/<DIRECTORY_NAME>' '<SECOND_FILEPATH>/<DIRECTORY_NAME>'`

Markdown tables will be saved to `<SECOND_FILEPATH>/<DIRECTORY_NAME>/<FILENAME>_table_<TABLENUMBER>.md`

