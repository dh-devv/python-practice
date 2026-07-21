print(0.1 + 0.2)
print(0.1 + 0.2 == 0.3)  # False

import math

print(math.isclose(0.1 + 0.2, 0.3))  # True

from decimal import Decimal

print(float(Decimal('0.1') + Decimal('0.2'))) # 0.3

