# app/utils/parsing.py


def parse_size(size: str) -> int:
    """
    Convert human-readable size into bytes.

    Examples:
        10MB -> 10485760
        1GB  -> 1073741824
    """

    size = size.strip().upper()

    units = {
        "KB": 1024,
        "MB": 1024**2,
        "GB": 1024**3,
    }

    for unit, multiplier in units.items():
        if size.endswith(unit):
            value = float(size.removesuffix(unit))
            return int(value * multiplier)

    return int(size)
