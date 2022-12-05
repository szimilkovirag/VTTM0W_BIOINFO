# MessengerRnaHandler dokumentáció
## Álatlános információk
A script lényege, hogy a bemenetként kapott DNS-t általakítja fehérjévé, a tanult módszerek alapján.
## Metódusok
### `__init__`:
- ez a construktor
- itt határozzuk meg a bemenetként kapott DNS értékét
### `run`:
- ez a metódus fogja hívni az összes többi metódust
- először transzkripcióval meghatározzuk az RNS-t
- majd az aminosavakat egy dictionary-be konvertájuk a `convert_json_to_dict` metódus segítségével
- az aminosavak eredetileg egy json file-ban vannak eltárolva
    - a kulcs az aminosavat tartalmazza
    - az érték pedig a azokat a bázishármasokat, amik kódolhatják az adott aminosavat
- végül meghatározzuk a fehérjét egy transzkripcióval, és ki is iratjuk a konzolra
### `transcription`:
- a paraméterként megkapott DNS szálat alakítjuk át messenger RNS-re a bázispárosodás törvénye alapján:
    - T --> A
    - A --> U
    - G --> C
    - C --> G
### `translation`:
- az mRNS-ből létrehozzun az aminosavakat
- `check_start_and_end`:
    - leellenőrizzük, hogy az aminosavlánc START codonnal kezdődik és END codonnal végződik
- `separate_start_and_metionin`:
    - a START-ot és a metonint ugyanaz a bázishármas kódolja, ebben a metódusban szétválasztjuk őket
    - ha a lánc elején van, akkor az START
    - ha a láncban van, akkor metonin