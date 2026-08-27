from app.knights.knight import Knight


def preparation(knight: Knight) -> dict:

    # apply armour
    # knight["protection"] = 0
    for armour in knight.armour:
        knight.protection += armour["protection"]

    # apply weapon
    knight.power += knight.weapon["power"]

    # apply potion if exist
    if knight.potion is not None:
        if "power" in knight.potion["effect"]:
            knight.power += knight.potion["effect"]["power"]

        if "protection" in knight.potion["effect"]:
            knight.protection += knight.potion["effect"]["protection"]

        if "hp" in knight.potion["effect"]:
            knight.hp += knight.potion["effect"]["hp"]

    # should return dict with name power, protection, hp params
    return {
        "name": knight.name,
        "power": knight.power,
        "protection": knight.protection,
        "hp": knight.hp}
