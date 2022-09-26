import random

random.seed(0)


class Agent:
    def __init__(self, x: int, y: int, name: str = 'A'):
        self.x, self.y = x, y
        self.name = name
        print("Agent created successfully!")

    def move(self, direction: str) -> None:
        # UP=W DOWN=S LEFT=A RIGHT=D
        moves = {
            'W': [1, 0],
            'S': [-1, 0],
            'D': [0, 1],
            'A': [0, -1],
            'default': [0, 0]
        }
        move = moves.get(direction, moves['default'])
        self.x += move[0]
        self.y += move[1]


class Scene:
    def __init__(self, n_rows: int, n_cols: int, weight: float = 80):
        # Generation of spaces and obstacles matrix.
        self.mat = [random.choices(['-', 'X'],
                                   k=n_cols,
                                   weights=(weight, 100 - weight))
                    for _ in range(n_rows)]
        self.agents = {}
        print("Scene created successfully!")

    def __str__(self):
        # String of the object
        print(self.mat)
        # Reversed. Last row becomes first row.
        # Needed since the (0, 0) is on top left corner.
        return "\n".join([" ".join(map(str, row)) for row in self.mat][::-1])

    def agent_tracking(self, agent: Agent):
        self.mat[agent.x][agent.y] = agent.name
        self.agents[agent.name] = agent


my_agent = Agent(2, 2)
my_scene = Scene(6, 6)
my_scene.agent_tracking(my_agent)
print(my_scene)
user_move = None

while user_move != "EXIT":
    user_move = input("Introduce move (W, S, D, A, EXIT): ").upper()
    my_agent.move(user_move)
    my_scene.agent_tracking(my_agent)
    print("Scene updated")
    print("Agent now at:", my_agent.x, my_agent.y)
    print(my_scene)
