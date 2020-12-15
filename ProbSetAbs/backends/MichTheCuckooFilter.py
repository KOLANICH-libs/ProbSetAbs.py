from ..core import BackendSource, BackendType, IBackend


class MichTheCuckooFilterBackend(IBackend):
	__slots__ = ()

	SOURCE = BackendSource.MichThe
	TYPE = BackendType.cuckoo

	def __init__(self, iters: int, errorRate: float) -> None:
		import cuckoofilter

		super().__init__(cuckoofilter.CuckooFilter(capacity=iters, fingerprint_size=10, bucket_size=2))

	def _load(self, bitMap: bytes) -> None:
		raise NotImplementedError
		self.f

	def add(self, data: bytes) -> None:
		self.f.insert(data)  # hashes itself

	def check(self, data: bytes) -> bool:
		return self.f.contains(data)  # hashes itself

	def _serialize(self) -> bytes:
		raise NotImplementedError
		for b in self.f.buckets:
			b.size
			b.b
