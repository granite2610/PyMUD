import uuid

from typing import List, Dict

from lib.models.entity import Entity, DescriptionItem, Exit, Inventory
from lib.models.enums import ExitType, LightLevel, Obscuration
from lib.models.npc import NPC


class Room(Entity):

    def __init__(self,
                 name: str,
                 description: str,
                 description_items: List[DescriptionItem] = None,
                 exits: List[Exit] = None,
                 light_level: LightLevel = LightLevel.BRIGHT,
                 obscuration: Obscuration = Obscuration.NONE,
                 ):
        self.uuid = uuid.uuid4()
        self.description_items = description_items
        self.light_level = light_level
        self.obscuration = obscuration
        self.exits = exits
        self.inventory = Inventory()
        self.npcs = []

        super().__init__(name, description)

    def add_npc(self, npc: NPC):
        self.npcs.append(npc)

    def add_exit(self, ex:Exit):
        self.exits.add(ex)

    def get_exits(self) -> Dict[str, Exit]:
        exits = {}
        for ex in self.exits:
            exits[ex.name] = ex
        return exits

    def get_exit(self, ex) -> Exit:
        return self.get_exits()[ex]

    def has_exit(self, ex: str) -> bool:
        if ex in self.get_exits().keys():
            return True
        return False