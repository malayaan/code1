Voici un récapitulatif des pistes explorées pour le **README** de ton projet :

---

## Pistes Explorées pour la Détection d'Incidents de Data Quality

### 1. **Approche Statistique** : Analyse des Deals Contribuant au *Unexplained PnL*

J'ai commencé par une approche statistique visant à identifier les deals au sein des portefeuilles affectés par des incidents de data quality (DQ). L'idée principale était de repérer les deals avec la plus forte contribution au unexplained PnL, en les considérant comme plus susceptibles d'être à l'origine des problèmes de qualité des données. Cependant, en comparant les deals identifiés par cette méthode avec ceux évoqués dans les commentaires des incidents, je ne retrouvais pas réellement les mêmes deals. Après discussion avec les analystes, j'ai conclu que cette méthode n'était pas adéquate pour résoudre le problème.

### 2. **Approches de Machine Learning**

#### A. **Classification des Portefeuilles**

J'ai exploré une classification au niveau des portefeuilles, cherchant à catégoriser les portefeuilles selon qu'ils étaient affectés ou non par un incident de DQ. Le problème principal de cette approche résidait dans le fait qu'elle n'exploitait pas la dimension temporelle. Nos labels étaient basés sur les rapports d'incidents, sans réel versioning des données modifiées. De plus, la temporalité était partiellement rompue, car certains incidents étaient déclarés au niveau GOP (groupe de portefeuilles), ce qui introduisait des "trous" dans les données temporelles disponibles.

#### B. **Détection d'Anomalies Semi-Supervisée au Niveau Deal**

J'ai ensuite mis en place une approche de détection d'anomalies semi-supervisée au niveau des deals. Utilisant un modèle d'Isolation Forest avec un scoreur personnalisé, cette méthode permettait d'intégrer l'expertise des analystes (qui connaissent les proportions attendues d'incidents) et de minimiser les faux positifs. Bien que cette approche ait montré une certaine efficacité, elle reste limitée par les données disponibles et les labels peu précis.

### 3. **Autres Pistes Explorées et Abandonnées**

J'ai également envisagé plusieurs autres méthodes, qui n'ont pas été retenues en raison des contraintes de données :

- **Graph Neural Networks (GNN)** : J'ai envisagé l'utilisation des GNN pour modéliser les relations entre les deals et portefeuilles, mais cette approche a été abandonnée car mes données ne sont pas adaptées à cette structure de graphe: les portefeuilles contiennent trop de deals et j'ai trop de portefeuilles pour contruire un grand nombre de graphes.
  
- **Classification des Portefeuilles par Time Series** : Une classification basée sur des séries temporelles des portefeuilles a été explorée, mais a dû être abandonnée en raison des "trous" dans mes données, empêchant une analyse chronologique continue.

- **Reconstruction du PnL via les Features Disponibles** : J'ai tenté une approche de reconstruction du PnL à partir des autres features disponibles dans les données. Cependant, cette approche a été abandonnée, car mes données étaient trop éloignées des données réelles utilisées par les analystes pour modéliser le PnL.
