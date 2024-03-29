import math


def norm_angle(a):
    a = a % 360
    if a > 180:
        a -= 360
    return a


class Move:
    def __init__(self, x, y, thrust, message=""):
        self.x, self.y, self.thrust, self.message = x, y, thrust, message

    def __str__(self):
        return f'{self.x} {self.y} {self.thrust} {self.message}'


class State:
    def __init__(self, checkpoints, checkpoint_index, x, y, vx, vy, angle, next_moves,
                 next_expected_moves, state_index=0, previous_state=None, passed_points=[]):
        self.checkpoints = checkpoints
        self.checkpoint_index = checkpoint_index
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.angle = angle
        self.next_moves = next_moves
        self.next_expected_moves = next_expected_moves
        self.previous_state = previous_state
        self.state_index = state_index
        self.next_state = None
        self.passed_points = passed_points

    def __str__(self):
        return f'{self.checkpoint_index}, {self.x}, {self.y}, {self.vx}, {self.vy}, {self.angle})'

    def copy(self):
        return State(self.checkpoints, self.checkpoint_index, self.x, self.y,
                     self.vx, self.vy, self.angle, self.next_moves, self.next_expected_moves,
                     self.state_index, self.previous_state, self.passed_points.copy())

    def next_checkpoint(self):
        return self.checkpoints[self.checkpoint_index % len(self.checkpoints)]

    def next_checkpoint2(self):
        return self.checkpoints[(self.checkpoint_index+1) % len(self.checkpoints)]

    def simulate(self):
        state_copy = self.copy()
        state_copy.simulate_move(self.next_moves[0])
        self.next_state = state_copy
        return state_copy

    def simulate_move(self, move):
        desired_angle = 180 * math.atan2(move.y - self.y, move.x - self.x) / math.pi
        da = norm_angle(desired_angle - self.angle)
        da = max(-18, min(18, da))
        saved_state = self.copy()
        self.angle = self.angle + da
        self.vx += move.thrust * math.cos(self.angle * math.pi / 180)
        self.vy += move.thrust * math.sin(self.angle * math.pi / 180)
        self.x = int(self.x + self.vx)
        self.y = int(self.y + self.vy)
        self.vx = int(0.85 * self.vx)
        self.vy = int(0.85 * self.vy)
        self.angle = round(self.angle) % 360
        xc, yc = self.next_checkpoint()
        dx, dy = self.x - xc, self.y - yc
        if dx * dx + dy * dy <= 600 * 600:
            self.checkpoint_index += 1
        self.state_index += 1
        self.previous_state = saved_state
        self.passed_points.append((saved_state.x, saved_state.y))
