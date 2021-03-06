import re

from django.core.exceptions import ValidationError


def validate_nip(nip: str):
    nip_regex = re.compile("^[0-9]{10}$")
    if nip_regex.match(nip) is None:
        raise ValidationError('Invalid NIP number')

    weights = [6, 5, 7, 2, 3, 4, 5, 6, 7]
    checksum = 0
    for i in range(len(nip)-1):
        checksum += weights[i] * int(nip[i])
    checksum %= 11
    if checksum != int(nip[9]):
        raise ValidationError('Invalid NIP number')
