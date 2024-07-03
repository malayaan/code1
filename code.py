from pytorch_lightning import Trainer
from pytorch_lightning.callbacks import ModelCheckpoint
from pytorch_lightning.loggers import TensorBoardLogger

# Configuration du ModelCheckpoint
checkpoint_callback = ModelCheckpoint(
    dirpath='checkpoints',
    filename='best-checkpoint',
    save_top_k=1,
    verbose=True,
    monitor='val_loss',
    mode='min'
)

# Configuration du TensorBoardLogger
logger = TensorBoardLogger("lightning_logs", name="surface-sequences")

# Configuration du Trainer avec le callback intégré et spécification pour l'usage de GPU
trainer = pl.Trainer(
    logger=logger,
    callbacks=[checkpoint_callback],
    max_epochs=n_epochs,
    accelerator='gpu',  # Spécifie que l'accélération par GPU est requise
    devices=1,  # Utilisation d'un GPU
    enable_progress_bar=True  # Active la barre de progression pour visualiser l'avancement de l'entraînement
)
