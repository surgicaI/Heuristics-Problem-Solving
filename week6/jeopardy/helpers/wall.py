class Wall:
    def __init__(self, type, coord, start, end):
        # 0 for horizontal, 1 for vertical
        self.type = type
        self.coord = coord
        self.start = start
        self.end = end
