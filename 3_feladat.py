def tipus():

    x = ['', 4, 'false']

    a = []
    for elem in x:

        if type(elem) is int:
            a.append('integer')

        if type(elem) is str:
            if elem.lower() in ['true', 'false']:
                a.append('boolean')
            else:
                a.append('string')

    print(a)


tipus()