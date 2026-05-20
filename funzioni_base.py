# Calcola la durata in minuti tra due orari


def calcola_durata_minuti(ora_inizio: str, ora_fine: str) -> int:

    ore_inizio, minuti_inizio = map(int, ora_inizio.split(":"))
    ore_fine, minuti_fine = map(int, ora_fine.split(":"))

    minuti_totali_inizio = ore_inizio * 60 + minuti_inizio
    minuti_totali_fine = ore_fine * 60 + minuti_fine

    if minuti_totali_fine < minuti_totali_inizio:
        raise ValueError("L'orario finale non può essere precedente a quello iniziale.")

    return minuti_totali_fine - minuti_totali_inizio





# Classifica una corsa in breve, media o lunga


def classifica_corsa(durata_minuti: int) -> str:

    if durata_minuti < 15:
        return "breve"

    elif durata_minuti <= 45:
        return "media"

    return "lunga"




# Restituisce statistiche sulle durate delle corse


def riepilogo_corse(lista_durate: list) -> dict:

    if len(lista_durate) == 0:
        return {}

    totale = len(lista_durate)

    media = sum(lista_durate) / totale

    massimo = max(lista_durate)

    minimo = min(lista_durate)

    brevi = 0
    medie = 0
    lunghe = 0


    for durata in lista_durate:

        categoria = classifica_corsa(durata)

        if categoria == "breve":
            brevi += 1

        elif categoria == "media":
            medie += 1

        else:
            lunghe += 1

    return {"totale": totale,"media": round(media, 2),"max": massimo,"min": minimo,"brevi": brevi,"medie": medie,"lunghe": lunghe}




# Questo file contiene alcune funzioni di utilità
# utilizzate per gestire e analizzare le corse del sistema VeloCittà.

# Le funzioni permettono di:
# - calcolare la durata di una corsa
# - classificare una corsa in breve, media o lunga
# - ottenere statistiche riassuntive sulle durate

# È stato utilizzato ValueError
# per controllare eventuali valori non validi negli orari.