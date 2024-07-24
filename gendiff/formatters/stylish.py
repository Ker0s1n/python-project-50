def exception_format_stylish(value):
    """
    Returns a variable after handling an exception.
    """
    if isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return 'null'
    elif type(value) is int:
        return value
    else:
        return str(value)


def make_value_for_stylish(key, val, function, deep_indent_size, deep_indent):
    """
    Returns data characterizing the passed key
    and the variable it contains as a list.
    """
    string = []
    match val.get('type'):
        case 'unchanged':
            indent = '  '
            string.append(
                f'\n{deep_indent}{indent}{key}: '
                f'{function(val["value"], deep_indent_size)}'
            )
        case 'changed':
            indent = '- '
            string.append(
                f'\n{deep_indent}{indent}{key}: '
                f'{function(val["old_value"], deep_indent_size)}'
            )
            indent = '+ '
            string.append(
                f'\n{deep_indent}{indent}{key}: '
                f'{function(val["new_value"], deep_indent_size)}'
            )
        case 'nested':
            indent = '  '
            string.append(
                f'\n{deep_indent}{indent}{key}: '
                f'{function(val["value"], deep_indent_size)}'
            )
        case 'deleted':
            indent = '- '
            string.append(
                f'\n{deep_indent}{indent}{key}: '
                f'{function(val["value"], deep_indent_size)}'
            )
        case 'added':
            indent = '+ '
            string.append(
                f'\n{deep_indent}{indent}{key}: '
                f'{function(val["value"], deep_indent_size)}'
            )
        case None:
            indent = '  '
            string.append(
                f'\n{deep_indent}{indent}{key}: '
                f'{function(val, deep_indent_size)}'
            )
    return string


def stylish(node, depth: int = 0, replacer: str = ' ', spaces_count: int = 4):
    """
    Returns data about the dictionary of changes
    in the form of a structured list of changes.
    """
    if not isinstance(node, dict):
        return exception_format_stylish(node)

    deep_indent_size = depth + spaces_count
    deep_indent = replacer * (deep_indent_size - 2)
    current_indent = replacer * depth

    result = ['{']
    for key, val in node.items():
        if isinstance(val, dict):
            result.extend(
                make_value_for_stylish(
                    key,
                    val,
                    stylish,
                    deep_indent_size,
                    deep_indent
                )
            )
        else:
            indent = '  '
            result.append(
                f'\n{deep_indent}{indent}{key}: '
                f'{stylish(val, deep_indent_size)}'
            )
    result.append(f'\n{current_indent}' + '}')
    return ''.join(result)
