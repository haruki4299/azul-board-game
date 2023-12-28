from azul_board import Board

class HumanPlayer:
    def __init__(self) -> None:
        self.board = Board()
        self.total_points = 0

class ComputerPlayer:
    def __init__(self) -> None:
        self.board = Board()
        self.total_points = 0