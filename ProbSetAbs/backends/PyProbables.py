from ..core import BackendSource, BackendType, IBackend


class PyProbablesBackend(IBackend):
	__slots__ = ()

	SOURCE = BackendSource.pyprobables

	def _load(self, bitMap: bytes) -> None:
		self.f._load(bitMap)

	def add(self, data: bytes) -> None:
		self.f.add(data)  # hashes itself

	def check(self, data: bytes) -> bool:
		return data in self.f  # hashes itself

	def _serialize(self) -> bytes:
		return bytes(self.f)


class PyProbablesBloomBackend(PyProbablesBackend):
	__slots__ = ()

	TYPE = BackendType.Bloom

	def __init__(self, iters: int, errorRate: float) -> None:
		from probables.blooms.bloom import BloomFilter

		super().__init__(BloomFilter(est_elements=iters, false_positive_rate=errorRate))


class PyProbablesCuckooBackend(PyProbablesBackend):
	__slots__ = ("errorRate",)

	TYPE = BackendType.cuckoo

	def __init__(self, iters: int, errorRate: float) -> None:
		from probables.cuckoo.cuckoo import CuckooFilter

		super().__init__(CuckooFilter.init_error_rate(errorRate, capacity=iters))
		self.errorRate = errorRate

	def _load(self, bitMap: bytes) -> None:
		super()._load(bitMap)
		self.f._set_error_rate(self.errorRate)
