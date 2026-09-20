from dataclasses import dataclass
import os
from dotenv import load_dotenv

load_dotenv()

@dataclass(frozen=True)
class Settings:
    city_name: str = os.getenv("CITY_NAME", "Eschwege, Hesse, Germany")
    walking_speed_kph: float = float(os.getenv("WALKING_SPEED_KPH", "5.0"))
    accessibility_max_origins: int = int(os.getenv("ACCESSIBILITY_MAX_ORIGINS", "750"))
    wikidata_enabled: bool = os.getenv("WIKIDATA_ENABLED", "true").lower() == "true"
    wikidata_max_entities: int = int(os.getenv("WIKIDATA_MAX_ENTITIES", "100"))
    wikidata_user_agent: str = os.getenv("WIKIDATA_USER_AGENT", "SmartCityKnowledgeGraph/3.0")

settings = Settings()
