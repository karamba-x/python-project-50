from gendiff.diff.formatter.plain import render_plain
from gendiff.diff.formatter.stylish import render_stylish
from gendiff.diff.formatter.json import render_json
from gendiff.parser import parse_data
from gendiff.diff.builder import build_diff
import json

def generate_diff(file_path1, file_path2, format_name='stylish'):
    data1 = parse_data(file_path1)
    data2 = parse_data(file_path2)

    diff = build_diff(data1, data2)

    if format_name == 'stylish':
        return '{\n' + render_stylish(diff) + '\n}'
    elif format_name == 'plain':
        return render_plain(diff)
    elif format_name == 'json':
        return json.dumps(render_json(diff), indent=2)
    else:
        raise ValueError(f"Unknown format: {format_name}")