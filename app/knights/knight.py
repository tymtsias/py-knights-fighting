from __future__ import annotations

from app.items.consumables.potion import Potion
from app.items.equipment.armor.armour import Armour
from app.items.equipment.weapon.weapon import Weapon


class Knight:
    def __init__(
        self,
        name: str,
        power: int,
        hp: int,
        armour: list[Armour],
        weapon: Weapon,
        potion: Potion,
    ) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion
        self.protection = 0
