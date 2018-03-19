"""
Duncan Rule, Sally Gao, Yi Hao
"""

class MDPState:
    """State class for a given space in gridworld, with directional attributes pointing to other squares.
    Each directional attribute is a tuple of coordinates (x, y). """

    def __init__(self, up, down, left, right, reward=-1, value=0):
        self.up = up
        self.down = down
        self.left = left
        self.right = right
        self.reward = reward
        self.value = value

    def __str__(self):
        return str(self.value)