import enum


class PaymentStatus(str, enum.Enum):
    """Stored as string values in the database (VARCHAR)."""

    pending = "pending"
    paid = "paid"
    failed = "failed"
