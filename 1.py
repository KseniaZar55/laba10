def p1():
    import json
    with open('for10/файл1.json', encoding='utf-8') as f:
        file = json.load(f)
    for product in file['products']:
        print('Название: ', product['name'])
        print('Цена: ', product['price'])
        print('Вес: ', product['weight'])
        if product['available']:
            print('В наличии.')
        else:
            print('Нет в наличии!')
        print('')

def p2():
    import json
    with open('for10/файл1.json', encoding='utf-8') as f:
        file = json.load(f)

    new = {}
    new['name'] = input('Введите название: ')
    new['price'] = input('Введите цену: ')
    new['weight'] = input('Введите вес: ')
    new['available'] = input('Товар в наличии? ').lower() == 'да'
    file['products'].append(new)

    with open('for10/файл1.json', 'w', encoding='utf-8') as f:
        json.dump(file, f, ensure_ascii = False, indent = 4)

    with open('for10/файл1.json', encoding='utf-8') as f:
        file = json.load(f)
    for product in file['products']:
        print('Название: ', product['name'])
        print('Цена: ', product['price'])
        print('Вес: ', product['weight'])
        if product['available']:
            print('В наличии.')
        else:
            print('Нет в наличии!')
        print('')

def p3():

    import json
    file = {}
    with open('for10/en-ru.txt', 'r', encoding = 'utf-8') as f:
        for line in f:
            en_word, ru_words = line.strip().split('-')
            for ru_word in ru_words.split(','):
                if ru_word not in file:
                    file[ru_word] = [en_word]
                else:
                    file[ru_word].append(en_word)

    with open('for10/ru-en.txt', 'w', encoding='utf-8') as f:
        for ru_word in sorted(file.keys()):
            en_words=','.join(sorted(file[ru_word]))
            f.write(f'{ru_word}-{en_words}\n')

    with open('for10/en-ru.json', 'w', encoding='utf-8') as f:
        json.dump(file, f, ensure_ascii=False, indent=4)