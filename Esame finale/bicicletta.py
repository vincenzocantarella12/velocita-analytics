# Classe base per rappresentare una bicicletta


class Bicicletta:

    def __init__(self, id_bici: str, tipo: str, stazione_corrente: str, km_percorsi: float, disponibile: bool = True):

        self.id_bici = id_bici
        self.tipo = tipo
        self.stazione_corrente = stazione_corrente

# Incapsulamento

        self._km_percorsi = km_percorsi

        self.disponibile = disponibile


# Proprietà in sola lettura

    @property
    def km_percorsi(self):

        return self._km_percorsi



# Aggiunge chilometri alla bici


    def aggiungi_km(self, km: float) -> None:

        if km <= 0:
            raise ValueError("I chilometri devono essere maggiori di zero.")

        self._km_percorsi += km


# Mostra lo stato della bici


    def stato_bici(self):

        if self.disponibile:
            return "Disponibile"

        return "In uso"


# Restituisce informazioni sulla bicicletta


    def dettagli(self):
        return {"id": self.id_bici,"tipo": self.tipo,"stazione": self.stazione_corrente,"km": self.km_percorsi,"disponibile": self.disponibile}



# Noleggia la bicicletta


    def noleggia(self, utente: str) -> str:

        if not self.disponibile:
            raise ValueError("La bicicletta è già in uso.")

        self.disponibile = False

        return f"La bicicletta {self.id_bici} è stata noleggiata da {utente}."



# Restituisce la bici aggiornando stazione e chilometri


    def restituisci(self, stazione: str, km_aggiunta: float) -> None:

        self.stazione_corrente = stazione

        self.aggiungi_km(km_aggiunta)

        self.disponibile = True


    def __str__(self):

        stato = "Disponibile" if self.disponibile else "In uso"

        return f"[{self.id_bici}] {self.tipo} | {self.stazione_corrente} | {self.km_percorsi:.1f} km | {stato}"


    def __repr__(self):

        return self.__str__()




# Sottoclasse per biciclette classiche


class BiciclettaClassica(Bicicletta):

    def __init__(self, id_bici: str, stazione_corrente: str, km_percorsi: float, taglia: str):

        super().__init__(id_bici, "classica", stazione_corrente, km_percorsi)



# Controllo validità taglia

        if taglia not in ["S", "M", "L"]:
            raise ValueError("Taglia non valida.")

        self.taglia = taglia

    def __str__(self):

        return f"{super().__str__()} | Taglia: {self.taglia}"




# Sottoclasse per biciclette elettriche



class BiciclettaElettrica(Bicicletta):

    def __init__(self, id_bici: str, stazione_corrente: str, km_percorsi: float, batteria_percentuale: int):

        super().__init__(id_bici, "elettrica", stazione_corrente, km_percorsi)



# Controllo validità batteria


        if batteria_percentuale < 0 or batteria_percentuale > 100:
            raise ValueError("Percentuale batteria non valida.")

        self.batteria_percentuale = batteria_percentuale



# Ricarica la batteria


    def ricarica(self, percentuale: int) -> None:

        self.batteria_percentuale += percentuale

        if self.batteria_percentuale > 100:
            self.batteria_percentuale = 100



# Override del metodo noleggia


    def noleggia(self, utente: str) -> str:

        if self.batteria_percentuale < 20:
            raise ValueError("Batteria troppo scarica.")

        return super().noleggia(utente)

    def __str__(self):

        return f"{super().__str__()} | 🔋 {self.batteria_percentuale}%"




# Sottoclasse aggiuntiva


class BiciclettaSportiva(Bicicletta):

    def __init__(self, id_bici: str, stazione_corrente: str, km_percorsi: float, numero_marce: int):

        super().__init__(id_bici, "sportiva", stazione_corrente, km_percorsi)

        self.numero_marce = numero_marce

    def __str__(self):

        return f"{super().__str__()} | Marce: {self.numero_marce}"




# Dimostrazione di polimorfismo


def stampa_flotta(biciclette: list) -> None:

    for bici in biciclette:
        print(bici)




# Questo file contiene le classi principali del progetto VeloCittà.
# È stata utilizzata la programmazione orientata agli oggetti (OOP)
# tramite ereditarietà, incapsulamento e polimorfismo.

# L'incapsulamento è stato applicato usando _km_percorsi
# insieme alla @property per impedire modifiche dirette ai chilometri.

# Le sottoclassi permettono di creare diversi tipi di biciclette
# aggiungendo attributi specifici e personalizzando alcuni metodi.

# Il polimorfismo viene mostrato tramite una funzione comune
# che lavora con oggetti di classi differenti senza controllarne il tipo.

# Sono stati aggiunti controlli extra per validare:
# - taglia delle biciclette classiche
# - percentuale della batteria delle bici elettriche