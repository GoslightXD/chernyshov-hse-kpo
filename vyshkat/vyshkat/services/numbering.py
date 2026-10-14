class InventoryNumberGenerator:
    def __init__(self, prefix: str = "VK"):
        self._prefix = prefix
        self._counter = 0

    def next(self) -> str:
        self._counter += 1
        return f"{self._prefix}-{self._counter:04d}"