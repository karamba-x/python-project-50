def format_value(value, depth):
    indent = '    ' * (depth + 1)

    if isinstance(value, dict):
        lines = []
        for k, v in value.items():
            lines.append(f"{indent}{k}: {format_value(v, depth + 1)}")
        closing_indent = '    ' * depth
        return f"{{\n{chr(10).join(lines)}\n{closing_indent}}}"

    if isinstance(value, bool):
        return 'true' if value else 'false'
    if value is None:
        return 'null'
    return str(value)


def render_stylish(diff, depth=0):
    lines = []
    indent_size = 4
    indent = ' ' * (depth * indent_size)

    for node in diff:
        key = node['key']
        match node['type']:
            case 'added':
                lines.append(f"{indent}  + {key}: "
                             f"{format_value(node['value'], depth + 1)}")
            case 'removed':
                lines.append(f"{indent}  - {key}: "
                             f"{format_value(node['value'], depth + 1)}")
            case 'unchanged':
                lines.append(f"{indent}    {key}: "
                             f"{format_value(node['value'], depth + 1)}")
            case 'changed':
                lines.append(f"{indent}  - {key}: "
                             f"{format_value(node['old_value'], depth + 1)}")
                lines.append(f"{indent}  + {key}: "
                             f"{format_value(node['new_value'], depth + 1)}")
            case 'nested':
                children = render_stylish(node['children'], depth + 1)
                lines.append(f"{indent}    {key}: {{\n"
                             f"{children}\n{indent}    }}")

    return '\n'.join(lines)