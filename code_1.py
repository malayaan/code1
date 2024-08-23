Pour déterminer si les Graph Convolutional Networks (GCNs) étaient appropriés pour mon projet, j'ai mené une revue approfondie de la littérature scientifique afin de comprendre leur potentiel et leurs limites. J'ai notamment étudié l'article fondateur de Kipf et Welling (2017), qui présente une méthode innovante pour l'apprentissage semi-supervisé sur des données structurées en graphes. Ce travail a démontré que les GCNs peuvent efficacement exploiter les relations entre nœuds dans des structures de données complexes, ce qui correspond bien à la nature arborescente de mes données. J'ai également examiné les travaux de Hamilton, Ying et Leskovec (2017), qui ont montré que les GCNs peuvent être appliqués à de grands graphes non vus pendant l'entraînement, offrant ainsi une robustesse dans des environnements de données évolutifs. Enfin, l'étude de Veličković et al. (2018) sur les Graph Attention Networks (GATs) m'a permis de comprendre comment les mécanismes d'attention peuvent améliorer la performance des GCNs en se concentrant sur les parties les plus pertinentes d'un graphe.

Ces recherches m'ont confirmé que les GCNs sont bien adaptés pour traiter des données structurées en graphes, comme celles de mon projet. Cependant, malgré leur potentiel, je n'ai trouvé aucune application des GCNs qui intègre pleinement la dimension temporelle, un aspect crucial pour l'analyse de mes données dynamiques. Cette lacune souligne un défi supplémentaire dans l'adaptation des GCNs à mon projet, nécessitant peut-être le développement de nouvelles approches pour combiner l'analyse temporelle et la structure en graphes de mes données.