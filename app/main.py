import copy
import json

from app.calculations.duel import duel
from app.calculations.preparations import preparation
from app.knights.knight import Knight

with open("app/knights/knights.json", "r") as file:
    knights_data = json.load(file)


def battle(knights_config: dict | None = None) -> dict:

    if knights_config is None:
        with open("app/knights/knights.json") as f:
            knights_config = json.load(f)
    knights_list = knights_config.get("values", knights_config)

    if "values" in knights_config:
        knights_list = knights_config["values"]
    else:
        knights_list = list(knights_config.values())

    knights_instances = []

    for i in knights_list:
        knight = Knight(
            name=i["name"],
            power=i["power"],
            hp=i["hp"],
            armour=(i["armour"]),
            weapon=i["weapon"],
            potion=i["potion"],
        )
        knights_instances.append(knight)

    lancelot = knights_instances[0]
    arthur = knights_instances[1]
    mordred = knights_instances[2]
    red_knight = knights_instances[3]

    prepared_lancelot = preparation(lancelot)
    prepared_arthur = preparation(arthur)
    prepared_mordred = preparation(mordred)
    prepared_red_knight = preparation(red_knight)

    duel_result_first = duel(
        copy.deepcopy(prepared_lancelot), copy.deepcopy(prepared_mordred)
    )
    duel_result_second = duel(
        copy.deepcopy(prepared_arthur), copy.deepcopy(prepared_red_knight)
    )

    print(duel_result_first | duel_result_second)

    return duel_result_first | duel_result_second


battle(knights_data)
