# Copyright (c) OpenMMLab. All rights reserved.
from abc import ABC, abstractmethod
from dataclasses import dataclass
from enum import Enum, auto


class EmbeddingType(Enum):
    """rotary embedding type."""
    Default = auto()
    LinearScaling = auto()
    DynamicNTKScaling = auto()
    Llama3 = auto()
    Yarn = auto()


@dataclass
class YarnParameters:
    """Yarn parameters."""
    beta_fast: int = 32
    beta_slow: float = 1
    mscale: int = 1
    mscale_all_dim: int = 0


class RotaryEmbeddingImpl(ABC):
    """rotary embedding implementation api."""

    @abstractmethod
    def forward(self, x, position_ids):
        """forward."""
        raise NotImplementedError


class RotaryEmbeddingBuilder(ABC):
    """rotary embedding implementation builder."""

    @staticmethod
    @abstractmethod
    def build(
        dim: int,
        max_position_embeddings: int = 2048,
        base: int = 10000,
        scaling_factor: float = 1.0,
        low_freq_factor: float = 1.0,
        high_freq_factor: float = 4.0,
        emb_type: EmbeddingType = EmbeddingType.Default,
    ):
        """build."""
        raise NotImplementedError
