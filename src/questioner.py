def question(*kwargs):
    yes = ["yes", "y", "ye", "Y", "YES", 'YE']
    no = ["no", "n", "NO", "n"]

    for arg, type_ in kwargs:
        if type_ == 'int':
            try:
                question = int(input(f'{arg}: '))
                yield (arg, question)
            except ValueError:
                raise ValueError('Use only numbers!')
        
        elif type_ == 'y/n':
            question = input(f'{arg}: ')
            if question in yes:
                yield (arg, True)
            elif question in no:
                yield (arg, False)
            else:
                raise Exception(f'Whats "{question}"?? use only yes or no!')

        elif type_ == 'str':
            question = input(f'{arg}: ')
            if question == '':
                yield (arg, None)
            else:
                yield (arg, question)
