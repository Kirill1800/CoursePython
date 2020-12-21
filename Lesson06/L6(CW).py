class Color:
    red = 0
    green = 0
    blue = 0

    def _init_(self, r, g, b):
        red = r
        green = g
        blue = b

    def toHex(self):
        return '#%02x%02x%02x' % (red, green, blue)


class ColorAlpha(Color):
    alpha = 1

    def _init_(self, r, g, b, a):
        red = r
        green = g
        blue = b
        alpha = a


gray = Color(80, 80, 80)

red = ColorAlpha(255, 0, 0, .5)

