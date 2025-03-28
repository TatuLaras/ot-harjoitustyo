
<!-- Laajennetaan nyt luokkakaaviota tuomalla esiin seuraavat asiat: -->
<!---->
<!-- Ruutuja on useampaa eri tyyppiä: -->
<!---->
<!-- Aloitusruutu -->
<!-- Vankila -->
<!-- Sattuma ja yhteismaa -->
<!-- Asemat ja laitokset -->
<!-- Normaalit kadut (joihin liittyy nimi) -->
<!-- Monopolipelin täytyy tuntea sekä aloitusruudun että vankilan sijainti. -->
<!---->
<!-- Jokaiseen ruutuun liittyy jokin toiminto. -->
<!---->
<!-- Sattuma- ja yhteismaaruutuihin liittyy kortteja, joihin kuhunkin liittyy joku toiminto. -->
<!---->
<!-- Toimintoja on useanlaisia. Ei ole vielä tarvetta tarkentaa toiminnon laatua. -->
<!---->
<!-- Normaaleille kaduille voi rakentaa korkeintaan 4 taloa tai yhden hotellin. Kadun voi omistaa joku pelaajista. Pelaajilla on rahaa. -->
<!---->

```mermaid
 classDiagram
    Monopolipeli "1" -- "2" Noppa
    Monopolipeli "1" -- "1" Pelilauta
    Monopolipeli "1" -- "1" Aloitusruutu
    Monopolipeli "1" -- "1" Vankila

    Ruutu "1" -- "1" Ruutu : seuraava
    Ruutu "1" -- "0..8" Pelinappula


    Ruutu <|-- Aloitusruutu
    Ruutu <|-- Vankila
    Ruutu <|-- Sattuma
    Ruutu <|-- Yhteismaa
    Ruutu <|-- Asema
    Ruutu <|-- Laitos
    Ruutu <|-- Katu

    Sattuma "1" -- "1" SattumaKorttipakka
    Yhteismaa "1" -- "1" YhteismaaKorttipakka
    SattumaKorttipakka "1" -- "*" Toiminto
    YhteismaaKorttipakka "1" -- "*" Toiminto
    Korttipakka <|-- SattumaKorttipakka
    Korttipakka <|-- YhteismaaKorttipakka

    Katu "1" -- "0..5" Talo

    Pelilauta "1" -- "40" Ruutu
    Pelinappula "1" -- "1" Pelaaja
    Pelaaja "2..8" -- "1" Monopolipeli

    Pelaaja "1" -- "1" Raha

```
