from gendiff.parser import parse_data
from gendiff.diff.builder import build_diff
from gendiff.diff.formatter.stylish import render_stylish

def generate_diff(file_path1, file_path2, format_name='stylish'):
    data1 = parse_data(file_path1)
    data2 = parse_data(file_path2)

    diff = build_diff(data1, data2)

    if format_name == 'stylish':
        return '{\n' + render_stylish(diff) + '\n}'
    else:
        raise ValueError(f"Unknown format: {format_name}")