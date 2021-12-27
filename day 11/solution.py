def has_consecutive(password: str) -> bool:
    for a, b, c in zip(password, password[1:], password[2:]):
        if ord(a) + 1 == ord(b) and ord(a) + 2 == ord(c):
            return True
    return False


def has_pairs(password: str) -> bool:
    for ch in 'abcdefghjkmnpqrstuvwxyz':
        pair = ch + ch
        if pair in password:
            for ch2 in 'abcdefghjkmnpqrstuvwxyz':
                pair2 = ch2 + ch2
                if pair2 in password.replace(pair, '_', 1):
                    return True
    return False


def is_valid(password: str) -> bool:
    if has_pairs(password) and has_consecutive(password):
        for ch in 'iol':
            if ch in password:
                return False
        return True

    return False


def inc_password(password: str) -> str:
    password_ls = list(password)
    for index, char in reversed(list(enumerate(password_ls))):
        if char in 'hnk':
            password_ls[index] = chr(ord(char) + 2)
            break
        elif char != 'z' and char not in 'iol':
            password_ls[index] = chr(ord(char) + 1)
            break
        else:
            password_ls[index] = 'a'
    password = ''.join(password_ls)
    print(password)
    return password


def q1(password: str) -> str:

    password = inc_password(password)
    while not is_valid(password):
        password = inc_password(password)

    return password


if __name__ == '__main__':
    from time import perf_counter as pc
    st = pc()
    print(f'Part 1: {q1("hxbxwxba")}')
    pt1 = pc()
    print(f'Part 2: {q1("hxbzzzzz")}')
    pt2 = pc()

    print(f'Time for execution:\n\
            Part 1: {(pt1-st)*1000}ms\n\
            Part 2: {(pt2-pt1)*1000}ms\n\
            Total: {(pt2-st)*1000}ms')
