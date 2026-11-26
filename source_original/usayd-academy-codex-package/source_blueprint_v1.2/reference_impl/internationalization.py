"""Reference contract algorithms for spec tests only, not shipping Laravel code."""
from datetime import datetime, timezone
from decimal import Decimal
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError

CURRENCY_DIGITS={'EGP':2,'SAR':2,'AED':2,'QAR':2,'OMR':2,'USD':2,'EUR':2,'GBP':2,'KWD':3,'BHD':3}

def to_minor(value, currency):
    code=currency.upper()
    if code not in CURRENCY_DIGITS:raise ValueError('unsupported currency fixture')
    v=Decimal(str(value));digits=CURRENCY_DIGITS[code]
    scaled=v*(Decimal(10)**digits)
    if v<0 or scaled!=scaled.to_integral_value():raise ValueError('invalid sub-minor precision or negative amount')
    return int(scaled)

def choose_market(explicit=None,stored=None,coarse_ip=None):
    # Billing country deliberately NOT included: it must be independently verified.
    return explicit or stored or coarse_ip or None

def resolve_local_wall_time(local_naive, timezone_id):
    """Return 0 nonexistent, 1 unique or 2 ambiguous UTC instants for a local wall time."""
    if local_naive.tzinfo is not None:raise ValueError('expected naive local datetime')
    tz=ZoneInfo(timezone_id)
    instants=[]
    for fold in (0,1):
        candidate=local_naive.replace(tzinfo=tz,fold=fold).astimezone(timezone.utc)
        check=candidate.astimezone(tz)
        if check.replace(tzinfo=None)==local_naive and candidate not in instants:
            instants.append(candidate)
    return sorted(instants)
