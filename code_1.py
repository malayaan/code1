### Feature Engineering pour les Colonnes Textuelles

Dans le cadre de mon projet, le **Feature Engineering** des colonnes textuelles a été un aspect essentiel pour améliorer la qualité et la pertinence des données en vue de la détection des anomalies de qualité des données (DQ). Ce processus a impliqué plusieurs étapes clés pour transformer des informations textuelles en données vectorielles exploitables par des algorithmes de machine learning.

#### **1. Regroupement des Product Types :**
Les *Product Types* décrivent les différentes natures des instruments financiers présents dans les données. Cela inclut une variété de produits tels que les **Shares**, **Options Leg**, **Index Forward**, **Dividend Leg**, **Stock Future**, **Basket Forward**, et **Trackers**. Ces catégories de produits se comportent différemment en termes de risque, mais certains partagent des caractéristiques communes qui justifient un regroupement.

Sur la base des témoignages des analystes, j'ai créé un **mapping** pour regrouper les types de produits en **Product Type Groups**. L'objectif était de simplifier l'analyse en regroupant les produits susceptibles de présenter des comportements similaires en termes de métriques de risque et de détection des incidents de DQ. Par exemple, les **Shares** et les **Stock Futures** peuvent être regroupés sous une même catégorie, car ils présentent des dynamiques similaires.

#### **2. Vectorisation des Colonnes Textuelles :**
Outre les *Product Types*, j'avais également des colonnes pour les noms de portefeuilles et les sous-jacents. Pour ces colonnes, ainsi que pour les *Product Type Groups* nouvellement créés, j'ai choisi une approche de vectorisation inspirée du traitement du langage naturel (NLP).

J'ai utilisé un modèle **Word2Vec** pour obtenir des *embeddings* des valeurs textuelles. L'idée était de traiter chaque ligne de mes données comme une phrase composée de trois éléments : le *Product Type Group*, le *nom du portefeuille*, et le *nom du sous-jacent*. Cette approche permet d'entraîner le modèle Word2Vec sur ces "phrases", générant ainsi des vecteurs d'embeddings qui capturent la proximité sémantique entre différents termes.

#### **3. Optimisation des Embeddings par Analyse en Composantes Principales (PCA) :**
Après avoir obtenu les embeddings via Word2Vec, j'ai utilisé une **Analyse en Composantes Principales (PCA)** pour déterminer la dimension optimale des vecteurs d'embeddings. L'objectif était de réduire la dimensionnalité tout en conservant le maximum d'inertie, c'est-à-dire l'essentiel de l'information contenue dans les données.

En pratique, j'ai déterminé que trois dimensions suffisaient pour capturer les informations pertinentes pour les *underlying names*, les *portfolios*, et les *Product Type Groups*. Cette réduction dimensionnelle permet à mon algorithme de détection d'anomalies de mieux interpréter les relations entre les différents éléments, en exploitant des embeddings qui traduisent la similarité comportementale entre certains sous-jacents en termes d'incidents de DQ.

#### **Références Techniques :**
Pour approfondir l'implémentation de **Word2Vec**, je me suis référé à l'article fondateur de **Mikolov et al. (2013)**, qui présente le modèle et ses applications principales dans le domaine du NLP. Ce modèle est basé sur l'idée que les mots apparaissant dans des contextes similaires ont des significations proches, une approche qui a montré son efficacité pour capturer les relations sémantiques entre les mots. L'application de Word2Vec dans le cadre de mon projet a permis de traduire des concepts financiers en vecteurs numériques exploitables par des modèles prédictifs, une démarche alignée avec les meilleures pratiques en NLP et en machine learning.

En résumé, ce travail de Feature Engineering sur les colonnes textuelles a permis de structurer les données de manière à améliorer la précision des modèles de détection d'anomalies, tout en assurant une représentation cohérente et pertinente des informations textuelles critiques.