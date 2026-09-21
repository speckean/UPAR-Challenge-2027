"""Baseline: the usual two-step recipe, with a model that ignores the pixels.

    1. predict attribute probabilities for every gallery image
    2. rank the gallery by the distance between those and each query

Replace predict_attributes() with your attribute model, or replace the whole
body of rank_gallery() if your method matches queries and images differently.
"""
from __future__ import annotations

import json
import os
from typing import Any

import numpy as np

ASSET_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                          "assets", "attribute_prior.json")

_PRIOR: dict[str, float] = {}


def load_model() -> None:
    global _PRIOR
    # A real submission loads its weights here, e.g.
    # torch.load(os.path.join(HERE, "assets", "model.pth"))
    with open(ASSET_PATH, "r", encoding="utf-8") as fh:
        prior = json.load(fh)
    _PRIOR = dict(zip(prior["attribute_names"], prior["positive_rate"]))


def predict_attributes(gallery: list[dict[str, Any]], attribute_names: list[str]) -> np.ndarray:
    """(gallery images x attributes) probabilities. Open g["image_path"] here."""
    row = [_PRIOR.get(name, 0.0) for name in attribute_names]
    return np.tile(np.asarray(row, dtype=np.float32), (len(gallery), 1))


def rank_gallery(sample: dict[str, Any]) -> dict[str, Any]:
    if not _PRIOR:
        load_model()
    probs = predict_attributes(sample["gallery"], sample["attribute_names"])
    queries = np.asarray(sample["queries"], dtype=np.float32)

    # L1 distance between a binary query q and probabilities p, without building
    # the (queries x gallery x attributes) tensor:  sum|q - p| = sum(p) + q . (1 - 2p)
    distances = probs.sum(1)[None, :] + queries @ (1.0 - 2.0 * probs).T

    # (queries x gallery). Smaller = better match. Ties keep the gallery order.
    return {"distances": distances}
