
#chara head images

image side ben = "images/inventory/inventory_hud/head.png"
image side sarg = "images/char/head/sarg_head.png"
image side sam = "images/char/head/sam_head.png"
#chara defines

define BAG = Character("Bagman",color="#b66c12")
define BAL = Character("Baldi")
define BEN = Character("Benjamin", image = "ben")
define BON = Character("Bonehead")
define DAV = Character("David")
define DEE = Character("Deerik")
define DOM = Character("Domonic")
define DRI = Character("Drill Sarg",color="#12a3b6", image = "sarg")
define JES = Character("Jesus")
define MAR = Character("Marc")
default selected_item = None
define MEO = Character("Meowbahh")
define MIK = Character("Mike")
define MAR = Character("Marc")
define EMA = Character("Emma")
define MYS = Character("Mystery Man")
define PLA = Character("Placeholder")
define PRE = Character("President")
define LT = Character("Lieutenant", color="#c4a74a") # Added Lieutenant
define SAM = Character("Samuel",color="#b66c1261", image = "sam")
define SIM = Character("Sim")
define SUL = Character("Sultan",color="#aeadb7")
define ZUN = Character("Zundamon",color="#B9D08B")
#default 
define Q = Character ("?????",color="#0000FF")
define Q2 = Character ("?????",color="#8fe406ff")
define Q3 = Character ("??????",color="#14a122")
define Q4 = Character ("???????",color="#97239e")
define k =Character("Keemstar",color="#0000FF")
define co = Character("Commanding Officer Miller",color="#0000FF")
#Background
image ani1_background:
    Animation(
        "images/bg/Starting_Room/2/satgescene1.png", 0.1,
        "images/bg/Starting_Room/2/satgescene2.png", 0.1,
        "images/bg/Starting_Room/2/satgescene3.png", 0.1,
        "images/bg/Starting_Room/2/satgescene4.png", 0.1,
        "images/bg/Starting_Room/2/satgescene5.png", 0.1,
        "images/bg/Starting_Room/2/satgescene6.png", 0.1,
        "images/bg/Starting_Room/2/satgescene7.png", 0.1,
        "images/bg/Starting_Room/2/satgescene8.png", 0.1,
        "images/bg/Starting_Room/2/satgescene9.png", 99999999.1 # Holds on the last frame (not always needed)
    )
    xysize (config.screen_width, config.screen_height) # always needed to upscale image to frame

image smolbenwalk:
    "images/char/Benjerman/walk/smolbenwalk[walk_frame + 1].png"
image drillsargpickup:
    xysize (config.screen_width, config.screen_height)
    "images/bg/Starting_Room/3/drillsargpickupstart1.png"
    pause 0.6
    "images/bg/Starting_Room/3/drillsargpickupstart2.png"
    pause 0.1
    "images/bg/Starting_Room/3/drillsargpickupstart3.png"
    pause 0.1
    "images/bg/Starting_Room/3/drillsargpickupstart4.png"
    pause 0.1
    "images/bg/Starting_Room/3/drillsargpickupstart5.png"
    pause 0.1
    "images/bg/Starting_Room/3/drillsargpickupstart6.png"
    pause 0.1
    "images/bg/Starting_Room/3/drillsargpickupstart7.png"
    pause 0.1
    "images/bg/Starting_Room/3/drillsargpickupstart8.png"
    pause 0.1
    "images/bg/Starting_Room/3/drillsargpickupstart9.png"
    pause 0.1
    "images/bg/Starting_Room/3/drillsargpickupstart10.png"
    pause 0.1
    "images/bg/Starting_Room/3/drillsargpickupstart11.png"
    pause 0.1
    "images/bg/Starting_Room/3/drillsargpickupstart11.png" 
    pause 0.1
    "images/bg/Starting_Room/3/drillsargpickupstart13.png"


image empty_stage_animation:
    Animation(
        "images/bg/Starting_Room/empty/emptystage1.png", 0.1,
        "images/bg/Starting_Room/empty/emptystage2.png", 0.1,
        "images/bg/Starting_Room/empty/emptystage3.png", 0.1,
        "images/bg/Starting_Room/empty/emptystage4.png", 0.1,
        "images/bg/Starting_Room/empty/emptystage5.png", 0.1,
        "images/bg/Starting_Room/empty/emptystage6.png", 0.1,
        "images/bg/Starting_Room/empty/emptystage7.png", 0.1,
        "images/bg/Starting_Room/empty/emptystage8.png", 0.1,
        "images/bg/Starting_Room/empty/emptystage9.png", 99999.0 
    )
    xysize (config.screen_width, config.screen_height)



image 0drillsargpickupstart0:
    "images/bg/Starting_Room/4/0drillsargpickupstart10.png" 
    xysize (config.screen_width, config.screen_height)
image burn1drillsargpickup:
    xysize (config.screen_width, config.screen_height)
    "images/bg/Starting_Room/7/burn1drillsargpickup1.png"
    pause 0.3
    "images/bg/Starting_Room/7/burn1drillsargpickup2.png"
    pause 0.3
    "images/bg/Starting_Room/7/burn1drillsargpickup3.png"
    pause 0.3
    "images/bg/Starting_Room/7/burn1drillsargpickup4.png"
    pause 0.3
    "images/bg/Starting_Room/7/burn1drillsargpickup5.png"
    pause 0.3
    "images/bg/Starting_Room/7/burn1drillsargpickup6.png"
    pause 0.3
    "images/bg/Starting_Room/7/burn1drillsargpickup7.png"
    pause 0.3
    "images/bg/Starting_Room/7/burn1drillsargpickup8.png"
    pause 0.3
    "images/bg/Starting_Room/7/burn1drillsargpickup9.png"
    pause 0.3
    "images/bg/Starting_Room/7/burn1drillsargpickup10.png"
    pause 0.3
    "images/bg/Starting_Room/7/burn1drillsargpickup11.png"
    pause 0.3
    "images/bg/Starting_Room/7/burn1drillsargpickup12.png"
    pause 0.3
    Animation(
    "images/bg/Starting_Room/7/burn1drillsargpickup13.png", 0.3,
    "images/bg/Starting_Room/7/burn1drillsargpickup14.png", 0.3
    )
    

image 0drillsargpickupstart:
    "images/bg/Starting_Room/3/0drillsargpickupstart.png" 
    xysize (config.screen_width, config.screen_height)

image satgescene9:
    "images/bg/Starting_Room/2/satgescene9.png" 
    xysize (config.screen_width, config.screen_height)

image chair:
    xysize (config.screen_width, config.screen_height)
image ani2_background:
    xysize (config.screen_width, config.screen_height)
    "images/bg/Starting_Room/1/ani2stagescene1.png"
    pause 0.4
    "images/bg/Starting_Room/1/ani2stagescene2.png" 
    pause 0.4
    "images/bg/Starting_Room/1/ani2stagescene1.png"
    pause 0.4
    "images/bg/Starting_Room/1/ani2stagescene2.png"
    pause 0.4
    "images/bg/Starting_Room/1/ani2stagescene3.png" 
    pause 0.1
    "images/bg/Starting_Room/1/ani2stagescene4.png" 
    pause 0.1
    "images/bg/Starting_Room/1/ani2stagescene5.png"
    pause 0.2
    "images/bg/Starting_Room/1/ani2stagescene6.png" 
    pause 0.15
    "images/bg/Starting_Room/1/ani2stagescene7.png" 
    pause 0.25
    "images/bg/Starting_Room/1/ani2stagescene8.png" 
    pause 0.3
    "images/bg/Starting_Room/1/ani2stagescene9.png" 
    pause 0.1

    Animation(
        "images/bg/Starting_Room/3/3_sitting/sittinganistagescene3.png", 5.8,
        "images/bg/Starting_Room/3/3_sitting/sittinganistagescene4.png", 0.1,
        "images/bg/Starting_Room/3/3_sitting/sittinganistagescene5.png", 0.1,
        "images/bg/Starting_Room/3/3_sitting/sittinganistagescene6.png", 0.1,
        "images/bg/Starting_Room/3/3_sitting/sittinganistagescene3.png", 5.8,
        "images/bg/Starting_Room/3/3_sitting/sittinganistagescene9.png", 0.1,
        "images/bg/Starting_Room/3/3_sitting/sittinganistagescene10.png", 0.1,
        "images/bg/Starting_Room/3/3_sitting/sittinganistagescene3.png", 5.8,
        "images/bg/Starting_Room/3/3_sitting/sittinganistagescene13.png", 0.1,
        "images/bg/Starting_Room/3/3_sitting/sittinganistagescene14.png", 0.1,
        "images/bg/Starting_Room/3/3_sitting/sittinganistagescene15.png", 0.1  
    )

image anistagescene:
    Animation(
        "images/bg/Starting_Room/4/0drillsargpickupstart1.png", 0.3,
        "images/bg/Starting_Room/4/0drillsargpickupstart2.png", 0.3,
        "images/bg/Starting_Room/4/0drillsargpickupstart3.png", 0.3,
        "images/bg/Starting_Room/4/0drillsargpickupstart4.png", 0.3,
        "images/bg/Starting_Room/4/0drillsargpickupstart5.png", 0.3,
        "images/bg/Starting_Room/4/0drillsargpickupstart6.png", 0.3,
        "images/bg/Starting_Room/4/0drillsargpickupstart7.png", 0.3,
        "images/bg/Starting_Room/4/0drillsargpickupstart8.png", 0.3,
        "images/bg/Starting_Room/4/0drillsargpickupstart9.png", 0.3,
        "images/bg/Starting_Room/4/0drillsargpickupstart10.png", 0.3,
        "images/bg/Starting_Room/4/0drillsargpickupstart0.png", 99999.0  
    )
    xysize (config.screen_width, config.screen_height)

image projector_hum_animation:
    xysize (config.screen_width, config.screen_height) 
    "images/bg/Starting_Room/5/projector_on1.png"
    pause 0.5
    "images/bg/Starting_Room/5/projector_on2.png"
    pause 0.5
    "images/bg/Starting_Room/5/projector_on3.png"
    pause 0.5
    "images/bg/Starting_Room/5/projector_on4.png"
    pause 0.5
    "images/bg/Starting_Room/5/projector_on5.png"
    pause 0.5
    "images/bg/Starting_Room/5/projector_on6.png"
    pause 0.5
    "images/bg/Starting_Room/5/projector_on7.png"
    pause 0.5
    Animation(
        "images/bg/Starting_Room/5/projector_on8.png", 0.5,
        "images/bg/Starting_Room/5/projector_on9.png", 0.5,
        "images/bg/Starting_Room/5/projector_on10.png", 0.5,
        "images/bg/Starting_Room/5/projector_on11.png", 0.5,
        "images/bg/Starting_Room/5/projector_on12.png", 0.5,
        "images/bg/Starting_Room/5/projector_on13.png", 0.5, 
        "images/bg/Starting_Room/5/projector_on12.png", 0.5, 
        "images/bg/Starting_Room/5/projector_on13.png", 0.5, 
        "images/bg/Starting_Room/5/projector_on12.png", 0.5, 
        "images/bg/Starting_Room/5/projector_on13.png", 0.5, 
        "images/bg/Starting_Room/5/projector_on18.png", 0.5,
        "images/bg/Starting_Room/5/projector_on12.png", 0.5  
    )