def get_initials_and_length(full_name):
    cleaned = ' '.join(full_name.split())
    parts = cleaned.split(' ')
    initials = ''.join([p[0].upper() for p in parts])
    length = len(cleaned)
    return initials, length

input_str = input('Введите ФИО: ')
initials, length = get_initials_and_length(input_str)
print(f"{initials} {length}")