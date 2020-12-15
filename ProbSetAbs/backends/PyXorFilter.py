from ..core import BackendSource, BackendType, IBackend


class PyXorFilterBackend(IBackend):
	__slots__ = ()

	SOURCE = BackendSource.pyxorfilter
	TYPE = BackendType.xor

	def __init__(self, iters: int, errorRate: float) -> None:
		from pyxorfilter import Xor8, Xor16

		super().__init__(Xor16(iters))

	def _load(self, bitMap: bytes) -> None:
		raise NotImplementedError

	def add(self, data: bytes) -> None:
		self.f.populate([data])

	def check(self, data: bytes) -> bool:
		return self.f[data]  # hashes itself

	def _serialize(self) -> bytes:
		raise NotImplementedError
