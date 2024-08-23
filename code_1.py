Dans le cadre de l'analyse des données de risques, trois dates spécifiques sont souvent considérées : **la date de maturité effective**, **la date de maturité globale**, et **la date de pricing**. 

1. **Effective Maturity** (maturité effective) : C'est la date à laquelle un instrument financier, tel qu'une obligation ou un contrat dérivé, arrive à expiration, et le principal est remboursé. Cette date reflète l'échéance réelle de l'instrument après avoir pris en compte toutes les conditions spécifiques, telles que les options d'appel ou de remboursement anticipé.

2. **Global Maturity** (maturité globale) : Cette date représente l'échéance prévue initialement pour l'instrument, sans tenir compte des ajustements ou des modifications pouvant survenir pendant la durée de vie de l'instrument. Elle est souvent utilisée comme une référence pour les conditions générales du contrat.

3. **Pricing Date** (date de pricing) : C'est la date à laquelle le prix de l'instrument est fixé ou évalué. Cette date est essentielle pour la valorisation du PnL (Profit and Loss) et des effets associés.

**Transformation en colonnes booléennes :**
En convertissant ces dates en deux colonnes booléennes :
- **pricingdate_global_maturity** : Indique si la date de pricing correspond à la date de maturité globale.
- **pricingdate_effective_maturity** : Indique si la date de pricing correspond à la date de maturité effective.

**Intérêt de cette transformation :**
Cette transformation permet de détecter facilement des incohérences ou des anomalies dans les données, qui pourraient signaler des problèmes de qualité des données (DQ). Par exemple, si une date de pricing correspond à la maturité effective mais pas à la maturité globale, cela pourrait indiquer un ajustement récent qui n'a pas été correctement pris en compte dans toutes les parties du système. De telles anomalies pourraient fausser les calculs de PnL ou d'autres métriques de risque, ce qui rend cette vérification cruciale.

Cette approche s'appuie sur l'expérience partagée par les analystes, qui ont souligné l'importance de surveiller les incohérences temporelles pour identifier les erreurs potentielles dans les données de marché et les processus de valorisation. En automatisant cette vérification, on améliore la capacité à détecter ces problèmes rapidement et à les corriger avant qu'ils n'affectent les analyses financières.