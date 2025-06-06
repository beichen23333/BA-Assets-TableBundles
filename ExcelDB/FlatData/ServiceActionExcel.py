
import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class ServiceActionExcel:
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = ServiceActionExcel()
        x.Init(buf, n + offset)
        return x

    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)


    def ServiceActionType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def IsLegacy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0


    def GoodsId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0




    @staticmethod
    def Start(builder): builder.StartObject(3)
    @staticmethod
    def End(builder): return builder.EndObject()


    @staticmethod
    def AddServiceActionType(builder, ServiceActionType): builder.PrependInt32Slot(0, ServiceActionType, 0)


    @staticmethod
    def AddIsLegacy(builder, IsLegacy): builder.PrependBoolSlot(1, IsLegacy, 0)


    @staticmethod
    def AddGoodsId(builder, GoodsId): builder.PrependInt64Slot(2, GoodsId, 0)

