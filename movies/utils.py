from django.core.exceptions import ValidationError


def min_value_validator(value):
    if value < 0:
        raise ValidationError(
            "Rank qiymati 1 va unda katta bo'lishi kerak",
            params={"value": value}
        )
    
def max_value_validator(value):
    if value > 5:
        raise ValidationError(
            "Rank qiymati 5 va unda kichik bo'lishi kerak",
            params={"value": value}
        )
    
def truncate(text: str):
    if len(text) < 15:
        return text
    return text[:15] + "..."
