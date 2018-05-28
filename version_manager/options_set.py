from typing import Dict, List


def get_parameter_values(values_list: List[str]) -> Dict[str, str]:
    result = dict()  # type: Dict[str, str]

    if not values_list:
        return result

    for value in values_list:
        tokens = value.split('=', 2)
        result[tokens[0]] = tokens[1]

    return result
