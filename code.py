pip uninstall torch torchvision torchaudio
pip install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu123
import torch
print(torch.__version__)
print(torch.cuda.is_available())
