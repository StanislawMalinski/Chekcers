import torch
from torch import nn
from torch import tensor


class Model(nn.Module):
    def __init__(self, seq):
        super().__init__()
        self._pipe = nn.Sequential(*seq)

    def forward(self, x):
        return self._pipe(x)


# [0, 0, 0, 0] - puste pole
# [1, 0, 0, 0] - pionek białego
# [0, 1, 0, 0] - pionek czarnego
# [0, 0, 1, 0] - damka białego
# [0, 0, 0, 1] - damka czarnego

if __name__ == "__main__":
    list = [nn.Linear(4, 200),
            nn.ReLU(),
            nn.Linear(200, 128),
            nn.ReLU(),
            nn.Linear(128, 64),
            nn.ReLU(),
            nn.Linear(64, 1),
            nn.Softmax(dim=0)] # Idk if it should be dim=0 XD
    input = torch.Tensor([[[0 for _ in range(4)] for _ in range(4)] for _ in range(8)])
    print(input)
    m = Model(list)
    print(m(input))