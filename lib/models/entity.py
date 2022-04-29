import uuid

from typing import List, Dict

from lib.models.enums import ExitType, LightLevel, Obscuration


class Entity(object):
    def __init__(self, name=None, description=None):
        self.uuid = uuid.uuid4()
        self.name = name
        self.description = description


class Weapon(Entity):
    def __init__(self, name: str, description: str, damage: int):
        self.damage = damage
        super().__init__(name, description)


class Exit(Entity):
    def __init__(self, name, description, destination, exit_type: ExitType):
        self.destination = destination
        self.type = exit_type
        super().__init__(name, description)


class DescriptionItem():
    '''Similar to Entity, but distinct in that you'll never be able to pick up
    a description item. It exists just for flavour text. Every noun in a room's
    description should have a corresponding description item.
    '''
    def __init__(self, name: str, aliases: List[str], description: str):
        self.name = name
        self.aliases = aliases
        self.description = description


class Inventory(object):
    def __init__(self):
        self.inventory = {}

    def add_item(self, item: Entity) -> str:
        self.inventory[item.uuid] = item
        return f"{item.name} added!"

    def remove_item(self, item: Entity) -> str:
        i = self.inventory.get(item.uuid)
        if i:
            self.inventory.pop(item.uuid)
            return f"{item.name} removed!"
        else:
            return f"Inventory does not contain {item.name}"

    def has_item(self, item: Entity) -> bool:
        return self.inventory.get(item.uuid) != False

    def get_items(self) -> Dict[str, Entity]:
        return self.inventory.items()
