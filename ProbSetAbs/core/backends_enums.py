from enum import IntEnum


class BackendSource(IntEnum):
	unknown = 0
	pyprobables = 1
	Bloom2 = 2
	HuyDhn = 3
	MichThe = 4
	pyxorfilter = 5
