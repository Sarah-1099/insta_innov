# insta-innov

## Présentation du Projet
Ce projet a été réalisé dans le cadre du **Rush 4 - User Segmentation** du Bootcamp Data. L'objectif, confié par le département de l'Innovation d'Instagram, est double :
1. Analyser et mesurer scientifiquement l'impact de l'utilisation de l'application sur le bien-être des utilisateurs (stress, bonheur, sommeil).
2. Construire une segmentation comportementale actionnable en production pour permettre aux équipes produit de concevoir des fonctionnalités adaptées à chaque profil.

---

## Répartition de l'Équipe et Responsabilités
Conformément aux exigences du cahier des charges, voici la distribution des rôles et des responsabilités au sein du groupe :

* **[Sarah Mahjoub] :** 
  * Responsable de l'analyse réglementaire et juridique complète (RGPD Union Européenne, lois UK et protection des mineurs) liée au croisement des données d'utilisation et de santé.
  *  Pilotage, relecture et validation de l'intégralité du développement Python du Notebook (coordination du Feature Engineering, du K-Means et de l'Arbre de décision développés par le reste de l'équipe).
* **[Sophie Tandé] :**
  * Responsable de l'analyse réglementaire et juridique complète (RGPD Union Européenne, lois UK et protection des mineurs) liée au croisement des données d'utilisation et de santé.
  * Pilotage, relecture et validation de l'intégralité du développement Python du Notebook (coordination du Feature Engineering, du K-Means et de l'Arbre de décision développés par le reste de l'équipe).
  * Installation, configuration de l'environnement collaboratif Git pour l'équipe.
* **[Emmannuelle Foutou]  :**
  * Écriture du code Python pour le notebook.
  * Rédaction des conclusions statistiques, interprétation des segments d'utilisateurs et documentation des limites du modèle dans le Notebook.
* **[Léonie Degeraud] :**
  * Écriture du code Python pour le notebook.
  * Rédaction des conclusions statistiques, interprétation des segments d'utilisateurs et documentation des limites du modèle dans le Notebook.
* **[Stève Christian Fanta] :**
  * Écriture du code Python pour le notebook.
  * Conception du support de présentation (PowerPoint) pour synthétiser les résultats et les recommandations stratégiques.

---

## Technologies et Bibliothèques utilisées

Sous notre supervision, l'environnement de travail de l'équipe a été configuré avec la stack technique suivante :

* **Gestion des données :** `pandas`, `numpy`
* **Graphiques :** `matplotlib`
* **Machine Learning & Modèles (`scikit-learn`) :**
  * Clustering : `KMeans`
  * Modèles prédictifs : `LogisticRegression`, `HistGradientBoostingClassifier`
  * Préparation : `StandardScaler`, `train_test_split`, `make_pipeline`
* **Évaluation du modèle :** `silhouette_score`, `adjusted_rand_score`, `cohen_kappa_score`, `roc_auc_score`
* **Outils système :** `pathlib`, `json`, `time`, `warnings`

### Installation rapide
Pour lancer le projet sans erreur, exécutez simplement cette commande dans votre terminal :
```bash
pip install pandas numpy matplotlib scikit-learn
```

### Lancement
Ouvrir le fichier `.ipynb` dans VS Code (avec l'environnement virtuel `.venv` activé) ou Google Colab et cliquer sur **Run All**.