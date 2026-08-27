from __future__ import annotations


class Armour:
    def __init__(self, armour_part_name: str, protection: int) -> None:
        self.armour_part_name = armour_part_name
        self.protection = protection
