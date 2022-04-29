from typing import Dict

from game_data import rooms
from lib.models.character import Character
from lib.models.npc import NPC
from mudserver import MudServer
from lib.models.player import Player

# TODO: Is there too much in this class now?
# The util didn't make sense anymore, because it was too tightly linked


class GameState(object):
    def __init__(self, server: MudServer):
        self.server = server
        self.players: Dict[str, Character] = {}

    def update(self):
        self.server.update()

    def add_player(self, player: Player):
        self.players[player.uuid] = player

    def remove_player(self, player: Character):
        del(self.players[player.uuid])

    def list_players(self):
        for player in self.players.values():
            yield player

    def list_other_players(self, exclude_player: Player):
        for player in self.list_players():
            if player.uuid != exclude_player.uuid:
                yield player

    def handle_player_join(self):
        for event in self.server.get_new_player_events():
            new_client = event.client
            new_player = Player(new_client, self.server)
            self.add_player(new_player)
            self.tell_player(new_player, "What is your name?")

    def handle_player_leave(self):
        for event in self.server.get_disconnected_player_events():
            disconnected_client = event.client
            disconnected_player = self.find_player_by_client_id(disconnected_client.uuid)
            if not disconnected_player:
                continue

            for player_id, player in self.players.items():
                self.tell_player(player, "{} quit the game".format(disconnected_player.name))

            self.remove_player(disconnected_player)

    def tell_player(self, player: Character, message: str):
        self.server.send_message(player.client.uuid, message)

    def attack_character(self, attacker: Character, defender_name: str):
        if self.find_character_by_name(defender_name):
            defender = self.find_character_by_name(defender_name)
            if defender and attacker.get_location() == defender.get_location():
                defender.take_damage(10)
                self.tell_player(attacker, f"You attacked {defender.name}")

    def find_character_by_name(self, char_name: str) -> Character:
        for uuid, character in self.players.items():
            if character.name == char_name:
                return character

    def find_npcs_in_room(self, room_id) -> [NPC]:
        room = rooms.get(room_id)
        if room:
            return room.npcs
        return []

    def move_character(self):
        pass

    def broadcast(self, message: str):
        for player in self.players.values():
            self.tell_player(player, message)

    def find_player_by_client_id(self, client_id: str) -> Character:
        for player_id, player in self.players.items():
            if player.client.uuid == client_id:
                return player
