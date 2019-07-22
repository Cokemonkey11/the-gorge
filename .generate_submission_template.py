#!/usr/bin/env python
import sys
import textwrap


MAP_NAME = "The Gorge"
AUTHOR   = "Cokemonkey11"


INTRODUCTION = (

    """

        The Gorge is a battleships-style AoS/MOBA that focuses on simplicity.
        It uses automatically firing weapons, and some innovative systems, to
        produce a design that's nostalgic, yet fun.

    """,

    """

        What make The Gorge different?  Design principles: (1) Short games aide
        replayability and reduce burnout (2) Bias for action means big damage
        and low durability leads to faster-paced gameplay (3) MOBA design
        principles focus more on action and less on grinding (4) Fresh means not
        being afraid to do things new-and-improved (5) Classic battleships is a
        competitive and brilliant game - when in doubt, remain unbroken.

    """,

    """

        The western nations and eastern faction have long been allies and shared
        knowledge, as well as technology; but the recent discovery of numerous,
        rich resource deposits near an unnamed gorge has resulted in a bitter
        standoff.
        Secure your team's victory in one final cacophony of helicopters,
        explosives, and other armament.

    """,
)


SCREENSHOTS = (
    ("Last-hit for creep bounty", "http://i.imgur.com/PE862R1.jpg"),
    ("Enchanted frost wyrms can disable towers", "https://i.imgur.com/eKHPGvt.jpg"),
)


ABILITIES = (
    (
        # "https://i.imgur.com/xSoqYuZ.png",
        (
            # "Don Rogo: Your hero.",
        )
    ),
)

REPOSITORY_URI = "https://bitbucket.org/Cokemonkey11/the-gorge/"

CHANGELOG = (
    (
        "0.13.2",
        "NEXT",
        (
            "Fixed a bug where shields would cause you to kill yourself.",
            "Adjusted base layout and increased repair-port repair rate.",
            "Selected pages in keep/utility ports are now saved/reselected.",
            "Minor performance improvement and auditing capability.",
        )
    ),
    (
        "0.13.1",
        "20 Jul 2019",
        (
            "Made changes to crewmembers to clarify stats and sell value.",
            "All long-range crew are now incapable of hitting structures.",
            "Significant rework to crewmember balance, improves synergy.",
        )
    ),
    (
        "0.13.0",
        "16 Jul 2019",
        (
            "Reworked vision/pathing to behave more like classic Battleships.",
            "Disabled global trading and added a send-gold ability to trader.",
            "[trading] fixed the broken spider venom job.",
            "Reworked crewmembers slightly to reduce the learning curve.",
            "Top weapon stats are now displayed at the end of the match.",
        )
    ),
    (
        "0.12.4",
        "22 Jun 2019",
        (
            "minor improvements related to the use of DamageEvent (wurst).",
            "fixed a minor cosmetic bug that made creeps appear to be healing.",
        )
    ),
    (
        "0.12.3",
        "19 Jun 2019",
        (
            "regression: scoreboard fixed, when more than 5 players present.",
            "fixed a minor desync at end-of-game.",
            "very minor code tidying.",
        )
    ),
    (
        "0.12.2",
        "18 Jun 2019",
        (
            "Fixed an error related to a 1.31.1 regression (DD wurst NPE).",
            "Fixed a bug where selling or dropping hull never reset reduction.",
            "Minor refactoring to use WurstCommand and DamageEvent libraries.",
            "Minor new singleplayer commands added.",
        )
    ),
    (
        "0.12.1",
        "9 Jun 2019",
        (
            "Fixed a fatal problem related to a 1.31 regression (map crash).",
            "Fixed a bug where a player gets bounty when a team-kill occurs.",
            "Improved messages for when a team-kill occurs.",
            "Fixed a potential damage-detection problem.",
            "Wurst optimiser and local optimiser are now enabled.",
            "Fixed a cosmetic bug that made healing effects on dead units.",
            "Enchanted frost wyrms now appear more blue.",
        )
    ),
    (
        "0.12.0",
        "14 Apr 2019",
        (
            "Fixed a bug where next-page buttons don't work if your inventory is full.",
            "The interceptor now has a crowd control (damage) ability.",
            "The frigate now has a sustain (healing) ability.",
            "The battleship now has a sustain (healing) ability.",
            "Fixed a bug where the singleplayer -fast command wouldn't work if you changed ship.",
            "Minor tooltip fixes.",
        )
    ),
    (
        "0.11.2",
        "7 Apr 2019",
        (
            "Fixed a desync when a player uses the -music command.",
        )
    ),
    (
        "0.11.1",
        "7 Apr 2019",
        (
            "Fixed a major bug where players get gold if they destroy themselves.",
            "Music can now be disabled with the `-music` command.",
            "Fixed a minor bug that allowed players to select other pages of keep and utility port.",
            "Minor increase to DTS-12 projectile height to aid with aiming.",
            "Reduced the cooldown time on the Sell Crewmember ability.",
            "Replaced singleplayer chat commands from backslash to hyphen.",
        )
    ),
    (
        "0.11.0",
        "31 Mar 2019",
        (
            "Player ships are now heroes, and the F2 hotkey can be used!",
            "This map now uses an up-to-date wurst standard library.",
            "Adjusted spawn behavior so that creeps would stack up less.",
            "Maybe bug fix: a minor change in enchanting stones.",
            "Many object-defined units are now defined in wurst."
        )
    ),
    (
        "0.10.1",
        "27 Mar 2019",
        (
            "Fixed a major bug related to recently respawned ships not losing invulnerability.",
            "Fixed a minor tooltip bug.",
            "Fixed a couple minor cosmetic blemishes."
        )
    ),
    (
        "0.10.0 (blacklisted)",
        "18 Mar 2019",
        (
            "This map is now written entirely in wurst!",
            "Added 3 new movespeed items and 3 new hitpoint regen items.",
            "Improved behavior when a player leaves the game.",
            "Ships are now invulnerable for 6 seconds on respawn.",
            "Added further ownership indicators for the enchanting stones.",
            "Added further repair indicators for the repair ports."
        )
    ),
    (
        "0.9.1",
        "24 Feb 2017",
        (
            "This map is now written entirely in Jurst, the jass-friendly Wurst dialect!",
            "Revamped the behavior and apperance of central outposts",
            "Sky Barge new ability: Reactive Shields.",
            "Zeppelin new ability: Helium Overdrive.",
            "Improved the user-friendliness of repair ports.",
            "Added a third trading route",
            "Improved tooltip consistency.",
            "General balance adjustments",
            "General fixes and tidying.",
        )
    ),

    (
        "0.1.0c",
        "16 May 2014",
        (
            "Additional terrain improvements by Kino.",
            "More bug fixes and improvements.",
            "Some undocumented/unknown improvements.",
        )
    ),

    (
        "0.0.8c",
        "01 Feb 2014",
        (
            "The map has received a large terrain makeover thanks to Kino! Kino has done more work in two days on the terrain than I could do in two weeks. Do check it out!",
            "Your farm of neutral monsters is now displayed in the multiboard",
            "A second trade-related job has been added",
            "Three new tier-3 cannons have been added",
            "Paracopter now has a unique ability: SL-15 Shroud Generator",
            "The music has been extended slightly",
            "Various small bug fixes and improvements",
        )
    ),

    (
        "0.0.7?",
        "21 Jan 2014",
        (
            "Helicopter now has a unique ability",
            "Created multiboard and some basic stat tracking",
            "Added bounties for pvp",
            "Dying no longer drops your items",
            "Repair port should be fixed in multiplayer (?)",
            "Can no longer drop and pick up items to abuse item sale trigger",
            "Added two new ships: Skybarge (basic battleship with 10 crew slots) and Zeppelin (basic interceptor)",
            "Extended music slightly",
            "Marginal terrain improvements",
            "Made third tier of weapons (mostly structural change)",
            "Many more small changes and improvements",
        )
    ),

    (
        "0.0.6?",
        "16 Jan 2014?",
        (
            "Initial release.",
        )
    )
)

HOSTING            = True
CONTRIBUTING       = "I will merge atomic, well-formed pull-requests if they are consistent with my design policies and issue tracker."

def write(st):
    sys.stdout.write(st)


def print_section_header(title):
    write("[R][H3][color=#CCAA00]" + title + "[/color][/H3][R]\n")


def get_paragraph(paragraph):
    p = paragraph.strip().replace('\n', ' ').replace('\t', '')
    return textwrap.fill(p, width=90) + "\n\n"


def print_paragraph(paragraph):
    write(get_paragraph(paragraph))


def print_header():
    write("[CENTER]\n[TABLE]\n[CENTER]\n[H3][color=#60A600]")
    write(MAP_NAME)
    write("[/color][/H3]\n[color=#CCAA00][B]A map by ")
    write(AUTHOR)
    write("[/B][/color]\n\n")


def print_contents():
    write("[BOX=Contents]")
    if INTRODUCTION:
        write("* Introduction\n")
    if SCREENSHOTS:
        write("* Screenshots\n")
    # if ABILITIES:
    #     write("* Abilities\n")
    if REPOSITORY_URI:
        write("* Version Control\n")
    if CHANGELOG:
        write("* Changelog\n")
    if HOSTING:
        write("* Hosting\n")
    if CONTRIBUTING:
        write("* Contributing\n")
    write("[/BOX]\n[/CENTER]\n\n")


def print_introduction():
    if INTRODUCTION:
        print_section_header("Introduction")
        for paragraph in INTRODUCTION:
            print_paragraph(paragraph)

def print_screenshots():
    if SCREENSHOTS:
        print_section_header("Screenshots")
        write("\n\n")
        for shot in SCREENSHOTS:
            write("[hidden=" + shot[0] + "]\n[img]" + shot[1] + "[/img]\n[/hidden]\n\n")


def print_abilities():
    if ABILITIES:
        print_section_header("Abilities")
        write("\n\n[otable]\n")
        for race in ABILITIES:
            write("[tr]\n[tdalt][img]" + race[0] + "[/img][/tdalt]\n[tdalt]")
            for paragraph in race[1][0:-1]:
                print_paragraph(paragraph)
            write(get_paragraph(race[1][-1])[0:-2])
            write("[/tdalt]\n[/tr]\n")
        write("[/otable]\n\n")


def print_repository_uri():
    if REPOSITORY_URI:
        print_section_header("Version Control")
        write("\n\n")
        print_paragraph("All iterations of this map are maintained in a public git repository at [url]" + REPOSITORY_URI + "[/url]")


def print_changelog():
    if CHANGELOG:
        print_section_header("Changelog")
        write("\n\n")
        for log in CHANGELOG[0:5]:
            write("[color=#ffcc00]" + log[0] + "[/color] [color=#999999]" + log[1] + "[/color]:\n[list]")
            for point in log[2]:
                write(get_paragraph("[*] " + point)[0:-2] + "\n")
            write("[/list]\n\n")

        if CHANGELOG[5:]:
            write("[hidden=Older Changes]")
            for log in CHANGELOG[5:]:
                write("[color=#ffcc00]" + log[0] + "[/color] [color=#999999]" + log[1] + "[/color]:\n[list]")
                for point in log[2]:
                    write(get_paragraph("[*] " + point)[0:-2] + "\n")
                write("[/list]\n\n")
            write("[/hidden]")


def print_hosting():
    if HOSTING:
        print_section_header("Automatic Hosting")
        print_paragraph("Release versions of this map are uploaded to both [url=http://makemehost.com/]MMH[/url] and [url=http://entgaming.net/]ENT[/url].")


def print_contributing():
    if CONTRIBUTING:
        print_section_header("Contributing")
        print_paragraph(CONTRIBUTING)


def print_footer():
    write("[/TABLE]\n[/CENTER]\n")

print_header()
print_contents()
print_introduction()
print_screenshots()
# print_abilities()
print_repository_uri()
print_changelog()
# print_hosting()
print_contributing()
print_footer()
