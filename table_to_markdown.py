#!/usr/bin/env python3
import sys
import os
from typing import Text

import camelot
from tabulate import tabulate


def convert_tables_to_md(pdf_file_name: Text,
                         output_dir: Text = None,
                         input_root_dir: Text = None):  # TODO: what does this do?
    """Convert pdf table to markdown and save as markdown file."""
    print('Converting', pdf_file_name, '...')
    pdf_file_name_without_ext = os.path.splitext(pdf_file_name)[0]

    # Use Camelot to extract tables
    tables = camelot.read_pdf(pdf_file_name,
                              pages='all')

    for i in range(len(tables)):
        df = tables[i].df

        # Get table headers
        new_header = df.iloc[0]  # grab the first row for the header
        new_header = [h.replace('\n', '') for h in new_header]  # replace newlines if any
        new_header = ['&#xfeff;' if len(h) == 0 else h for h in new_header]  # replace all empty spaces with zero width non breaking space
        df = df[1:]  # take the data less the header row
        df.columns = new_header  # set the header row as the df header

        # Remove newlines and empty cells within table if any
        df = df.replace('\n', ' ', regex=True)
        df = df.replace('', '&#xfeff;', regex=True)

        # Convert table to markdown
        md = tabulate(df, tablefmt='github', headers='keys', showindex=False) + '\n'

        # Get output file path
        (input_dir, input_file) = os.path.split(pdf_file_name_without_ext)
        output_file_suffix = 'table_' + str(i) + '.md'
        if output_dir:
            # Create output dir
            if not os.path.exists(output_dir):
                os.makedirs(output_dir)

            # Create output subdir
            subdir = os.path.join(*input_dir.split(os.sep)[1:])
            subdir_path = os.path.join(output_dir, subdir)
            if not os.path.exists(subdir_path):
                os.makedirs(subdir_path)

            output_file_path = os.path.join(subdir_path, input_file + '_' + output_file_suffix)
        else:
            output_file_path = os.path.join(input_dir, input_file + '_' + output_file_suffix)

        # Save tables
        print('Saving table', str(output_file_path) + '...')
        with open(output_file_path, 'w') as md_file:
            md_file.write(md)


def is_pdf(filename: Text) -> bool:
    """Check if file is pdf based on file name."""
    return os.path.splitext(filename)[1] == '.pdf'


# Get user input
user_input_pdf_path = sys.argv[1]
user_output_md_path = sys.argv[2] if len(sys.argv) == 3 else None

if is_pdf(user_input_pdf_path):
    try:
        convert_tables_to_md(pdf_file_name=user_input_pdf_path)
    except:
        print('[ERROR] Conversion failed for', user_input_pdf_path)
else:
    for subdir, dirs, files in os.walk(user_input_pdf_path):
        for file in files:
            file_name = os.path.join(subdir, file)
            if is_pdf(filename=file_name):
                try:
                    convert_tables_to_md(pdf_file_name=file_name, output_dir=user_output_md_path)  # input_root_dir=user_input_pdf_path) TODO: what does this do
                except:
                    print('[ERROR] Conversion failed for', file_name)
