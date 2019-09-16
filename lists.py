bases = ['life', 'earth', 'water', 'fire', 'air', 'light', 'dark', 'psychic',
         'arcane']
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
aspect_num = {
    0: 30,
    1: 50,
    2: 17
}
aspects = bases.copy()
gods = 0

for base in bases:
    gods += 1
    print("%s | (%s)" % (base, domains[base]))
    for aspect1 in aspects:
        if (aspect1 != base):
            gods += 1
            print("%s %s | (%s/%s)" % (base, aspect1, domains[base],
                                       domains[aspect1]))
            for aspect2 in aspects:
                if aspect2 != aspect1 and aspect2 != base:
                    gods += 1
                    print("%s %s %s | (%s/%s/%s)" % (base, aspect1, aspect2,
                                                     domains[base],
                                                     domains[aspect1],
                                                     domains[aspect2]))

gods += 1
print('void | (orange)')

print(str(gods))
