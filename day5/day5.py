from hashlib import md5
puzzle_input = 'uqwqemis'

idx = 0
password = ['_', '_', '_', '_', '_', '_', '_', '_', ]
while True:
    m = md5()
    m.update((puzzle_input+str(idx)).encode('utf-8'))
    hex = m.hexdigest()
    if hex[0:5] == '00000':
        try:
            if int(hex[5]) < 8:
                if password[int(hex[5])] == '_':
                    password[int(hex[5])] = hex[6]
                    print(password)
        except ValueError:
            pass
    idx += 1
    if '_' not in password:
        print(''.join(password))
        break
