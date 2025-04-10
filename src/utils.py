def flatten(value: str | None) -> str:
    if value is None:
        return ""
    return value


def safe_cast_to_int(value: str | int) -> int:
    if isinstance(value, int):
        return value

    value = "".join([c for c in value if c.isdigit() or c == "-"])
    try:
        return int(value)
    except ValueError:
        return 0
