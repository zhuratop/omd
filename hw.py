# Guido van Rossum <guido@python.org>


def step2_umbrella():
    print('Когда она выходила из бара, то решила пойти, отработать смену.')
    print('Там ей пригодился зонт, ведь она укрылась им и спала ☂️')


def step2_no_umbrella():
    print(
        'Когда она выходила из бара, то заказала такси '
        'и поехала на объект.'
    )
    print(
        'Но, вспомнив, что у нее нет зонта, '
        'она поехала спать. ️'
    )


def step1():
    print(
        'Утка-маляр 🦆 решила выпить зайти в бар. '
        'Взять ей зонтик? ☂️'
    )
    option = ''
    options = {'да': True, 'нет': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()

    if options[option]:
        return step2_umbrella()
    return step2_no_umbrella()


if __name__ == '__main__':
    step1()
