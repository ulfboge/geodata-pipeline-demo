from pathlib import Path
import json
import logging
import geopandas as gpd

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
OUTPUT_DIR = BASE_DIR / "output"
LOG_DIR = BASE_DIR / "logs"
CONFIG_PATH = BASE_DIR / "config.json"

OUTPUT_DIR.mkdir(exist_ok=True)
LOG_DIR.mkdir(exist_ok=True)

logging.basicConfig(
    filename=LOG_DIR / "pipeline.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def load_config():
    with open(CONFIG_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

def main():
    logging.info("Pipeline started")
    config = load_config()

    input_file = DATA_DIR / config["input_file"]
    output_file = OUTPUT_DIR / config["output_file"]
    min_area_ha = config["min_area_ha"]
    layer_name = config.get("input_layer")

    try:
        gdf = gpd.read_file(input_file, layer=layer_name)
        logging.info(f"Loaded {len(gdf)} features from {input_file}")

        if gdf.crs is None:
            raise ValueError("Input data has no CRS defined")

        gdf["area_ha"] = gdf.geometry.area / 10000
        result = gdf[gdf["area_ha"] >= min_area_ha].copy()
        result["processed"] = True

        result.to_file(output_file, driver="GPKG")
        logging.info(f"Saved {len(result)} features to {output_file}")
        print(f"Klart. {len(result)} features sparade till {output_file}")

    except Exception as e:
        logging.exception(f"Pipeline failed: {e}")
        raise

if __name__ == "__main__":
    main()
