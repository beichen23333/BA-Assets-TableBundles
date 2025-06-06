
import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class ConquestEventExcel:
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = ConquestEventExcel()
        x.Init(buf, n + offset)
        return x

    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)


    def EventContentId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def MainStoryEventContentId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def ConquestEventType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def UseErosion(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0


    def UseUnexpectedEvent(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0


    def UseCalculate(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0


    def UseConquestObject(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0


    def EvnetMapGoalLocalize(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def EvnetMapNameLocalize(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def MapEnterScenarioGroupId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def EvnetScenarioBG(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def ManageUnitChange(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def AssistCount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(28))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def PlayTimeLimitInSeconds(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(30))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def AnimationUnitAmountMin(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(32))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def AnimationUnitAmountMax(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(34))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def AnimationUnitDelay(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(36))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0


    def LocalizeUnexpected(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(38))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def LocalizeErosions(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(40))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def LocalizeStep(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(42))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def LocalizeTile(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(44))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def LocalizeMapInfo(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(46))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def LocalizeManage(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(48))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def LocalizeUpgrade(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(50))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def LocalizeTreasureBox(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(52))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def IndividualErosionDailyCount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(54))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0




    @staticmethod
    def Start(builder): builder.StartObject(26)
    @staticmethod
    def End(builder): return builder.EndObject()


    @staticmethod
    def AddEventContentId(builder, EventContentId): builder.PrependInt64Slot(0, EventContentId, 0)


    @staticmethod
    def AddMainStoryEventContentId(builder, MainStoryEventContentId): builder.PrependInt64Slot(1, MainStoryEventContentId, 0)


    @staticmethod
    def AddConquestEventType(builder, ConquestEventType): builder.PrependInt32Slot(2, ConquestEventType, 0)


    @staticmethod
    def AddUseErosion(builder, UseErosion): builder.PrependBoolSlot(3, UseErosion, 0)


    @staticmethod
    def AddUseUnexpectedEvent(builder, UseUnexpectedEvent): builder.PrependBoolSlot(4, UseUnexpectedEvent, 0)


    @staticmethod
    def AddUseCalculate(builder, UseCalculate): builder.PrependBoolSlot(5, UseCalculate, 0)


    @staticmethod
    def AddUseConquestObject(builder, UseConquestObject): builder.PrependBoolSlot(6, UseConquestObject, 0)


    @staticmethod
    def AddEvnetMapGoalLocalize(builder, EvnetMapGoalLocalize): builder.PrependUOffsetTRelativeSlot(7, flatbuffers.number_types.UOffsetTFlags.py_type(EvnetMapGoalLocalize), 0)

    @staticmethod
    def AddEvnetMapNameLocalize(builder, EvnetMapNameLocalize): builder.PrependUOffsetTRelativeSlot(8, flatbuffers.number_types.UOffsetTFlags.py_type(EvnetMapNameLocalize), 0)

    @staticmethod
    def AddMapEnterScenarioGroupId(builder, MapEnterScenarioGroupId): builder.PrependInt64Slot(9, MapEnterScenarioGroupId, 0)


    @staticmethod
    def AddEvnetScenarioBG(builder, EvnetScenarioBG): builder.PrependUOffsetTRelativeSlot(10, flatbuffers.number_types.UOffsetTFlags.py_type(EvnetScenarioBG), 0)

    @staticmethod
    def AddManageUnitChange(builder, ManageUnitChange): builder.PrependInt32Slot(11, ManageUnitChange, 0)


    @staticmethod
    def AddAssistCount(builder, AssistCount): builder.PrependInt32Slot(12, AssistCount, 0)


    @staticmethod
    def AddPlayTimeLimitInSeconds(builder, PlayTimeLimitInSeconds): builder.PrependInt32Slot(13, PlayTimeLimitInSeconds, 0)


    @staticmethod
    def AddAnimationUnitAmountMin(builder, AnimationUnitAmountMin): builder.PrependInt32Slot(14, AnimationUnitAmountMin, 0)


    @staticmethod
    def AddAnimationUnitAmountMax(builder, AnimationUnitAmountMax): builder.PrependInt32Slot(15, AnimationUnitAmountMax, 0)


    @staticmethod
    def AddAnimationUnitDelay(builder, AnimationUnitDelay): builder.PrependFloat32Slot(16, AnimationUnitDelay, 0)


    @staticmethod
    def AddLocalizeUnexpected(builder, LocalizeUnexpected): builder.PrependUOffsetTRelativeSlot(17, flatbuffers.number_types.UOffsetTFlags.py_type(LocalizeUnexpected), 0)

    @staticmethod
    def AddLocalizeErosions(builder, LocalizeErosions): builder.PrependUOffsetTRelativeSlot(18, flatbuffers.number_types.UOffsetTFlags.py_type(LocalizeErosions), 0)

    @staticmethod
    def AddLocalizeStep(builder, LocalizeStep): builder.PrependUOffsetTRelativeSlot(19, flatbuffers.number_types.UOffsetTFlags.py_type(LocalizeStep), 0)

    @staticmethod
    def AddLocalizeTile(builder, LocalizeTile): builder.PrependUOffsetTRelativeSlot(20, flatbuffers.number_types.UOffsetTFlags.py_type(LocalizeTile), 0)

    @staticmethod
    def AddLocalizeMapInfo(builder, LocalizeMapInfo): builder.PrependUOffsetTRelativeSlot(21, flatbuffers.number_types.UOffsetTFlags.py_type(LocalizeMapInfo), 0)

    @staticmethod
    def AddLocalizeManage(builder, LocalizeManage): builder.PrependUOffsetTRelativeSlot(22, flatbuffers.number_types.UOffsetTFlags.py_type(LocalizeManage), 0)

    @staticmethod
    def AddLocalizeUpgrade(builder, LocalizeUpgrade): builder.PrependUOffsetTRelativeSlot(23, flatbuffers.number_types.UOffsetTFlags.py_type(LocalizeUpgrade), 0)

    @staticmethod
    def AddLocalizeTreasureBox(builder, LocalizeTreasureBox): builder.PrependUOffsetTRelativeSlot(24, flatbuffers.number_types.UOffsetTFlags.py_type(LocalizeTreasureBox), 0)

    @staticmethod
    def AddIndividualErosionDailyCount(builder, IndividualErosionDailyCount): builder.PrependInt64Slot(25, IndividualErosionDailyCount, 0)

