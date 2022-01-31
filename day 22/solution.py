
from dataclasses import dataclass
from functools import cache


@dataclass
class Effect:
    damage: int
    armor: int
    mana: int
    hp: int
    turns: int
    cost: int
    index: int

    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Effect) and self.damage == __o.damage and self.armor == __o.armor and self.mana == __o.mana and self.turns == __o.turns and self.hp == __o.hp

    def __hash__(self) -> int:
        return hash((self.damage, self.armor, self.mana, self.turns, self.hp))

    def copy(self) -> 'Effect':
        return Effect(self.damage, self.armor, self.mana, self.hp, self.turns, self.cost, self.index)


spells = [
    Effect(4, 0, 0, 0, 0, 53, 1), #magic missile
    Effect(2, 0, 0, 2, 0, 73, 2), #drain
    Effect(0, 7, 0, 0, 6, 113, 3), #shield
    Effect(3, 0, 0, 0, 6, 173, 4), #poison
    Effect(0, 0, 101, 0, 5, 229, 5) #recharge
]

@dataclass
class Character:
    hp: int
    damage: int
    mana: int
    effects: list[Effect]

    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Character) and self.hp == __o.hp and self.damage == __o.damage and self.mana == __o.mana and self.effects == __o.effects

    def __hash__(self) -> int:
        return hash((self.hp, self.damage, self.mana, tuple(self.effects)))

    def advance_turn(self):

        current_damage = self.damage

        for effect in self.effects: # instant spells
            if effect.turns == 0:
                self.hp += effect.hp
                current_damage += effect.damage

        self.effects = [effect for effect in self.effects if effect.turns > 0]

        for effect in self.effects: # other spells
            effect.turns -= 1
            if effect.turns == 0:
                self.effects.remove(effect)

        self.mana += sum(effect.mana for effect in self.effects)

        return current_damage

    def take_damage(self, damage):
        armor = sum(effect.armor for effect in self.effects)
        self.hp -= max(1, damage - armor)

    def copy(self):
        effects_copy = [effect.copy() for effect in self.effects]
        return Character(self.hp, self.damage, self.mana, effects_copy)

    def has_effect(self, index):
        return any(effect.index == index for effect in self.effects if effect.turns > 1)




@dataclass
class BattleState:
    cost: int
    character: Character
    boss: Character

    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, BattleState) and self.character == __o.character and self.boss == __o.boss

    def __hash__(self) -> int:
        return hash((self.character, self.boss))

    def do_turn(self, spell_index):
        self.character.effects.append(spells[spell_index].copy())
        self.character.mana -= spells[spell_index].cost
        self.cost += spells[spell_index].cost

        character_damage = self.character.advance_turn()
        boss_damage = self.boss.advance_turn()

        self.character.take_damage(boss_damage)
        self.boss.take_damage(character_damage)

@cache
def make_more_games(game):
    completed_games = set()
    new_games = set()
    for i in range(len(spells)):
        if game.character.mana < spells[i].cost or game.character.has_effect(i):
            continue
        new_game = BattleState(game.cost, game.character.copy(), game.boss.copy())
        new_game.do_turn(i)
        if new_game.boss.hp <= 0:
            print(new_game)
            completed_games.add(new_game)
            continue
        if new_game.character.hp <= 0:
            continue
        new_games.add(new_game)

    return new_games, completed_games

def q1():
    boss = Character(58, 9, 0, [])
    player = Character(50, 0, 500, [])

    games = set()

    games.add(BattleState(0, player, boss))

    completed_games = set()

    while games:
        new_games = set()
        for g in games:
            n_g, c_g = make_more_games(g)
            new_games.update(n_g)
            completed_games.update(c_g)
        games = new_games
    
    return find_lowest_cost(completed_games)

def find_lowest_cost(games):
    lowest_cost = None
    for game in games:
        if lowest_cost is None or game.cost < lowest_cost:
            lowest_cost = game.cost
    return lowest_cost


def q2():
    boss = Character(58, 9, 0, [])
    player = Character(50, 0, 500, [])

    games = set()

    games.add(BattleState(0, player, boss))

    completed_games = set()

    while games:
        new_games = set()
        for g in games:
            g.player.hp -= 1
            if g.player.hp <= 0:
                continue
            n_g, c_g = make_more_games(g)
            new_games.update(n_g)
            completed_games.update(c_g)
        games = new_games
    
    return find_lowest_cost(completed_games)


if __name__ == '__main__':
    from time import perf_counter as pc
    st = pc()
    print(f'Part 1: {q1()}')
    pt1 = pc()
    print(f'Part 2: {q2()}')
    pt2 = pc()

    print(f'Time for execution:\n\
            Part 1: {(pt1-st)*1000}ms\n\
            Part 2: {(pt2-pt1)*1000}ms\n\
            Total: {(pt2-st)*1000}ms')
