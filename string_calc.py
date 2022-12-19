def new_calc():
    while True:
        calc_new = input('Введите выражение (0 - для выхода): ')
        compiled_str = compile(calc_new, 'string', 'eval')
        print(eval(compiled_str))
        if calc_new == '0':
            print('СПАСИБО! ДО СВИДАНИЯ!')
            break
