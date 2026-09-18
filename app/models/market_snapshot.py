from dataclasses import dataclass, field
from typing import Dict, List, Optional


@dataclass
class StrikeData:
    strike: float

    ce_ltp: Optional[float] = None
    pe_ltp: Optional[float] = None

    ce_oi: Optional[int] = None
    pe_oi: Optional[int] = None

    ce_change_oi: Optional[int] = None
    pe_change_oi: Optional[int] = None

    ce_iv: Optional[float] = None
    pe_iv: Optional[float] = None


@dataclass
class MarketSnapshot:

    index_name: str

    spot_price: float

    expiry: str

    timestamp: str

    pcr: Optional[float] = None

    max_pain: Optional[float] = None

    atm_strike: Optional[float] = None

    support: List[float] = field(default_factory=list)

    resistance: List[float] = field(default_factory=list)

    strikes: List[StrikeData] = field(default_factory=list)