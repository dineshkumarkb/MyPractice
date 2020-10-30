def test_func():
    try:
        x = 10
        return x
    except Exception as e:
        x = 20
        return x
    finally:
        x = 30
        return x
print(test_func())