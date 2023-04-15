s = 'My Name is Julia'

if 'Name' in s:
    print('Substring found')

index: int = s.find('Name')
if index != -1:
    print(f'Substring found at index {index}')


def test_abs1() -> None:
    assert abs(-42) == 42, "Should be absolute value of a number"


def test_abs2() -> None:
    assert abs(-42) == -42, "Should be absolute value of a number"


if __name__ == "__main__":
    test_abs1()
    test_abs2()
    print("Everything passed")
