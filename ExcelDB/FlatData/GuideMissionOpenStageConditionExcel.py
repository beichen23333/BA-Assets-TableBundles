
import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class GuideMissionOpenStageConditionExcel:
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = GuideMissionOpenStageConditionExcel()
        x.Init(buf, n + offset)
        return x

    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)


    def SeasonId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def OrderNumber(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def TabLocalizeCode(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def ClearScenarioModeId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def LockScenarioTextLocailzeCode(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def ShortcutScenarioUI(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def ClearStageId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def LockStageTextLocailzeCode(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def ShortcutStageUI(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None




    @staticmethod
    def Start(builder): builder.StartObject(9)
    @staticmethod
    def End(builder): return builder.EndObject()


    @staticmethod
    def AddSeasonId(builder, SeasonId): builder.PrependInt64Slot(0, SeasonId, 0)


    @staticmethod
    def AddOrderNumber(builder, OrderNumber): builder.PrependInt64Slot(1, OrderNumber, 0)


    @staticmethod
    def AddTabLocalizeCode(builder, TabLocalizeCode): builder.PrependUOffsetTRelativeSlot(2, flatbuffers.number_types.UOffsetTFlags.py_type(TabLocalizeCode), 0)

    @staticmethod
    def AddClearScenarioModeId(builder, ClearScenarioModeId): builder.PrependInt64Slot(3, ClearScenarioModeId, 0)


    @staticmethod
    def AddLockScenarioTextLocailzeCode(builder, LockScenarioTextLocailzeCode): builder.PrependUOffsetTRelativeSlot(4, flatbuffers.number_types.UOffsetTFlags.py_type(LockScenarioTextLocailzeCode), 0)

    @staticmethod
    def AddShortcutScenarioUI(builder, ShortcutScenarioUI): builder.PrependUOffsetTRelativeSlot(5, flatbuffers.number_types.UOffsetTFlags.py_type(ShortcutScenarioUI), 0)

    @staticmethod
    def AddClearStageId(builder, ClearStageId): builder.PrependInt64Slot(6, ClearStageId, 0)


    @staticmethod
    def AddLockStageTextLocailzeCode(builder, LockStageTextLocailzeCode): builder.PrependUOffsetTRelativeSlot(7, flatbuffers.number_types.UOffsetTFlags.py_type(LockStageTextLocailzeCode), 0)

    @staticmethod
    def AddShortcutStageUI(builder, ShortcutStageUI): builder.PrependUOffsetTRelativeSlot(8, flatbuffers.number_types.UOffsetTFlags.py_type(ShortcutStageUI), 0)
