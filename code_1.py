Dans le cadre de mon projet, la gestion des données manquantes a représenté un enjeu majeur, en particulier dans un contexte où certains effets du PnL peuvent être absents pour certains types de produits. Ces absences créent des lacunes dans les données qui, si elles ne sont pas traitées correctement, peuvent fausser les résultats des modèles prédictifs.

### Remplacement des Données Manquantes

Pour pallier l'absence de certains effets du PnL, j'ai opté pour une méthode simple mais efficace : remplacer les données manquantes par des zéros. Cette approche est particulièrement pertinente lorsque l'absence d'un effet est justifiée par la nature même du produit financier, c'est-à-dire que cet effet n'est tout simplement pas applicable. Par exemple, si un produit n'est pas censé générer un certain type de revenu ou de perte, il est logique de considérer que cet effet est nul.

### Min-encoding avec les Embeddings

Dans d'autres cas, les données manquantes ne sont pas simplement des zéros par défaut. Parfois, il manque des informations critiques comme le *Product Type* ou d'autres attributs clés. Pour ces cas-là, j'ai utilisé une approche de *min-encoding* avec les embeddings précédemment mis en place. Le *min-encoding* permet de remplacer les valeurs manquantes par les valeurs minimales observées dans les données d'entraînement pour ces embeddings, garantissant ainsi que les données manquantes ne perturbent pas le modèle en introduisant des biais.

### Adaptation aux Besoins Métier

L'un des défis majeurs de cette approche a été la nécessité d'adapter les solutions de manière personnalisée en fonction des besoins spécifiques des analystes. Il n'était pas possible d'appliquer une méthode standardisée de gestion des données manquantes ; chaque situation nécessitait une évaluation précise pour déterminer la meilleure approche. Cette flexibilité a été essentielle pour aligner le travail technique avec les attentes métier et assurer la pertinence des résultats.

### Prévention du Data Leakage

Un aspect crucial de cette démarche a été de prévenir le **data leakage**. Pour ce faire, j'ai veillé à séparer rigoureusement les données entre les ensembles d'entraînement (train) et de test avant de procéder à tout traitement, y compris la gestion des données manquantes et l'application des embeddings. Cela a permis de s'assurer que les modèles ne bénéficient pas d'informations qu'ils ne devraient pas avoir lors de la phase de test, garantissant ainsi l'intégrité des résultats.

Ce travail minutieux de gestion des données, qu'il s'agisse de combler les lacunes ou de créer des représentations vectorielles robustes, a permis de renforcer la qualité des données utilisées et, par conséquent, la fiabilité des analyses et des modèles développés.