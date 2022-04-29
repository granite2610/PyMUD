from dataclasses import dataclass, field
from typing import List, Dict

from lib.constants import DEFAULT_START_LOCATION
from lib.models.client import NpcClient
from lib.models.character import Character
from lib.models.character_class import CharacterClass
from lib.models.entity import Entity, Inventory
from lib.models.enums import Ability, Skill, Alignment


class NPC(Character):

    _DEFAULT_LEVEL = 0
    _DEFAULT_XP = 0
    _DEFAULT_HP = 1
    _DEFAULT_AC = 10

    def __init__(self,
                 client: NpcClient,
                 name: str ,
                 description: str = None,
                 character_class: CharacterClass = None,
                 level: int = _DEFAULT_LEVEL,
                 background: str = None,
                 race: str = None,
                 alignment: Alignment = None,
                 xp: int = _DEFAULT_XP,
                 abilities: Dict[Ability, int] = None,
                 skills: List[Skill] = None,
                 max_hp: int = _DEFAULT_HP, 
                 armor_class: int = _DEFAULT_AC,
                 hd_value: int = 0,
                 hd_total: int = 0,
                 inventory: Inventory = None):

        self.name = name
        self.character_class = character_class
        self.level = level
        self.background = background
        self.race = race
        self.alignment = alignment
        self.xp = xp
        self.abilities = abilities
        self.skills = skills
        self.max_hp = max_hp
        self.current_hp: int = self.max_hp
        self.temporary_hp: int = 0
        self.armor_class = armor_class
        self.hd_value = hd_value
        self.hd_total = hd_total
        self.death_save_success: int = 0
        self.death_save_failure: int = 0
        self.inventory: Inventory = inventory
        self._location = ""

        super().__init__(client, name, description)

    def move(self, destination: str):
        pass
        # self._location = destination
        # rooms[self._location].inventory.add_item(self)

