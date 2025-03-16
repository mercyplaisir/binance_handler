class SymbolNotFound(Exception):
    ...

class OrderNotSent(Exception):
    ...

class TimestampOutofWindow(Exception):
    ...


class BinanceApiError(Exception):
    ...

class MarginInsufficient(Exception):
    ...
class QuantityLessOrEqualToZero(Exception):
    ...
class NotionalTooSmall(Exception):
    ...
errors = {
    -2019 : MarginInsufficient,
    -1021: TimestampOutofWindow,
    -4003: QuantityLessOrEqualToZero,
    -4164: NotionalTooSmall,
}
def get_error(code):
    if errors.get(code):
        return errors[code]
    return BinanceApiError
