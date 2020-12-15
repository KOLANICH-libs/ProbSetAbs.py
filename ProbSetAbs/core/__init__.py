import typing
from abc import ABCMeta, abstractmethod
from collections.abc import ByteString, Set
from enum import IntEnum

from .backends_enums import BackendSource


class BackendType(IntEnum):
	unknown = 0
	Bloom = 1
	cuckoo = 2
	xor = 2


_backendsRegistry = {el: {} for el in BackendType if el}


class IBackendMeta(ABCMeta):
	__slots__ = ()

	def __new__(cls: typing.Type["IBackend"], className: str, parents: typing.Tuple[typing.Type, ...], attrs: typing.Dict[str, typing.Any]) -> "IBackend":  # pylint:disable=arguments-differ
		res = super().__new__(cls, className, parents, attrs)

		source = attrs.get("SOURCE", None)
		tp = attrs.get("TYPE", None)

		if parents:
			if source is None:
				source = getattr(parents[0], "SOURCE", None)

			if tp is None:
				tp = getattr(parents[0], "TYPE", None)

		if source is not None and tp is not None:
			_backendsRegistry[tp][source] = res

		return res

	@property
	def slug(cls) -> str:
		return ":".join(el.name for el in cls.typeHeaderTuple)

	@property
	def typeHeaderTuple(cls) -> typing.Tuple[BackendType, BackendSource]:
		return (cls.TYPE, cls.SOURCE)

	@property
	def prettyName(cls) -> str:
		return cls.__name__ + " (" + cls.slug + ")"

	@property
	def typeHeader(cls) -> ByteString:
		res = bytes(cls.typeHeaderTuple)
		assert len(res) == cls.typeHeaderLength
		return res

	@property
	def typeHeaderLength(cls) -> int:
		return 2


def getBackend(tp: BackendType, source: BackendSource) -> IBackendMeta:
	return _backendsRegistry[tp][source]


def getAllBackends() -> typing.Iterator[IBackendMeta]:
	for t in _backendsRegistry.values():
		for b in t.values():
			yield b


def getBackendsByType(tp: BackendType) -> typing.Iterable[IBackendMeta]:
	return _backendsRegistry[tp].values()


class IBackend(metaclass=IBackendMeta):
	__slots__ = ("f",)

	SOURCE = BackendSource.unknown  # type: BackendSource
	TYPE = None  # type: BackendType

	def __init__(self, f: typing.Any) -> None:
		self.f = f

	def __contains__(self, data: ByteString) -> bool:
		return self.check(data)

	@classmethod
	def parseTypeHeaderTuple(cls, bitMap: ByteString) -> typing.Tuple[BackendType, BackendSource]:
		return (BackendType(bitMap[0]), BackendSource(bitMap[1]))

	def load(self, bitMap: ByteString) -> None:
		realTypeHeader = self.__class__.parseTypeHeaderTuple(bitMap[: self.__class__.typeHeaderLength])

		if self.__class__.typeHeaderTuple != realTypeHeader:
			raise ValueError("The blob is from another backend (needed from " + repr(self.__class__.typeHeaderTuple) + ")", realTypeHeader)

		self._load(bitMap[self.__class__.typeHeaderLength :])

	@abstractmethod
	def _load(self, bitMap: ByteString) -> None:
		raise NotImplementedError

	@abstractmethod
	def add(self, data: ByteString) -> None:
		raise NotImplementedError

	@abstractmethod
	def check(self, data: ByteString) -> bool:
		raise NotImplementedError

	@abstractmethod
	def _serialize(self) -> ByteString:
		raise NotImplementedError

	def __bytes__(self) -> ByteString:
		return self.__class__.typeHeader + self._serialize()


def getBackendByData(data: ByteString) -> IBackendMeta:
	return getBackend(*IBackend.parseTypeHeaderTuple(data))


def parseBackendSlug(slug: str) -> typing.Tuple[BackendType, BackendSource]:
	slug = slug.split(":")
	if len(slug) != IBackend.typeHeaderLength:
		raise ValueError("Invalid backend slug. It must contain 2 components.")

	tp, src = slug

	try:
		tp = BackendType(int(tp))
	except ValueError:
		tp = BackendType[tp]

	try:
		src = BackendSource(int(tp))
	except ValueError:
		src = BackendSource[tp]

	return (tp, src)


def getBackendBySlug(slug: str) -> IBackendMeta:
	return getBackend(*parseBackendSlug(slug))
