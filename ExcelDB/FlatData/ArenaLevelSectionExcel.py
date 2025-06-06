
import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class ArenaLevelSectionExcel:
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = ArenaLevelSectionExcel()
        x.Init(buf, n + offset)
        return x

    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)


    def ArenaSeasonId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def StartLevel(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def LastLevel(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def UserCount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0




    @staticmethod
    def Start(builder): builder.StartObject(4)
    @staticmethod
    def End(builder): return builder.EndObject()


    @staticmethod
    def AddArenaSeasonId(builder, ArenaSeasonId): builder.PrependInt64Slot(0, ArenaSeasonId, 0)


    @staticmethod
    def AddStartLevel(builder, StartLevel): builder.PrependInt64Slot(1, StartLevel, 0)


    @staticmethod
    def AddLastLevel(builder, LastLevel): builder.PrependInt64Slot(2, LastLevel, 0)


    @staticmethod
    def AddUserCount(builder, UserCount): builder.PrependInt64Slot(3, UserCount, 0)

