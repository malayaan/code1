### Rapport de Stage : Détection des Incidents de Qualité des Données dans les Valeurs de PnL

#### Introduction
Mon stage a pour objectif principal de détecter les incidents de qualité des données (DQ) dans les différents aspects des activités bancaires. En adoptant une démarche structurée et méthodique, j'ai progressivement concentré mes efforts sur les valeurs de PnL (Profit and Loss). Voici un aperçu de la logique et des étapes clés de ma démarche durant le premier mois de stage.

#### Immersion et Compréhension du Contexte

Dès le début du stage, il était crucial de comprendre l'environnement bancaire et les rôles des différents acteurs impliqués. J'ai participé à des sessions d'onboarding pour m'immerger dans cet environnement complexe. Les rencontres avec des analystes, notamment Benjamin Pocard et Caroline Cao, m'ont permis de découvrir les outils et interfaces utilisés, comme l'application MM, essentielle pour consulter les consommations et valorisations par périmètre. Ces échanges m'ont également aidé à comprendre les interactions entre analystes et traders, et à cerner les tâches quotidiennes qui composent leur travail.

Parallèlement, nous avons mis en place une organisation structurée avec des points hebdomadaires regroupant Caroline, Benjamin et ma tutrice Nathalie Sertier, afin de suivre régulièrement l'avancement du projet et d'éviter l'effet tunnel.

#### Analyse Exploratoire et Identification des Patterns

Une fois le contexte assimilé, j'ai entamé une analyse exploratoire des incidents de DQ. L'objectif était de dégager des patterns et des points d'attention en étudiant la répartition temporelle des incidents et leur distribution par périmètre. Cette phase exploratoire m'a permis de mieux comprendre les circonstances des incidents et de poser des bases solides pour les analyses futures.

J'ai également poursuivi l'analyse statistique des rapports d'incidents pour identifier les circonstances et les points communs entre incidents de même métrique. Cette analyse a révélé que les incidents étaient particulièrement fréquents et impactants au niveau des valeurs de PnL, ce qui a orienté mes analyses subséquentes.

#### Approfondissement de la Compréhension du Dataflow

Pour structurer efficacement ma démarche, j'ai approfondi ma compréhension du dataflow et des applications utilisées par les analystes, en particulier MyMetrics. Cette application est cruciale pour certifier les consommations et valorisations de PnL, ainsi que pour effectuer les ajustements nécessaires.

En parallèle, j'ai exploré l'adaptabilité des Graph Convolutional Networks (GCN) à nos données. Cette approche m'a semblé prometteuse pour classifier les inputs en fonction de la structure analytique de la banque, du GOP jusqu'au deal, car c'est souvent à ce niveau que les incidents se produisent. J'ai également pris connaissance du travail de Djahiz Meliani, qui propose un algorithme de drill down pour reproduire le travail de certification des analystes. Cette découverte a inspiré certaines des méthodes que j'ai envisagées pour mon propre projet.

#### Nettoyage et Préparation des Données

Une étape essentielle de ma démarche a été le nettoyage des données. J'ai identifié et éliminé les faux positifs dans les données d'incidents, ce qui a permis de clarifier et de fiabiliser le dataset. Ensuite, j'ai préparé les données pour les analyses ultérieures, en sélectionnant soigneusement les dates et périmètres pertinents, tout en tenant compte des contraintes de capacité de nos machines.

La détection de doublons dans les signalements de problèmes de DQ a été un autre aspect crucial. Une étude statistique a permis de mieux comprendre ces doublons et d'affiner les données. J'ai aussi rencontré des difficultés pour comprendre le PnL et ce qu'il contient réellement, surtout n'ayant pas de formation en finance. L'accès aux données de PnL, bien que difficile au début, s'est finalement révélé possible, ce qui a validé ma volonté d'aller dans cette direction.

#### Focalisation sur les Valeurs de PnL

Bien que le sujet de mon stage ne soit pas restreint aux valeurs de PnL, plusieurs facteurs m'ont conduit à me concentrer sur cet aspect spécifique :

- **Concentration des Incidents** : Les incidents de qualité des données sont particulièrement fréquents et impactants au niveau des valeurs de PnL.
- **Outils et Données Disponibles** : Les outils et données disponibles, comme MyMetrics, se sont révélés bien adaptés à une analyse approfondie du PnL, facilitant ainsi la détection et la correction des incidents de DQ. L'accès aux données de PnL, bien que difficile au début, s'est finalement révélé possible, ce qui a validé ma volonté d'aller dans cette direction.
- **Adaptation des Méthodes** : Les difficultés initiales pour comprendre le PnL et son contenu ont été surmontées, confirmant la pertinence de cette focalisation pour apporter des résultats concrets.

#### Conclusion

Ce premier mois a été structuré autour de la compréhension du contexte, l'analyse exploratoire des données, l'approfondissement du dataflow, et la préparation des données pour l'analyse. Chaque étape a contribué à construire une base solide, permettant d'avancer de manière méthodique vers la détection des incidents de qualité des données, avec un focus particulier sur les valeurs de PnL.

---