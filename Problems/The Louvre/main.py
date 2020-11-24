class Painting:
    museum = 'The Louvre'

    def __init__(self, title, painter, year_of_creation):
        self.title = title
        self.painter = painter
        self.year_of_creation = year_of_creation



painting = Painting(input(), input(), input())


print(f'"{painting.title}" by {painting.painter} ({painting.year_of_creation}) hangs in the Louvre.')

