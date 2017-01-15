#!/usr/bin/env python
from random import randrange

import click

STR=0
INT=1
WIS=2
DEX=3
CON=4
CHA=5

def rollstat():
    return sum((randrange(6)+1 for x in range(3)))


def rollstats():
    return [rollstat() for stat in range(6)]


def evalstats(stats):
    classes = [
        {'name': 'Fighter', 'primes': [STR], 'reqs': []},
        {'name': 'Mage', 'primes': [INT], 'reqs': []},
        {'name': 'Cleric', 'primes': [WIS], 'reqs': []},
        {'name': 'Thief', 'primes': [DEX], 'reqs': []},
        {'name': 'Assassin', 'primes': [STR, DEX], 'reqs': []},
        {'name': 'Bard', 'primes': [CHA, DEX], 'reqs': []},
        {'name': 'Bladedancer', 'primes': [WIS, DEX], 'reqs': []},
        {'name': 'Explorer', 'primes': [STR, DEX], 'reqs': []},
        {'name': 'Vaultguard', 'primes': [STR], 'reqs': [(CON, 9)]},
        {'name': 'Craftpriest', 'primes': [WIS], 'reqs': [(CON, 9)]},
        {'name': 'Spellsword', 'primes': [STR, INT], 'reqs': []},
        {'name': 'Nightblade', 'primes': [DEX, INT], 'reqs': []},
        {},
        {'name': 'Anti-paladin', 'primes': [STR, CHA], 'reqs': []},
        {'name': 'Barbarian', 'primes': [STR, CON], 'reqs': []},
        {'name': 'Delver', 'primes': [DEX], 'reqs': [(CON, 9)]},
        {'name': 'Fury', 'primes': [STR], 'reqs': [(CON, 9)]},
        {'name': 'Machinist', 'primes': [INT, DEX], 'reqs': [(CON, 9)]},
        {'name': 'Courtier', 'primes': [INT, CHA], 'reqs': [(INT, 9)]},
        {'name': 'Enchanter', 'primes': [INT, CHA], 'reqs': [(INT, 9)]},
        {'name': 'Ranger', 'primes': [STR, DEX], 'reqs': [(INT, 9)]},
        {'name': 'Trickster', 'primes': [CON, CHA], 'reqs': [(CON, 9), (INT, 9)]},
        {'name': 'Mystic', 'primes': [WIS, DEX, CON, CHA], 'reqs': []},
        {'name': 'Wonderworker', 'primes': [INT, WIS], 'reqs': [(i, 11) for i in range(6)]},
        {'name': 'Paladin', 'primes': [STR, CHA], 'reqs': []},
        {'name': 'Pristess', 'primes': [WIS, CHA], 'reqs': []},
        {'name': 'Shaman', 'primes': [WIS], 'reqs': []},
        {'name': 'Gladiator', 'primes': [STR], 'reqs': [(STR, 9), (DEX, 9), (CON, 9)]},
        {'name': 'Venturer', 'primes': [CHA], 'reqs': []},
        {'name': 'Warlock', 'primes': [INT], 'reqs': []},
        {'name': 'Witch', 'primes': [WIS, CHA], 'reqs': []},
        {'name': 'Ruinguard', 'primes': [STR, INT], 'reqs': [(INT, 9), (WIS, 9), (CHA, 9)]},
        ]
    allowed_classes = ''
    for cls in classes:
        if cls == {}:
            allowed_classes += '\n'
            continue

        prime = min((stats[prime] for prime in cls['primes']))

        if prime > 15:
            fitness = 3
        elif prime > 12:
            fitness = 2
        elif prime > 8:
            fitness = 1
        else:
            fitness = 0

        for req in cls['reqs']:
            if stats[req[0]] < req[1]:
                fitness = 0
                break

        if fitness == 0:
            allowed_classes += ' '*len(cls['name']) + '  '
        elif fitness == 1:
            allowed_classes += cls['name'] + '  '
        elif fitness == 2:
            allowed_classes += cls['name'] + '+ '
        elif fitness == 3:
            allowed_classes += cls['name'] + '* '

    click.echo(allowed_classes)


def printstats(stats):
    click.echo('STR:{:>3} INT:{:>3} WIS:{:>3} DEX:{:>3} CON:{:>3} CHA:{:>3}'.format(*stats))
    evalstats(stats)
    click.echo('')


@click.command()
@click.option('-c', '--count', default=1, help='Number of characters.')
def generate(count):
    """Character roller for ACKS."""
    for x in range(count):
        stats = rollstats()
        printstats(stats)

if __name__ == '__main__':
    generate()
