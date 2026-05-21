from funzioni_base import calcola_durata_minuti, riepilogo_corse
from bicicletta import BiciclettaClassica, BiciclettaElettrica, BiciclettaSportiva, stampa_flotta
from flotta_bici import FlottaBici


# CREAZIONE FLOTTA

flotta = FlottaBici("Milano")


# BICICLETTE INIZIALI
# Sono state inserite alcune biciclette già presenti nella flotta
# per simulare un sistema reale già avviato.

bici1 = BiciclettaClassica("MI-001", "Duomo", 120.5, "M")
bici2 = BiciclettaElettrica("MI-002", "Cadorna", 340.0, 78)
bici3 = BiciclettaSportiva("MI-003", "Navigli", 98.7, 18)

flotta.aggiungi(bici1)
flotta.aggiungi(bici2)
flotta.aggiungi(bici3)


# MENU INTERATTIVO

while True:

    print("\n--- Menu VeloCittà ---\n")
    print(" ")
    print("1. Aggiungi bicicletta")
    print("2. Mostra biciclette")
    print("3. Cerca bicicletta")
    print("4. Noleggia bicicletta")
    print("5. Restituisci bicicletta")
    print("6. Statistiche flotta")
    print("7. Elimina bicicletta")
    print("8. Ordina biciclette per km")
    print("9. Test funzioni base")
    print("0. Esci")

    scelta = input("\nInserisci una scelta: ")


# AGGIUNTA BICICLETTA

    if scelta == "1":

        print("\nTIPI DISPONIBILI\n")
        print(" ")
        print("- Classica")
        print("- Elettrica")
        print("- Sportiva")

        tipo = input("\nScegli il tipo di bicicletta: ").strip().lower()

        numero_id = input("Numero ID bicicletta: ")
        id_bici = f"MI-{numero_id.zfill(3)}"


# CONTROLLO ID DUPLICATO

        bici_esistente = False

        for bici in flotta.biciclette:

            if bici.id_bici == id_bici:

                bici_esistente = True
                break

        if bici_esistente:

            print("\nEsiste già una bicicletta con questo ID.")
            continue

        stazione = input("Stazione corrente: ")

        try:

            km = float(input("Km percorsi: "))

        except ValueError:

            print("\nInserisci un numero valido.")
            continue

        try:

            if tipo == "classica":

                taglia = input("Taglia (S/M/L): ").upper()
                bici = BiciclettaClassica(id_bici, stazione, km, taglia)

            elif tipo == "elettrica":

                batteria = int(input("Percentuale batteria: "))
                bici = BiciclettaElettrica(id_bici, stazione, km, batteria)

            elif tipo == "sportiva":

                marce = int(input("Numero marce: "))
                bici = BiciclettaSportiva(id_bici, stazione, km, marce)

            else:

                print("\nTipo non valido.")
                continue

            flotta.aggiungi(bici)

            print(f"\nBicicletta {id_bici} aggiunta correttamente.")

        except ValueError as errore:

            print(errore)


# MOSTRA BICICLETTE

    elif scelta == "2":

        print("\n--- ELENCO BICICLETTE ---\n")

        stampa_flotta(flotta.biciclette)


# CERCA BICICLETTA

    elif scelta == "3":

        numero_id = input("Inserisci numero ID bicicletta: ")
        id_bici = f"MI-{numero_id.zfill(3)}"

        try:

            bici = flotta.cerca_per_id(id_bici)

            print("\n--- DETTAGLI BICICLETTA ---\n")

            dettagli = bici.dettagli()

            for chiave, valore in dettagli.items():

                print(f"{chiave}: {valore}")

        except KeyError as errore:

            print(errore)


# NOLEGGIA BICICLETTA

    elif scelta == "4":

        numero_id = input("Inserisci numero ID bicicletta: ")
        id_bici = f"MI-{numero_id.zfill(3)}"

        utente = input("Nome utente: ")

        try:

            bici = flotta.cerca_per_id(id_bici)

            print(bici.noleggia(utente))

        except (KeyError, ValueError) as errore:

            print(errore)


# RESTITUISCI BICICLETTA

    elif scelta == "5":

        numero_id = input("Inserisci numero ID bicicletta: ")
        id_bici = f"MI-{numero_id.zfill(3)}"

        stazione = input("Nuova stazione: ")

        try:

            km = float(input("Km percorsi: "))

        except ValueError:

            print("\nInserisci un numero valido.")
            continue

        try:

            bici = flotta.cerca_per_id(id_bici)

            bici.restituisci(stazione, km)

            print("\nBicicletta restituita correttamente.")

        except (KeyError, ValueError) as errore:

            print(errore)


# STATISTICHE FLOTTA

    elif scelta == "6":

        stats = flotta.statistiche()

        print("\n--- STATISTICHE FLOTTA ---\n")

        print(f"Totale biciclette: {stats['totale']}")
        print(f"Biciclette disponibili: {stats['disponibili']}")
        print(f"Biciclette in uso: {stats['in_uso']}")
        print(f"Km totali flotta: {stats['km_totali_flotta']:.1f}")
        print(f"Km medi per bici: {stats['km_medi_per_bici']:.1f}")


# ELIMINA BICICLETTA

    elif scelta == "7":

        numero_id = input("Inserisci numero ID bicicletta: ")
        id_bici = f"MI-{numero_id.zfill(3)}"

        try:

            flotta.rimuovi(id_bici)

            print("\nBicicletta eliminata correttamente.")

        except KeyError as errore:

            print(errore)


# ORDINA BICICLETTE

    elif scelta == "8":

        bici_ordinate = sorted(flotta.biciclette, key=lambda bici: bici.km_percorsi)

        print("\n--- BICICLETTE ORDINATE PER KM ---\n")

        for bici in bici_ordinate:

            print(bici)


# TEST FUNZIONI BASE

    elif scelta == "9":

        durata1 = calcola_durata_minuti("08:30", "09:10")
        durata2 = calcola_durata_minuti("14:00", "14:20")
        durata3 = calcola_durata_minuti("18:15", "19:30")

        lista_durate = [durata1, durata2, durata3]

        print("\nRIEPILOGO CORSE\n")

        print(riepilogo_corse(lista_durate))


# USCITA PROGRAMMA

    elif scelta == "0":

        conferma = input("\nSei sicuro di voler uscire? (s/n): ").lower()

        if conferma == "s":

            print("\nChiusura programma...")
            break


# SCELTA NON VALIDA

    else:

        print("\nScelta non valida.")



# Questo file rappresenta il punto di avvio del progetto VeloCittà.
# Tramite un menu interattivo è possibile utilizzare
# le principali funzionalità del sistema di bike sharing.

# Il programma permette di:
# - aggiungere biciclette
# - visualizzare la flotta
# - cercare biciclette tramite ID
# - gestire noleggi e restituzioni
# - eliminare biciclette
# - ordinare biciclette per chilometri
# - consultare statistiche della flotta

# Sono state utilizzate classi OOP con:
# - ereditarietà
# - incapsulamento
# - polimorfismo

# La funzione stampa_flotta() mostra il polimorfismo
# applicando la stessa operazione a oggetti di classi differenti
# senza controlli espliciti sul tipo.