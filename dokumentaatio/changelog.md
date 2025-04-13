# Changelog
## Viikko 3
- Projektirunko tehty.
- Käyttäjä voi lisätä ja poistaa kansioita joista nuotteja haetaan.
- Ohjelma hakee kaikki pdf-tiedostot kyseisistä kansioista ja indeksoi ne tietokantaan.
- Käyttäjä voi nähdä listan nuoteista.
- Lisätty muutama triviaaleja SQL-kyselyjä generoiva funktio.
- Testattu SQL-kyselyjä generoivat funktiot.
- Lisätty `BaseRepository`-luokka, joka tarjoaa repositorioille yhteiset perustoiminnallisuudet, kuten triviaalien SQL-kyselyiden ajo edellämainittuja generaattoreita käyttäen.
- Lisätty `BaseEntity`-luokka, joka sisältää `to_dict` -metodin, jolla entiteetit voidaan muuntaa python-sanakirjoiksi sopimattomat kentät huomiotta jättäen.
- Lisätty `SettingsRepository` -luokka, jolla voidaan hallinnoida asetuksia tietokannassa. Tällä hetkellä luokka vastaa indeksoitavista kansioista.
- Lisätty `Sheet` (entity) ja `SheetRepository` -luokat, joiden avulla nuotteja voidaan hallinnoida tietokannassa.
- Lisätty `SheetService` -luokka, johon voi eriyttää sovelluksen nuottien hallinnointiin liittyvää logiikkaa.

## Viikko 4
- Luotu käyttöliittymä nuottien tietojen tarkasteluun ja muokkaukseen
- Käyttäjä voi avata nuotin PDF-lukijallaan
- Lisätty `SearchParameter`-luokka jonka avulla voi luoda suodattimia ja muuntaa niitä SQL-muotoiseksi WHERE-lausekkeeksi
- Suurimpaan osaan ei-käyttöliittymän logiikasta automaattitestit

## Viikko 5
- Toteutettu hakuehtojen luominen ja hakujen teko
- Yleistetty kansioiden hallintakomponentti käytettäväksi minkä tahansa merkkijonolistan kanssa
- Käyttäjä voi lisätä soittimia asetuksista ja muuttaa nuotin soitinta
- Suurin osa uudesta logiikasta automaattitestauksen alle
- Poistettu testi joka testasi sitä että <, > yms. operaattoreita ei sallita käytettäväksi merkkijonojen kanssa, sillä päätin että käyttäjällä on lupa käyttää niitä ehtojen kuten "tulee merkkijonon 'xyx' jälkeen aakkosjärjestyksessä" tekoon.

