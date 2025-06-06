
import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class ContentEnterCostReduceExcel:
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = ContentEnterCostReduceExcel()
        x.Init(buf, n + offset)
        return x

    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)


    def EnterCostReduceGroupId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def ContentType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def StageId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def ReduceEnterCostType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def ReduceEnterCostId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def ReduceAmount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0




    @staticmethod
    def Start(builder): builder.StartObject(6)
    @staticmethod
    def End(builder): return builder.EndObject()


    @staticmethod
    def AddEnterCostReduceGroupId(builder, EnterCostReduceGroupId): builder.PrependInt64Slot(0, EnterCostReduceGroupId, 0)


    @staticmethod
    def AddContentType(builder, ContentType): builder.PrependInt32Slot(1, ContentType, 0)


    @staticmethod
    def AddStageId(builder, StageId): builder.PrependInt64Slot(2, StageId, 0)


    @staticmethod
    def AddReduceEnterCostType(builder, ReduceEnterCostType): builder.PrependInt32Slot(3, ReduceEnterCostType, 0)


    @staticmethod
    def AddReduceEnterCostId(builder, ReduceEnterCostId): builder.PrependInt64Slot(4, ReduceEnterCostId, 0)


    @staticmethod
    def AddReduceAmount(builder, ReduceAmount): builder.PrependInt64Slot(5, ReduceAmount, 0)

