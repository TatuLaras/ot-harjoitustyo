# Nuottien ja tabulatuurien hallintasovellus, vaatimusmäärittely

Kyseessä on sovellus, jolla voi hallinnoida tabulatuuri- ja nuottikokoelmaa.
Käyttäjä antaa sovellukselle kansion, jossa nuotit sijaitsevat PDF-muodossa.
Tämän jälkeen sovellus indeksoi nuotit, jonka jälkeen käyttäjä voi lisätä niihin erinäistä metatietoa (nimi, säveltäjä, tyylilaji, itse määritelty kategoria, vaikeustaso jne.) ja selata kokoelmaansa erinäisin hakutyökaluin.

## Ominaisuudet
- [x] Nuotit haetaan käyttäjän määrittelemästä kansiosta automaattisesti
- [x] Käyttäjä voi muokata nuotin tietoja (nimi, säveltäjä, tyylilaji, itse määritelty kategoria, vaikeustaso jne.)
- [x] Käyttäjä voi tehdä hakuja tietokantaan minkä tahansa kentän ja hakuehdon perusteella
- [ ] Käyttäjä voi luoda dynaamisia kokoelmia nuottihauista
- [ ] Käyttäjä voi luoda ja selata kokoelmia nuoteista
- [ ] Mahdollisuus pitää kirjaa nuottien soittokerroista, ainakin tasolla "soitettu 24.3.2025 klo 20:00"
- [x] Nuotit avataan käyttäjän itse määrittelemää PDF-lukijaa käyttäen

## Lisäominaisuudet
- Sovellus voisi pyrkiä automaattisesti täydentämään tietoja ennen käyttäjän manuaalista täsmennystä, esimerkiksi tiedoston nimeä ja sisältöä käyttäen, kenties yhdistettynä johonkin internetin asiaankuuluvaan tietokantaan.
- Sovelluksessa voisi olla Spaced Repetition System (SRS) -tyyppinen ominaisuus, jossa käyttäjä raportoi ohjelmalle soittaessaan nuotin. Ohjelma muistaa tämän ja tietyn ajan kuluttua ohjelma kehottaa käyttäjää soittamaan kyseisen sävellyksen uudestaan. Käyttäjä raportoi ohjelmalle kuinka hyvin soitto onnistui ja ohjelma sen mukaan aikatauluttaa sen jälleen uudelleen soitettavaksi joko eksponentiaalisen kaavan mukaan kauemmas tulevaisuuteen tai lähempänä kerrattavaksi.
- Sovellus voisi jonkin yksinkertaisen kaavan mukaan suositella nuotteja soitettavaksi, esimerkiksi nuotit joita ei ole vielä soitettu ja jotka ovat vaikeustasoltaan samankaltaisia tai hieman vaikeampia kuin aiemmin soitetut nuotit.
- Kenties jotain PDF-renderöintikirjastoa käyttäen sovellukseen voisi toteuttaa sisäänrakennetun näkymän nuotteihin, josta löytyy joitain soittajalle hyödyllisiä ominaisuuksia kuten automaattisen skrollauksen ajan mittaan.
