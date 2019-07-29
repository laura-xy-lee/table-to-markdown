"""Unit tests for table_to_markdown module"""

import subprocess
import os
import uuid
import shutil


def create_tmp_dir(root_dir=None,
                   prefix='tmpdir'):
    dirName = prefix + '_' + uuid.uuid4().__str__()
    if root_dir:
        dirName = os.path.join(root_dir, dirName)

    try:
        os.mkdir(dirName)
    except FileExistsError:
        print("Directory ", dirName, " already exists")
        exit()  # Exit test script if tmp directory already exists
    return dirName


def test_convert_pdf_file():
    # Create tmp directory
    dirName = create_tmp_dir(prefix='tmpdir1')

    # Copy test.pdf to tmp directory
    shutil.copyfile('tests/test.pdf', os.path.join(dirName, 'test.pdf'))

    bashCommand = "python table_to_markdown.py " + os.path.join(dirName, "test.pdf")
    subprocess.check_output(bashCommand.split())

    # Check that md file has been created
    assert os.path.exists(os.path.join(dirName, 'test_table_0.md'))

    # Remove tmp directory
    shutil.rmtree(dirName)


def test_convert_pdf_nested_dir():
    # Create tmp directory
    dirName = create_tmp_dir(prefix='tmpdir2')

    # Create two tmp subdir
    path_to_subdirName_1 = create_tmp_dir(root_dir=dirName)
    path_to_subdirName_2 = create_tmp_dir(root_dir=dirName)

    # Create subdir in subdir1
    path_to_subsubdirName_1 = create_tmp_dir(root_dir=path_to_subdirName_1, prefix='subsubdir1')

    # Copy test.pdf to subdir
    shutil.copyfile('tests/test.pdf', os.path.join(path_to_subdirName_1, 'test.pdf'))
    shutil.copyfile('tests/test.pdf', os.path.join(path_to_subdirName_2, 'test.pdf'))
    shutil.copyfile('tests/test.pdf', os.path.join(path_to_subsubdirName_1, 'test.pdf'))

    bashCommand = "python table_to_markdown.py " + dirName
    subprocess.check_output(bashCommand.split())

    # Check that md files have been created
    assert os.path.exists(os.path.join(path_to_subdirName_1, 'test_table_0.md'))
    assert os.path.exists(os.path.join(path_to_subdirName_2, 'test_table_0.md'))
    assert os.path.exists(os.path.join(path_to_subsubdirName_1, 'test_table_0.md'))

    # Remove tmp directory
    shutil.rmtree(dirName)


def test_convert_pdf_nested_dir_to_specific_dir():
    # Create tmp directory
    dirName = create_tmp_dir(prefix='tmpdir3')

    # Create two tmp subdir
    path_to_subdirName_1 = create_tmp_dir(root_dir=dirName, prefix='subdir1')
    path_to_subdirName_2 = create_tmp_dir(root_dir=dirName, prefix='subdir2')

    # Create subdir in subdir1
    path_to_subsubdirName_1 = create_tmp_dir(root_dir=path_to_subdirName_1, prefix='subsubdir1')

    # Copy test.pdf to subdir
    shutil.copyfile('tests/test.pdf', os.path.join(path_to_subdirName_1, 'test.pdf'))
    shutil.copyfile('tests/test.pdf', os.path.join(path_to_subdirName_2, 'test.pdf'))
    shutil.copyfile('tests/test.pdf', os.path.join(path_to_subsubdirName_1, 'test.pdf'))

    output_dirName = 'output_' + uuid.uuid4().__str__()
    bashCommand = "python table_to_markdown.py " + dirName + ' ' + output_dirName
    subprocess.check_output(bashCommand.split())

    # Check that md files have been created
    subdir1 = os.path.join(*os.path.split(path_to_subdirName_1)[1:])
    subdir2 = os.path.join(*os.path.split(path_to_subdirName_2)[1:])
    subsubdir1 = os.path.join(*path_to_subsubdirName_1.split(os.sep)[1:])
    assert os.path.exists(os.path.join(output_dirName, subdir1, 'test_table_0.md'))
    assert os.path.exists(os.path.join(output_dirName, subdir2, 'test_table_0.md'))
    assert os.path.exists(os.path.join(output_dirName, subsubdir1, 'test_table_0.md'))

    # Remove tmp directory
    shutil.rmtree(dirName)
    shutil.rmtree(output_dirName)
