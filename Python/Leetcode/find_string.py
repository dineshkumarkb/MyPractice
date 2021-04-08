def find_string(haystack: str, needle: str) -> int:
    if not needle:
        return 0
    return haystack.find(needle)


print(find_string("aaaa", "bba"))