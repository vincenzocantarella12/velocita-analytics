# Task 5 — Analisi Numerica con NumPy
# VeloCittà — simulazione dati corse

import numpy as np


# 5.1 — GENERAZIONE DATI


np.random.seed(42)


# Durate corse - distribuzione normale


durate = np.random.normal(28, 12, 500)
durate = np.clip(durate, 1, None).astype(int)



# Km percorsi - proporzionali alla durata


km = durate * np.random.uniform(0.15, 0.25, size=500)
km = np.round(km, 2)



# Velocità media km/h


velocita = km / (durate / 60)




# Funzione riepilogo


def riepilogo(array, nome):

    print(f"\n--- {nome} ---")
    print("shape:", array.shape)
    print("dtype:", array.dtype)
    print("min:", np.min(array))
    print("max:", np.max(array))
    print("media:", np.mean(array))
    print("std:", np.std(array))




# Riepiloghi


riepilogo(durate, "DURATE")
riepilogo(km, "KM")
riepilogo(velocita, "VELOCITÀ")




# 5.2 — SLICING E SELEZIONE



# Prime 10 e ultime 10 corse


prime_10 = durate[:10]

ultime_10 = durate[-10:]


print("\nPrime 10 durate:", prime_10)

print("Ultime 10 durate:", ultime_10)




# Fancy indexing


indici = np.array([0, 42, 99, 150, 200, 350, 499])

selezione = durate[indici]


print("\nSelezione fancy indexing:", selezione)




# Maschera booleana


maschera = durate > 45

print("\nCorse > 45 minuti:", np.sum(maschera))

print("Distanza media:", np.mean(km[maschera]))




# Indici velocità massima/minima



idx_max_vel = np.argmax(velocita)

idx_min_vel = np.argmin(velocita)


print("\nIndice velocità massima:", idx_max_vel)

print("Velocità max:", velocita[idx_max_vel])


print("\nIndice velocità minima:", idx_min_vel)

print("Velocità min:", velocita[idx_min_vel])





# 5.3 — STATISTICHE E NORMALIZZAZIONE


# Percentili


percentili = np.percentile(durate, [25, 50, 75, 90])


print("\nPercentili durate:")

print("25%:", percentili[0])
print("50%:", percentili[1])
print("75%:", percentili[2])
print("90%:", percentili[3])




# Min-max normalization


durate_norm = (durate - np.min(durate)) / (np.max(durate) - np.min(durate))


print("\nNormalizzazione check (min, max):")

print(np.min(durate_norm), np.max(durate_norm))




# Correlazione Pearson


corr = np.corrcoef(durate, km)[0, 1]

print("\nCorrelazione durate-km:", corr)



# Commento:
# La correlazione positiva indica
# che all’aumentare della durata
# aumentano anche i km percorsi.




# 5.4 — SERIE TEMPORALE SIMULATA


np.random.seed(42)


# Corse giornaliere


corse_giornaliere = np.random.randint(80, 200, size=30)




# Media mobile 7 giorni


media_mobile = np.convolve(corse_giornaliere,np.ones(7) / 7,mode='valid')




# Giorni massimo/minimo


giorno_max = np.argmax(corse_giornaliere) + 1

giorno_min = np.argmin(corse_giornaliere) + 1


print("\nGiorno con più corse:", giorno_max,"valore:", np.max(corse_giornaliere))

print("Giorno con meno corse:", giorno_min,"valore:", np.min(corse_giornaliere))




# Riepilogo finale


print("\n--- Riepilogo (giorno, corse, media mobile) ---")


for i in range(len(corse_giornaliere)):

    giorno = i + 1

    corse = corse_giornaliere[i]


    if i >= 6:

        media = round(media_mobile[i - 6], 2)

    else:

        media = "-"

    print(f"Giorno {giorno} | Corse: {corse} | Media mobile: {media}")




# Questo file utilizza NumPy
# per simulare e analizzare dati numerici
# relativi alle corse del sistema VeloCittà.

# Sono state utilizzate:
# - distribuzioni casuali
# - slicing
# - fancy indexing
# - maschere booleane
# - statistiche descrittive
# - correlazione
# - normalizzazione
# - simulazioni temporali

# La media mobile permette di osservare
# l’andamento delle corse nel tempo
# riducendo le variazioni giornaliere.