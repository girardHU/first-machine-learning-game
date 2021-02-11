class Move:

    def __init__(self, distance_to_win_initial):
        self.distance_to_win_initial = distance_to_win_initial
        self.distance_to_win_final = None
        self.move_number = None
        self.iskilling_move = None
        self.iswinning_move = None
        self.isbouncing_move = None
        self.move_score = None

        self.isflagged = False