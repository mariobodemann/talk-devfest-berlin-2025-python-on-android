import math
import random
import sys

def slackify(color: str | tuple, letter: str):
    if isinstance(color, type(())):
        color = color[random.Random().randint(0, len(color) - 1)]

    if letter.isdigit():
        num_to_slack = [
            ":zero:", ":one:", ":two:", ":three:", ":four:", ":five:", ":six:", ":seven:", ":eight:", ":nine:",
        ]
        try:
            return num_to_slack[int(letter)]
        except ValueError:
            return num_to_slack[0]
    elif letter == ' ':
        return '   '
    elif letter == '?':
        return f":alphabet-{color}-question:"
    elif letter == '!':
        return f":alphabet-{color}-exclamation:"
    else:
        return f":alphabet-{color.lower()}-{letter.lower()}:"


default_fraktur = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!? "
fonts = {
    'none': default_fraktur,
    'bbb': "┌┐└┘│─╔╗╚╝║═┏┓┗┛┃━╭╮╰╯█▉▊▋┌┐└┘│─╔╗╚╝║═┏┓┗┛┃━╭╮╰╯█▉▊▋┌┐└┘│─╔╗╚╝║═┏┓┗┛┃━╭╮╰╯█▉▊▋",
    'bold': "𝐀𝐁𝐂𝐃𝐄𝐅𝐆𝐇𝐈𝐉𝐊𝐋𝐌𝐍𝐎𝐏𝐐𝐑𝐒𝐓𝐔𝐕𝐖𝐗𝐘𝐙𝐚𝐛𝐜𝐝𝐞𝐟𝐠𝐡𝐢𝐣𝐤𝐥𝐦𝐧𝐨𝐩𝐪𝐫𝐬𝐭𝐮𝐯𝐰𝐱𝐲𝐳𝟎𝟏𝟐𝟑𝟒𝟓𝟔𝟕𝟖𝟗!? ",
    'bold-italic': "𝑨𝑩𝑪𝑫𝑬𝑭𝑮𝑯𝑰𝑱𝑲𝑳𝑴𝑵𝑶𝑷𝑸𝑹𝑺𝑻𝑼𝑽𝑾𝑿𝒀𝒁𝒂𝒃𝒄𝒅𝒆𝒇𝒈𝒉𝒊𝒋𝒌𝒍𝒎𝒏𝒐𝒑𝒒𝒓𝒔𝒕𝒖𝒗𝒘𝒙𝒚𝒛𝟎𝟏𝟐𝟑𝟒𝟓𝟔𝟕𝟖𝟗!? ",
    'bold-sans': "𝗔𝗕𝗖𝗗𝗘𝗙𝗚𝗛𝗜𝗝𝗞𝗟𝗠𝗡𝗢𝗣𝗤𝗥𝗦𝗧𝗨𝗩𝗪𝗫𝗬𝗭𝗮𝗯𝗰𝗱𝗲𝗳𝗴𝗵𝗶𝗷𝗸𝗹𝗺𝗻𝗼𝗽𝗾𝗿𝘀𝘁𝘂𝘃𝘄𝘅𝘆𝘇𝟬𝟭𝟮𝟯𝟰𝟱𝟲𝟳𝟴𝟵!? ",
    'border': "𝔸𝔹ℂ𝔻𝔼𝔽𝔾ℍ𝕀𝕁𝕂𝕃𝕄ℕ𝕆ℙℚℝ𝕊𝕋𝕌𝕍𝕎𝕏𝕐ℤ𝕒𝕓𝕔𝕕𝕖𝕗𝕘𝕙𝕚𝕛𝕜𝕝𝕞𝕟𝕠𝕡𝕢𝕣𝕤𝕥𝕦𝕧𝕨𝕩𝕪𝕫𝟘𝟙𝟚𝟛𝟜𝟝𝟞𝟟𝟠𝟡!? ",
    'cards': "🂠🂡🂢🂣🂤🂥🂦🂧🂨🂩🂪🂫🂬🂭🂮🂱🂲🂳🂴🂵🂶🂷🂸🂹🂺🂻🂼🂽🂾🃁🃂🃃🃄🃅🃆🃇🃈🃉🃊🃋🃌🃍🃎🃑🃒🃓🃔🃕🃖🃗🃘🃙🃚🃛🃜🃝🃞🃟🃟🃟🃟🃟!? ",
    'censored': list(map(lambda x: '█', default_fraktur)),
    'cesar': "AMWOEZKFYBVXPQCGDLJRITNUHSbfnzuymvokwaecxjghrtqpisld321465897?! ",
    'chess': "♔♕♖♗♘♙♚♛♜♝♞♟︎♔♕♖♗♘♙♚♛♜♝♞♟︎♔♕♖♗♘♙♚♛♜♝♞♟︎♔♕♖♗♘♙♚♛♜♝♞♟︎♔♕♖♗♘♙♚♛♜♝♞♟︎!? ",
    'circle': "ⒶⒷⒸⒹⒺⒻⒼⒽⒾⒿⓀⓁⓂⓃⓄⓅⓆⓇⓈⓉⓊⓋⓌⓍⓎⓏⓐⓑⓒⓓⓔⓕⓖⓗⓘⓙⓚⓛⓜⓝⓞⓟⓠⓡⓢⓣⓤⓥⓦⓧⓨⓩ⓪①②③④⑤⑥⑦⑧⑨!? ",
    'circle-bold': "🅐🅑🅒🅓🅔🅕🅖🅗🅘🅙🅚🅛🅜🅝🅞🅟🅠🅡🅢🅣🅤🅥🅦🅧🅨🅩🅐🅑🅒🅓🅔🅕🅖🅗🅘🅙🅚🅛🅜🅝🅞🅟🅠🅡🅢🅣🅤🅥🅦🅧🅨🅩⓿❶❷❸❹❺❻❼❽❾!? ",
    'double': "𝔸𝔹ℂ𝔻𝔼𝔽𝔾ℍ𝕀𝕁𝕂𝕃𝕄ℕ𝕆ℙℚℝ𝕊𝕋𝕌𝕍𝕎𝕏𝕐ℤ𝕒𝕓𝕔𝕕𝕖𝕗𝕘𝕙𝕚𝕛𝕜𝕝𝕞𝕟𝕠𝕡𝕢𝕣𝕤𝕥𝕦𝕧𝕨𝕩𝕪𝕫𝟘𝟙𝟚𝟛𝟜𝟝𝟞𝟟𝟠𝟡!? ",
    'fraktur': "𝔄𝔅ℭ𝔇𝔈𝔉𝔊ℌℑ𝔍𝔎𝔏𝔐𝔑𝔒𝔓𝔔ℜ𝔖𝔗𝔘𝔙𝔚𝔛𝔜ℨ𝔞𝔟𝔠𝔡𝔢𝔣𝔤𝔥𝔦𝔧𝔨𝔩𝔪𝔫𝔬𝔭𝔮𝔯𝔰𝔱𝔲𝔳𝔴𝔵𝔶𝔷0123456789!? ",
    'fraktur-bold': "𝕬𝕭𝕮𝕯𝕰𝕱𝕲𝕳𝕴𝕵𝕶𝕷𝕸𝕹𝕺𝕻𝕼𝕽𝕾𝕿𝖀𝖁𝖂𝖃𝖄𝖅𝖆𝖇𝖈𝖉𝖊𝖋𝖌𝖍𝖎𝖏𝖐𝖑𝖒𝖓𝖔𝖕𝖖𝖗𝖘𝖙𝖚𝖛𝖜𝖝𝖞𝖟𝟎𝟏𝟐𝟑𝟒𝟓𝟔𝟕𝟖𝟗!? ",
    'italic': "𝘈𝘉𝘊𝘋𝘌𝘍𝘎𝘏𝘐𝘑𝘒𝘓𝘔𝘕𝘖𝘗𝘘𝘙𝘚𝘛𝘜𝘝𝘞𝘟𝘠𝘡𝘢𝘣𝘤𝘥𝘦𝘧𝘨𝘩𝘪𝘫𝘬𝘭𝘮𝘯𝘰𝘱𝘲𝘳𝘴𝘵𝘶𝘷𝘸𝘹𝘺𝘻0123456789!? ",
    'italic-sans': "𝘈𝘉𝘊𝘋𝘌𝘍𝘎𝘏𝘐𝘑𝘒𝘓𝘔𝘕𝘖𝘗𝘘𝘙𝘚𝘛𝘜𝘝𝘞𝘟𝘠𝘡𝘢𝘣𝘤𝘥𝘦𝘧𝘨𝘩𝘪𝘫𝘬𝘭𝘮𝘯𝘰𝘱𝘲𝘳𝘴𝘵𝘶𝘷𝘸𝘹𝘺𝘻0123456789!? ",
    'lower': default_fraktur.lower(),
    'mono': "𝙰𝙱𝙲𝙳𝙴𝙵𝙶𝙷𝙸𝙹𝙺𝙻𝙼𝙽𝙾𝙿𝚀𝚁𝚂𝚃𝚄𝚅𝚆𝚇𝚈𝚉𝚊𝚋𝚌𝚍𝚎𝚏𝚐𝚑𝚒𝚓𝚔𝚕𝚖𝚗𝚘𝚙𝚚𝚛𝚜𝚝𝚞𝚟𝚠𝚡𝚢𝚣𝟶𝟷𝟸𝟹𝟺𝟻𝟼𝟽𝟾𝟿!? ",
    'morse': ["·– ", "–··· ", "–·–· ", "–·· ", "· ", "··–· ", "––· ", "···· ", "·· ", "·––– ", "–·– ", "·–·· ", "–– ", "–· ", "––– ", "·––· ", "––·– ", "·–· ", "··· ", "– ", "··– ", "···– ", "·–– ", "–··– ", "–·–– ", "––·· ", "·– ", "–··· ", "–·–· ", "–·· ", "· ", "··–· ", "––· ", "···· ", "·· ", "·––– ", "–·– ", "·–·· ", "–– ", "–· ", "––– ", "·––· ", "––·– ", "·–· ", "··· ", "– ", "··– ", "···– ", "·–– ", "–··– ", "–·–– ", "––·· ", "––––– ", "·–––– ", "··––– ", "···–– ", "····– ", "····· ", "–···· ", "––··· ", "–––·· ", "––––· ", " ", " ","/ "],
    'numbers': list(map(lambda x: f"{ord(x):d} ", default_fraktur)),
    'numbers-binary': list(map(lambda x: f"{ord(x):0b} ", default_fraktur)),
    'numbers-hex': list(map(lambda x: f"0x{ord(x):X} ", default_fraktur)),
    'parenthesized': "🄐🄑🄒🄓🄔🄕🄖🄗🄘🄙🄚🄛🄜🄝🄞🄟🄠🄡🄢🄣🄤🄥🄦🄧🄨🄩⒜⒝⒞⒟⒠⒡⒢⒣⒤⒥⒦⒧⒨⒩⒪⒫⒬⒭⒮⒯⒰⒱⒲⒳⒴⒵⒪⑴⑵⑶⑷⑸⑹⑺⑻⑼!? ",
    'rect': "🄰🄱🄲🄳🄴🄵🄶🄷🄸🄹🄺🄻🄼🄽🄾🄿🅀🅁🅂🅃🅄🅅🅆🅇🅈🅉🄰🄱🄲🄳🄴🄵🄶🄷🄸🄹🄺🄻🄼🄽🄾🄿🅀🅁🅂🅃🅄🅅🅆🅇🅈🅉𝟶𝟷𝟸𝟹𝟺𝟻𝟼𝟽𝟾𝟿!? ",
    'rect-bold': "🅰🅱🅲🅳🅴🅵🅶🅷🅸🅹🅺🅻🅼🅽🅾🅿🆀🆁🆂🆃🆄🆅🆆🆇🆈🆉🅰🅱🅲🅳🅴🅵🅶🅷🅸🅹🅺🅻🅼🅽🅾🅿🆀🆁🆂🆃🆄🆅🆆🆇🆈🆉0123456789!? ",
    'rect-dotted': "🇦🇧🇨🇩🇪🇫🇬🇭🇮🇯🇰🇱🇲🇳🇴🇵🇶🇷🇸🇹🇺🇻🇼🇽🇾🇿🇦🇧🇨🇩🇪🇫🇬🇭🇮🇯🇰🇱🇲🇳🇴🇵🇶🇷🇸🇹🇺🇻🇼🇽🇾🇿0123456789!? ",
    'script': "𝒜𝐵𝒞𝒟𝐸𝐹𝒢𝐻𝐼𝒥𝒦𝐿𝑀𝒩𝒪𝒫𝒬𝑅𝒮𝒯𝒰𝒱𝒲𝒳𝒴𝒵𝒶𝒷𝒸𝒹𝑒𝒻𝑔𝒽𝒾𝒿𝓀𝓁𝓂𝓃𝑜𝓅𝓆𝓇𝓈𝓉𝓊𝓋𝓌𝓍𝓎𝓏𝟢𝟣𝟤𝟥𝟦𝟧𝟨𝟩𝟪𝟫!? ",
    'script-bold': "𝓐𝓑𝓒𝓓𝓔𝓕𝓖𝓗𝓘𝓙𝓚𝓛𝓜𝓝𝓞𝓟𝓠𝓡𝓢𝓣𝓤𝓥𝓦𝓧𝓨𝓩𝓪𝓫𝓬𝓭𝓮𝓯𝓰𝓱𝓲𝓳𝓴𝓵𝓶𝓷𝓸𝓹𝓺𝓻𝓼𝓽𝓾𝓿𝓌𝓍𝓎𝓏𝟢𝟣𝟤𝟥𝟦𝟧𝟨𝟩𝟪𝟫!? ",
    'slack': list(map(lambda x: slackify('white', x), default_fraktur)),
    'slack-random': list(map(lambda x: slackify(('yellow', 'white'), x), default_fraktur)),
    'slack-yellow': list(map(lambda x: slackify('yellow', x), default_fraktur)),
    'small-caps': "ABCDEFGHIJKLMNOPQRSTUVWXYZᴀʙᴄᴅᴇғɢʜɪᴊᴋʟᴍɴᴏᴘǫʀsᴛᴜᴠᴡxʏᴢ𝟢𝟣𝟤𝟥𝟦𝟧𝟨𝟩𝟪𝟫!? ",
    'upper': default_fraktur.upper(),
}

boxes = {
    'single': '┌─┐│ │└─┘',
    'cheap': '+-+| |+-+',
    'double': '╔═╗║ ║╚═╝',
    'thick': '┏━┓┃ ┃┗━┛',
    'round': '╭─╮│ │╰─╯',
}

box_alignments = {
    'left': lambda m,l: f"{m:{l}s}",
    'center': lambda m,l: m.center(l),
    'right': lambda m,l: m.rjust(l),
}

def term_color(color):
    r, g, b = color
    r = round(max(0.0, min(5.0, r * 6.0)))
    g = round(max(0.0, min(5.0, g * 6.0)))
    b = round(max(0.0, min(5.0, b * 6.0)))

    return int(16 + r + g * 6 + b * 6 * 6)


def hsv(index, length):
    # rainbow
    bucket_size = length / 6.0
    index_in_bucket = index / bucket_size - math.floor(index / bucket_size)

    # r1, g+, b0
    if index < bucket_size:
        r = 1.0
        g = index_in_bucket
        b = 0.0

    # r-, g1, b0
    elif index < 2 * bucket_size:
        r = 1.0 - index_in_bucket
        g = 1.0
        b = 0.0

    # r0, g1, b+
    elif index < 3 * bucket_size:
        r = 0.0
        g = 1.0
        b = index_in_bucket

    # r0, g-, b1
    elif index < 4 * bucket_size:
        r = 0.0
        g = 1.0 - index_in_bucket
        b = 1.0

    # r+, g0, b1
    elif index < 5 * bucket_size:
        r = index_in_bucket
        g = 0.0
        b = 1.0

    # r+, g0, b-
    else:  # index < 6 * bucket_size
        r = 1.0
        g = 0.0
        b = 1.0 - index_in_bucket

    return r, g, b


def rainbowify(message, as_html=False):
    def rainbow(index, char):
        color = hsv(index, len(message))

        if as_html:
            r, g, b = color
            return f"<font style=\"color:rgb({int(r * 255)},{int(g * 255)},{int(b * 255)})\">{char}</font>"
        else:
            return f"\033[38;5;{term_color(color)}m{char}\033[m"

    return "".join(
        list(
            map(
                lambda item: rainbow(item[0], item[1]),
                enumerate(message)
            )
        )
    )


def index_in_font(c: str) -> int | None:
    if c.isalpha():
        if c.isupper():
            return ord(c) - ord('A')
        else:
            return ord(c) - ord('a') + 26
    elif c.isdigit():
        return 2*26 + int(c)
    elif c == ' ' or c == '\t':
        return -1
    elif c == '?':
        return -2
    elif c == '!':
        return -3
    else:
        return None


def fraktur(message, font):
    out = ''
    if font in fonts:
        for c in message:
            index = index_in_font(c)
            if index:
                out += fonts[font][index]
            else:
                out += c
    else:
        print(f"Font '{font}' not found.", file=sys.stderr)
        return message

    return out


def fraktur_all(message, selected_fonts=None, modes=None, box=None, align=None)-> str:
    if not modes:
        modes = []

    if selected_fonts is None:
        selected_fonts = list(fonts.keys())

    orig_message = message

    results = ''
    for font in sorted(selected_fonts):
        if box:
            message = boxify(orig_message, box, align)

        result = fraktur(message, font)

        if 'rainbow' in modes:
            html = 'html' in modes
            result = "".join(rainbowify(result, html))

        if 'name' in modes:
            sep = "\n" if box else " "

            result = f"{font}:{sep}{result}"

        results += result + '\n'

    return results


def boxify(message, box=None, align=None):
    if not box:
        box = 'single'
    if not align:
        align = 'left'

    if box == 'all':
        result = message
        for allBox in boxes:
            result = boxify(result, allBox, align)
        return result
    else:
        lines = message.splitlines()
        max_line = max(lines,key=len)
        max_line_length = len(max_line)

        if box in boxes:
            nw,n,ne,w,c,e,sw,s,se = boxes[box]

            top = nw + n*max_line_length + ne
            inner = [w + box_alignments[align](x, max_line_length) + e for x in lines]
            bottom = sw + s*max_line_length + se

            return '\n'.join([top,*inner,bottom])
        else:
            print(f'Box "{box}" not found. Ignored.',file=sys.stderr)
            return message


def generate(message: str, font: str = None, modes: list = None, box: str = None, align: str = None) -> str:
    if not modes:
        modes = []

    if not font:
        return fraktur_all(message, ['fraktur'], modes, box, align)
    else:
        if font == 'all':
            return fraktur_all(message, list(fonts.keys()), modes, box, align)
        else:
            if font in fonts:
                return fraktur_all(message, [font], modes, box, align)
            else:
                found_fonts = list(filter(lambda x: x.lower().find(font.lower()) > -1, fonts.keys()))
                if len(found_fonts) > 0:
                    return fraktur_all(message, found_fonts, modes, box, align)
                else:
                    return f"Font {font} not found."

def main():
    import sys
    import argparse

    parser = argparse.ArgumentParser(
        prog=sys.argv[0],
        description="Frakturing all the things, aka make them beautiful or at least try.",
    )

    parser.add_argument(
        'message',
        type=str,
        nargs='*',
        default=["Hello World."],
        help="Text to be frakturzied. Defaults to 'Hello World.'."
    )
    parser.add_argument(
        '--font', '-f',
        metavar='FONT | all',
        help=f'One font of "{", ".join(fonts.keys())}", or "all" for all fonts consecutively.'
    )
    parser.add_argument(
        '--modes', '-m',
        metavar='MODE',
        action='store',
        type=str,
        nargs='*',
        help='One of these modes: "rainbow, html, name".'
    )
    parser.add_argument(
        '--box', '-b',
        metavar='BOX',
        help=f'Select a box from "{", ".join(boxes.keys())}".'
    )
    parser.add_argument(
        '--align', '-a',
        metavar='ALIGNMENT',
        help=f'Select a text alignment (in box) from one of "{", ".join(box_alignments.keys())}".'
    )
    parser.add_argument(
        '--list', '-l',
        action='store_true',
        help='List all fonts. Excluding meta fonts (like \'all\').'
    )

    args = parser.parse_args()
    doit = True
    if not args.message:
        print('No "message" given')
        args.message = 'Hello World.'
    elif args.list:
        print(",".join(fonts.keys()))
        doit = False
    else:
        map(lambda x: x.strip(), args.message)

        args.message = " ".join(args.message)
        if len(args.message.strip()) == 0:
            print('No message given')
            args.message = 'Hello World.'

    if doit:
        result = generate(
            message=args.message,
            font=args.font,
            modes=args.modes,
            box=args.box,
            align=args.align
        )

        print(result)


if __name__ == "__main__":
    main()
