def get_word_catalog(query_set):
    data = list(query_set)
    res = {}
    for item in data:
        book_name = item['book_name']
        unit = item['unit']
        res.update({book_name: {'name': book_name, 'unit': {}}})
    for item in data:
        book_name = item['book_name']
        unit = item['unit']
        res[book_name]['unit'].update({unit: []})
    for item in data:
        book_name = item['book_name']
        unit = item['unit']
        classes = item['classes']
        res[book_name]['unit'][unit].append(classes)
    return res
