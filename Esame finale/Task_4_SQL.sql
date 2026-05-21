-- Task 4 — SQL Teorico
-- VeloCittà Analytics


-- D1 — Tutte le corse a Milano ordinate per data decrescente

SELECT c.id_corsa,
       c.id_bici,
       c.data_corsa,
       c.durata_minuti
FROM corse c
JOIN stazioni s ON c.stazione_partenza = s.nome
WHERE s.citta = 'Milano'
ORDER BY c.data_corsa DESC;

-- Spiegazione:
-- Mostra tutte le corse partite da stazioni di Milano
-- ordinate dalla più recente alla più vecchia.



-- D2 — Numero di biciclette elettriche per città

SELECT citta,
       COUNT(*) AS numero_bici_elettriche
FROM biciclette
WHERE tipo = 'elettrica'
GROUP BY citta
ORDER BY numero_bici_elettriche DESC;

-- Spiegazione:
-- Conta il numero di biciclette elettriche
-- presenti in ogni città
-- ordinando i risultati in modo decrescente.



-- D3 — Durata media, massima e minima per tipo di bicicletta

SELECT b.tipo,
       AVG(c.durata_minuti) AS durata_media,
       MAX(c.durata_minuti) AS durata_massima,
       MIN(c.durata_minuti) AS durata_minima
FROM corse c
JOIN biciclette b ON c.id_bici = b.id_bici
GROUP BY b.tipo;

-- Spiegazione:
-- Calcola media, massimo e minimo
-- della durata delle corse
-- per ogni tipologia di bicicletta.



-- D4 — Stazioni di Milano con più di 50 arrivi in aprile 2026

SELECT s.nome,
       COUNT(c.id_corsa) AS numero_arrivi
FROM stazioni s
INNER JOIN corse c ON s.nome = c.stazione_arrivo
WHERE s.citta = 'Milano'
  AND c.data_corsa BETWEEN '2026-04-01' AND '2026-04-30'
GROUP BY s.nome
HAVING COUNT(c.id_corsa) > 50
ORDER BY numero_arrivi DESC;

-- Spiegazione:
-- Mostra le stazioni della città di Milano
-- che hanno ricevuto più di 50 arrivi
-- durante il mese di aprile 2026.



-- D5 — Utenti Premium con almeno 10 corse

SELECT u.id_utente,
       u.nome,
       COUNT(c.id_corsa) AS numero_corse,
       SUM(c.km_percorsi) AS km_totali
FROM utenti u
JOIN corse c ON u.id_utente = c.id_utente
WHERE u.tipo_abbonamento = 'Premium'
GROUP BY u.id_utente, u.nome
HAVING COUNT(c.id_corsa) >= 10
ORDER BY km_totali DESC;

-- Spiegazione:
-- Seleziona gli utenti Premium
-- con almeno 10 corse effettuate
-- mostrando numero totale di corse
-- e chilometri percorsi complessivi.



-- D6 — Analisi flusso stazioni

SELECT s.nome AS stazione,
       s.citta,
       COUNT(c_in.id_corsa) AS arrivi,
       COUNT(c_out.id_corsa) AS partenze,
       COUNT(c_in.id_corsa) - COUNT(c_out.id_corsa) AS bilancio
FROM stazioni s
LEFT JOIN corse c_in ON s.nome = c_in.stazione_arrivo
LEFT JOIN corse c_out ON s.nome = c_out.stazione_partenza
GROUP BY s.nome, s.citta
ORDER BY bilancio DESC;

-- Spiegazione:
-- La query analizza il flusso delle biciclette
-- nelle diverse stazioni calcolando:
-- numero di arrivi, partenze e bilancio finale.

-- Il bilancio permette di individuare
-- le stazioni che accumulano biciclette
-- e quelle che invece tendono a svuotarsi,
-- informazione utile per la redistribuzione della flotta.