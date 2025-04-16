def format_value(value):
    if isinstance(value, dict):
        return '[complex value]'
    if isinstance(value, str):
        return f"'{value}'"
    if isinstance(value, bool):
        return 'true' if value else 'false'
    if value is None:
        return 'null'
    return str(value)


def render_plain(diff, parent=''):
    lines = []

    for node in diff:
        key = node['key']
        full_key = f'{parent}.{key}' if parent else key

        match node['type']:
            case 'added':
                value = format_value(node['value'])
                lines.append(
                    f"Property '{full_key}' was added with value: {value}")
            case 'removed':
                lines.append(f"Property '{full_key}' was removed")
            case 'changed':
                old_value = format_value(node['old_value'])
                new_value = format_value(node['new_value'])
                lines.append(
                    f"Property '{full_key}' was updated. From {old_value} "
                    f"to {new_value}"
                )
            case 'nested':
                lines.append(render_plain(node['children'], full_key))

    return '\n'.join(lines)