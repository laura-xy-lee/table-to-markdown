# PDF Table to Markdown Converter

To convert tables in pdf files to markdown, run:

`python pdf-tables-to-markdown.py '<FILEPATH>/<FILENAME>.pdf'`

or pass a directory as variable to convert all pdf files within the directory:

`python pdf-tables-to-markdown.py '<FILEPATH>/<DIRECTORY>'`

---

Output file will be saved to `<FILEPATH>/<FILENAME>_<TABLENUMBER>.md`. 
Each table found in the pdf will be saved to a separate file.
