
import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class MiniGameDreamReplayScenarioExcel:
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = MiniGameDreamReplayScenarioExcel()
        x.Init(buf, n + offset)
        return x

    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)


    def EventContentId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def ScenarioGroupId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def Order(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def ReplaySummaryTitleLocalize(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0


    def ReplaySummaryLocalizeScenarioId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0


    def ReplayScenarioResource(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def IsReplayScenarioHorizon(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0




    @staticmethod
    def Start(builder): builder.StartObject(7)
    @staticmethod
    def End(builder): return builder.EndObject()


    @staticmethod
    def AddEventContentId(builder, EventContentId): builder.PrependInt64Slot(0, EventContentId, 0)


    @staticmethod
    def AddScenarioGroupId(builder, ScenarioGroupId): builder.PrependInt64Slot(1, ScenarioGroupId, 0)


    @staticmethod
    def AddOrder(builder, Order): builder.PrependInt64Slot(2, Order, 0)


    @staticmethod
    def AddReplaySummaryTitleLocalize(builder, ReplaySummaryTitleLocalize): builder.PrependUint32Slot(3, ReplaySummaryTitleLocalize, 0)


    @staticmethod
    def AddReplaySummaryLocalizeScenarioId(builder, ReplaySummaryLocalizeScenarioId): builder.PrependUint32Slot(4, ReplaySummaryLocalizeScenarioId, 0)


    @staticmethod
    def AddReplayScenarioResource(builder, ReplayScenarioResource): builder.PrependUOffsetTRelativeSlot(5, flatbuffers.number_types.UOffsetTFlags.py_type(ReplayScenarioResource), 0)

    @staticmethod
    def AddIsReplayScenarioHorizon(builder, IsReplayScenarioHorizon): builder.PrependBoolSlot(6, IsReplayScenarioHorizon, 0)

