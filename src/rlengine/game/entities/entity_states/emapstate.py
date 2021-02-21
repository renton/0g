from .estate import EState, EStatefulMixin


class EMapState(EState):
    def __init__(self):
        EState.__init__(self)


class EMapStatefulMixin(EStatefulMixin):
    def __init__(self):
        EStatefulMixin.__init__(self)
