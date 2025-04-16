

def format_value(value):
    """
    Форматирует значение для вывода в формате JSON.
    Если это сложная структура (словарь), возвращается строка '[complex value]'.
    """
    if isinstance(value, dict):
        return '[complex value]'
    if isinstance(value, bool):
        return 'true' if value else 'false'
    if value is None:
        return 'null'
    return value


def render_json(diff):
    """
    Рендерит различия в формате JSON.
    """
    result = []

    for node in diff:
        key = node['key']
        property_diff = {"key": key}

        match node['type']:
            case 'added':
                property_diff["status"] = "added"
                property_diff["value"] = format_value(node['value'])
            case 'removed':
                property_diff["status"] = "removed"
            case 'changed':
                property_diff["status"] = "changed"
                property_diff["old_value"] = format_value(node['old_value'])
                property_diff["new_value"] = format_value(node['new_value'])
            case 'nested':
                property_diff["status"] = "nested"
                property_diff["children"] = render_json(node['children'])

        result.append(property_diff)

    return result