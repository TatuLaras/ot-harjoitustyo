# A program for managing sheet music and guitar tabulature
Using this program, a user can keep track of their collection of PDF sheet music and tabulature.

## Dependencies
- `qt6`
- `xdg-open`

The program will open sheets in the default program for pdf files defined for xdg-open.

## Installation
Install dependencies using:
```
$ poetry install
```

Run the program using:
```
$ poetry run invoke start
```

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

