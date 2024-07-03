trainer = pl.Trainer(
    logger=logger,
    callbacks=[checkpoint_callback],
    max_epochs=n_epochs,
    accelerator='gpu',  # Spécifie que l'accélération par GPU est requise
    devices=1,  # Utilisation d'un GPU
    enable_progress_bar=True  # Active la barre de progression pour visualiser l'avancement de l'entraînement
)