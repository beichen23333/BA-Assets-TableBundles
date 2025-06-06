
import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class OpenConditionExcel:
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = OpenConditionExcel()
        x.Init(buf, n + offset)
        return x

    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)


    def OpenConditionContentType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def LockUI(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.String(a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return ""

    def LockUILength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    def LockUIIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        return o == 0


    def ShortcutPopupPriority(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def ShortcutUIName(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.String(a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return ""

    def ShortcutUINameLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    def ShortcutUINameIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        return o == 0


    def ShortcutParam(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def Scene(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def HideWhenLocked(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0


    def AccountLevel(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def ScenarioModeId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def CampaignStageId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def MultipleConditionCheckType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def OpenDayOfWeek(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def OpenHour(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(28))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def CloseDayOfWeek(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(30))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def CloseHour(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(32))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def OpenedCafeId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(34))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def CafeIdforCafeRank(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(36))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def CafeRank(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(38))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def ContentsOpenShow(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(40))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0


    def ContentsOpenShortcutUI(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(42))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None




    @staticmethod
    def Start(builder): builder.StartObject(20)
    @staticmethod
    def End(builder): return builder.EndObject()


    @staticmethod
    def AddOpenConditionContentType(builder, OpenConditionContentType): builder.PrependInt32Slot(0, OpenConditionContentType, 0)


    @staticmethod
    def AddLockUI(builder, LockUI): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(LockUI), 0)
    @staticmethod
    def StartLockUIVector(builder, numElems): return builder.StartVector(4, numElems, 4)


    @staticmethod
    def AddShortcutPopupPriority(builder, ShortcutPopupPriority): builder.PrependInt64Slot(2, ShortcutPopupPriority, 0)


    @staticmethod
    def AddShortcutUIName(builder, ShortcutUIName): builder.PrependUOffsetTRelativeSlot(3, flatbuffers.number_types.UOffsetTFlags.py_type(ShortcutUIName), 0)
    @staticmethod
    def StartShortcutUINameVector(builder, numElems): return builder.StartVector(4, numElems, 4)


    @staticmethod
    def AddShortcutParam(builder, ShortcutParam): builder.PrependInt32Slot(4, ShortcutParam, 0)


    @staticmethod
    def AddScene(builder, Scene): builder.PrependUOffsetTRelativeSlot(5, flatbuffers.number_types.UOffsetTFlags.py_type(Scene), 0)

    @staticmethod
    def AddHideWhenLocked(builder, HideWhenLocked): builder.PrependBoolSlot(6, HideWhenLocked, 0)


    @staticmethod
    def AddAccountLevel(builder, AccountLevel): builder.PrependInt64Slot(7, AccountLevel, 0)


    @staticmethod
    def AddScenarioModeId(builder, ScenarioModeId): builder.PrependInt64Slot(8, ScenarioModeId, 0)


    @staticmethod
    def AddCampaignStageId(builder, CampaignStageId): builder.PrependInt64Slot(9, CampaignStageId, 0)


    @staticmethod
    def AddMultipleConditionCheckType(builder, MultipleConditionCheckType): builder.PrependInt32Slot(10, MultipleConditionCheckType, 0)


    @staticmethod
    def AddOpenDayOfWeek(builder, OpenDayOfWeek): builder.PrependInt32Slot(11, OpenDayOfWeek, 0)


    @staticmethod
    def AddOpenHour(builder, OpenHour): builder.PrependInt64Slot(12, OpenHour, 0)


    @staticmethod
    def AddCloseDayOfWeek(builder, CloseDayOfWeek): builder.PrependInt32Slot(13, CloseDayOfWeek, 0)


    @staticmethod
    def AddCloseHour(builder, CloseHour): builder.PrependInt64Slot(14, CloseHour, 0)


    @staticmethod
    def AddOpenedCafeId(builder, OpenedCafeId): builder.PrependInt64Slot(15, OpenedCafeId, 0)


    @staticmethod
    def AddCafeIdforCafeRank(builder, CafeIdforCafeRank): builder.PrependInt64Slot(16, CafeIdforCafeRank, 0)


    @staticmethod
    def AddCafeRank(builder, CafeRank): builder.PrependInt64Slot(17, CafeRank, 0)


    @staticmethod
    def AddContentsOpenShow(builder, ContentsOpenShow): builder.PrependBoolSlot(18, ContentsOpenShow, 0)


    @staticmethod
    def AddContentsOpenShortcutUI(builder, ContentsOpenShortcutUI): builder.PrependUOffsetTRelativeSlot(19, flatbuffers.number_types.UOffsetTFlags.py_type(ContentsOpenShortcutUI), 0)
