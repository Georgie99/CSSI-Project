import webapp2
import jinja2
import random
import os
from model import Character
from model import User
from google.appengine.api import users
from google.appengine.ext import ndb

jinja_environment = jinja2.Environment(
    loader = jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions = ['jinja2.ext.autoescape'],
    autoescape = False)

def putChars():
    Mario= Character(name= "Mario", speed= 7, strength= 8 , skill= 1, color= "red", wiki_link= "https://www.ssbwiki.com/Mario", image_url= "http://mario.nintendo.com/assets/img/home/intro/mario-pose2.png", up_b="Super Punch Jump", side_b="Cape", down_b="FLUDD",votes=0)
    Luigi= Character(name= "Luigi", speed= 3, strength= 9 , skill= 1, color= "green", wiki_link= "https://www.ssbwiki.com/Luigi", image_url="https://www.ssbwiki.com/images/thumb/e/e2/Luigi_SSB4.png/250px-Luigi_SSB4.png", up_b="Super Jump Punch", side_b="Green Missile", down_b="Luigi Cyclone",votes=0)
    Peach= Character(name= "Peach", speed= 3, strength= 8, skill= 2, color= "pink", wiki_link= "https://www.ssbwiki.com/Princess_Peach",image_url="https://vignette.wikia.nocookie.net/nintendo/images/8/83/Peach_MP100.png/revision/latest?cb=20170918143319&path-prefix=en", up_b="Peach Parasol", side_b="Peach Bomber", down_b="Vegetable",votes=0)
    Bowser= Character(name= "Bowser", speed= 7, strength= 6, skill= 2 , color= "green", wiki_link= "https://www.ssbwiki.com/Bowser",image_url="https://www.mariowiki.com/images/thumb/7/7e/Bowser_-_Mario_Party_10.png/250px-Bowser_-_Mario_Party_10.png", up_b="Whirling Fortress", side_b="Flying Slam", down_b="Bowser Bomb",votes=0)
    Dr_Mario= Character(name= "Dr. Mario", speed= 2, strength= 6, skill= 3 , color= "black", wiki_link= "https://www.ssbwiki.com/Dr._Mario", image_url="https://www.mariowiki.com/images/thumb/e/ec/Dr_Mario_-_Dr_Mario_Miracle_Cure.png/250px-Dr_Mario_-_Dr_Mario_Miracle_Cure.png", up_b="Super Jump Punch", side_b="Super Sheet", down_b="Dr. Tornado",votes=0)
    Yoshi= Character(name= "Yoshi", speed= 8, strength= 7, skill= 2 , color= "green", wiki_link= "https://www.ssbwiki.com/Yoshi", image_url="https://www.mariowiki.com/images/thumb/4/4d/Yoshi_-_Mario_Party_10.png/150px-Yoshi_-_Mario_Party_10.png", up_b="Egg Throw", side_b="Egg Roll", down_b="Yoshi Bomb",votes=0)
    Donkey_Kong= Character(name= "Donkey Kong", speed= 8, strength= 7, skill= 2 , color= "red", wiki_link= "https://www.ssbwiki.com/Donkey_Kong", image_url="https://www.ssbwiki.com/images/thumb/5/5f/Donkey_Kong_SSB4.png/250px-Donkey_Kong_SSB4.png", up_b="Spinning Kong", side_b="Hand Slap", down_b="Headbutt",votes=0)
    Diddy_Kong= Character(name= "Diddy Kong", speed= 8, strength= 9, skill= 1 , color= "red", wiki_link= "https://www.ssbwiki.com/Diddy_Kong", image_url="https://vignette.wikia.nocookie.net/donkeykong/images/7/76/Diddy_kong_01.png/revision/latest?cb=20120710020003", up_b="Rocket Barrel Boost", side_b="Monkey Flip", down_b="Banana Peel",votes=0)
    Link= Character(name= "Link", speed= 2, strength= 5, skill= 2 , color= "green", wiki_link= "https://www.ssbwiki.com/Link", image_url="https://vignette.wikia.nocookie.net/videogames-fanon/images/1/1d/Link_SSB4_box.png/revision/latest?cb=20150615103921", up_b="Spin Attack", side_b="Gale Boomerang", down_b="Bomb",votes=0)
    Zelda= Character(name= "Zelda", speed= 2, strength= 4, skill= 3, color= "pink", wiki_link= "https://www.ssbwiki.com/Princess_Zelda", image_url="https://www.zelda.com/assets/img/about/zelda_play.png",up_b="Farore\'s Wind", side_b="Din\'s Fire", down_b="Phantom Slash",votes=0)
    Sheik= Character(name= "Sheik", speed= 9, strength= 9, skill= 1 , color= "blue", wiki_link= "https://www.ssbwiki.com/Sheik", image_url="https://vignette.wikia.nocookie.net/zelda/images/8/82/Sheik_%28SSB_3DS_%26_Wii_U%29.png/revision/latest?cb=20140414232000", up_b="Vanish", side_b="Burst Grenade", down_b="Bouncing Fish",votes=0)
    Ganondorf= Character(name= "Ganondorf", speed= 1, strength= 6, skill= 3 , color= "black", wiki_link= "https://www.ssbwiki.com/Ganondorf", image_url="https://vignette.wikia.nocookie.net/zelda/images/0/05/Ganondorf_Artwork_%28Ocarina_of_Time%29.png/revision/latest/scale-to-width-down/254?cb=20110427012646", up_b="Dark Dive", side_b="Flame Choke", down_b="Wizard\'s Foot",votes=0)
    Toon_Link= Character(name= "Toon Link", speed= 6, strength= 5, skill= 2, color= "green", wiki_link= "https://www.ssbwiki.com/Toon_Link", image_url="https://www.ssbwiki.com/images/thumb/0/0d/ToonLinkHWL.png/275px-ToonLinkHWL.png", up_b="Spin Attack", side_b="Boomerang", down_b="Bomb",votes=0)
    Samus= Character(name= "Samus", speed= 4, strength= 4, skill= 3 , color= "orange", wiki_link= "https://www.ssbwiki.com/Samus_Aran", image_url="https://upload.wikimedia.org/wikipedia/en/thumb/2/21/Metroidprime3_1.png/220px-Metroidprime3_1.png", up_b="Screw Attack", side_b="Missile", down_b="Bomb",votes=0)
    Zero_Suit_Samus= Character(name= "Zero Suit Samus", speed= 9, strength= 9, skill= 1, color= "blue", wiki_link= "https://www.ssbwiki.com/Zero_Suit_Samus", image_url="https://www.ssbwiki.com/images/thumb/5/59/Zero_Suit_Samus_SSB4.png/250px-Zero_Suit_Samus_SSB4.png", up_b="Boost Kick", side_b="Plasma Whip", down_b="Flip Jump",votes=0)
    Kirby= Character(name= "Kirby", speed= 3, strength= 6, skill= 3, color= "pink", wiki_link= "https://www.ssbwiki.com/Kirby", image_url="https://upload.wikimedia.org/wikipedia/en/thumb/5/5c/Kirby.png/220px-Kirby.png", up_b="Final Cutter", side_b="Hammer Flip", down_b="Stone",votes=0)
    Meta_Knight= Character(name= "Meta Knight", speed= 8, strength= 9, skill= 1, color= "blue", wiki_link= "https://www.ssbwiki.com/Meta_Knight", image_url="https://upload.wikimedia.org/wikipedia/en/thumb/6/6a/Meta_knight_art.png/220px-Meta_knight_art.png", up_b="Shuttle Loop", side_b="Drill Rush", down_b="Dimensional Cape",votes=0)
    King_Dedede= Character(name= "King Dedede", speed= 2, strength= 5, skill= 3, color= "red", wiki_link= "https://www.ssbwiki.com/King_Dedede", image_url="https://www.ssbwiki.com/images/thumb/5/5b/King_Dedede_KSA.png/275px-King_Dedede_KSA.png", up_b="Super Dedede Jump", side_b="Gordo Toss", down_b="Jet Hammer",votes=0)
    Fox= Character(name= "Fox", speed= 9, strength= 8, skill= 1, color= "green", wiki_link= "https://www.ssbwiki.com/Fox_McCloud", image_url="https://www.ssbwiki.com/images/thumb/7/74/Fox_SSB4.png/250px-Fox_SSB4.png", up_b="Fire Fox", side_b="Fox Illusion", down_b="Reflector",votes=0)
    Falco= Character(name= "Falco", speed= 4, strength= 7, skill= 3, color= "blue", wiki_link= "https://www.ssbwiki.com/Falco_Lombardi", image_url="https://www.ssbwiki.com/images/thumb/5/5f/Falco_SSB4.png/250px-Falco_SSB4.png", up_b="Fire Bird", side_b="Falco Phantasm", down_b="Reflector",votes=0)
    Pikachu= Character(name= "Pikachu", speed= 9, strength= 8, skill= 1, color= "yellow", wiki_link= "https://www.ssbwiki.com/Pikachu", image_url="https://www.ssbwiki.com/images/thumb/a/a0/Pikachu_SSB4.png/250px-Pikachu_SSB4.png", up_b="Quick Attack", side_b="Skull Bash", down_b="Thunder",votes=0)
    Jigglypuff= Character(name= "Jigglypuff", speed= 5, strength= 6, skill= 3, color= "pink", wiki_link= "https://www.ssbwiki.com/Jigglypuff", image_url="https://www.ssbwiki.com/images/thumb/a/a6/Jigglypuff_SSB4.png/250px-Jigglypuff_SSB4.png", up_b="Sing", side_b="Pound", down_b="Rest",votes=0)
    Mewtwo= Character(name= "Mewtwo", speed= 9, strength= 8, skill= 1, color= "pink", wiki_link= "https://www.ssbwiki.com/Mewtwo", image_url="https://www.ssbwiki.com/images/thumb/d/da/Mewtwo_SSB4.png/250px-Mewtwo_SSB4.png", up_b="Up B", side_b="Left/Right B", down_b="Down B",votes=0)
    Charizard= Character(name= "Charizard", speed= 7, strength= 5, skill= 3, color= "orange", wiki_link= "https://www.ssbwiki.com/Charizard", image_url="https://www.ssbwiki.com/images/thumb/c/c1/Charizard_SSB4.png/300px-Charizard_SSB4.png", up_b="Fly", side_b="Flare Blitz", down_b="Rock Smash",votes=0)
    Lucario= Character(name= "Lucario", speed= 4, strength= 8, skill= 1, color= "blue", wiki_link= "https://www.ssbwiki.com/Lucario", image_url="https://www.ssbwiki.com/images/thumb/a/af/Lucario_SSB4.png/250px-Lucario_SSB4.png", up_b="Extreme Speed", side_b="Force Palm", down_b="Double Team",votes=0)
    Captain_Falcon= Character(name= "Captain Falcon", speed= 9, strength= 9, skill= 2, color= "blue", wiki_link= "https://www.ssbwiki.com/Captain_Falcon", image_url="https://www.ssbwiki.com/images/thumb/7/74/GX_Captain_Falcon.png/275px-GX_Captain_Falcon.png", up_b="Falcon Dive", side_b="Raptor Boost", down_b="Falcon Kick",votes=0)
    Ness= Character(name= "Ness", speed= 3, strength= 9, skill= 2, color= "red", wiki_link= "https://www.ssbwiki.com/Ness", image_url="https://www.ssbwiki.com/images/thumb/1/1a/Ness_SSB4.png/250px-Ness_SSB4.png", up_b="PK Thunder", side_b="PK Fire", down_b="PSI Magnet",votes=0)
    Lucas= Character(name= "Lucas", speed= 4, strength= 7, skill= 2, color= "yellow", wiki_link= "https://www.ssbwiki.com/Lucas", image_url="https://www.ssbwiki.com/images/thumb/8/88/Lucas_SSB4.png/250px-Lucas_SSB4.png", up_b="Up Special", side_b="Left/Right Special", down_b="Down Special",votes=0)
    Marth= Character(name= "Marth", speed= 8, strength= 7, skill= 1, color= "blue", wiki_link= "https://www.ssbwiki.com/Marth", image_url="https://www.ssbwiki.com/images/thumb/7/79/Marth_SSB4.png/250px-Marth_SSB4.png", up_b="Dolphin Slash", side_b="Dancing Blade", down_b="Counter",votes=0)
    Roy= Character(name= "Roy", speed= 9, strength= 8, skill= 3, color= "blue", wiki_link= "https://www.ssbwiki.com/Roy", image_url="https://www.ssbwiki.com/images/thumb/4/45/Roy_SSB4.png/250px-Roy_SSB4.png", up_b="Up Special", side_b="Left/Right Special", down_b="Down Special",votes=0)
    Ike= Character(name= "Ike", speed= 5, strength= 7, skill= 3, color= "red", wiki_link= "https://www.ssbwiki.com/Ike", image_url="https://www.ssbwiki.com/images/thumb/e/e8/Ike_SSB4.png/250px-Ike_SSB4.png", up_b="Aether", side_b="Quick Draw", down_b="Counter",votes=0)
    Mr_Game_Watch= Character(name= "Mr. Game & Watch", speed= 6, strength= 6, skill= 3, color= "black", wiki_link= "https://www.ssbwiki.com/Mr._Game_%26_Watch", image_url="https://www.ssbwiki.com/images/thumb/b/b2/Mr._Game_%26_Watch_SSB4.png/250px-Mr._Game_%26_Watch_SSB4.png", up_b="Fire", side_b="Judge", down_b="Oil Panic",votes=0)
    Pit= Character(name= "Pit", speed= 5, strength= 7, skill= 2, color= "blue", wiki_link= "https://www.ssbwiki.com/Pit", image_url="https://www.ssbwiki.com/images/thumb/4/41/Pit_SSB4.png/250px-Pit_SSB4.png", up_b="Power of Flight", side_b="Upperdash Arm", down_b="Guardian Orbitars",votes=0)
    Wario= Character(name= "Wario", speed= 7, strength= 6, skill= 3, color= "yellow", wiki_link= "https://www.ssbwiki.com/Wario",image_url="https://www.ssbwiki.com/images/thumb/1/15/Wario_SSB4.png/250px-Wario_SSB4.png", up_b="Corkscrew", side_b="Wario Bike", down_b="Wario Waft",votes=0)
    Olimar= Character(name= "Olimar", speed= 2, strength= 6, skill= 2, color= "yellow", wiki_link= "https://www.ssbwiki.com/Captain_Olimar", image_url="https://www.ssbwiki.com/images/thumb/2/20/Olimar_SSB4.png/250px-Olimar_SSB4.png", up_b="Winged Pikmin", side_b="Pikmin Throw", down_b="Pikmin Order",votes=0)
    rob= Character(name= "R.O.B.", speed= 6, strength= 6, skill= 2, color= "black", wiki_link= "https://www.ssbwiki.com/R.O.B.", image_url="https://www.ssbwiki.com/images/thumb/b/b6/R.O.B._SSB4.png/245px-R.O.B._SSB4.png", up_b="Robo Burner", side_b="Arm Rotor", down_b="Gyro",votes=0)
    Sonic= Character(name= "Sonic", speed= 10, strength= 8, skill= 1, color= "blue", wiki_link= "https://www.ssbwiki.com/Sonic_the_Hedgehog", image_url="https://www.ssbwiki.com/images/thumb/f/f3/Sonic_SSB4.png/250px-Sonic_SSB4.png", up_b="Spring Jump", side_b="Spin Dash", down_b="Spin Charge",votes=0)
    Rosalina_Luma= Character(name= "Rosalina & Luma", speed= 6, strength= 6, skill= 1, color= "blue", wiki_link= "https://www.ssbwiki.com/Rosalina", image_url="https://www.ssbwiki.com/images/thumb/c/c8/Rosalina_SSB4.png/250px-Rosalina_SSB4.png", up_b="Launch Star", side_b="Star Bits", down_b="Gravitational Pull",votes=0)
    Bowser_Jr= Character(name= "Bowser Jr.", speed= 5, strength= 5, skill= 3, color= "green", wiki_link= "https://www.ssbwiki.com/Bowser_Jr.", image_url="https://www.ssbwiki.com/images/thumb/5/5e/Bowser_Jr._artwork.png/320px-Bowser_Jr._artwork.png", up_b="Abandon Ship", side_b="Clown Kart Dash", down_b="Mechakoopa",votes=0)
    Greninja= Character(name= "Greninja", speed= 9, strength= 8, skill= 2, color= "blue", wiki_link= "https://www.ssbwiki.com/Greninja", image_url="https://www.ssbwiki.com/images/thumb/5/5e/Greninja_SSB4.png/250px-Greninja_SSB4.png", up_b="Hydro Pump", side_b="Shadow Sneak", down_b="Substitute",votes=0)
    Robin= Character(name= "Robin", speed= 2, strength= 7, skill= 3, color= "black", wiki_link= "https://www.ssbwiki.com/Robin", image_url="https://vignette.wikia.nocookie.net/ssb/images/0/06/Robin_%28male%29.png/revision/latest/scale-to-width-down/250?cb=20160311000432", up_b="Elwind", side_b="Arcfire", down_b="Nosferatu",votes=0)
    Lucina= Character(name= "Lucina", speed= 8, strength=6, skill= 2, color= "blue", wiki_link= "https://www.ssbwiki.com/Lucina", image_url="https://www.ssbwiki.com/images/thumb/5/55/Lucina_SSB4.png/250px-Lucina_SSB4.png", up_b="Dolphin Slash", side_b="Dancing Blade", down_b="Counter",votes=0)
    Corrin = Character(name= "Corrin", speed= 4, strength= 8, skill= 2, color="blue", wiki_link= "https://www.ssbwiki.com/Corrin", image_url="https://vignette.wikia.nocookie.net/ssb/images/c/cc/Corrin_%28female%29.png/revision/latest?cb=20160310235032", up_b="Dragon Ascent", side_b="Counter Surge", down_b="Dragon Lunge",votes=0)
    Palutena= Character(name= "Palutena", speed= 8, strength= 5, skill= 3, color= "green", wiki_link= "https://www.ssbwiki.com/Palutena",image_url="https://www.ssbwiki.com/images/thumb/8/8e/Palutena_Uprising.png/250px-Palutena_Uprising.png", up_b="Warp", side_b="Reflect Barrier", down_b="Counter",votes=0)
    Dark_Pit = Character(name= "Dark Pit", speed= 5, strength= 7, skill= 2, color= "black", wiki_link= "https://www.ssbwiki.com/Dark_Pit", image_url="https://www.ssbwiki.com/images/thumb/0/06/Dark_Pit_SSB4.png/250px-Dark_Pit_SSB4.png", up_b="Power of FLight", side_b="Electrshock Arm", down_b="Guardian Orbitars",votes=0)
    Villager= Character(name= "Villager", speed= 2, strength= 7, skill= 2, color= "red", wiki_link= "https://www.ssbwiki.com/Villager", image_url="https://www.ssbwiki.com/images/thumb/e/eb/Villager_SSB4.png/250px-Villager_SSB4.png", up_b="Ballon Trip", side_b="Lloid Rocket", down_b="Timber",votes=0)
    Little_Mac= Character(name= "Little Mac", speed= 9, strength= 9, skill= 3, color= "green", wiki_link= "https://www.ssbwiki.com/Little_Mac", image_url="https://www.ssbwiki.com/images/thumb/3/3c/Little_Mac_SSB4.png/250px-Little_Mac_SSB4.png", up_b="Rising Uppercut", side_b="Jolt Haymaker", down_b="Slip Counter",votes=0)
    Wii_Fit_Trainer= Character(name= "Wii Fit Trainer", speed= 6, strength= 7, skill= 3, color= "blue", wiki_link= "https://www.ssbwiki.com/Wii_Fit_Trainer", image_url="https://vignette.wikia.nocookie.net/ssb/images/e/e9/Male_Wii_Fit_Trainer_SSB4.png/revision/latest?cb=20160310234723", up_b="Super Hoop", side_b="Left/Right Special", down_b="Deep Breathing",votes=0)
    Shulk= Character(name= "Shulk", speed= 5, strength= 5, skill= 2, color= "red", wiki_link= "https://www.ssbwiki.com/Shulk", image_url="https://www.ssbwiki.com/images/thumb/d/d3/Shulk_SSB4.png/250px-Shulk_SSB4.png", up_b="Air Slash", side_b="Back Slash", down_b="Vision",votes=0)
    Duck_Hunt = Character(name= "Duck Hunt", speed= 6, strength= 4, skill= 2, color= "orange", wiki_link= "https://www.ssbwiki.com/Duck_Hunt", image_url="https://www.ssbwiki.com/images/thumb/2/2e/Duck_Hunt_SSB4.png/250px-Duck_Hunt_SSB4.png", up_b="Duck Jump", side_b="Clay Shooting", down_b="Wild Gunman",votes=0)
    Mega_Man= Character(name= "Mega Man", speed= 4, strength= 5, skill= 3, color= "blue", wiki_link= "https://www.ssbwiki.com/Mega_Man", image_url="https://www.ssbwiki.com/images/thumb/b/bf/Mega_Man_SSB4.png/250px-Mega_Man_SSB4.png", up_b="Rush Coil", side_b="Crash Bomber", down_b="Leaf Shield",votes=0)
    Pac_Man= Character(name= "Pac-Man", speed= 5, strength= 5, skill= 3, color= "yellow", wiki_link= "https://www.ssbwiki.com/Pac-Man", image_url="https://www.ssbwiki.com/images/thumb/0/0f/Pac-Man_World_2.png/275px-Pac-Man_World_2.png", up_b="Pac-Jump", side_b="Power Pellet", down_b="Fire Hyrant",votes=0)
    Ryu= Character(name= "Ryu", speed= 5, strength= 8 , skill= 1, color= "red", wiki_link= "https://www.ssbwiki.com/Ryu", image_url="https://www.ssbwiki.com/images/thumb/6/63/Ryu_SSB4.png/250px-Ryu_SSB4.png", up_b="Dragon Punch", side_b="Hurricane", down_b="Focus Attack",votes=0)
    Cloud = Character(name= "Cloud", speed= 9, strength= 9, skill= 1, color= "black", wiki_link= "https://www.ssbwiki.com/Cloud_Strife", image_url="https://www.ssbwiki.com/images/thumb/5/57/Cloud_SSB4.png/255px-Cloud_SSB4.png", up_b="Climhazzard", side_b="Cross Slash", down_b="Limit Break",votes=0)
    Bayonetta= Character(name= "Bayonetta", speed= 5, strength= 10, skill= 1, color= "black", wiki_link= "https://www.ssbwiki.com/Bayonetta", image_url="https://vignette.wikia.nocookie.net/ssb/images/c/cd/Bayonetta_Original_SSB4.png/revision/latest?cb=20160310235439", up_b="Witch Twist", side_b="After Burner Kick", down_b="Witch Time/Bat Within",votes=0)
    Mario.put()
    Luigi.put()
    Peach.put()
    Bowser.put()
    Dr_Mario.put()
    Yoshi.put()
    Donkey_Kong.put()
    Diddy_Kong.put()
    Link.put()
    Zelda.put()
    Sheik.put()
    Ganondorf.put()
    Toon_Link.put()
    Samus.put()
    Zero_Suit_Samus.put()
    Kirby.put()
    Meta_Knight.put()
    King_Dedede.put()
    Fox.put()
    Falco.put()
    Pikachu.put()
    Jigglypuff.put()
    Mewtwo.put()
    Charizard.put()
    Lucario.put()
    Captain_Falcon.put()
    Ness.put()
    Lucas.put()
    Marth.put()
    Roy.put()
    Ike.put()
    Mr_Game_Watch.put()
    Pit.put()
    Wario.put()
    Olimar.put()
    rob.put()
    Sonic.put()
    Rosalina_Luma.put()
    Bowser_Jr.put()
    Greninja.put()
    Robin.put()
    Lucina.put()
    Corrin.put()
    Palutena.put()
    Dark_Pit.put()
    Villager.put()
    Little_Mac.put()
    Wii_Fit_Trainer.put()
    Shulk.put()
    Duck_Hunt.put()
    Mega_Man.put()
    Pac_Man.put()
    Ryu.put()
    Cloud.put()
    Bayonetta.put()


class HomePage(webapp2.RequestHandler):
    def get(self):
        home_template = jinja_environment.get_template('templates/home.html')
        self.response.write(home_template.render())

class LoginPage(webapp2.RequestHandler):
    def get(self):
        chars_fetch = Character.query().fetch()
        if(chars_fetch==[]):
            putChars()
        login_template = jinja_environment.get_template('templates/login.html')
        user = users.get_current_user()
        print(user)
        user_query = User.query()
        user_fetch = user_query.fetch()
        if user:
            email_address = user.nickname()
            signout_link_html = '<a class="mdl-button mdl-js-button mdl-button--raised mdl-js-ripple-effect starttext" href="%s">sign out</a>' % (users.create_logout_url('/'))
            previous_user = False
            for i in user_fetch:
                if(str(i.email_address)==email_address):
                    previous_user = True
                    now_user = i
            if previous_user:
                text1 = "Welcome %s!" % (now_user.first_name)
                text2 ="<form action='/home'><button class='mdl-button mdl-js-button mdl-button--raised mdl-js-ripple-effect starttext'>Go to Site</button><br> %s <br></form><br>" % signout_link_html
            else:
                text1 = "Welcome, %s!  Please sign up!" % (email_address)
                text2 = "<br><form method='post'><p style='color: white; font-size: 18px;'>First name: </p><input type='text' name='first_name'><p style='color: white; font-size: 18px;'>Last name: </p><input type='text' name='last_name'><br><input type='submit' class='mdl-button mdl-js-button mdl-button--raised mdl-js-ripple-effect starttext'></form><br> %s <br>" %  (signout_link_html)
        else:
            text1 = "Welcome! Please log in!"
            text2 = "<br><a class='mdl-button mdl-js-button mdl-button--raised mdl-js-ripple-effect starttext' href='%s'>Sign in</a>" % (users.create_login_url('/'))
        text_dict = {'text1':text1,'text2':text2}
        self.response.write(login_template.render(text_dict))
    def post(self):
        user = users.get_current_user()
        print(user)
        email_address = user.nickname()
        first_name = self.request.get("first_name")
        last_name = self.request.get("last_name")
        new_user = User(email_address=email_address,first_name=first_name,last_name=last_name,saved_chars=[])
        new_user.put()
        self.redirect('/home')

class PreferencePage(webapp2.RequestHandler):
    def get(self,input_dict={}):
        prefs_template = jinja_environment.get_template('templates/prefs.html')
        self.response.write(prefs_template.render(input_dict))
        user = users.get_current_user()
        print(user)
    def post(self):
        user = users.get_current_user()
        print(user)
        user_query = User.query()
        if user:
            user_fetch = user_query.filter(User.email_address==user.nickname()).fetch()[0]
            user_id = user_fetch.key.id()
            print(user_id)
        if(self.request.get("type")=="show"):
            skill = self.request.get("skill")
            pref = self.request.get("pref")
            color = self.request.get("color")
            character_query = Character.query()
            if(pref=="strength"):
                characters = character_query.filter(Character.skill==int(skill),Character.color==color,Character.strength>5).order(-Character.strength).fetch()
            else:
                characters = character_query.filter(Character.skill==int(skill),Character.color==color,Character.speed>5).order(-Character.speed).fetch()
            if(characters==[]):
                if(pref=="strength"):
                    characters = character_query.filter(Character.skill==int(skill),Character.strength>5).order(-Character.strength).fetch()
                else:
                    characters = character_query.filter(Character.skill==int(skill),Character.speed>5).order(-Character.speed).fetch()
            character_dict = {'characters':characters,'userid':user_id}
            self.get(character_dict)
        elif(self.request.get("type")=="addChar"):
            user_fetch = User.query().fetch()
            for i in user_fetch:
                print(i.key.id())
                if(i.key.id()==int(self.request.get("userId"))):
                    now_user = i
            now_user.saved_chars.append(ndb.Key('Character',int(self.request.get("characterKey"))))
            print(self.request.get("characterKey"))
            now_user.put()
        elif(self.request.get("type")=="addVote"):
            char_fetch = Character.query().fetch()
            for i in char_fetch:
                # print(i.key.id())
                print(self.request.get("characterKey"))
                if(i.key.id()==int(self.request.get("characterKey"))):
                    now_char = i
            now_char.votes = now_char.votes + 1
            now_char.put()
class AboutPage(webapp2.RequestHandler):
    def get(self):
        n = ''
        home_template = jinja_environment.get_template('templates/about.html')
        character_query = Character.query()
        characters= character_query.order(Character.name).fetch()
        character_dict = {'characters':characters}
        # def NameandrandomNumber(name):
        #     thing="../%s/%d.gif"%(name, random.randint(1,4))
        #     return thing
        self.response.write(home_template.render(character_dict))
    def post(self):
        char_fetch = Character.query().fetch()
        for i in char_fetch:
            print(self.request.get("characterKey"))
            if(i.key.id()==int(self.request.get("characterKey"))):
                now_char = i
        now_char.votes = now_char.votes + 1
        now_char.put()

class ProfilePage(webapp2.RequestHandler):
    def get(self):
        profile_template = jinja_environment.get_template('templates/profile.html')
        user = users.get_current_user()
        print(user)
        user_query = User.query()
        user_fetch = user_query.fetch()
        signout_link_html = '<a href="%s">sign out</a>' % (users.create_logout_url('/'))
        line2 = ""
        line3 = ""
        if user:
            for i in user_fetch:
                email_address = user.nickname()
                if(i.email_address==email_address):
                    now_user = i
            line2 = "Welcome " + now_user.first_name + " " + now_user.last_name
            line3 = "Your email address: " + now_user.email_address
        else:
            line2 = "Sorry, please log in to continue."
            line3 = ""
        lines_dict = {'line2':line2,'line3':line3, 'line1':now_user.saved_chars}
        self.response.write(profile_template.render(lines_dict))

class LeaderboardPage(webapp2.RequestHandler):
    def get(self):
        leaderboard_template = jinja_environment.get_template('templates/leaderboard.html')
        characters = Character.query().order(-Character.votes).fetch()
        char_div = {'characters':characters}
        self.response.write(leaderboard_template.render(char_div))

app = webapp2.WSGIApplication([
    ('/', LoginPage),
    ('/home',HomePage),
    ('/prefs', PreferencePage),
    ('/abt', AboutPage),
    ('/profile',ProfilePage),
    ('/leaderboard',LeaderboardPage)
], debug=True)
