# Geodata Pipeline Demo

Automatiserat geodataflöde byggt med Python och GitHub Actions.

## Vad det gör

- Läser in geodata från GeoPackage
- Beräknar area i hektar
- Filtrerar features baserat på minsta area (konfigurerbart)
- Sparar resultatet till ett nytt GeoPackage
- Loggar varje körning

## Teknik

- Python / GeoPandas
- Git / GitHub Actions
- GeoPackage

## Kör lokalt

```bash
pip install -r requirements.txt
python scripts/process.py
```

## Konfiguration

Redigera `config.json` för att ändra indata, utdata eller tröskelvärde.
