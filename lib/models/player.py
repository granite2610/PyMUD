from abc import ABC

from game_data import rooms
from lib.models.client import Client
from lib.models.character import Character
from lib.models.client import Client
from lib.models.npc import NPC
from mudserver import MudServer


class Player(Character, ABC):

    def __init__(self, client: Client, server: MudServer, creature: NPC = None):
        self.server = server

        if creature:
            super().__init__(
                 client,
                 creature.name,
                 creature.description,
                 creature.character_class,
                 creature.level,
                 creature.background,
                 creature.race,
                 creature.alignment,
                 creature.xp,
                 creature.abilities,
                 creature.skills,
                 creature.max_hp, 
                 creature.armor_class,
                 creature.hd_value,
                 creature.hd_total,
                 creature.inventory
            )

        super().__init__(client)

    def message(self, message):
        self.server.send_message(self.client.uuid, message)

    def say(self, msg: str):
        self.server.send_message(self.client.uuid, msg)

    def tell(self, msg: str):
        self.server.send_message(self.client.uuid, msg)

    def move(self, destination):
        super().move(destination)
        self.message(f"You arrive at '{self._location}'")
        self.message(rooms[self._location].description)

    def attack(self, character: Character):
        character.take_damage(10)