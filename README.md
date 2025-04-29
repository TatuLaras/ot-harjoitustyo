# A program for managing sheet music and guitar tabulature
Using this program, a user can keep track of their collection of PDF sheet music and tabulature.

## Dependencies
- `qt6`
- `xdg-open`

The program will open sheets in the default program for pdf files defined for xdg-open.
Only Linux is officially supported.

## Installation
Install dependencies using:
```
$ poetry install
```

Run the program using:
```
$ poetry run invoke start
```

## Usage
To use the program to manage your sheet music, you need to provide it with a directory to look for them.
To do this, go to Edit > Preferences > Sheet music folders and press the Add folder -button.
This will open your operating system's file picker to choose your directory.
Sheet music directories can be deleted by highlighting the directory by clicking on it and then clicking the Delete folder -button.

Once the sheet music directory / directories have been set, a scan can be performed by clicking the Refresh -button on the top toolbar.
A list of music sheets will appear in the central list view widget, each corresponding to a PDF-file in the sheet music directories.

### Edit properties
To add metadata to a sheet music, click on the sheet music item in the sheet music list view in the center of the screen to open it for editing in the right-hand-side Sheet properties panel.
In there you can edit the information and save either by clicking the Save -button or by clicking another item in the sheet music list view.

### Instruments
In the Sheet properties, you can set an instrument for a piece though a drop-down menu. 
All possible instruments are managed in Edit > Preferences > Instruments.
You can manage these in the same way as sheet music directories.

### Advanced search
You can perform searches across your music sheets using the Search parameters -panel above the sheet music list view.
There, a condition can be added by using the Add -button present.
After this, a "condition line" will appear, where you can edit which column is checked, in which way and against which value.

Multiple condition lines can be added. A sheet must fulfill all the conditions to be shown.

Conditions can be removed using the Delete -button to the right of the condition line.

#### Comparison types
| Type | Field must [x] |
|-|-|
| EQUIVALENT | be EQUIVALENT to the query |
| GREATER | be of GREATER numeric value or come later in alphabetic ordering than the query |
| GREATER_EQUAL | be of GREATER or equal numeric value or come later in alphabetic ordering than the query |
| LESS | be of LESSer numeric value or come earlier in alphabetic ordering than the query |
| LESS_EQUAL | be of LESSer or equal numeric value or come earlier in alphabetic ordering than the query |
| LESS_EQUAL | be of LESSer or equal numeric value or come earlier in alphabetic ordering than the query |
| CONTAINS | CONTAIN the query |



## Command-line tasks
The unit tests can be run with:
```
$ poetry run invoke test
```

An HTML coverage report can be generated (and opened on Linux) with:
```
$ poetry run invoke coverage-report
```

A plain coverage report can be generated using:
```
$ poetry run invoke coverage
```


## Documentation (Finnish)
- [Vaatimusmäärittely](dokumentaatio/vaatimusmaarittely.md)
- [Työaikakirjanpito](dokumentaatio/tyoaikakirjanpito.md)
- [Changelog](dokumentaatio/changelog.md)
- [Arkkitehtuuri](dokumentaatio/arkkitehtuuri.md)

