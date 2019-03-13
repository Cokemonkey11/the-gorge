
import sys
import textwrap


MAP_NAME           = "The Gorge"
AUTHOR             = "Cokemonkey11"


INTRODUCTION = (

    """

        The Gorge is a battleships-style aos that focuses on simplicity. It uses
        automatically firing weapons and interesting systems to produce a design
        that's nostalgic yet fun.

    """,

    """

        The western nations and eatern faction have long been allies and shared
        knowledge, as well as technology; but the recent discoery of numerous
        rich resource deposits near an unnamed gorge has resulted in a bitter
        standoff. Secure your team's victory in one final cacophony of
        helicopters, explosives, and other armament.

    """,
)


SCREENSHOTS = (
    ("Last-hit for bounty", "http://i.imgur.com/PE862R1.jpg"),
)


ABILITIES = (
    (
        # "https://i.imgur.com/xSoqYuZ.png",
        (
            # "Don Rogo: Your hero.",
        )
    ),
)

REPOSITORY_URI     = "https://bitbucket.org/Cokemonkey11/the-gorge/"

CHANGELOG          = (
    (
        "next",
        "2019",
        (
            "This map is now written entirely in wurst!",

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

def write(str):
    sys.stdout.write(str)


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
            write("[hidden=Older Changes")
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
print_hosting()
print_contributing()
print_footer()
