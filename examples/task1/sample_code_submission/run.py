"""Baseline: returns the attribute prior for every image, ignoring the pixels.

Replace the body of load_model() and predict_image() with your model. The
ingestion program calls:

    load_model()                 once, load your weights here
    predict_image(sample)        once per image

Define predict_batch(samples) instead of predict_image to run batched.
"""
from __future__ import annotations

import json
import os
from typing import Any

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


def predict_image(sample: dict[str, Any]) -> list[float]:
    if not _PRIOR:
        load_model()
    # One probability per attribute, in the order of sample["attribute_names"].
    # An attribute counts as present above 0.5.
    return [_PRIOR.get(name, 0.0) for name in sample["attribute_names"]]
