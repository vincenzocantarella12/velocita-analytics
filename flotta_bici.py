from bicicletta import Bicicletta


# Classe che rappresenta una flotta di biciclette


class FlottaBici:

    def __init__(self, citta: str):

        self.citta = citta

        self.biciclette = []


    def aggiungi(self, bici: Bicicletta) -> None:

        self.biciclette.append(bici)


    def rimuovi(self, id_bici: str) -> None:

        for bici in self.biciclette:

            if bici.id_bici == id_bici:
                self.biciclette.remove(bici)
                return

        raise KeyError("Bicicletta non trovata.")


    def cerca_per_id(self, id_bici: str) -> Bicicletta:

        for bici in self.biciclette:

            if bici.id_bici == id_bici:
                return bici

        raise KeyError("Bicicletta non trovata.")


    def disponibili(self) -> list:

        return [bici for bici in self.biciclette if bici.disponibile]


    def statistiche(self) -> dict:

        totale = len(self.biciclette)
        disponibili = len(self.disponibili())
        in_uso = totale - disponibili
        km_totali = sum(bici.km_percorsi for bici in self.biciclette)
        km_medi = km_totali / totale if totale > 0 else 0

        return {"totale": totale, "disponibili": disponibili, "in_uso": in_uso, "km_totali_flotta": round(km_totali, 2), "km_medi_per_bici": round(km_medi, 2)}


    def __len__(self):

        return len(self.biciclette)


    @classmethod
    def da_lista(cls, citta: str, dati: list):

        flotta = cls(citta)

        for elemento in dati:

            bici = Bicicletta(elemento["id"], elemento["tipo"], elemento["stazione"], elemento["km"])

            flotta.aggiungi(bici)

        return flotta
    
    
    

# Questo file gestisce la flotta di biciclette del sistema.
# La classe FlottaBici contiene metodi per aggiungere,
# cercare, rimuovere e analizzare le biciclette disponibili.

# È stato utilizzato KeyError quando una bicicletta
# non viene trovata tramite il suo identificatore.

# Il metodo @classmethod da_lista()
# permette di creare rapidamente una flotta
# partendo da una lista di dizionari.

# Il metodo speciale __len__()
# consente di usare len() direttamente sugli oggetti FlottaBici.