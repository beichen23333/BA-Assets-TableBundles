
import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class MiniGameDreamDailyPointExcel:
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = MiniGameDreamDailyPointExcel()
        x.Init(buf, n + offset)
        return x

    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)


    def UniqueId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def EventContentId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def TotalParameterMin(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def TotalParameterMax(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def DailyPointCoefficient(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def DailyPointCorrectionValue(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0




    @staticmethod
    def Start(builder): builder.StartObject(6)
    @staticmethod
    def End(builder): return builder.EndObject()


    @staticmethod
    def AddUniqueId(builder, UniqueId): builder.PrependInt64Slot(0, UniqueId, 0)


    @staticmethod
    def AddEventContentId(builder, EventContentId): builder.PrependInt64Slot(1, EventContentId, 0)


    @staticmethod
    def AddTotalParameterMin(builder, TotalParameterMin): builder.PrependInt64Slot(2, TotalParameterMin, 0)


    @staticmethod
    def AddTotalParameterMax(builder, TotalParameterMax): builder.PrependInt64Slot(3, TotalParameterMax, 0)


    @staticmethod
    def AddDailyPointCoefficient(builder, DailyPointCoefficient): builder.PrependInt64Slot(4, DailyPointCoefficient, 0)


    @staticmethod
    def AddDailyPointCorrectionValue(builder, DailyPointCorrectionValue): builder.PrependInt64Slot(5, DailyPointCorrectionValue, 0)

