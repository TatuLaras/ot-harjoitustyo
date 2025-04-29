# Arkkitehtuurikuvaus

Sovellus tallentaa tietonsa SQLite-tietokantaan, jonka skeema löytyy tiedostosta `src/schema.sql` ja heijastuu `src/entities/` -hakemiston entity-luokissa.

`src/repositories/` -hakemistosta löytyy repositorioluokkia, jotka hallinnoivat näiden olioiden noutoa tietokannasta ja tallennuksesta sinne.
Eritystapaus repositorioluokista on `BaseRepository`, jonka muiden repositorioiden on tarkoitus periä saadakseen yleisiä tietokannan käyttötapoja helpommin käyttöönsä.

`src/services/` -hakemistossa on service-luokkia joiden tarkoitus olisi huolehtia sovelluslogiikasta.
Tämän sovelluksen tapauksessa logiikkaa ei kuitenkaan ole kovinkaan paljoa, joten kyseisten luokkien rooli jää repositorioluokkien wrapperiksi.
Luokat ovat kuitenkin olemassa mikäli sovellusta laajennetaan ja logiikkaa CRUD-operaatioiden ulkopuolelta tarvitaan.

`src/user_interface/` sisältää käyttöliittymäkoodin, joka on tekemisissä muun applikaation kanssa service-luokkien kautta.
Käyttöliittymän on jaoteltu luokkiin ns. komponenteittain ja ylemmän tason komponentit voivat koostua useammasta muusta komponentista.
Asetusvalikkoa koskeva koodi on erillään `src/user_interface/preference_window/` -hakemistossa.

## Luokkakaavio

```mermaid
classDiagram
    class UI

    class SettingsService
    class SheetService

    class SettingsRepository
    class SheetRepository

    class Sheet
    class SheetDirectory

    UI..>SettingsService
    UI..>SheetService
    SettingsService..>SettingsRepository
    SheetService..>SheetRepository
    SheetService..>Sheet
    SheetRepository..>Sheet
    SettingsService..>Instrument
    SettingsRepository..>Instrument
    SettingsService..>SheetDirectory
    SettingsRepository..>SheetDirectory
    UI..>Sheet
```

## Sekvenssikaavio tapahtumasta nuotin tietojen muokkaus
```mermaid
sequenceDiagram
    SheetProperties (UI) ->>SheetService: update_sheet(sheet)
    activate SheetService
    SheetService ->>SheetRepository: update(sheet)
    deactivate SheetService
    activate SheetRepository
    SheetRepository ->>SheetRepository: trivial_insert("sheet", sheet, DuplicateHandling.UPDATE)
    SheetRepository ->>SheetRepository: trivial_insert_many("sheet", [sheet], DuplicateHandling.UPDATE)
    SheetRepository ->>sql_query_generators: sql_trivial_insert_generate("sheet", sheet, DuplicateHandling.UPDATE)
    sql_query_generators ->>SheetRepository: query
    SheetRepository ->>sqlite3.Connection: execute(query)
    SheetRepository ->>sqlite3.Connection: commit()
    deactivate SheetRepository

```
