# Arkkitehtuurikuvaus

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
    SettingsService..>SheetDirectory
    SettingsRepository..>SheetDirectory
    UI..>Sheet
```
