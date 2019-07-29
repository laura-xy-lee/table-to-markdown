#!/usr/bin/env python3
import sys
import os
from typing import Text

import camelot
from tabulate import tabulate


def convert_tables_to_md(pdf_file_name: Text, input_root_dir: Text):
    """Convert pdf table to markdown and save as markdown file."""

    filename = os.path.splitext(pdf_file_name)[0]
    print('Converting', pdf_file_name, '...')

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

        (input_dir, input_file) = os.path.split(filename)
        output_dir = os.path.join(sys.argv[2], os.path.relpath(input_dir, input_root_dir)) if len(sys.argv) == 3 else None
        output_file_suffix = 'table_' + str(i) + '.md'
        output_file_path = (os.path.join(output_dir, input_file + '_' + output_file_suffix)
                            if output_dir is not None
                            else os.path.join(filename, 'tables', output_file_suffix))

        print('Saving table', str(output_file_path) + '...')

        # Create output directories
        if output_dir is None:
            if not os.path.exists(filename):
                os.makedirs(filename)
            if not os.path.exists(os.path.join(filename, 'tables')):
                os.makedirs(os.path.join(filename, 'tables'))
        else:
            if not os.path.exists(output_dir):
                os.makedirs(output_dir)

        # Save tables
        with open(output_file_path, 'w') as md_file:
            md_file.write(md)


def is_pdf(filename: Text) -> bool:
    """Check if file is pdf based on file name."""
    return os.path.splitext(filename)[1] == '.pdf'


user_input = sys.argv[1]

if is_pdf(user_input):
    try:
        convert_tables_to_md(pdf_file_name=user_input)
    except:
        print('[ERROR] Conversion failed for', user_input)
else:
    for subdir, dirs, files in os.walk(user_input):
        for file in files:
            file_name = os.path.join(subdir, file)
            if is_pdf(filename=file_name):
                try:
                    convert_tables_to_md(pdf_file_name=file_name, input_root_dir=user_input)
                except:
                    print('[ERROR] Conversion failed for', file_name)