# Rush 4 – Segmentation des utilisateurs d'Instagram (Insta Innov)

Segmentation des utilisateurs fondée sur leur usage, lien entre usage et bien-être (stress, sommeil,
bonheur), règle d'affectation d'un nouvel utilisateur, limites et protection des données.

## Livrables

| Livrable | Emplacement |
|---|---|
| Notebook (s'exécute de haut en bas, résultats identiques à chaque exécution) | `rush4_segmentation.ipynb` |
| Slides de soutenance (15 min) | à venir |

## Lancer le notebook

```
python -m venv .venv
.venv\Scripts\activate            (Windows)
pip install -r requirements.txt
jupyter notebook rush4_segmentation.ipynb      puis « Run All »
```

Les deux extraits doivent être dans `data/` :
`instagram_usage_lifestyleSafe.csv` et `instagram_users_lifestyleSafe.csv`.

## Règles du projet

- Graine aléatoire fixée (`GRAINE = 42`) : deux exécutions donnent les mêmes résultats.
- Confidentialité : aucune ligne d'utilisateur affichée, aucun groupe affiché de moins de 100 personnes.
- Les segments n'utilisent que des colonnes d'usage, connues pour tous les utilisateurs ; le bien-être
  ne sert qu'à les évaluer.

## Répartition du travail

| Binôme | Membres | Responsabilités |
|---|---|---|
| A – Données | Sarah, Sophie | Choix des données, exploration, notebook propre et reproductible |
| B – Segmentation | Léonie, Emmy | Variables, segments, affectation d'un nouvel utilisateur |
| C – Évaluation & conformité | Stève, Myriam | Critères, évaluation, limites, RGPD, slides |
