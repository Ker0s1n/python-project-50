from gendiff.file_parser import parse_file


def make_value_for_difference(
        key,
        value,
        another_value,
        node,
        another_node,
        function,
        depth
):
    """
    Returns data characterizing the passed key
    and the variable it contains as a dictionary.
    """
    if key not in node:
        return {'type': 'added', 'value': another_value}
    elif key not in another_node:
        return {'type': 'deleted', 'value': value}
    elif isinstance(value, dict) and isinstance(another_value, dict):
        return {
            'type': 'nested',
            'value': function(value, another_value, depth + 1)}
    else:
        if value != another_value:
            return {
                'type': 'changed',
                'old_value': value,
                'new_value': another_value}
        else:
            return {'type': 'unchanged', 'value': value}


def difference(node1, node2, depth: int = 0):
    """
    Returns a dictionary with the data for each key
    in the two dictionaries passed as arguments.
    """
    result = {}
    for key in sorted(node1.keys() | node2.keys()):
        value1 = node1.get(key)
        value2 = node2.get(key)
        result[key] = make_value_for_difference(
            key,
            value1,
            value2,
            node1,
            node2,
            difference,
            depth
        )
    return result


def make_diff(file1, file2):
    """
    Returns a dictionary showing the differences
    between the two files that were transferred.
    """
    input1 = parse_file(file1)
    input2 = parse_file(file2)
    return difference(input1, input2)
