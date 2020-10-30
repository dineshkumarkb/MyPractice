def add(num1,num2):
    return num1 + num2


def sub(num1, num2):
    return num1 - num2


def validate_ids(metadata):
    print(" The metadata is ", metadata)
    if metadata.get('copystatus') == 'completed':
        return True
    return False