# Task 7 — Visualizzazione
# VeloCittà — analisi grafica dei dati

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# STILE GLOBALE

plt.rcParams["figure.figsize"] = (10, 6)
plt.rcParams["axes.titlesize"] = 14
plt.rcParams["axes.labelsize"] = 11

sns.set_theme(style="whitegrid")


# PALETTE COLORBLIND FRIENDLY


palette_citta = ["#0072B2", "#E69F00", "#009E73"] 
palette_tipo = ["#56B4E9", "#D55E00", "#CC79A7"]


# CREAZIONE CARTELLA OUTPUT

os.makedirs("output", exist_ok=True)


# DATI SIMULATI

np.random.seed(42)

citta_list = ["Milano", "Roma", "Torino"]

giorni_settimana = [
    "Lunedì",
    "Martedì",
    "Mercoledì",
    "Giovedì",
    "Venerdì",
    "Sabato",
    "Domenica"
]

df_corse = pd.DataFrame({
    "citta": np.random.choice(citta_list, 100),
    "durata_minuti": np.random.randint(5, 80, 100),
    "tipo": np.random.choice(["classica", "elettrica", "sportiva"], 100),
    "fascia_oraria": np.random.choice(["mattina", "pomeriggio", "sera"], 100),
    "giorno_settimana": np.random.choice(giorni_settimana, 100)
})


# KM REALISTICI

df_corse["km_percorsi"] = np.round(
    df_corse["durata_minuti"] * np.random.uniform(0.15, 0.30, 100),
    2
)

df_utenti = pd.DataFrame({
    "tipo_abbonamento": np.random.choice(["Basic", "Premium"], 50)
})

df_corse["velocita_media"] = df_corse["km_percorsi"] / (df_corse["durata_minuti"] / 60)


# GRAFICO 1 — SERIE TEMPORALE

giorni = pd.date_range("2026-01-01", periods=30)

serie = pd.DataFrame({
    "giorno": giorni,
    "Milano": np.random.randint(80, 200, 30),
    "Roma": np.random.randint(60, 180, 30),
    "Torino": np.random.randint(50, 150, 30)
})

plt.figure()

plt.plot(serie["giorno"], serie["Milano"], label="Milano", color=palette_citta[0], linewidth=2)
plt.plot(serie["giorno"], serie["Roma"], label="Roma", color=palette_citta[1], linewidth=2)
plt.plot(serie["giorno"], serie["Torino"], label="Torino", color=palette_citta[2], linewidth=2)

plt.title("Andamento corse giornaliere per città")
plt.xlabel("Giorno")
plt.ylabel("Numero corse")

plt.legend()

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig("output/01_serie_temporale.png")

plt.show()

plt.close()


# GRAFICO 2 — DISTRIBUZIONE DURATE

plt.figure()

sns.histplot(data=df_corse, x="durata_minuti", hue="citta", kde=True, element="step", palette=palette_citta)

plt.title("Distribuzione durate corse per città")
plt.xlabel("Durata (minuti)")
plt.ylabel("Frequenza")

plt.tight_layout()

plt.savefig("output/02_distribuzione_durate.png")

plt.show()

plt.close()


# GRAFICO 3 — FASCE ORARIE

plt.figure()

sns.barplot(data=df_corse, x="fascia_oraria", y="km_percorsi", hue="tipo", palette=palette_tipo)

plt.title("Corse per fascia oraria e tipo bici")
plt.xlabel("Fascia oraria")
plt.ylabel("Km medi")

plt.legend(title="Tipo bici")

plt.tight_layout()

plt.savefig("output/03_fasce_orarie.png")

plt.show()

plt.close()


# GRAFICO 4 — SCATTER

plt.figure()

for i, citta in enumerate(citta_list):

    subset = df_corse[df_corse["citta"] == citta]

    plt.scatter(
        subset["durata_minuti"],
        subset["velocita_media"],
        label=citta,
        color=palette_citta[i],
        alpha=0.7
    )

m, b = np.polyfit(df_corse["durata_minuti"], df_corse["velocita_media"], 1)

plt.plot(df_corse["durata_minuti"], m * df_corse["durata_minuti"] + b, color="black", linewidth=2)

plt.title("Durata vs Velocità media")
plt.xlabel("Durata (minuti)")
plt.ylabel("Velocità media (km/h)")

plt.legend()

plt.tight_layout()

plt.savefig("output/04_scatter_durata_velocita.png")

plt.show()

plt.close()


# GRAFICO 5 — DASHBOARD

fig, axs = plt.subplots(2, 2, figsize=(12, 8))

df_corse["citta"].value_counts().plot(kind="bar", ax=axs[0, 0], color=palette_citta)

axs[0, 0].set_title("Corse per città")

df_utenti["tipo_abbonamento"].value_counts().plot(
    kind="pie",
    autopct="%1.1f%%",
    ax=axs[0, 1],
    colors=["#0072B2", "#E69F00"]
)

axs[0, 1].set_title("Abbonamenti utenti")

(df_corse.groupby("citta")["km_percorsi"].sum()).plot(
    kind="bar",
    ax=axs[1, 0],
    color=palette_citta
)

axs[1, 0].set_title("Km totali per città")

sns.boxplot(data=df_corse, x="tipo", y="durata_minuti", ax=axs[1, 1], palette=palette_tipo)

axs[1, 1].set_title("Durata per tipo bici")

plt.suptitle("Dashboard VeloCittà")

plt.tight_layout()

plt.savefig("output/05_dashboard.png")

plt.show()

plt.close()


# GRAFICO EXTRA 1 — VELOCITÀ MEDIA

plt.figure()

velocita_citta = df_corse.groupby("citta")["velocita_media"].mean()

velocita_citta.plot(kind="bar", color=palette_citta)

plt.title("Velocità media per città")
plt.xlabel("Città")
plt.ylabel("Velocità media (km/h)")

plt.tight_layout()

plt.savefig("output/06_velocita_media_citta.png")

plt.show()

plt.close()


# GRAFICO EXTRA 2 — CORSE PER TIPO

plt.figure()

sns.countplot(data=df_corse, x="tipo", palette=palette_tipo)

plt.title("Numero corse per tipo bici")
plt.xlabel("Tipo bici")
plt.ylabel("Numero corse")

plt.tight_layout()

plt.savefig("output/07_corse_tipo_bici.png")

plt.show()

plt.close()


# GRAFICO EXTRA 3 — GIORNI SETTIMANA

plt.figure()

ordine_giorni = [
    "Lunedì",
    "Martedì",
    "Mercoledì",
    "Giovedì",
    "Venerdì",
    "Sabato",
    "Domenica"
]

sns.countplot(data=df_corse, x="giorno_settimana", order=ordine_giorni, palette="colorblind")

plt.title("Corse per giorno della settimana")
plt.xlabel("Giorno")
plt.ylabel("Numero corse")

plt.xticks(rotation=20)

plt.tight_layout()

plt.savefig("output/08_corse_giorni_settimana.png")

plt.show()

plt.close()