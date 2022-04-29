from lib.models.character import Character
from lib.models.character_class import CharacterClass
from lib.models.client import NpcClient
from lib.models.npc import NPC
from lib.models.room import Room, Exit, DescriptionItem
from lib.models.enums import ExitType, Ability

rooms = {}


def add_room(room: Room):
    rooms[room.name] = room


trader_class = CharacterClass("commoner", "A lowly commoner", "2d8", Ability.CHARISMA, [], [], [])
trader_class.name = "commoner"

merchant = NPC(
    client=NpcClient(),
    name="Doug",
    description="Doug the merchant",
    character_class=trader_class
)
merchant.name = "Doug"

# This is unpleasant to work with.
tavern = Room(name='tavern',
              description="You're in a cozy tavern warmed by an open fire.",
              description_items=[
                  DescriptionItem(name='fire',
                                  aliases=['open fire'],
                                  description='A warm, inviting fire.')
              ],
              exits=[
                  Exit(name='outside',
                       description='A door leading to the outside.',
                       destination='outside',
                       exit_type=ExitType.DOOR)
              ]
              )
tavern.add_npc(merchant)
add_room(
    tavern
)


add_room(
    Room(name='outside',
         description="You're standing outside a tavern. It's raining.",
         exits=[
             Exit(
                 name='inside',
                 description='A door leading back inside.',
                 destination='tavern',
                 exit_type=ExitType.DOOR)
         ]
         )
)
