import sys
import math


def norm_angle(a):
    a = a % 360  # 0..360
    if a > 180:
        a -= 360  # -180..180
    return a

def parse_move(line: str):
    f = line.split(" ")
    return Move(int(f[0]), int(f[1]), int(f[2]))

class Move:
    def __init__(self, x, y, thrust, message=""):
        self.x, self.y, self.thrust, self.message = x, y, thrust, message

    def __str__(self):
        return f'{self.x} {self.y} {self.thrust} {self.message}'



class State:
    def __init__(self, checkpoints, checkpoint_index, x, y, vx, vy, angle, next_moves, next_expected_moves):
        self.checkpoints = checkpoints
        self.checkpoint_index = checkpoint_index
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.angle = angle
        self.next_moves = next_moves
        self.next_expected_moves = next_expected_moves

    def __str__(self):
        return f'State(checkpoints, {self.checkpoint_index}, {self.x}, {self.y}, {self.vx}, {self.vy}, {self.angle})'

    def copy(self):
        return State(self.checkpoints, self.checkpoint_index, self.x, self.y, self.vx, self.vy, self.angle)

    def next_checkpoint(self):
        return self.checkpoints[self.checkpoint_index % len(self.checkpoints)]

    def simulate(self):
        desired_angle = 180 * math.atan2(self.next_moves[0].y - self.y, self.next_moves[0].x - self.x) / math.pi
        da = norm_angle(desired_angle - self.angle)
        da = max(-18, min(18, da))
        self.angle = self.angle + da
        self.vx += self.next_moves[0].thrust * math.cos(self.angle * math.pi / 180)
        self.vy += self.next_moves[0].thrust * math.sin(self.angle * math.pi / 180)
        self.x = int(self.x + self.vx)
        self.y = int(self.y + self.vy)
        self.vx = int(0.85 * self.vx)
        self.vy = int(0.85 * self.vy)
        self.angle = round(self.angle) % 360
        xc, yc = self.next_checkpoint()
        dx, dy = self.x - xc, self.y - yc
        if dx * dx + dy * dy <= 600 * 600:
            self.checkpoint_index += 1
