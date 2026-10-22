
import pandas as pd
from pathlib import Path

# 1. Charger les données CSV
dossier = Path(__file__).parent
fichier = dossier / "Data" / "Donnees_nettoyees.csv"

df = pd.read_csv(fichier, sep=";")

# Vérifier le nombre de lignes et de colonnes
print("Dimensions du fichier :", df.shape)

# Afficher les noms des colonnes
print("\nNoms des colonnes :")
print(df.columns.tolist())

# Afficher les cinq premières lignes
print("\nAperçu des données :")
print(df.head())

# 2. Vérifier la qualité des données

# Afficher les types de données
print("\n--- TYPES DES COLONNES ---")
print(df.dtypes)

# Compter les valeurs manquantes
print("\n--- VALEURS MANQUANTES ---")
print(df.isnull().sum().sort_values(ascending=False))

# Compter les lignes en double
print("\n--- DOUBLONS ---")
print("Nombre de lignes dupliquées :", df.duplicated().sum())

# Vérifier les identifiants utilisateurs
print("\n--- IDENTIFIANTS UTILISATEURS ---")
print("Nombre d'identifiants uniques :", df["user_id"].nunique())
print("Nombre de lignes :", len(df))

# Statistiques descriptives des colonnes numériques
print("\n--- STATISTIQUES DESCRIPTIVES ---")
print(df.describe().round(2))

# 3. Exploration du profil des utilisateurs d'un point de vue sociodémographique

# Age
print("\n--- AGE DES UTILISATEURS ---")
print(df["age"].describe())

# Genre
print("\n--- REPARTITION PAR GENRE ---")
print(df["gender"].value_counts())

# Pays
print("\n--- REPARTITION PAR PAYS ---")
print(df["country"].value_counts().head(10))

# Situation professionnelle
print("\n--- SITUATION PROFESSIONNELLE ---")
print(df["employment_status"].value_counts())

# Zone geographique : urbaine ou rurale
print("\n--- ZONE GEOGRAPHIQUE ---")
print(df["urban_rural"].value_counts())

# Niveau de revenu
print("\n--- NIVEAU DE REVENU ---")
print(df["income_level"].value_counts())

# Situation amoureuse
print("\n--- SITUATION AMOUREUSE ---")
print(df["relationship_status"].value_counts())

# Presence d'enfants
print("\n--- PRESENCE D'ENFANTS ---")
print(df["has_children"].value_counts())


# 4. Comparaison des profils et du temps d'activité quotidien

variables_profil = [
    "urban_rural",
    "income_level",
    "relationship_status",
    "has_children",
    "gender",
    "employment_status",
]

for variable in variables_profil:
    tableau = df.groupby(variable, observed=True)[
        "daily_active_minutes_instagram"
    ].agg(
        nombre_utilisateurs="count",
        temps_moyen="mean",
        temps_median="median",
        ecart_type="std"
    ).round(2)

    print(f"\n--- TEMPS D'ACTIVITE SELON {variable.upper()} ---")
    print(tableau)

# 5. Comparaison de l'âge et du temps d'activité quotidien

df["categorie_age"] = pd.cut(
    df["age"],
    bins=[0, 18, 25, 35, 45, 55, 65, float("inf")],
    labels=[
        "18 ans et moins",
        "19-25 ans",
        "26-35 ans",
        "36-45 ans",
        "46-55 ans",
        "56-65 ans",
        "66 ans et plus"
    ]
)

tableau_age = df.groupby("categorie_age")[
    "daily_active_minutes_instagram"
].agg(
    nombre_utilisateurs="count",
    temps_moyen="mean",
    temps_median="median",
    ecart_type="std"
).round(2)

print("\n--- TEMPS D'ACTIVITE SELON L'AGE ---")
print(tableau_age)

# 6. Comparer le bonheur et le temps passé sur Instagram
# Variables de profil à analyser
variables_profil = [
    "categorie_age",
    "urban_rural",
    "income_level",
    "relationship_status",
    "has_children",
    "gender",
    "employment_status"
]

# Comparer le bonheur et le temps passé sur Instagram
for variable in variables_profil:
    tableau = df.groupby(variable, observed=False).agg(
        nombre_utilisateurs=("self_reported_happiness", "count"),
        bonheur_moyen=("self_reported_happiness", "mean"),
        temps_moyen=("daily_active_minutes_instagram", "mean")
    ).round(2)

    print(f"\n--- ANALYSE SELON : {variable} ---")
    print(tableau)

# Corrélation entre temps sur Instagram et bonheur
# pour chaque catégorie de profil

for variable in variables_profil:
    print(f"\n--- CORRELATION SELON : {variable} ---")

    for categorie, groupe in df.groupby(variable, observed=False):
        donnees = groupe[
            ["daily_active_minutes_instagram", "self_reported_happiness"]
        ].dropna()

        if len(donnees) >= 2:
            correlation = donnees[
                "daily_active_minutes_instagram"
            ].corr(donnees["self_reported_happiness"])

            print(
                f"{categorie} : "
                f"corrélation = {correlation:.2f} "
                f"(n = {len(donnees)})"
            )

# 8. Comparer le sommeil et le temps passé sur Instagram
# Variables de profil à analyser
variables_profil = [
    "categorie_age",
    "urban_rural",
    "income_level",
    "relationship_status",
    "has_children",
    "gender",
    "employment_status"
]

# Comparer le sommeil et le temps passé sur Instagram
for variable in variables_profil:
    tableau = df.groupby(variable, observed=False).agg(
        nombre_utilisateurs=("sleep_hours_per_night", "count"),
        sommeil_moyen=("sleep_hours_per_night", "mean"),
        temps_moyen=("daily_active_minutes_instagram", "mean")
    ).round(2)

    print(f"\n--- ANALYSE SELON : {variable} ---")
    print(tableau)

# Corrélation entre temps sur Instagram et sommeil
# pour chaque catégorie de profil

for variable in variables_profil:
    print(f"\n--- CORRELATION SELON : {variable} ---")

    for categorie, groupe in df.groupby(variable, observed=False):
        donnees = groupe[
            ["daily_active_minutes_instagram", "sleep_hours_per_night"]
        ].dropna()

        if len(donnees) >= 2:
            correlation = donnees[
                "daily_active_minutes_instagram"
            ].corr(donnees["sleep_hours_per_night"])

            print(
                f"{categorie} : "
                f"corrélation = {correlation:.2f} "
                f"(n = {len(donnees)})"
            )

# 9. Comparer le stress et le temps passé sur Instagram
# Variables de profil à analyser
variables_profil = [
    "categorie_age",
    "urban_rural",
    "income_level",
    "relationship_status",
    "has_children",
    "gender",
    "employment_status"
]

# Comparer le stress et le temps passé sur Instagram
for variable in variables_profil:
    tableau = df.groupby(variable, observed=False).agg(
        nombre_utilisateurs=("perceived_stress_score", "count"),
        stress_moyen=("perceived_stress_score", "mean"),
        temps_moyen=("daily_active_minutes_instagram", "mean")
    ).round(2)

    print(f"\n--- ANALYSE SELON : {variable} ---")
    print(tableau)

# Corrélation entre temps sur Instagram et stress
# pour chaque catégorie de profil

for variable in variables_profil:
    print(f"\n--- CORRELATION SELON : {variable} ---")

    for categorie, groupe in df.groupby(variable, observed=False):
        donnees = groupe[
            ["daily_active_minutes_instagram", "perceived_stress_score"]
        ].dropna()

        if len(donnees) >= 2:
            correlation = donnees[
                "daily_active_minutes_instagram"
            ].corr(donnees["perceived_stress_score"])

            print(
                f"{categorie} : "
                f"corrélation = {correlation:.2f} "
                f"(n = {len(donnees)})"
            )


# 8. Exploration du profil des utilisateurs d'un point de vue habitudes de vie
# Sommeil
print("\n--- DUREE DE SOMMEIL ---")
print(df["sleep_hours_per_night"].describe())

# Alimentation
print("\n--- HABITUDES ALIMENTAIRES ---")
print(df["diet_quality"].value_counts())

# Tabac
print("\n--- FUMEURS ---")
print(df["smoking"].value_counts())

# Alcool
print("\n--- CONSOMMATION D'ALCOOL ---")
print(df["alcohol_frequency"].value_counts())

# STRESS
print("\n--- NIVEAU DE STRESS ---")
print(df["perceived_stress_score"].value_counts())

# IMC
print("\n--- IMC ---")
print(df["body_mass_index"].value_counts())

# Niveau de tension (systolique)
print("\n--- TENSION ARTERIELLE (SYSTOLIQUE) ---")
print(df["blood_pressure_systolic"].value_counts())

# Niveau de tension (diastolique)
print("\n--- TENSION ARTERIELLE (DIASTOLIQUE) ---")
print(df["blood_pressure_diastolic"].value_counts())

# Pas quotidiens
print("\n--- NOMBRE DE PAS QUOTIDIENS ---")
print(df["daily_steps_count"].value_counts())

# Heure de travail par semaine
print("\n--- NOMBRE D'HEURES DE TRAVAIL PAR SEMAINE ---")
print(df["weekly_work_hours"].value_counts())

# Hobbies
print("\n--- NOMBRE DE HOBBIES ---")
print(df["hobbies_count"].value_counts())

# Evènements sociaux par mois
print("\n--- NOMBRE D'EVENEMENTS SOCIAUX PAR MOIS ---")
print(df["social_events_per_month"].value_counts())

# Livres lus par an
print("\n--- NOMBRE DE LIVRES LUS PAR AN ---")
print(df["books_read_per_year"].value_counts())

# Bénévolat
print("\n--- TEMPS DE BENEVOLAT PAR MOIS ---")
print(df["volunteer_hours_per_month"].value_counts())

# Voyage
print("\n--- NOMBRE DE VOYAGES PAR AN ---")
print(df["travel_frequency_per_year"].value_counts())

# 9. Comparaison des profils et du temps d'activité quotidien

variables_profil = [
    "sleep_hours_per_night",
    "diet_quality",
    "smoking",
    "alcohol_frequency",
    "perceived_stress_score",
    "body_mass_index",
    "blood_pressure_systolic",
    "blood_pressure_diastolic",
    "daily_steps_count",
    "weekly_work_hours",
    "hobbies_count",
    "social_events_per_month",
    "books_read_per_year",
    "volunteer_hours_per_month",
    "travel_frequency_per_year"
]

for variable in variables_profil:
    tableau = df.groupby(variable, observed=True)[
        "daily_active_minutes_instagram"
    ].agg(
        nombre_utilisateurs="count",
        temps_moyen="mean",
        temps_median="median",
        ecart_type="std"
    ).round(2)

    print(f"\n--- TEMPS D'ACTIVITE SELON {variable.upper()} ---")
    print(tableau)

# 10. Comparer le bonheur et le temps passé sur Instagram
# Variables de profil à analyser
variables_profil = [
    "sleep_hours_per_night",
    "diet_quality",
    "smoking",
    "alcohol_frequency",
    "perceived_stress_score",
    "body_mass_index",
    "blood_pressure_systolic",
    "blood_pressure_diastolic",
    "daily_steps_count",
    "weekly_work_hours",
    "hobbies_count",
    "social_events_per_month",
    "books_read_per_year",
    "volunteer_hours_per_month",
    "travel_frequency_per_year"
]

 
# 11. CREATION DES CATEGORIES D'HABITUDES DE VIE
# 1. Sommeil
df["categorie_sommeil"] = pd.cut(
    df["sleep_hours_per_night"],
    bins=[-float("inf"), 6, 7, 9, float("inf")],
    labels=["Moins de 6 h", "6 à moins de 7 h",
            "7 à moins de 9 h", "9 h et plus"],
    right=False
)

# 2. Qualité de l'alimentation : conserver les modalités existantes
df["categorie_alimentation"] = df["diet_quality"].astype("category")

# 3. Tabagisme : conserver les modalités existantes
df["categorie_tabagisme"] = df["smoking"].astype("category")

# 4. Fréquence de consommation d'alcool
df["categorie_alcool"] = df["alcohol_frequency"].astype("category")

# 5. Stress : trois groupes selon la distribution des scores
df["categorie_stress"] = pd.qcut(
    df["perceived_stress_score"].rank(method="first"),
    q=3,
    labels=["Stress faible", "Stress intermédiaire", "Stress élevé"]
)

# 6. IMC : trois groupes selon la distribution observée
df["categorie_imc"] = pd.qcut(
    df["body_mass_index"].rank(method="first"),
    q=3,
    labels=["IMC bas", "IMC intermédiaire", "IMC élevé"]
)

# 7. Pression artérielle systolique : trois groupes
df["categorie_tension_systolique"] = pd.qcut(
    df["blood_pressure_systolic"].rank(method="first"),
    q=3,
    labels=["Valeurs basses", "Valeurs intermédiaires", "Valeurs élevées"]
)

# 8. Pression artérielle diastolique : trois groupes
df["categorie_tension_diastolique"] = pd.qcut(
    df["blood_pressure_diastolic"].rank(method="first"),
    q=3,
    labels=["Valeurs basses", "Valeurs intermédiaires", "Valeurs élevées"]
)

# 9. Nombre de pas quotidiens
df["categorie_pas"] = pd.cut(
    df["daily_steps_count"],
    bins=[-float("inf"), 5000, 7500, 10000, float("inf")],
    labels=["Moins de 5 000", "5 000 à 7 499",
            "7 500 à 9 999", "10 000 et plus"],
    right=False
)

# 10. Heures de travail par semaine
df["categorie_temps_travail"] = pd.cut(
    df["weekly_work_hours"],
    bins=[-float("inf"), 0, 30, 40, float("inf")],
    labels=["Aucune heure", "1 à 29 h",
            "30 à 40 h", "Plus de 40 h"],
    right=False
)

# 11. Nombre de loisirs
df["categorie_loisirs"] = pd.cut(
    df["hobbies_count"],
    bins=[-float("inf"), 1, 3, 5, float("inf")],
    labels=["Aucun", "1 à 2", "3 à 4", "5 et plus"],
    right=False
)

# 12. Événements sociaux par mois
df["categorie_evenements_sociaux"] = pd.cut(
    df["social_events_per_month"],
    bins=[-float("inf"), 1, 3, 6, float("inf")],
    labels=["Aucun", "1 à 2", "3 à 5", "6 et plus"],
    right=False
)

# 13. Livres lus par an
df["categorie_lecture"] = pd.cut(
    df["books_read_per_year"],
    bins=[-float("inf"), 1, 6, 13, float("inf")],
    labels=["Aucun", "1 à 5", "6 à 12", "13 et plus"],
    right=False
)

# 14. Heures de bénévolat par mois
df["categorie_benevolat"] = pd.cut(
    df["volunteer_hours_per_month"],
    bins=[-float("inf"), 1, 5, 11, float("inf")],
    labels=["Aucune heure", "1 à 4 h", "5 à 10 h", "Plus de 10 h"],
    right=False
)

# 15. Voyages par an
df["categorie_voyages"] = pd.cut(
    df["travel_frequency_per_year"],
    bins=[-float("inf"), 1, 3, 6, float("inf")],
    labels=["Aucun", "1 à 2", "3 à 5", "6 et plus"],
    right=False
)

print("Toutes les catégories ont été créées."),

 # Catégories 
colonnes_categories = [
    "categorie_sommeil",
    "categorie_alimentation",
    "categorie_tabagisme",
    "categorie_alcool",
    "categorie_stress",
    "categorie_imc",
    "categorie_tension_systolique",
    "categorie_tension_diastolique",
    "categorie_pas",
    "categorie_temps_travail",
    "categorie_loisirs",
    "categorie_evenements_sociaux",
    "categorie_lecture",
    "categorie_benevolat",
    "categorie_voyages"
]

for colonne in colonnes_categories:
    print(f"\n--- {colonne} ---")
    print(df[colonne].value_counts(dropna=False))


# 12. Comparer le bonheur et le temps passé sur Instagram
for variable in colonnes_categories:
    tableau = df.groupby(variable, observed=False).agg(
        nombre_utilisateurs=("self_reported_happiness", "count"),
        bonheur_moyen=("self_reported_happiness", "mean"),
        temps_moyen=("daily_active_minutes_instagram", "mean")
    ).round(2)

    print(f"\n--- ANALYSE SELON : {variable} ---")
    print(tableau)


# Corrélation entre temps sur Instagram et bonheur
# pour chaque catégorie de profil

for variable in colonnes_categories:
    print(f"\n--- CORRELATION SELON : {variable} ---")

    for categorie, groupe in df.groupby(variable, observed=False):
        donnees = groupe[
            ["daily_active_minutes_instagram", "self_reported_happiness"]
        ].dropna()
        
        if len(donnees) >= 2:
            correlation = donnees[
                "daily_active_minutes_instagram"
            ].corr(donnees["self_reported_happiness"])

            print(
                f"{categorie} : "
                f"corrélation = {correlation:.2f} "
                f"(n = {len(donnees)})"
            )


# 13. Comparer le sommeil et le temps passé sur Instagram
for variable in colonnes_categories:
    tableau = df.groupby(variable, observed=False).agg(
        nombre_utilisateurs=("sleep_hours_per_night", "count"),
        sommeil_moyen=("sleep_hours_per_night", "mean"),
        temps_moyen=("daily_active_minutes_instagram", "mean")
    ).round(2)

    print(f"\n--- ANALYSE SELON : {variable} ---")
    print(tableau)


# Corrélation entre temps sur Instagram et sommeil
# pour chaque catégorie de profil

for variable in colonnes_categories:
    print(f"\n--- CORRELATION SELON : {variable} ---")

    for categorie, groupe in df.groupby(variable, observed=False):
        donnees = groupe[
            ["daily_active_minutes_instagram", "sleep_hours_per_night"]
        ].dropna()
        
        if len(donnees) >= 2:
            correlation = donnees[
                "daily_active_minutes_instagram"
            ].corr(donnees["sleep_hours_per_night"])

            print(
                f"{categorie} : "
                f"corrélation = {correlation:.2f} "
                f"(n = {len(donnees)})"
            )


# 14.Comparer le stress et le temps passé sur Instagram
for variable in colonnes_categories:
    tableau = df.groupby(variable, observed=False).agg(
        nombre_utilisateurs=("perceived_stress_score", "count"),
        stress_moyen=("perceived_stress_score", "mean"),
        temps_moyen=("daily_active_minutes_instagram", "mean")
    ).round(2)

    print(f"\n--- ANALYSE SELON : {variable} ---")
    print(tableau)


# Corrélation entre temps sur Instagram et stress
# pour chaque catégorie de profil

for variable in colonnes_categories:
    print(f"\n--- CORRELATION SELON : {variable} ---")

    for categorie, groupe in df.groupby(variable, observed=False):
        donnees = groupe[
            ["daily_active_minutes_instagram", "perceived_stress_score"]
        ].dropna()
        
        if len(donnees) >= 2:
            correlation = donnees[
                "daily_active_minutes_instagram"
            ].corr(donnees["perceived_stress_score"])

            print(
                f"{categorie} : "
                f"corrélation = {correlation:.2f} "
                f"(n = {len(donnees)})"
            )


# 14. Exploration du profil des utilisateurs d'un point de vue utilisation d'Instagram

# Sessions d'Instagram
print("\n--- SESSIONS PAR JOUR ---")
print(df["sessions_per_day"].value_counts())

# Posts créés
print("\n--- POSTS CRÉÉS PAR SEMAINE ---")
print(df["posts_created_per_week"].value_counts())

# Réels regardés
print("\n--- RÉELS REGARDÉS PAR JOUR ---")
print(df["reels_watched_per_day"].value_counts())

# Stories regardées
print("\n--- STORIES REGARDÉES PAR JOUR ---")
print(df["stories_viewed_per_day"].value_counts())

# Likes
print("\n--- LIKES DONNÉS PAR JOUR ---")
print(df["likes_given_per_day"].value_counts())

# Commentaires
print("\n--- COMMENTAIRES ÉCRITS PAR JOUR ---")
print(df["comments_written_per_day"].value_counts())

# DM envoyés
print("\n--- DM ENVOYÉS PAR SEMAINE ---")
print(df["dms_sent_per_week"].value_counts())

# DM reçus
print("\n--- DM REÇUS PAR SEMAINE ---")
print(df["dms_received_per_week"].value_counts())

# Publicités vues
print("\n--- PUBLICITÉS VUES PAR JOUR ---")
print(df["ads_viewed_per_day"].value_counts())

# Pubicités cliquées
print("\n--- PUBLICITÉS CLIQUÉES PAR JOUR ---")
print(df["ads_clicked_per_day"].value_counts())

# Temps passé sur le fil d'actualité
print("\n--- TEMPS PASSÉ SUR LE FIL D'ACTUALITÉ PAR JOUR ---")
print(df["time_on_feed_per_day"].value_counts())

# Temps passé sur l'exploration
print("\n--- TEMPS PASSÉ SUR L'EXPLORATION PAR JOUR ---")
print(df["time_on_explore_per_day"].value_counts())

# Temps passé sur les messages
print("\n--- TEMPS PASSÉ SUR LES MESSAGES PAR JOUR ---")
print(df["time_on_messages_per_day"].value_counts())

# Temps passé sur les réels
print("\n--- TEMPS PASSÉ SUR LES RÉELS PAR JOUR ---")
print(df["time_on_reels_per_day"].value_counts())

# Nombre de followers
print("\n--- NOMBRE DE FOLLOWERS ---")
print(df["followers_count"].value_counts())

# Nombre de followings
print("\n--- NOMBRE DE FOLLOWINGS ---")
print(df["following_count"].value_counts())

# Fonctionnalités premium utilisées
print("\n--- FONCTIONNALITÉS PREMIUM UTILISÉES ---")
print(df["uses_premium_features"].value_counts())

# Taux de réponses aux notifications
print("\n--- TAUX DE RÉPONSES AUX NOTIFICATIONS ---")
print(df["notification_response_rate"].value_counts())

# Date de création du compte
print("\n--- DATE DE CRÉATION DU COMPTE ---")
print(df["account_creation_year"].describe())

# Dernière connexion
print("\n--- DERNIÈRE CONNEXION ---")
print(df["last_login_date"].describe())

# Durée moyenne de session 
print("\n--- DURÉE MOYENNE DE SESSION ---")
print(df["average_session_length_minutes"].describe())

# Type de contenu préféré
print("\n--- TYPE DE CONTENU PRÉFÉRÉ ---")
print(df["content_type_preference"].value_counts())

# Type de thème préféré
print("\n--- TYPE DE THÈME PRÉFÉRÉ ---")
print(df["preferred_content_theme"].value_counts())

# Niveau de paramètre de confidentialité
print("\n--- NIVEAU DE PARAMÈTRE DE CONFIDENTIALITÉ ---")
print(df["privacy_setting_level"].value_counts())

# Double authentification
print("\n--- DOUBLE AUTHENTIFICATION ---")
print(df["two_factor_auth_enabled"].value_counts())

# Biométrie activée
print("\n--- BIOMÉTRIE ACTIVÉE ---")
print(df["biometric_login_used"].value_counts())

# Nombre de compte liés
print("\n--- NOMBRE DE COMPTES LIÉS ---")
print(df["linked_accounts_count"].value_counts())

# Statut d'inscription
print("\n--- STATUT D'INSCRIPTION ---")
print(df["subscription_status"].value_counts())

# Score d'engagement de l'utilisateur
print("\n--- SCORE D'ENGAGEMENT DE L'UTILISATEUR ---")
print(df["user_engagement_score"].describe())

# 15. Comparaison des profils et du temps d'activité quotidien
variables_profil = [
    "sessions_per_day",
    "posts_created_per_week",
    "reels_watched_per_day",
    "stories_viewed_per_day",
    "likes_given_per_day",
    "comments_written_per_day",
    "dms_sent_per_week",
    "dms_received_per_week",
    "ads_viewed_per_day",
    "ads_clicked_per_day",
    "time_on_feed_per_day",
    "time_on_explore_per_day",
    "time_on_messages_per_day",
    "time_on_reels_per_day",
    "followers_count",
    "following_count",
    "uses_premium_features",
    "notification_response_rate",
    "account_creation_year",
    "last_login_date",
    "average_session_length_minutes",
    "content_type_preference",
    "preferred_content_theme",
    "privacy_setting_level",
    "two_factor_auth_enabled",
    "biometric_login_used",
    "linked_accounts_count",
    "subscription_status",
    "user_engagement_score"
]


for colonne in df.columns:
    if "content" in colonne.lower() or "theme" in colonne.lower():
        print(repr(colonne))

for variable1 in variables_profil:
    tableau1 = df.groupby(variable1, observed=False)[
        "daily_active_minutes_instagram"
    ].agg(["count", "mean", "median", "std"]).round(2)

    tableau1 = tableau1.rename(columns={
        "count": "nombre_utilisateurs",
        "mean": "temps_moyen",
        "median": "temps_median",
        "std": "ecart_type"
    })

    print(f"\n--- TEMPS D'ACTIVITE SELON {variable1.upper()} ---")
    print(tableau1)


# 16.CATEGORIES DES VARIABLES D'UTILISATION D'INSTAGRAM

# Sessions par jour
df["categorie_sessions"] = pd.cut(
    df["sessions_per_day"],
    bins=[-float("inf"), 3, 6, 11, float("inf")],
    labels=["0 à 2", "3 à 5", "6 à 10", "Plus de 10"],
    right=False
)

# Publications par semaine
df["categorie_publications"] = pd.cut(
    df["posts_created_per_week"],
    bins=[-float("inf"), 1, 3, 6, float("inf")],
    labels=["0", "1 à 2", "3 à 5", "6 et plus"],
    right=False
)

# Reels regardés par jour
df["categorie_reels"] = pd.cut(
    df["reels_watched_per_day"],
    bins=[-float("inf"), 10, 30, 60, float("inf")],
    labels=["0 à 9", "10 à 29", "30 à 59", "60 et plus"],
    right=False
)

# Stories vues par jour
df["categorie_stories"] = pd.cut(
    df["stories_viewed_per_day"],
    bins=[-float("inf"), 10, 30, 60, float("inf")],
    labels=["0 à 9", "10 à 29", "30 à 59", "60 et plus"],
    right=False
)

# Likes donnés par jour
df["categorie_likes"] = pd.cut(
    df["likes_given_per_day"],
    bins=[-float("inf"), 20, 50, 100, float("inf")],
    labels=["0 à 19", "20 à 49", "50 à 99", "100 et plus"],
    right=False
)

# Commentaires écrits par jour
df["categorie_commentaires"] = pd.cut(
    df["comments_written_per_day"],
    bins=[-float("inf"), 1, 5, 10, float("inf")],
    labels=["0", "1 à 4", "5 à 9", "10 et plus"],
    right=False
)

# Messages envoyés par semaine
df["categorie_messages_envoyes"] = pd.cut(
    df["dms_sent_per_week"],
    bins=[-float("inf"), 1, 10, 30, float("inf")],
    labels=["0", "1 à 9", "10 à 29", "30 et plus"],
    right=False
)

# Messages reçus par semaine
df["categorie_messages_recus"] = pd.cut(
    df["dms_received_per_week"],
    bins=[-float("inf"), 10, 30, 60, float("inf")],
    labels=["0 à 9", "10 à 29", "30 à 59", "60 et plus"],
    right=False
)

# Publicités vues par jour
df["categorie_publicites_vues"] = pd.cut(
    df["ads_viewed_per_day"],
    bins=[-float("inf"), 10, 20, 40, float("inf")],
    labels=["0 à 9", "10 à 19", "20 à 39", "40 et plus"],
    right=False
)

# Publicités cliquées par jour
df["categorie_publicites_cliquees"] = pd.cut(
    df["ads_clicked_per_day"],
    bins=[-float("inf"), 1, 3, 6, float("inf")],
    labels=["0", "1 à 2", "3 à 5", "6 et plus"],
    right=False
)

# Temps passé sur le fil d'actualité
df["categorie_temps_fil"] = pd.cut(
    df["time_on_feed_per_day"],
    bins=[-float("inf"), 30, 60, 120, float("inf")],
    labels=["Moins de 30 min", "30 à 59 min",
            "60 à 119 min", "120 min et plus"],
    right=False
)

# Temps passé sur Explorer
df["categorie_temps_explorer"] = pd.cut(
    df["time_on_explore_per_day"],
    bins=[-float("inf"), 10, 30, 60, float("inf")],
    labels=["Moins de 10 min", "10 à 29 min",
            "30 à 59 min", "60 min et plus"],
    right=False
)

# Temps passé dans les messages
df["categorie_temps_messages"] = pd.cut(
    df["time_on_messages_per_day"],
    bins=[-float("inf"), 10, 30, 60, float("inf")],
    labels=["Moins de 10 min", "10 à 29 min",
            "30 à 59 min", "60 min et plus"],
    right=False
)

# Temps passé sur les Reels
df["categorie_temps_reels"] = pd.cut(
    df["time_on_reels_per_day"],
    bins=[-float("inf"), 15, 30, 60, float("inf")],
    labels=["Moins de 15 min", "15 à 29 min",
            "30 à 59 min", "60 min et plus"],
    right=False
)

# Nombre d'abonnés : quartiles
df["categorie_abonnes"] = pd.qcut(
    df["followers_count"].rank(method="first"),
    q=4,
    labels=["Faible", "Moyen-faible", "Moyen-élevé", "Élevé"]
)

# Nombre de comptes suivis : quartiles
df["categorie_comptes_suivis"] = pd.qcut(
    df["following_count"].rank(method="first"),
    q=4,
    labels=["Faible", "Moyen-faible", "Moyen-élevé", "Élevé"]
)

# Fonctionnalités premium
df["categorie_premium"] = df["uses_premium_features"].astype("category")

# Taux de réponse aux notifications : quartiles
df["categorie_reponse_notifications"] = pd.qcut(
    df["notification_response_rate"].rank(method="first"),
    q=4,
    labels=["Faible", "Moyen-faible", "Moyen-élevé", "Élevé"]
)

# Année de création du compte
df["account_creation_year"] = pd.to_datetime(
    df["account_creation_year"], errors="coerce"
)

anciennete_compte = (
    pd.Timestamp.today().normalize() - df["account_creation_year"]
).dt.days / 365.25

df["categorie_anciennete_compte"] = pd.cut(
    anciennete_compte,
    bins=[-float("inf"), 1, 3, 5, float("inf")],
    labels=["Moins de 1 an", "1 à moins de 3 ans",
            "3 à moins de 5 ans", "5 ans et plus"],
    right=False
)


# Date de dernière connexion
print("\n--- DERNIÈRE CONNEXION ---")

# Convertir les valeurs en véritables dates
df["last_login_date"] = pd.to_datetime(
    df["last_login_date"],
    errors="coerce"
)

print(df["last_login_date"].describe())

# Calculer le nombre de jours depuis la dernière connexion
jours_depuis_connexion = (
    pd.Timestamp.today().normalize() - df["last_login_date"]
).dt.days

# Créer des catégories selon la récence de connexion
df["categorie_recence_connexion"] = pd.cut(
    jours_depuis_connexion,
    bins=[-float("inf"), 1, 7, 30, float("inf")],
    labels=[
        "Moins de 1 jour",
        "1 à 6 jours",
        "7 à 29 jours",
        "30 jours et plus"
    ],
    right=False
)

# Durée moyenne d'une session
df["categorie_duree_session"] = pd.cut(
    df["average_session_length_minutes"],
    bins=[-float("inf"), 2, 5, 10, float("inf")],
    labels=["Moins de 2 min", "2 à moins de 5 min",
            "5 à moins de 10 min", "10 min et plus"],
    right=False
)

# Type de contenu préféré
df["categorie_type_contenu"] = df["content_type_preference"].astype("category")

# Thème de contenu préféré
df["categorie_theme_contenu"] = df["preferred_content_theme"].astype("category")

# Niveau de confidentialité
df["categorie_confidentialite"] = df["privacy_setting_level"].astype("category")

# Authentification à deux facteurs
df["categorie_double_authentification"] = df["two_factor_auth_enabled"].astype("category")

# Connexion biométrique
df["categorie_connexion_biometrique"] = df["biometric_login_used"].astype("category")

# Nombre de comptes liés
df["categorie_comptes_lies"] = pd.cut(
    df["linked_accounts_count"],
    bins=[-float("inf"), 1, 2, 3, float("inf")],
    labels=["0", "1", "2", "3 et plus"],
    right=False
)

# Statut d'abonnement
df["categorie_abonnement"] = df["subscription_status"].astype("category")

# Score d'engagement : quartiles
df["categorie_engagement"] = pd.qcut(
    df["user_engagement_score"].rank(method="first"),
    q=4,
    labels=["Faible", "Moyen-faible", "Moyen-élevé", "Élevé"]
)

print("Création des catégories terminée.")

# Catégories 
colonnes_categories_bis = [
    "categorie_sessions",
    "categorie_publications",
    "categorie_reels",
    "categorie_stories",
    "categorie_likes",
    "categorie_commentaires",
    "categorie_messages_envoyes",
    "categorie_messages_recus",
    "categorie_publicites_vues",
    "categorie_publicites_cliquees",
    "categorie_temps_fil",
    "categorie_temps_explorer",
    "categorie_temps_messages",
    "categorie_temps_reels",
    "categorie_abonnes",
    "categorie_comptes_suivis",
    "categorie_premium",
    "categorie_reponse_notifications",
    "categorie_anciennete_compte",
    "categorie_recence_connexion",
    "categorie_recence_connexion",
    "categorie_duree_session",
    "categorie_type_contenu",
    "categorie_theme_contenu",
    "categorie_confidentialite",
    "categorie_double_authentification",
    "categorie_connexion_biometrique",
    "categorie_comptes_lies",
    "categorie_abonnement",
    "categorie_engagement"
    ]

for colonne in colonnes_categories:
    print(f"\n--- {colonne} ---")
    print(df[colonne].value_counts(dropna=False))


# 17. Comparer le bonheur et le temps passé sur Instagram
for variable in colonnes_categories_bis:
    tableau = df.groupby(variable, observed=False).agg(
        nombre_utilisateurs=("self_reported_happiness", "count"),
        bonheur_moyen=("self_reported_happiness", "mean"),
        temps_moyen=("daily_active_minutes_instagram", "mean")
    ).round(2)

    print(f"\n--- ANALYSE SELON : {variable} ---")
    print(tableau)

# Corrélation entre temps sur Instagram et bonheur
# pour chaque catégorie de profil

for variable in colonnes_categories_bis:
    print(f"\n--- CORRELATION SELON : {variable} ---")

    for categorie, groupe in df.groupby(variable, observed=False):
        donnees = groupe[
            ["daily_active_minutes_instagram", "self_reported_happiness"]
        ].dropna()

        if len(donnees) >= 2:
            correlation = donnees[
                "daily_active_minutes_instagram"
            ].corr(donnees["self_reported_happiness"])

            print(
                f"{categorie} : "
                f"corrélation = {correlation:.2f} "
                f"(n = {len(donnees)})"
            )

# 18. Comparer le sommeil et le temps passé sur Instagram
for variable in colonnes_categories_bis:
    tableau = df.groupby(variable, observed=False).agg(
        nombre_utilisateurs=("sleep_hours_per_night", "count"),
        sommeil_moyen=("sleep_hours_per_night", "mean"),
        temps_moyen=("daily_active_minutes_instagram", "mean")
    ).round(2)

    print(f"\n--- ANALYSE SELON : {variable} ---")
    print(tableau)

# Corrélation entre temps sur Instagram et sommeil
# pour chaque catégorie de profil

for variable in colonnes_categories_bis:
    print(f"\n--- CORRELATION SELON : {variable} ---")

    for categorie, groupe in df.groupby(variable, observed=False):
        donnees = groupe[
            ["daily_active_minutes_instagram", "sleep_hours_per_night"]
        ].dropna()

        if len(donnees) >= 2:
            correlation = donnees[
                "daily_active_minutes_instagram"
            ].corr(donnees["sleep_hours_per_night"])

            print(
                f"{categorie} : "
                f"corrélation = {correlation:.2f} "
                f"(n = {len(donnees)})"
            )

# 19. Comparer le stress et le temps passé sur Instagram
for variable in colonnes_categories_bis:
    tableau = df.groupby(variable, observed=False).agg(
        nombre_utilisateurs=("perceived_stress_score", "count"),
        stress_moyen=("perceived_stress_score", "mean"),
        temps_moyen=("daily_active_minutes_instagram", "mean")
    ).round(2)

    print(f"\n--- ANALYSE SELON : {variable} ---")
    print(tableau)

# Corrélation entre temps sur Instagram et stress
# pour chaque catégorie de profil

for variable in colonnes_categories_bis:
    print(f"\n--- CORRELATION SELON : {variable} ---")

    for categorie, groupe in df.groupby(variable, observed=False):
        donnees = groupe[
            ["daily_active_minutes_instagram", "perceived_stress_score"]
        ].dropna()

        if len(donnees) >= 2:
            correlation = donnees[
                "daily_active_minutes_instagram"
            ].corr(donnees["perceived_stress_score"])

            print(
                f"{categorie} : "
                f"corrélation = {correlation:.2f} "
                f"(n = {len(donnees)})"
            )
            
