def find_parent_keys(d, key, val):
    """
    Recursively derives parent keys from a target
    key and value inside a nested dictionary.

    Args:
        d (dict): nested dictionary
        key (str): target key
        val (any): target value

    Returns:
        list: list of parent keys (if present) and
        the target key. Input to update_key_value.
    """
    if d:
        for k, v in d.items():
            if k == key and v == val:
                return [k]
            elif isinstance(v, dict):
                p = find_parent_keys(v, key, val)
                if p:
                    return [k] + p
            elif isinstance(v, list):
                p = find_parent_keys(v[1], key, val)
                if p:
                    return [k] + p
    else:
        return [key]


def update_key_value(d, p_keys, key, val, GET_SIZE=True, nest_depth=0):
    """
    Recursively searches for a target key inside a nested
    dictionary to either replace or extend the target value,
    respectively being a string ("dir") or sub-dictionary
    (being the second element inside a two-element list for
    GET_SIZE=True, with the other being directory size) with
    an empty dictionary or key-value pair, respectively.

    Args:
        d (dict): nested dictionary. Input to
        find_directory_size for GET_SIZE=True
        p_keys (list): list containing the parent keys
        (can be none) of the target key, and the target
        key itself. Output of find_parent_keys
        key (str): target key
        val (dict): empty dictionary or key-value pair
        to replace or extend the target value (a string
        or dictionary resp.) with
        GET_SIZE (bool): boolean for calculating the total sizes
        of the filesystem directories to solve the Day 7 puzzle.
        -> If True (default), a two-element list consisting
        of the total directory size and a sub-dictionary is
        assigned to each directory key
        -> If False, the filesystem directories are simply
        represented as nested sub-dictionaries without an
        outer list structure, because why not :p
        nest_depth (int, optional): recursion counter
        variable to keep track of the current dictionary
        nesting level. Defaults to 0

    Returns:
        dict: nested dictionary with updated key value, being
        a list (GET_SIZE=True) or sub-dictionary (GET_SIZE=False).
    """
    MAX_DEPTH = len(p_keys) - 1
    for k, v in d.items():
        if nest_depth > MAX_DEPTH:
            return d
        elif k == key and nest_depth == MAX_DEPTH:
            nest_depth += 1
            if isinstance(v, list):
                if val[next(iter(val))].isdigit():
                    v[0] = v[0] + int(val[next(iter(val))])
                v[1].update(val)
            elif isinstance(v, dict):
                v.update(val)
            elif isinstance(v, str):
                d.update({k: val})
        elif k == p_keys[nest_depth] and nest_depth < MAX_DEPTH:
            if GET_SIZE:
                if isinstance(val, dict) and val:
                    if val[next(iter(val))].isdigit():
                        v[0] = v[0] + int(val[next(iter(val))])
                update_key_value(
                    v[1], p_keys, key, val, GET_SIZE, nest_depth + 1
                )
            else:
                update_key_value(v, p_keys, key, val, GET_SIZE, nest_depth + 1)
            return d
    return d


def find_directory_size(d, MAX_SIZE=None, MIN_SIZE=None, size=0):
    """
    Recursively scans the nested filesystem dictionary
    obtained with update_key_value for directory sizes
    needed to solve Part One and Two of the Day 7 puzzle.

    Args:
        d (dict): nested filesystem dictionary. Output
        of update_key_value (GET_SIZE=True)
        MAX_SIZE (int, optional): maximum total directory
        size for Part One. Defaults to None but set it to
        100000 for answering Part One
        MIN_SIZE (int, optional): minimal total directory
        size for Part Two. Defaults to None but set it to
        d["/"][0] - 40000000 for answering Part Two
        size (int, optional): variable to keep track
        of the directory sizes. Defaults to 0 for it
        to be updated through recursion

    Returns:
        int: final size update, being the answer to Part One or Two
    """
    if MAX_SIZE is None and MIN_SIZE is None:
        return d["/"][0]
    elif MIN_SIZE is not None and size == 0:
        size = d["/"][0]
    for v in d.values():
        if isinstance(v, list):
            if MAX_SIZE is not None and MIN_SIZE is None:
                if v[0] <= MAX_SIZE:
                    size += v[0]
                size = find_directory_size(v[1], MAX_SIZE, MIN_SIZE, size)
            elif MAX_SIZE is None and MIN_SIZE is not None:
                if size > v[0] and v[0] - MIN_SIZE > 0:
                    size = v[0]
                size = find_directory_size(v[1], MAX_SIZE, MIN_SIZE, size)
    return size
