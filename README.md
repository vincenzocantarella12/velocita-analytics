# VeloCittà Analytics

## Vincenzo Cantarella


# Descrizione del progetto

VeloCittà Analytics è un progetto sviluppato in Python che simula un sistema di bike sharing attivo nelle città di Milano, Roma e Torino.

Il progetto combina programmazione orientata agli oggetti, SQL teorico, NumPy, Pandas e visualizzazione dati per costruire un sistema completo di gestione e analisi delle biciclette e delle corse.

L’obiettivo è analizzare dati simulati relativi a utenti, biciclette e noleggi attraverso statistiche, aggregazioni e grafici.


# Installazione librerie

Aprire il terminale nella cartella del progetto ed eseguire:

pip install -r requirements.txt


# Requirements

Il file requirements.txt contiene:

numpy>=1.24
pandas>=2.0
matplotlib>=3.7
seaborn>=0.12


# Struttura del progetto

velocita-analytics/

├── funzioni_base.py
├── bicicletta.py
├── flotta_bici.py
├── main.py
├── task4_sql.sql
├── task5_numpy.py
├── task6_pandas.py
├── task7_visualizzazione.py
├── requirements.txt
├── README.md
└── output/


# Esecuzione degli script


## Task 1 — Funzioni base

funzioni_base.py

Contiene:
- calcolo durata corse
- classificazione corse
- riepilogo statistico


## File di supporto OOP

bicicletta.py

Contiene:
- classe base Bicicletta
- sottoclassi:
  - BiciclettaClassica
  - BiciclettaElettrica
  - BiciclettaSportiva
- metodi di noleggio e restituzione
- polimorfismo e override


flotta_bici.py

Contiene:
- gestione della flotta biciclette
- aggiunta biciclette
- ricerca per ID
- eliminazione biciclette
- statistiche della flotta


## Task 2 e Task 3 — OOP

main.py

Il file avvia un menu interattivo per:
- aggiungere biciclette
- noleggiare biciclette
- restituire biciclette
- cercare biciclette
- eliminare biciclette
- visualizzare statistiche della flotta


## Task 4 — SQL teorico

Aprire il file:

task4_sql.sql

Il file contiene query SQL e spiegazioni testuali relative all’analisi del sistema.


## Task 5 — Analisi NumPy

task5_numpy.py

Il file esegue:
- generazione dati numerici
- statistiche
- slicing
- normalizzazione
- correlazione
- media mobile


## Task 6 — Analisi Pandas

task6_pandas.py

Il file esegue:
- creazione DataFrame
- pulizia dati
- gestione NaN
- merge
- groupby
- pivot table
- statistiche aggregate


## Task 7 — Visualizzazione

task7_visualizzazione.py

Il file genera grafici e dashboard salvandoli automaticamente nella cartella:

output/

I grafici vengono anche mostrati automaticamente a schermo.


# Output generati

Nella cartella output vengono salvati:
- serie temporali
- histogrammi
- scatter plot
- dashboard
- boxplot
- grafici statistici aggiuntivi

Tutti i file vengono esportati in formato PNG.


# Considerazioni

Durante lo sviluppo del progetto la parte più complessa è stata organizzare correttamente le classi OOP e collegare tra loro biciclette, flotte e operazioni di noleggio.

Anche la gestione dei dati con Pandas ha richiesto attenzione, soprattutto durante la pulizia dei dataset e la sostituzione dei valori mancanti.

La parte di visualizzazione è stata utile per comprendere meglio l’andamento delle corse e il comportamento degli utenti nelle diverse città.

Un aspetto interessante dei dati simulati è che alcune città mostrano velocità medie e utilizzi differenti a seconda della fascia oraria e del tipo di bicicletta.

In futuro il progetto potrebbe essere migliorato aggiungendo:
- database reali
- file CSV esterni
- autenticazione utenti
- mappe geografiche
- dashboard interattive

Questo progetto ha permesso di applicare insieme diversi argomenti del corso in un unico sistema completo e realistico.
