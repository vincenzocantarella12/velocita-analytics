# Task 6 — Pandas: Caricamento, Pulizia e Analisi
# VeloCittà — analisi corse, bici e utenti

import numpy as np
import pandas as pd

np.random.seed(42)


# CREAZIONE DATAFRAME

n_corse = 80
n_bici = 20
n_utenti = 25

citta_list = ["Milano", "Roma", "Torino"]
fasce = ["mattina", "pomeriggio", "sera"]


# DATAFRAME CORSE

df_corse = pd.DataFrame({
    "id_corsa": [f"C{i}" for i in range(n_corse)],
    "id_bici": np.random.choice([f"B{i}" for i in range(n_bici)], n_corse),
    "id_utente": np.random.choice([f"U{i}" for i in range(n_utenti)], n_corse),
    "citta": np.random.choice(citta_list, n_corse),
    "data_corsa": pd.date_range("2026-01-01", periods=n_corse),
    "durata_minuti": np.random.randint(5, 80, n_corse).astype(float),

# Km più realistici

    "km_percorsi": np.round(
        np.random.randint(5, 80, n_corse) *
        np.random.uniform(0.15, 0.35, n_corse),
        2
    ),

    "fascia_oraria": np.random.choice(fasce, n_corse)
})


# Inserimento NaN

for i in np.random.choice(df_corse.index, 8, replace=False):

    if np.random.rand() > 0.5:
        df_corse.loc[i, "durata_minuti"] = np.nan

    else:
        df_corse.loc[i, "km_percorsi"] = np.nan


# Inserimento duplicati

df_corse = pd.concat(
    [df_corse, df_corse.sample(5)],
    ignore_index=True
)


# DATAFRAME BICI

df_bici = pd.DataFrame({
    "id_bici": [f"B{i}" for i in range(n_bici)],
    "tipo": np.random.choice(
        ["classica", "elettrica", "sportiva"],
        n_bici
    ),
    "citta": np.random.choice(citta_list, n_bici),
    "anno_acquisto": np.random.randint(2018, 2025, n_bici),
    "costo_acquisto": np.round(
        np.random.uniform(300, 2000, n_bici),
        2
    )
})


# DATAFRAME UTENTI

df_utenti = pd.DataFrame({
    "id_utente": [f"U{i}" for i in range(n_utenti)],
    "nome": [f"Utente_{i}" for i in range(n_utenti)],
    "citta": np.random.choice(citta_list, n_utenti),
    "tipo_abbonamento": np.random.choice(
        ["Basic", "Premium"],
        n_utenti
    ),
    "data_iscrizione": pd.date_range(
        "2025-01-01",
        periods=n_utenti
    )
})


# PULIZIA DATI

print("\nINFO PRIMA PULIZIA\n")

print(f"Numero righe: {df_corse.shape[0]}")
print(f"Numero colonne: {df_corse.shape[1]}")

print("\nVALORI NULLI\n")

print(df_corse.isnull().sum())

print("\nTIPI DI DATI\n")

print(df_corse.dtypes)

print("\nDESCRIBE PRIMA PULIZIA\n")

print(df_corse.describe())


# Rimozione duplicati

df_corse = df_corse.drop_duplicates()


# Riempimento NaN durata_minuti

df_corse["durata_minuti"] = df_corse["durata_minuti"].fillna(
    df_corse.groupby("citta")["durata_minuti"]
    .transform("median")
)


# Riempimento NaN km_percorsi

df_corse["km_percorsi"] = df_corse["km_percorsi"].fillna(
    df_corse["durata_minuti"] * 0.18
)


# Conversione datetime

df_corse["data_corsa"] = pd.to_datetime(
    df_corse["data_corsa"]
)


# Colonne temporali

df_corse["mese"] = df_corse["data_corsa"].dt.month


giorni_italiani = {
    "Monday": "Lunedì",
    "Tuesday": "Martedì",
    "Wednesday": "Mercoledì",
    "Thursday": "Giovedì",
    "Friday": "Venerdì",
    "Saturday": "Sabato",
    "Sunday": "Domenica"
}


df_corse["giorno_settimana"] = (
    df_corse["data_corsa"]
    .dt.day_name()
    .map(giorni_italiani)
)


print("\nINFO DOPO PULIZIA\n")

print(f"Numero righe: {df_corse.shape[0]}")
print(f"Numero colonne: {df_corse.shape[1]}")

print("\nVALORI NULLI\n")

print(df_corse.isnull().sum())

print("\nTIPI DI DATI\n")

print(df_corse.dtypes)

print("\nDESCRIBE DOPO PULIZIA\n")

print(df_corse.describe())


# APPLY E COLONNE DERIVATE

def classifica_corsa(durata):

    if durata < 15:
        return "breve"

    elif durata <= 45:
        return "media"

    else:
        return "lunga"


df_corse["tipo_corsa"] = (
    df_corse["durata_minuti"]
    .apply(classifica_corsa)
)


# Velocità media

df_corse["velocita_media"] = (
    df_corse["km_percorsi"] /
    (df_corse["durata_minuti"] / 60)
)


# Costo stimato

def costo_stimato(minuti):

    if minuti < 15:
        return 1.50

    elif minuti <= 45:
        return 2.50 + 0.10 * (minuti - 15)

    else:
        return 5.00 + 0.08 * (minuti - 45)


df_corse["costo_stimato"] = (
    df_corse["durata_minuti"]
    .apply(costo_stimato)
)


# AGGREGAZIONI

group_citta = df_corse.groupby("citta").agg({
    "id_corsa": "count",
    "durata_minuti": "mean",
    "km_percorsi": "sum",
    "costo_stimato": "sum"
})


print("\nGROUP BY CITTÀ\n")

print(group_citta)


group_fascia = df_corse.groupby(
    "fascia_oraria"
).agg({
    "id_corsa": "count",
    "velocita_media": "mean"
})


print("\nGROUP BY FASCIA ORARIA\n")

print(group_fascia)


pivot = pd.pivot_table(
    df_corse,
    index="citta",
    columns="tipo_corsa",
    values="id_corsa",
    aggfunc="count",
    fill_value=0
)


print("\nPIVOT TABLE\n")

print(pivot)


# MERGE DATASET

df_merge = (
    df_corse
    .merge(df_bici, on="id_bici")
    .merge(df_utenti, on="id_utente")
)


# Rinomina colonne duplicate

df_merge = df_merge.rename(columns={
    "citta_x": "citta_corsa",
    "citta_y": "citta_bici",
    "citta": "citta_utente"
})


print("\nMERGE DATASET\n")

print(df_merge.head())


print("\nCOLONNE DATAFRAME MERGE\n")

for colonna in df_merge.columns:

    print(f"- {colonna}")


# TOP ANALYSIS

top_bici = (
    df_corse["id_bici"]
    .value_counts()
    .head(5)
)


print("\nTOP 5 BICI PER CORSE\n")

print(top_bici)


top_utenti = (
    df_merge[df_merge["tipo_abbonamento"] == "Premium"]
    .groupby("id_utente")["costo_stimato"]
    .sum()
    .sort_values(ascending=False)
    .head(3)
)


print("\nTOP 3 UTENTI PREMIUM PER COSTO\n")

print(top_utenti)


# STATISTICHE EXTRA

print("\nCITTÀ CON PIÙ CORSE\n")

corse_per_citta = (
    df_corse["citta"]
    .value_counts()
)

print(corse_per_citta)


print("\nFASCIA ORARIA PIÙ UTILIZZATA\n")

fascia_piu_usata = (
    df_corse["fascia_oraria"]
    .mode()[0]
)

print(f"Fascia oraria più utilizzata: {fascia_piu_usata}")


print("\nGIORNO CON PIÙ CORSE\n")

giorni_piu_frequenti = (
    df_corse["giorno_settimana"]
    .value_counts()
)

print(giorni_piu_frequenti)


# Questo file utilizza Pandas
# per simulare e analizzare dati
# relativi alle corse del sistema VeloCittà.

# Sono state utilizzate:
# - creazione DataFrame
# - gestione NaN
# - rimozione duplicati
# - apply
# - groupby
# - merge
# - pivot table
# - statistiche descrittive

# Le colonne derivate permettono
# di ottenere informazioni aggiuntive
# come velocità media, costo stimato
# e classificazione delle corse.

# Le statistiche finali aiutano
# ad analizzare l’utilizzo del servizio
# nelle diverse città e fasce orarie.