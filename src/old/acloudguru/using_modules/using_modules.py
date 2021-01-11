import math
from strhelpers import reverse, str_shuffle as shuffle

name = 'Robin Smorenburg'

assert math.ceil(14.11) == 15
assert (
    reverse(name) == 'grubneromS niboR'
)
assert type(shuffle(name)) == str
assert sorted(shuffle(name)) == sorted(name)
