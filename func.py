def get_summ(one, two, delimiter='&'):
    string = f'{one}{delimiter}{two}'
    return string.upper()


if __name__ == "__main__":
    print(get_summ('Learn', 'python'))
