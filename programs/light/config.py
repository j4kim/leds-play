import os


def _float_env(name, default):
    try:
        return float(os.getenv(name, default))
    except (TypeError, ValueError):
        return float(default)


LATITUDE = _float_env("LIGHT_LATITUDE", "46.2043907")
LONGITUDE = _float_env("LIGHT_LONGITUDE", "6.1431577")

# API de lever/coucher de soleil. Par défaut on utilise l'API publique sunrise-sunset.org.
# Si vous souhaitez utiliser Sunsethue, changez simplement cette URL via la variable d'environnement.
SUN_API_URL = os.getenv("LIGHT_SUN_API_URL", "https://api.sunrise-sunset.org/json")

# Pour tester rapidement le comportement jour/nuit sans appeler une API.
FORCE_DAY = os.getenv("LIGHT_FORCE_DAY", "0").strip().lower() in ("1", "true", "yes")
FORCE_NIGHT = os.getenv("LIGHT_FORCE_NIGHT", "0").strip().lower() in ("1", "true", "yes")
