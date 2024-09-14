#!/usr/bin/python3

FILENAME_IN  = 'cotm.gba'
FILENAME_OUT = 'hack.gba'

ALPHABET = "eatorinslhdcu.mwpgfybkAvHSMICDRT?W!P,BEG+'NV()Fx-[]→←↑↓LUqj20zKO%51J3XYZ/48&"

ALPHABET_OFFSET      = 0x28
CHARACTER_SPACE      = 0x26
CHARACTER_NEWLINE    = 0x09
CHARACTER_WAIT       = 0x03
CHARACTER_END        = 0x00
BYTE_NEWLINE         = b'\x09'
BYTES_NEXT_SCREEN    = b'\x02\x09\x01\x0a'

OFFSET_DASH_TEXT_1   = 0x393b92
OFFSET_DASH_TEXT_2   = 0x393eae

OFFSET_TACKLE_TEXT_1 = 0x393c39
OFFSET_TACKLE_TEXT_2 = 0x393f13

# Originals:
# DASH_SCREENS = (
#         'Double tap forward to\nperform a dash move.',
#         )
# TACKLE_SCREENS = (
#         'Forward + Special\nMove button makes the\nplayer charge.',
#         'Some blocks can be\ndestroyed with this\nmove.',
#         )

DASH_SCREENS = (
        'Hold R to perform\na dash move.',
        )
TACKLE_SCREENS = (
        'Forward+Down+R makes\nthe player charge.',
        'Some blocks can be\ndestroyed with this\nmove.',
        )


def convert_character(c):
    if c == ' ':
        return CHARACTER_SPACE
    if c == '\n':
        return CHARACTER_NEWLINE
    return ALPHABET.index(c) + ALPHABET_OFFSET


def convert_screen(s):
    return bytearray(convert_character(c) for c in s)


def convert_screens(screens):
    return BYTES_NEXT_SCREEN.join(convert_screen(screen) for screen in screens)


def replace_text(rom, offset, screens, last_byte):
    data = convert_screens(screens)
    for i, b in enumerate(data):
        rom[offset+i] = b
    rom[offset+i+1] = CHARACTER_WAIT
    rom[offset+i+2] = last_byte


def fix_dash_text(rom):
    replace_text(rom, OFFSET_DASH_TEXT_1, DASH_SCREENS, 0x1d)
    replace_text(rom, OFFSET_DASH_TEXT_2, DASH_SCREENS, 0x00)


def fix_tackle_text(rom):
    replace_text(rom, OFFSET_TACKLE_TEXT_1, TACKLE_SCREENS, 0x1d)
    replace_text(rom, OFFSET_TACKLE_TEXT_2, TACKLE_SCREENS, 0x00)


def main():
    with open(FILENAME_IN, 'rb') as inf:
        rom = bytearray(inf.read())

    fix_dash_text(rom)
    fix_tackle_text(rom)

    with open(FILENAME_OUT, 'wb') as outf:
        outf.write(rom)


if __name__ == '__main__':
    main()
