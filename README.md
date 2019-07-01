# PDF Table to Markdown Converter

To convert tables in pdf files to markdown, run:

`python pdf-tables-to-markdown.py '<FILEPATH>/<FILENAME>.pdf'`

or pass a directory as variable to convert all pdf files within the directory:

`python pdf-tables-to-markdown.py '<FILEPATH>/<DIRECTORY>'`

or pass two directories to convert all pdf files from the first directory to the second:

`python pdf-tables-to-markdown.py '<FILEPATH>/<DIRECTORY>' '<FILEPATH>/<DIRECTORY>'`

---

Output file will be saved to `<FILEPATH>/<FILENAME>/tables/table_<TABLENUMBER>.md`,
or `<SECOND_DIR>/<FILENAME>_table_<TABLENUMBER>.md`. 
Each table found in the pdf will be saved to a separate file.
