def exception_format_plain(value):
    """
    Returns a variable after handling an exception.
    """
    if isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return 'null'
    elif value == '[complex value]':
        return value
    elif type(value) is int:
        return value
    else:
        return f"'{str(value)}'"


def make_value_for_plain(key, val, function):
    """
    Returns data characterizing the passed key
    and the variable it contains as a string.
    """
    string = []
    match val.get('type'):
        case 'added':
            add = val.get('value')
            if isinstance(add, dict):
                string.append(
                    f"Property \'{key}\' was added "
                    f"with value: [complex value]"
                )
            else:
                string.append(
                    f'Property \'{key}\' was added '
                    f'with value: {exception_format_plain(add)}'
                )
        case 'deleted':
            string.append(f'Property \'{key}\' was removed')
        case 'nested': string.append(function(val.get('value'), key))
        case 'changed':
            value1 = val.get('old_value')
            value2 = val.get('new_value')
            if isinstance(value1, dict):
                value1 = function(val.get('old_value'))
            if isinstance(value2, dict):
                value2 = function(val.get('new_value'))
            string.append(
                f'Property \'{key}\' was updated. '
                f'From {exception_format_plain(value1)} to '
                f'{exception_format_plain(value2)}'
            )
    return string


def make_path(parent, child):
    """
    Returns a string containing the path to the specified dictionary key,
    considering its parents.
    """
    if parent:
        return f'{parent}.{child}'
    return child


def plain(node, parent_key: str = ''):
    """
    Returns data about the dictionary of changes
    in the form of a textual description.
    """
    if not isinstance(node, dict):
        return str(node)

    result = []
    for key, val in node.items():
        key = make_path(parent_key, key)
        if isinstance(val, dict):
            result.extend(make_value_for_plain(key, val, plain))
        else:
            result.append(exception_format_plain('[complex value]'))
    return '\n'.join(result)
