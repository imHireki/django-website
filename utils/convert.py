from data import fdicts


def bound_items(a, font):
    """ convert values """
    value = ''
    except_ones = [fdicts.squared, fdicts.squared_n, fdicts.inverted, fdicts.circled_n]

    if font in except_ones:
        if font == fdicts.squared or font == fdicts.squared_n:
            for c in a:
                c = c.lower()
                if c in font:
                    c = font[c]
                value += c

        elif font == fdicts.inverted:
            a = a[::-1]
            for c in a:
                if c in font:
                    c = font[c]
                value += c

        elif font == fdicts.circled_n:
            for c in a:
                c = c.upper()
                if c in font:
                    c = font[c]
                value += c

    else:
        for c in a:
            if c in font:
                c = font[c]
            value += c

    return value


def point_convert(button, value):
    """ point to the right convertion """
    treated_v = ''

    if   button ==  '0': treated_v = value.upper()

    elif button ==  '1': treated_v = value.title()

    elif button ==  '2': treated_v = value.lower()

    elif button ==  '3': treated_v = bound_items(value, fdicts.fraktur)

    elif button ==  '4': treated_v = bound_items(value, fdicts.fraktur_b)

    elif button ==  '5': treated_v = bound_items(value, fdicts.monospace)

    elif button ==  '6': treated_v = bound_items(value, fdicts.double_struck)

    elif button ==  '7': treated_v = bound_items(value, fdicts.script)

    elif button ==  '8': treated_v = bound_items(value, fdicts.script_b)

    elif button ==  '9': treated_v = bound_items(value, fdicts.circled_n)

    elif button == '10': treated_v = bound_items(value, fdicts.circled)

    elif button == '11': treated_v = bound_items(value, fdicts.squared)

    elif button == '12': treated_v = bound_items(value, fdicts.squared_n)

    elif button == '13': treated_v = bound_items(value, fdicts.serif_b)

    elif button == '14': treated_v = bound_items(value, fdicts.serif_i)

    elif button == '15': treated_v = bound_items(value, fdicts.serif_ib)

    elif button == '16': treated_v = bound_items(value, fdicts.sans_serif)

    elif button == '17': treated_v = bound_items(value, fdicts.sans_serif_b)

    elif button == '18': treated_v = bound_items(value, fdicts.sans_serif_i)

    elif button == '19': treated_v = bound_items(value, fdicts.sans_serif_ib)

    elif button == '20': treated_v = bound_items(value, fdicts.inverted)

    return treated_v
