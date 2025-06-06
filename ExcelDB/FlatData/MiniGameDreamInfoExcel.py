
import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class MiniGameDreamInfoExcel:
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = MiniGameDreamInfoExcel()
        x.Init(buf, n + offset)
        return x

    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)


    def EventContentId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def DreamMakerMultiplierCondition(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def DreamMakerMultiplierConditionValue(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def DreamMakerMultiplierMax(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def DreamMakerDays(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def DreamMakerActionPoint(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def DreamMakerParcelType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def DreamMakerParcelId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def DreamMakerDailyPointParcelType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def DreamMakerDailyPointId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def DreamMakerParameterTransfer(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def ScheduleCostGoodsId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def LobbyBGMChangeScenarioId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(28))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0




    @staticmethod
    def Start(builder): builder.StartObject(13)
    @staticmethod
    def End(builder): return builder.EndObject()


    @staticmethod
    def AddEventContentId(builder, EventContentId): builder.PrependInt64Slot(0, EventContentId, 0)


    @staticmethod
    def AddDreamMakerMultiplierCondition(builder, DreamMakerMultiplierCondition): builder.PrependInt32Slot(1, DreamMakerMultiplierCondition, 0)


    @staticmethod
    def AddDreamMakerMultiplierConditionValue(builder, DreamMakerMultiplierConditionValue): builder.PrependInt64Slot(2, DreamMakerMultiplierConditionValue, 0)


    @staticmethod
    def AddDreamMakerMultiplierMax(builder, DreamMakerMultiplierMax): builder.PrependInt64Slot(3, DreamMakerMultiplierMax, 0)


    @staticmethod
    def AddDreamMakerDays(builder, DreamMakerDays): builder.PrependInt64Slot(4, DreamMakerDays, 0)


    @staticmethod
    def AddDreamMakerActionPoint(builder, DreamMakerActionPoint): builder.PrependInt64Slot(5, DreamMakerActionPoint, 0)


    @staticmethod
    def AddDreamMakerParcelType(builder, DreamMakerParcelType): builder.PrependInt32Slot(6, DreamMakerParcelType, 0)


    @staticmethod
    def AddDreamMakerParcelId(builder, DreamMakerParcelId): builder.PrependInt64Slot(7, DreamMakerParcelId, 0)


    @staticmethod
    def AddDreamMakerDailyPointParcelType(builder, DreamMakerDailyPointParcelType): builder.PrependInt32Slot(8, DreamMakerDailyPointParcelType, 0)


    @staticmethod
    def AddDreamMakerDailyPointId(builder, DreamMakerDailyPointId): builder.PrependInt64Slot(9, DreamMakerDailyPointId, 0)


    @staticmethod
    def AddDreamMakerParameterTransfer(builder, DreamMakerParameterTransfer): builder.PrependInt64Slot(10, DreamMakerParameterTransfer, 0)


    @staticmethod
    def AddScheduleCostGoodsId(builder, ScheduleCostGoodsId): builder.PrependInt64Slot(11, ScheduleCostGoodsId, 0)


    @staticmethod
    def AddLobbyBGMChangeScenarioId(builder, LobbyBGMChangeScenarioId): builder.PrependInt64Slot(12, LobbyBGMChangeScenarioId, 0)

