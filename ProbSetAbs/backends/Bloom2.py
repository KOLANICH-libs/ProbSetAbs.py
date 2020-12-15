from ..core import BackendSource, BackendType, IBackend


class Bloom2Backend(IBackend):
	__slots__ = ()

	SOURCE = BackendSource.Bloom2
	TYPE = BackendType.Bloom

	def __init__(self, iters: int, errorRate: float) -> None:
		import bloom_filter2

		super().__init__(bloom_filter2.BloomFilter(start_fresh=True, max_elements=iters, error_rate=errorRate))

	def _load(self, bitMap: bytes) -> None:
		self.f.backend.array_ = self.f.backend.array_.__class__(self.f.backend.array_.typecode, bitMap)

	def add(self, data: bytes) -> None:
		self.f.add(data)  # hashes itself

	def check(self, data: bytes) -> bool:
		return data in self.f  # hashes itself

	def _serialize(self) -> bytes:
		return bytes(self.f.backend.array_)
