class Move:

    def __init__(self, distance_to_win_initial=None, vector=None):
        self.distance_to_win_initial = distance_to_win_initial
        self.distance_to_win_final = None
        self.move_number = None
        self.iskilling_move = False
        self.iswinning_move = False
        self.isbouncing_move = False
        self.move_score = None

        self.isflagged = False

        self.vector = vector