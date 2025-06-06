
import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class ConstEventCommonExcel:
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = ConstEventCommonExcel()
        x.Init(buf, n + offset)
        return x

    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)


    def EventContentHardStageCount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def EventStrategyPlayTimeLimitInSeconds(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def SubEventChangeLimitSeconds(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def SubEventInstantClear(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0


    def CardShopProbWeightCount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def CardShopProbWeightRarity(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def MeetupScenarioReplayResource(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def MeetupScenarioReplayTitleLocalize(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def SpecialOperactionCollectionGroupId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def TreasureNormalVariationAmount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def TreasureLoopVariationAmount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def TreasureLimitVariationLoopCount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def TreasureLimitVariationClearLoopCount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(28))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def EventStoryReplayHideEventContentId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(30))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0




    @staticmethod
    def Start(builder): builder.StartObject(14)
    @staticmethod
    def End(builder): return builder.EndObject()


    @staticmethod
    def AddEventContentHardStageCount(builder, EventContentHardStageCount): builder.PrependInt32Slot(0, EventContentHardStageCount, 0)


    @staticmethod
    def AddEventStrategyPlayTimeLimitInSeconds(builder, EventStrategyPlayTimeLimitInSeconds): builder.PrependInt64Slot(1, EventStrategyPlayTimeLimitInSeconds, 0)


    @staticmethod
    def AddSubEventChangeLimitSeconds(builder, SubEventChangeLimitSeconds): builder.PrependInt64Slot(2, SubEventChangeLimitSeconds, 0)


    @staticmethod
    def AddSubEventInstantClear(builder, SubEventInstantClear): builder.PrependBoolSlot(3, SubEventInstantClear, 0)


    @staticmethod
    def AddCardShopProbWeightCount(builder, CardShopProbWeightCount): builder.PrependInt64Slot(4, CardShopProbWeightCount, 0)


    @staticmethod
    def AddCardShopProbWeightRarity(builder, CardShopProbWeightRarity): builder.PrependInt32Slot(5, CardShopProbWeightRarity, 0)


    @staticmethod
    def AddMeetupScenarioReplayResource(builder, MeetupScenarioReplayResource): builder.PrependUOffsetTRelativeSlot(6, flatbuffers.number_types.UOffsetTFlags.py_type(MeetupScenarioReplayResource), 0)

    @staticmethod
    def AddMeetupScenarioReplayTitleLocalize(builder, MeetupScenarioReplayTitleLocalize): builder.PrependUOffsetTRelativeSlot(7, flatbuffers.number_types.UOffsetTFlags.py_type(MeetupScenarioReplayTitleLocalize), 0)

    @staticmethod
    def AddSpecialOperactionCollectionGroupId(builder, SpecialOperactionCollectionGroupId): builder.PrependInt64Slot(8, SpecialOperactionCollectionGroupId, 0)


    @staticmethod
    def AddTreasureNormalVariationAmount(builder, TreasureNormalVariationAmount): builder.PrependInt32Slot(9, TreasureNormalVariationAmount, 0)


    @staticmethod
    def AddTreasureLoopVariationAmount(builder, TreasureLoopVariationAmount): builder.PrependInt32Slot(10, TreasureLoopVariationAmount, 0)


    @staticmethod
    def AddTreasureLimitVariationLoopCount(builder, TreasureLimitVariationLoopCount): builder.PrependInt32Slot(11, TreasureLimitVariationLoopCount, 0)


    @staticmethod
    def AddTreasureLimitVariationClearLoopCount(builder, TreasureLimitVariationClearLoopCount): builder.PrependInt32Slot(12, TreasureLimitVariationClearLoopCount, 0)


    @staticmethod
    def AddEventStoryReplayHideEventContentId(builder, EventStoryReplayHideEventContentId): builder.PrependInt32Slot(13, EventStoryReplayHideEventContentId, 0)

