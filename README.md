#Parser

Tento Python skript s využitím knižnice **BeautifulSoup** a **requests** je určený na extrahovanie informácií o letákoch z webovej stránky [Prospektmaschine](https://www.prospektmaschine.de/hypermarkte/). 
Skript zbiera informácie o letákoch, ako sú názov letáku, náhľad obrázka, názov obchodu, platnosť od a platnosť do, a tieto údaje ukladá do formátu **JSON**.

## Požiadavky

- Python 3.x
- Nainštalované knižnice:
  - `requests`
  - `beautifulsoup4`

## Použitie

Skript sa pripojí na webovú stránku [https://www.prospektmaschine.de/hypermarkte/](https://www.prospektmaschine.de/hypermarkte/), extrahuje informácie o letákoch a uloží tieto údaje do súboru **`output.json`** v rovnakom adresári.

### Výstup

Výstupný súbor **output.json** bude vyzerať takto:

```json
[
    {
        "title": "Onlineshop",
        "thumbnail": "https://eu.leafletscdns.com/thumbor/I3OdlemOLLFpnPA86KXTkUBxciU=/full-fit-in/240x240/filters:format(webp):quality(65)/de/data/6/319422/0.jpg?t=1740668594",
        "shop_name": "Norma",
        "valid_from": "10.02.2025",
        "valid_to": " 16.03.2025",
        "parsed_time": "2025-03-16 16:33:27"
    },
    {
        "title": "Hessen",
        "thumbnail": "https://eu.leafletscdns.com/thumbor/uCfnLHugTFuVAkSkcFyG6aTYTTM=/full-fit-in/240x240/filters:format(webp):quality(65)/de/data/1/324612/0.jpg?t=1740898647",
        "shop_name": "Lidl",
        "valid_from": "17.03.2025",
        "valid_to": " 22.03.2025",
        "parsed_time": "2025-03-16 16:33:27"
    },
]
```

Každý záznam v JSON obsahuje:

- **title**: Názov letáku.
- **thumbnail**: URL obrázku náhľadu letáku.
- **shop_name**: Názov obchodu (napr. Kaufland, Edeka).
- **valid_from**: Dátum začiatku platnosti letáku.
- **valid_to**: Dátum konca platnosti letáku.
- **parsed_time**: Čas, kedy bol leták spracovaný.
