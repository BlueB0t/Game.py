#Mr. Wiebe is awesome!
#-------------------------------------------------------------------------------
import pickle
import sys

node = None

class Room:
    def __init__(self, name, north, east, south, west, up, down, n, e, s, w, u, d, yes, y, no, description):
        self.name = name
        self.n = n
        self.s = s
        self.w = w
        self.e = e
        self.u = u
        self.d = d
        self.yes = yes
        self.y = y
        self.no = no
        self.north =north
        self.south = south
        self.west = west
        self.east = east
        self.up =   up
        self.down =  down
        self.description = description

    def move(self, direction):
        global node
        node = globals()[getattr(self, direction)]

#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
#==============================================================Intro Screen==============================================================
intro_screen = Room("_____________________", None, None, None, None, None, None, None, None, None,  None, None, None, 'start_room', 'start_room', 'end_game', "Hello\ there! \n\
welcome to the pscycic adventure: Forgotten. You will explore the vast human psych, and each item you find will have its uses, whether it be useful then or later\
The Main objective for you, is well to try not to die and explore to the end! Have fun and remember you have: 0 checkpoints \n and PlEASE read the descriptions,\
it is essential to your survial... \n There may be typos, please forgive\n Note: whichever you choose to start the game, up\
 and down are implemented in the game frequently,\
as well these odd directions are used in a few hidden paths in the maps. Also, due to command errors, n cannot substitute no, n is for north.\
So type no please. \nhint: If you dont know where to go, READ the descriptions, or just use your head\n Your actions and choices to where you affect whats ahead...be wise")
#-------------------------------------------------------------------------------
#=======================================================Waking Up: Prephase Level====================================================================
start_room = Room("Awakening", None, None, None, None, None, None, None, None, None, None, None, None, 'wake_up2', 'wake_up2', 'clumsy', "You wake up,\
darkness really surround you. You have recognition to who you are, but you can see from your\
stationary position that you are in some quarters for a crew. A radio besides you blares on with static, then a lady exclaming: Hello?...\
.Is anyone there? Sector-19557 is in critical need- do you answer? \n yes/no")

wake_up2 = Room("Awakening", None, None, None, None, None, None, None, None, None, None,  None, None, 'wake_up3', 'wake_up3', 'clumsy', "Crew Mate:\
Thank god!-*static* look, we are in grave dange-*static*something on the ship..do you hear me?! \n yes/no")

wake_up3 = Room("Alone",None, None, None, None, 'crew_quarters', None, None, None,None, None, 'crew_quarters', None, None, None, None, "Crew Mate:\
good...good, now, hear me-*static* you need to- AAAH!*screams**static*.......*static continues* Youre probaly curious, you shoild probaly get UP...")

clumsy = Room("really?",None, None, None, None, None, None, None, None, None, None, None, None, 'crew_quarters', 'crew_quarters', 'crew_quarters', "You\
are startled by the blaring radio, and knock it over on the ground. Unfortunately, its not built\
very strong and lands with a crash on the gound, good job\n--------> continiue...y/no" )
#========================================================Level 1: The Ship===============================================================================
crew_quarters = Room("Crew Quarters", 'command_bridge', 'wash_room', None, 'hall1', None, None, 'command_bridge', 'wash_room', None, 'hall1', None, None,  None, None, None, "You\
are in the crew quarters, its prety dark so every thing is pretty obscure,\
a slightly open door leads north to the bridge, a doorway east leads to the crew washroom, and a path to a hall west. "  )

command_bridge = Room("The Command Bridge", 'cockpit', None, 'crew_quarters', None, None,None,  'cockpit', None, 'crew_quarters', None, None, None, None, None, None, "This\
is the command bridge, its a straight corridor with large glass panes on either\
side of you, space surrounding the ship with endless array of stars and a distant planet, below you only about 3ft down, are command consoles and empty chairs where monitors\
would sit. north of you is the cockpit" )

cockpit = Room("Cockpit", None, None, 'command_bridge', None, 'space_death', None, None, None, 'command_bridge', None, 'space_death', None, None, None, None, "This\
is the ships cockpit, the hum of technology surrounds you and small lights light up on the\
large motherboard. Two empty seats lay in front of you as well, for the pilot and the co-pilot, the vast open space exands beyond the glass....")

wash_room = Room("WashRoom", 'crew_quarters', None, None, None, None, 'hidden_hatch', 'crew_quarters', None, None, None, None, 'hidden_hatch',  None, None, None, "Its \
the crew washroom, its fairly large, but can only hold one crewmate at a time. There is\
a shower in front of you to the east wall, and a toilet next to it. the sink rests across from the toilet with streaks of blood leading to a knife in the sink bowl. Its\
pretty dim, and the toilet casts an unusually large shadow. The knife looks a little dull, probaly because a giant arrow pointing down is scratched on the mirror..hmm")

hall1 = Room("Hall", 'captains_quarters', 'crew_quarters', None, 'janitor_closet', None, None, 'captains_quarters', 'crew_quarters', None, 'janitor_closet', None, None, None, None, None, "You\
enter the creepy hall, it looks longer that it seems, ans a\
small window along the wall views the vast field of space. There is a door to the north that leads to the captains room, west is the janitors closet")

janitor_closet = Room("Janitors Closet", None, 'hall1', None, None, None , 'hatch_room', None, 'hall1', None, None, None , 'hatch_room', None, None, None,  "You\
peek into the janitors closet onboard the ship, the doors open a crack, the washbucket has\
been thrown aside and water is all over the floor, a hatch is revealed under the wahsbucket. Scratched on the wall, probaly with a knife, is and arrow pinting down ")

captains_quarters = Room("Captains Quarters", None, None, 'hall1', 'lobby', None, None, None, None, 'hall1', 'lobby', None, None, None, None, None,  "Its\
the captains quarters, the ceiling light flickers on and off every once and a while, the chair sitting\
at the amin desk is overturned and what seems to be a container with a mess of clothes and belongings spilling out. A long blood streak leads to the lobby\
west of you")

lobby = Room("Captians Lobby",  None, 'captains_quarters', None, 'observation_room', None, None, None, 'captains_quarters', None, 'observation_room', None, None, None, None, None, " The\
lobby is a small room with a magazine rack to the south wall, and a \
small reception desk to the captains room, the usual window on the noth wall was broken and you can see the blast doors are already shut. the bloodstreak ends abruptly at the west entrance\ to the observation room")

observation_room = Room("The Observation Room", 'pod_room', None, None, 'lobby', None, None, 'pod_room', None, None, 'lobby', None, None, None, None, None,  "You\
walk into the observation room, two large widows lay out in front of you, displaying the field\
of space in front of you, but one of the windows are shut with a bast door as well, you can see a body\
drifting off in the distace. a north entrance leads to th escape pod room")

pod_room = Room("Escape pod room", 'pod1', 'pod3', 'observation_room', 'pod2', None, None, 'pod1', 'pod3', 'observation_room', 'pod2', None, None, None, None, None,  "You\
enter the pod room, there is a large control panel that lights green indicating the pods\
are ready to launch, none were never lauched. There is a pod north with the number 1 above it, a pod west witha number 2 above it,\
and a pod east, with a number 3 above it, you also notice a yellow sign on the 3rd pod with unreadable alien language on it")

pod1 = Room("Pod one", None, None, None, None, None, None, None, None, None, None, None, None, 'death_room', 'death_room', 'death_room', "You \
approach the pod with the nimber one stamped above it, you press the pad hat opes up the shuttle, the door hisses, then\
creaks a little, hesatating. Suddently, the door is crushed and pulled into the vaccum of space, along with you...you die a horrible death....continue to death---> y/no")

pod2 = Room("Pod two", None, None, None, None, None, None, None, None, None, None, None, None,  'death_room', 'death_room', 'death_room', "You \
approach the pod with the number two stamped above, the launch pad is green and you gain access to the pod. As you\
walk into the escape pod, the rounding supports creak a little to your weight. the pod door closes and you sit in one of the six chairs.\n\
launching in: 5-4-3-2-1....and you feel the pod release from the station and the thrusters sputter.....safe at last....\n\
But wait! the creaking increasesn the suppoerts on the insides start to bend, the walls slowly crushing in like a tin can at the\
bottom of the ocean, with you in it\n continue to death y/no ")

pod3 = Room("Pod three", None, None, None, None, None, None, None, None, None, None, None, None,  'death_room', 'death_room', 'death_room', "You\
approach the pod with the number 3 printed above, and the strange yellow aien sign. the launch pad is red, but a few\
angry pounds turn it green. The pod door hisses and opens slowly, revealing what looks like a white-furry beast crouched away from you.\
Disturbed by the sound, it slowly rises, towering over you. Paralyzed with fear, you stand still as it rears its head towards you,\
it looks whats to be a snow yeti, but with a more concealed face and small horns jutting out of the side of its face, a wampa. It roars and lunges out at you......dark\n------> contunue to death y/no")
#---------------------------------------------------------------------------------
#---------------------------------------------------------------------------------
death_room = Room("You Dead",None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,  "Well, you died, I dont know how, but ya did, great! Its a nice time to quit,\n===================================================================== \n===================================================================== \n===================================================================== \
 '\n\
                                     ,--. \n\
                                    {    } \n\
                                    K,   } \n\
                                   /  ~Y` \n\
                              ,   /   / \n\
                             {_*-K.__/ \n\
                               `/-.__L._ \n\
                               /  * /`\_} \n\
                              /  * / \n\
                      ____   /  * / \n\
               ,-*~~~~    ~~/  * /_ \n\
             ,*             ``~~~  *,\n\
            (                        Y \n\
           {                         I \n\
          {      -                    `,\n\
          |       *,                   ) \n\
          |        |   ,..__      __. Y \n\
          |    .,_./  Y * / ^Y   J   )| \n\
          \           |* /   |   |   || \n\
           \          L_/    . _ (_,.*( \n\
            \,   ,      ^^*** / |      ) \n\
              \_  \          /,L]     / \n\
                *-_~-,       ` `   ./` \n\
                   `*{_            ) \n\
                       ^^\IIIIIIIII` \n\
          __   _____  _   _   ____ ___ _____ ____\n\
          \ \ / / _ \| | | | |  _ \_ _| ____|  _ \ \n\
           \ V / | | | | | | | | | | ||  _| | | | | \n\
            | || |_| | |_| | | |_| | || |___| |_| | \n\
            |_| \___/ \___/  |____/___|_____|____/  \n\
            ")



#==========================================================Level 2- The Plains==============================================================
hatch_room = Room("------------------", 'the_plains', None, None, None, None, None,'the_plains', None, None, None, None, None, None, None, None, "You\
approach the revealed hatch, and move the toppled washbucket. The hatch was fairly clean and is loose as you tug it open. You decide to hop in and land\
on soft floor...not carpetwise. The hatch above you slams shut with a wreching screech and you hear a clear clicking lock sound, you spot cracks of light\
north of you." )

the_plains = Room("The Plains", None, 'forest_entrance', None, 'forest_entrance2', None, None, None, 'forest_entrance', None, 'forest_entrance2', None, None, None, None, None, "You\
approach the door, as you are trudging you smell a growing earthly smell, as yo touchbthe sides of the tunnel it crumbles like dirt...You get to the door and\
can now describe it as wooden, with bright light shining trough the cracks. You twist the wooden knob and are slightly blinded by the shining light that hits\
you. As you adjust, you can make out a bright green field, plains outstretching, with the grassy area fully surrounded by tll forests. \nEast of you is an opening\
with a narrow, but stone-paved road, West is a more wider, but un-paved road, gnarly roots rise from the ground. " )

forest_entrance2 = Room("Gnarly Path", None, 'cobble_building', None, 'tavern/inn',None, None, None, 'cobble_building', None, 'tavern/inn',None, None, None, None, None, "You\
go down the more gnarly path, every once in a while stumbleing over a loose branch feeling watched by the old trees. You soon approach crossroads, a path leading\
east, and a path leading west. Particularly, and wreched old woman stands at the fork with a large cloak on, covering everyting but her extended arm, old wrinkled\
finger pointing to the path east. The lady is unresponsive." )

cobble_building = Room("Cobble Building", None, 'watch_tower', None, 'cellar', None, None, None, 'watch_tower', None, 'cellar', None, None, None, None, None, "You\
follow the road that the lady points to, you approach the cobble building and step inside. Two stone gargoyels stand on either side of the split descision between\
stairs on your east and west, with the west leading down and east leading up. The gargoyles both raise one arm and slowly point at a differnt stairwell...blood \
slowly drips from the their mouths. ")

cellar = Room("Cellar", 'cellar_room', None, None, None, None, None , 'cellar_room', None, None, None, None, None, None, None, None, "You enter a cellar, musky\
air fills the room, and a lone torch lights the room dim, barrels stacked on their sides fill the east wall and a doorway to another part of the cellar lies\
north, the door up is barred from the other side." )

cellar_room = Room("Cellar", None, None, 'cellar', 'armory', None, None , None, None, 'cellar', 'armory', None, None, None, None, None, "You are in the second\
cellar room, it looks identical to the last one, but a few barrels seem broken and a pile of bones with a sword lies at the bottom at one. West of you is an old Armory")

armory = Room("Dusty Armory", 'door1', 'cellar_room', None, 'hound_death', None, None, 'cellar_room', None, 'hound_death', None, None, None, None, None,None, "You enter\
the armory, the only source of light is a few small holes on the upper wall pouring light into the room. Dusty racks line the south wall, with a few swords covered \
thick in cobweb and dust. North of you is a stairway up, but a door west is pounding every once in a while, looks dangerous.")

hound_death = Room("Rawr", None, None, None, None, None, None, None, None, None, None, None, None, 'death_room', 'death_room', 'death_room', "You approach the banging\
door, and see a wooden bar holding the door close. You lift the bar up and open the door, to be met by a rather large egg in front of you. You see\
the top of the egg start to sprout open, and a small, spider-creature climbs out. It leaps onto your face, hugging it with great force until you die....\
crongrats .-.\n press y")

door1 = Room("Transition", None, None, 'armory', None, None, None, None, None, 'armory', None, None, None, 'wakeup', 'wakeup', 'endless', "You walk up the \
and approach the door.Thed door looks like a regular bedroom door...\nDo you wish to continue?")


watch_tower =Room("Watch Tower", 'walls_ridge', None, None, 'armory', None, None, 'walls_ridge', None, None, 'armory', None, None, None, None, None, "You are\
in the watch tower, it has a magnificient view of the land, in wich you can see mostly forest. North of you is the ridge of the wall, and west is the armory.")

walls_ridge = Room("Walls Ridge", 'watchtower2', None, None, None, None, None, 'watchtower2', None, None, None, None, None, None, None, None, "You approach the\
ridge, you can see on both sides of you the scenery of mountains and rolling hills, youre attracted to the watchtower in front of you. ")

watchtower2 = Room("Watch Tower", 'wallsridge2', None, None, None, None, None, 'wallsridge2', None, None, None, None, None, None, None, None, "You enter the \
watch tower, it is comepletely identical as the last tower, there is also another ridge north of you that strongly attracts you ")

wallsridge2 = Room("Walls Ridge", 'watchtower3', None, 'watchtower2', None, None, None, 'watchtower3', None, 'watchtower2', None, None, None, None, None, None, "You\
enter the walls ridge, same scenery, the hills and mountains that are equally as breathtaking, there is another watch tower north of you.")

watchtower3 = Room("Watch Tower", 'wallsridge3', None, None, None, None, None, 'wallsridge3', None, None, None, None, None, None, None, None,"You\
enter the watch tower, a wave of deja vu washes over you as it looks identical to the last two watch towers, you also catch a little movement as a clay pot rattles. There is the ridge north of you")

wallsridge3 = Room("Walls Ridge", 'watchtower4', None, 'watchtower3', None, None, None, 'watchtower4', None, 'watchtower3', None, None, None, None, None, None,"You\
walk out onto the walls ridge, again, and the same scenery lays out on either side of you, you hear scattering steps behind you, but there is nothing. ANother watchtower lays north of you ")

watchtower4 = Room("Watch Tower", 'wallsridge4', None, None, None, None, None, 'wallsridge4', None, None, None, None, None, None, None, None,"You\
enter the watchtower, same items, but you notice claw marks on the floor and a few windows looking outward are boarded up. The candle flickers as \
you hear more scatters behind you. North is another ridge ")

wallsridge4 = Room("Walls Ridge", 'watchtower5', None, 'ridge_death1', None, None, None, 'watchtower5', None, 'ridge_death1', None, None, None, None, None, None,"You\
leave the watchtower, now on the walls ridge, except everything was significantly different than before, the sunset was now bloodred, a disturbingly appealing\
view, now the scattering footsteps follow your every step. North lies the next watch tower  ")

ridge_death1 = Room("========================================",None, None, None, None, None, None, None, None, None, None, None, None, 'death_room', 'death_room', None, "You\
turn around as you freeze from the fear of something following you, as you turn you see what looks to be a small, red-fur rabbit. As you make eye contact with\
the creature, its small eyes turn blood red, and it starts to bulge on its arms and body. It twitches furiously, and grows to where it is triple the size of you\
. A giant wall of red fur towers above you as you see the not-so-cute rabbit face growl and lunge at you\n......press y")

watchtower5 = Room("Watch Tower", 'wallsridge5', None, None, None, None, None, 'wallsridge5', None, None, None, None, None, None, None, None,"You rush into\
the next tower with the assurance that something is following you. You can see a slight glare of small yellow eyes peering through a cracked jar that was \
just moving. You notice more scratch marks and blood streaks on the boarded windows. The room is tinted in red due to the one window with no boards. North \
is another ridge. ")

wallsridge5 = Room("Walls Ridge", 'watchtower6', None, 'ridge_death2', None, None, None, 'watchtower6', None, 'ridge_death2', None, None, None, None, None, None,"Crashing\
out onto the ridge again, you dont notice you surroundings but you hear those little steps getting faster! Hurry to the tower north of you, dont turn back....")

ridge_death2 = Room("=============================================", None, None, None, None, None, None, None, None, None, None, None, None, 'death_room', 'death_room', None,"You\
stop in your tracks, listening around you, no footsteps.....maybe I'm safe. You turn around to meet a horrifying creature. It looks like a rally tortured man,\
but with two left arms, and both have an extremely sharp blade jammed into the half severved left arms. The right arm is a more normal looking arm, but intead\
of nails on his index and thumb, he had large, sharp metal plaes sticking out acting as makeshift claws. Skin hangs off his face revealing muscle, This guy doent\
look like he wants to sit and talk about it,\n So you die :p ")

watchtower6 = Room("Watch Tower", None, 'cellar', None, None, None, 'cellar', None, 'cellar', None, None, None, 'cellar', None, None, None,"You barge past the\
door of the watchtower, slamming it behind you. You hear the scratches of the creature chasing you against the door, you bar the door. Suprisingly, the room \
is lit well, torches where they are placed and windows free of boards. The red tint in the sky is gone and all you see is dark out in the night. A open hatch\
east leads stairs down.")

































forest_entrance = Room("Paved Path", 'lone_cottage', None, None, None, None , None ,'lone_cottage', None, None, None, None , None, None, None, None, "You\
go down the paved path, trees nice and green, birds chirping snd such, but it wasnt THAT easy, you start to spot blood sreaks on the nicely paved stone,\
you approach a small cottage in the middle of the brush, quiet with no smoke out of the chimmeney. ")

lone_cottage = Room("Front Lawn", 'foyer', 'marked_path', None, None, None, None, 'foyer', 'marked_path', None, None, None, None, None, None, None, "You\
approach the cottage, the front lawn to be exact, the house looks empty and dark, there are also claw markings on the front door, whichs hangs loose north\
of you. East of you is an unmarked path" )

foyer = Room("Foyer", 'kitchen_cottage', 'living_cottage', 'front_lawn', 'bed_roomc', None, None, 'kitchen_cottage', 'living_cottage', 'front_lawn', 'bed_roomc', None, None, None, None, None, "Youre\
in the foyer, you can identify a pair of slippers in front of you, as well for large tuffs of fur scattered. North of you is the kitchen, East is the family\
living room, and west is where the main bedroom would be."  )

kitchen_cottage = Room("Kitchen", None, None, 'foyer', 'bed_roomc', None, None, None, None, 'foyer', 'bed_roomc', None, None, None, None, None, "You enter the\
kitchen the window on your right is shattered, and there seems to be a furnace, the lightly smells of pie, a pathway west leads to the bedroom" )

living_cottage = Room("Living Room", None, None, 'foyer', None, None, None, None, None, 'foyer', None, None, None, None, None, None, "You enter the living room\
, a grand fireplace sits there, with black smoldering wood in the fireplace." )

bed_roomc = Room("Bed Room", None, 'foyer', None, None, None, None, None, 'foyer', None, None, None, None, None, None, None, "You enter the bedroom to a gruesome\
scene, a putrid smell fills the air as you see what looks like a belched wolf dressed in older womans apparel, that is dead, he lies topside with a large, crude\
cut straight trough the center of its belly with stones toppling out of the cut. On the bed is bloody scissors that stains the sheets. ")






















#=============================================================Level 2- Fish Bowl==============================================================
hidden_hatch = Room("OoOoOoOoO", 'Water', None, None, None, None, None,'Water', None, None, None, None, None, None, None, None, "Questionably\
, you get on your knees and look behind the toilet its pretty dark, but you can make out a small handle and the waht looks like hatch. You grab\
the handle, and pull a little, it doesnt budge. You try again, but with a imense pull, loosening it and hearing a loud creak. with one last nudge\
, you lift the thick hatch, resting it against the side of the toilet, you dont smell anything yet, but when you jump down you land with a disturbing\
squish, and the putrid smell fills the air, and look! the hatch slams shut as well. \n You look around in the pitch black, you can faintly see an off \
and on small glow off in the north distace." )

Water = Room("UnderWater", None, None, None, None, 'Beach', 'Under_Castle', None, None, None, None, 'Beach', 'Under_Castle', None, None, None,  "You\
reach the light, the glow was a small light on what looks to be a small circular door, with a wheel handle, you turn the handle with a hard tug and it\
turns a little, you keep turning it until you feel the door budge, its silent as you hear water leaking from the door. The door becomes increasingly heavier\
as you tug it open more, and soon it pushes you back, water flooding in. You are flushed out trough the door and find yourself underwater, breath running out.\
In a flash, you see what looks like a castle down below you, up above you, you see light and what looks to be a beach.....Catching it at the corner of your eye\
is a glimmer of gold.  ")

Beach = Room("Beach", 'east_beach', None, None, None, None, None, 'east_beach', None, None, None, None, None, None, None, None,  "You decide to Swim up\
, as you're running out of breath and you're propelling yourself froward, you see the glint of gold again, exept along with it a large body rushing toward\
you. You swim faster, and feel your hands touch the sand, you crawl up to the shore to see the creature swim away, glint of gold. North of you is the east beach")

east_beach = Room("East Beach", 'glass_wall', 'hut', None, None, None, None,'glass_wall', 'hut', None, None, None, None, None, None, None , "You are at \
the east beach, the sand feels parcticularly synthetic. North of you is what looks to be a wall, and east of you is a hut.")

hut = Room("The Hut", None, None, None, 'east_beach', None, None,None, None, None, 'east_beach', None, None,None, None, None,'You are at the entrance of\
the hut, again, its very synthetic as well...')

glass_wall = Room("THE WALL", None, None, 'east_beach', None, None, None,None, None, 'east_beach', None, None, None, 'escape', 'escape', 'glass_wall', "You\
approach the glass wall, as you get closer, you see a large crack arching to the top, witch looks like the lip of a bowl. Interact with the crack? Yes/No" )
#==========================================================================================================================================================
Under_Castle = Room("OoOoOoOo", 'ballroom', None, None, None, None, None, 'ballroom', None, None, None, None, None, None, None, None, "You swim towards the\
underwater castle. As you're approaching a small door on the side of the castle, you see that glint of gold again, but this time you see where, or what, it \
belongs to.......\nA giant fish? Still endangered you swim faster and reach the door. You tug with all your strength and manage to topple inside and slam the\
door shut against the water pouring in. As you drop the latch, the door is banged forward a few times until the creture goes off.\n You are in a small entryway\
to the castle, North is the only path you can go." )

ballroom = Room("Balroom", None, 'dineroom', None, 'wine_stache', None, None, None, 'dineroom', None, 'wine_stache', None, None, "You enter a balroom, ceiling high,\
a litte bgger inside than what you spectated outside. There is a large circular dance floor in the middle, with one table sitting in the center. A large candle \
is in the middle of the table, creating most of the lighting, but also the two doors a crack open to your West and East" )

dineroom = Room("Dining Room", None, None, None, 'ballroom', None, None, None, None, None, 'ballroom', None, None, None, None, None, "You are in a Large dining\
Room fit for a king. A long tabe stretches out in front of you vertically, with no food on the table. Lining both the right and left walls, i doesnt make any \
sense, but its raining hard outside, Thunder shaking the room and lighting ging off and on, strecthing long shadows in the room." )

wine_statche = Room("Wine Room", None, 'ballroom', 'wine_death', None, 'atticC', None, None,'ballroom', 'wine_death', None, 'atticC', None, None, None, None,"You\
walk in to what looks like a wine stache, barrels fill the room with a heavy wine smell filling the air. Your only\
souce of light is a large hanging chandelier on what looks like and endless ceiling. South is a partly open small wine barrel, and on the wall is an arrow\
scrtched, pointing upward.")

wine_death = Room("Whelp", None, None, None, None, None, None,None, None, None, None, None, None, 'death_room', 'death_room', 'death_room', "You go to the barrel\
stumbling with extreme thirst for wine. As you begin to pry open a barrel, the lid pops off bouncing off your face. As you get up you see a bakers dozen of small\
adorable whelps stumble out. Piling up, they start to sorta-drunk fly, and alarmed by your presence they start to shoot poorly aimed fire balls. As youre stunned\
by the adorable spectacle, you catch on fire ")





#==============================================================Level 3- The House===========================================================================
escape = Room("---------------------------", 'bed', 'drawers', None, None, None, None,'bed', 'drawers', None, None, None, None, 'wakeup', 'wakeup', 'wakeup',"You reach\
toward the crack and feel that its uneven, you can see your reflection in the glass, when you look out, you see a large creature....wait! its a cat! The cat\
is massive, but is luckily on the other side of the glass, Which is also a little particular....Its a fishbowl! how did I get so small? before enough time to\
think, the cat strikes the glass, creating the already large crack to expand more. You hear as the glass stresses and finnally gives out, with you tumbling out\
with mixed sand and water out onto what looks like a wood surface. You tumble off the edge of the table, and land hard on the floor, spatting beside you is a huge\
goldfish which flops around hopelessly gasping for air, glinting gold. The huge cat leaps down and gulps the fish, the cat proceeds to sniff around\n\n\n\n You have reached the end of the beta, press y to continue..." )
#======================================================================================================================================================
wakeup = Room("Wake....Up", None, None, None,None,None,None,None, None, None, None,None,None,None,None, None, None, None, "You slowly open your eyes, and see a\
ceiling fan spinning above you slowly, you look to you sides and see a slightly cracked fishbowl on your drawer, and an artificial landscape on top of a dresser.\
Above you, a little off the side of the fan, hangs a spaceship model...........\n\n\n\n\n\nCongrats! You have finished the game!!\
'\
                                .   *        .       . \n\
                        *      -0- \n\
                        .                .  *       * .          .      *       o       . \n\
                o              |                           \n\
                        .     -O-              .             *\n\
                               |                                               .\n\
                      ____                            _         _       _   _                 _ \n\
                     / ___|___  _ __   __ _ _ __ __ _| |_ _   _| | __ _| |_(_) ___  _ __  ___| |\n\
                    | |   / _ \| ._ \ / _. | .__/ _. | __| | | | |/ _. | __| |/ _ \| ._ \/ __| |\n\
                    | |__| (_) | | | | (_| | | | (_| | |_| |_| | | (_| | |_| | (_) | | | \__ \_|\n\
                     \____\___/|_| |_|\__, |_|  \__,_|\__|\__,_|_|\__,_|\__|_|\___/|_| |_|___(_)\n\
                                      |___/ \n\
                      	                                                     |\n\
                            .   *        .       .            .      *      -o- \n\
                *              |                                             |\n\
                        .     -O-                     |\n\
                .              |        .     .      -0-       .      *       .       . \n\
                o                                     |\n\
                                    .     *\n\
                    .                         *      .     .       .      *       o       . \n\
\n\
                                            .\n\
                                    ")




#def save():
 #   global node
  #  with open('savegame.dat', 'wb') as f :
   #     pickle.dump([node, ],f, protocol=2)
    #print "Game: Saved"

#def load():
 #   global node, player
  #  with open('savegame.dat', 'rb') as f :
   #     name,  = pickle.load(f)
    #print "Past Game: Loaded"

node = intro_screen
while True:
    print node.name
    print node.description
    movement = ["north", "south", "east", "west","up", "down", "n", "e", "s", "w", "u", "d", "yes", "no", "y"]
    quit = ["q", "quit", "exit"]
    command = raw_input(" > ")

    if command in quit:
        sys.exit(0)

    #elif command in ["save"]:
     #   save()
    #elif command is ["load"]:
     #   load()


    if command in movement:
        try:
            node.move(command)
        except:
            print "You can't move that way"
