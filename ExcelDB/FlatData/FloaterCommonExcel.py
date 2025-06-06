
import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class FloaterCommonExcel:
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = FloaterCommonExcel()
        x.Init(buf, n + offset)
        return x

    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)


    def Id(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def TacticEntityType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def FloaterOffsetPosX(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def FloaterOffsetPosY(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def FloaterRandomPosRangeX(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def FloaterRandomPosRangeY(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0




    @staticmethod
    def Start(builder): builder.StartObject(6)
    @staticmethod
    def End(builder): return builder.EndObject()


    @staticmethod
    def AddId(builder, Id): builder.PrependInt64Slot(0, Id, 0)


    @staticmethod
    def AddTacticEntityType(builder, TacticEntityType): builder.PrependInt32Slot(1, TacticEntityType, 0)


    @staticmethod
    def AddFloaterOffsetPosX(builder, FloaterOffsetPosX): builder.PrependInt32Slot(2, FloaterOffsetPosX, 0)


    @staticmethod
    def AddFloaterOffsetPosY(builder, FloaterOffsetPosY): builder.PrependInt32Slot(3, FloaterOffsetPosY, 0)


    @staticmethod
    def AddFloaterRandomPosRangeX(builder, FloaterRandomPosRangeX): builder.PrependInt32Slot(4, FloaterRandomPosRangeX, 0)


    @staticmethod
    def AddFloaterRandomPosRangeY(builder, FloaterRandomPosRangeY): builder.PrependInt32Slot(5, FloaterRandomPosRangeY, 0)

