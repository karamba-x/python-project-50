import os
from gendiff.scripts.generate_diff import generate_diff

TEST_DIR = os.path.join(os.path.dirname(__file__), 'test_data')

def get_path(filename):
    return os.path.join(TEST_DIR, filename)

def test_identical_files():
    file1 = get_path('file1.json')
    file2 = get_path('file1.json')

    expected = '''{
    follow: False
    host: hexlet.io
    proxy: 123.234.53.22
    timeout: 50
}'''
    assert generate_diff(file1, file2) == expected

def test_diff_flat_files():
    file1 = get_path('file1.json')
    file2 = get_path('file2.json')

    expected = '''{
  - follow: False
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: True
}'''
    assert generate_diff(file1, file2) == expected