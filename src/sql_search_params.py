from typing import List
from entities.search_parameter import SearchParameter


def generate_where_query(params: List[SearchParameter]):
    if len(params) == 0:
        return "1=1"

    return_str = ""

    for i, param in enumerate(params):
        if i > 0:
            return_str += " AND "
        return_str += param.to_sql()

    return return_str
