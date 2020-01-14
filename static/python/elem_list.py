def elem_list():
    """Returns a list of magic/aspect combinations with a count of them"""
    bases = ['life', 'earth', 'water', 'fire', 'air',
             'light', 'dark', 'psychic', 'arcane']

    domains = {
        'life': ('teal', 20),
        'earth': ('green', 15),
        'water': ('blue', 15),
        'fire': ('red', 15),
        'air': ('yellow', 15),
        'light': ('white', 7.5),
        'dark': ('black', 7.5),
        'psychic': ('pink', 4.9),
        'arcane': ('purple', 0.1)
    }
    # aspect_num = {
    #     0: 30,
    #     1: 50,
    #     2: 20
    # }
    aspects = bases.copy()
    gods = 0
    elemList = []

    for base in bases:
        gods += 1
        elemList.append("%s | (%s)" % (base, domains[base][0]))
        for aspect1 in aspects:
            if (aspect1 != base):
                gods += 1
                elemList.append("%s %s | (%s/%s)" % (
                    base, aspect1, domains[base][0], domains[aspect1][0]))
                for aspect2 in aspects:
                    if aspect2 != aspect1 and aspect2 != base:
                        gods += 1
                        elemList.append("%s %s %s | (%s/%s/%s)" % (
                            base, aspect1, aspect2, domains[base][0],
                            domains[aspect1][0], domains[aspect2][0]))

    gods += 1
    elemList.append('void | (orange)')
    elemList.append(gods)

    return elemList
