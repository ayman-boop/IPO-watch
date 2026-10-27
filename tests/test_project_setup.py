"""Smoke tests: package imports and config files load and are well-formed."""

import importlib
import pkgutil

import ipo_watch
from ipo_watch.config import get_settings, load_yaml


def test_all_modules_import():
    for mod in pkgutil.walk_packages(ipo_watch.__path__, "ipo_watch."):
        importlib.import_module(mod.name)


def test_settings_defaults():
    assert get_settings().database_url.startswith("sqlite")


def test_schedule_config():
    schedule = load_yaml("schedule")
    assert schedule["edgar_rss"]["market_hours"] <= 15


def test_topics_config_shape():
    topics = load_yaml("topics")
    assert "LEADERSHIP" in topics and "CEO_TENURE" in topics["LEADERSHIP"]
    for category, subtopics in topics.items():
        for name, spec in subtopics.items():
            assert spec["direction"] in {"+", "-", "±"}, f"{category}.{name}"


def test_sections_reference_existing_extractors():
    sections = load_yaml("sections")
    for key, spec in sections.items():
        importlib.import_module(f"ipo_watch.edgar.extractors.{spec['extractor']}")
