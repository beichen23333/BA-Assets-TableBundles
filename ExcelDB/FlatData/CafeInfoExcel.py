
import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class CafeInfoExcel:
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = CafeInfoExcel()
        x.Init(buf, n + offset)
        return x

    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)


    def CafeId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def IsDefault(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0


    def OpenConditionCafeId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def OpenConditionCafeInvite(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0




    @staticmethod
    def Start(builder): builder.StartObject(4)
    @staticmethod
    def End(builder): return builder.EndObject()


    @staticmethod
    def AddCafeId(builder, CafeId): builder.PrependInt64Slot(0, CafeId, 0)


    @staticmethod
    def AddIsDefault(builder, IsDefault): builder.PrependBoolSlot(1, IsDefault, 0)


    @staticmethod
    def AddOpenConditionCafeId(builder, OpenConditionCafeId): builder.PrependInt32Slot(2, OpenConditionCafeId, 0)


    @staticmethod
    def AddOpenConditionCafeInvite(builder, OpenConditionCafeInvite): builder.PrependInt32Slot(3, OpenConditionCafeInvite, 0)

