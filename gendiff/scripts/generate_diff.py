from gendiff.scripts.parsers import parse_data

def generate_diff(file_path1, file_path2):
    dict1 = parse_data(file_path1)
    dict2 = parse_data(file_path2)

    all_keys = sorted(set(dict1.keys()) | set(dict2.keys()))
    lines = ['{']

    for key in all_keys:
        if key in dict1 and key not in dict2:
            lines.append(f"  - {key}: {dict1[key]}")
        elif key not in dict1 and key in dict2:
            lines.append(f"  + {key}: {dict2[key]}")
        elif dict1[key] != dict2[key]:
            lines.append(f"  - {key}: {dict1[key]}")
            lines.append(f"  + {key}: {dict2[key]}")
        else:
            lines.append(f"    {key}: {dict1[key]}")

    lines.append('}')
    return '\n'.join(lines)
