import torch

# Vérifie si CUDA est disponible
cuda_available = torch.cuda.is_available()
print("CUDA disponible:", cuda_available)

# Affiche le nombre de GPU disponibles et leurs noms si CUDA est disponible
if cuda_available:
    num_gpus = torch.cuda.device_count()
    print("Nombre de GPU(s) disponible(s):", num_gpus)
    for i in range(num_gpus):
        print(f"GPU {i}: {torch.cuda.get_device_name(i)}")
else:
    print("Aucun GPU compatible CUDA n'est disponible.")
