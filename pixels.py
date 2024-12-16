import importlib
import config

driver = importlib.import_module(f"drivers.{config.driver}.pixels")
pixels = driver.Pixels()
