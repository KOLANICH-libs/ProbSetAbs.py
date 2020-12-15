import typing

from ..core import BackendSource, BackendType, IBackend


class HuyDhnCuckooFilterBackend(IBackend):
	__slots__ = ()

	SOURCE = BackendSource.HuyDhn
	TYPE = BackendType.cuckoo

	def __init__(self, iters: typing.Optional[int], errorRate: float) -> None:
		from cuckoo.filter import BCuckooFilter, ScalableCuckooFilter

		if iters is not None:
			super().__init__(BCuckooFilter(capacity=iters, error_rate=errorRate))
		else:
			super().__init__(ScalableCuckooFilter(error_rate=errorRate))

	def _load(self, bitMap: bytes) -> None:
		self.f.buckets = self.f.buckets.__class__()
		self.f.buckets.frombytes(bitMap)

	def add(self, data: bytes) -> None:
		self.f.insert(data)  # hashes itself

	def check(self, data: bytes) -> bool:
		return self.f.contains(data)  # hashes itself

	def _serialize(self) -> bytes:
		return self.f.buckets.tobytes()
