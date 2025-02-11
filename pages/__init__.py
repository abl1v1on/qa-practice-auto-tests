from dataclasses import dataclass


locator = tuple[str, str]


@dataclass(frozen=True)
class FieldIsRequiredErrorMixin:
    REQUIRED_FIELD: str = 'This field is required.'
