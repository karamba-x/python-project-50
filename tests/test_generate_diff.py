import os
from gendiff.scripts.generate_diff import generate_diff

TEST_DIR = os.path.join(os.path.dirname(__file__), 'test_data')

def get_path(filename):
    return os.path.join(TEST_DIR, filename)

def test_identical_files():
    file1 = get_path('file1.json')
    file2 = get_path('file1.json')

    expected = '''{
    follow: false
    host: hexlet.io
    proxy: 123.234.53.22
    timeout: 50
}'''
    assert generate_diff(file1, file2) == expected

def test_diff_flat_files():
    file1 = get_path('file1.json')
    file2 = get_path('file2.json')

    expected = '''{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}'''
    assert generate_diff(file1, file2) == expected

def test_identical_yaml_files():
    file1 = get_path('file1.yml')
    file2 = get_path('file1.yml')

    expected = '''{
    follow: false
    host: hexlet.io
    proxy: 123.234.53.22
    timeout: 50
}'''
    assert generate_diff(file1, file2) == expected

def test_diff_flat_yaml_files():
    file1 = get_path('file1.yml')
    file2 = get_path('file2.yml')

    expected = '''{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}'''
    assert generate_diff(file1, file2) == expected


def test_nested_json_diff():
    file1 = get_path('nested1.json')
    file2 = get_path('nested2.json')

    expected = '''{
    common: {
      + follow: false
        setting1: Value 1
      - setting2: 200
      - setting3: true
      + setting3: null
      + setting4: blah blah
      + setting5: {
            key5: value5
        }
        setting6: {
            doge: {
              - wow: 
              + wow: so much
            }
            key: value
          + ops: vops
        }
    }
    group1: {
      - baz: bas
      + baz: bars
        foo: bar
      - nest: {
            key: value
        }
      + nest: str
    }
  - group2: {
        abc: 12345
        deep: {
            id: 45
        }
    }
  + group3: {
        deep: {
            id: {
                number: 45
            }
        }
        fee: 100500
    }
}'''

    assert generate_diff(file1, file2) == expected

def test_plain_format():
    file1 = get_path('nested1.json')
    file2 = get_path('nested2.json')

    expected = '''Property 'common.follow' was added with value: false
Property 'common.setting2' was removed
Property 'common.setting3' was updated. From true to null
Property 'common.setting4' was added with value: blah blah
Property 'common.setting5' was added with value: [complex value]
Property 'common.setting6.doge.wow' was updated. From  to so much
Property 'common.setting6.ops' was added with value: vops
Property 'group1.baz' was updated. From bas to bars
Property 'group1.nest' was updated. From [complex value] to str
Property 'group2' was removed
Property 'group3' was added with value: [complex value]'''

    assert generate_diff(file1, file2, 'plain') == expected