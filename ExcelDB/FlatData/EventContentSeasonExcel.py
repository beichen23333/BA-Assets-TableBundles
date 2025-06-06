
import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class EventContentSeasonExcel:
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = EventContentSeasonExcel()
        x.Init(buf, n + offset)
        return x

    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)


    def EventContentId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def OriginalEventContentId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def IsReturn(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0


    def Name(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def EventContentType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def OpenConditionContent(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def EventDisplay(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0


    def IconOrder(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def SubEventType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def SubEvent(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0


    def EventItemId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def MainEventId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def EventChangeOpenCondition(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(28))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def BeforehandExposedTime(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(30))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def EventContentOpenTime(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(32))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def EventContentCloseTime(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(34))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def ExtensionTime(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(36))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def MainIconParcelPath(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(38))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def SubIconParcelPath(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(40))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def BeforehandBgImagePath(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(42))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def MinigamePrologScenarioGroupId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(44))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def BeforehandScenarioGroupId(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(46))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int64Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 8))
        return 0

    def BeforehandScenarioGroupIdAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(46))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int64Flags, o)
        return 0

    def BeforehandScenarioGroupIdLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(46))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    def BeforehandScenarioGroupIdIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(46))
        return o == 0


    def MainBannerImagePath(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(48))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def MainBgImagePath(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(50))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def ShiftTriggerStageId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(52))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def ShiftMainBgImagePath(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(54))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def MinigameLobbyPrefabName(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(56))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def MinigameVictoryPrefabName(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(58))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def MinigameMissionBgPrefabName(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(60))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def MinigameMissionBgImagePath(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(62))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def CardBgImagePath(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(64))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def EventAssist(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(66))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0


    def EventContentReleaseType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(68))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def EventContentStageRewardIdPermanent(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(70))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def RewardTagPermanent(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(72))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def MiniEventShortCutScenarioModeId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(74))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def ScenarioContentCollectionGroupId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(76))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0




    @staticmethod
    def Start(builder): builder.StartObject(37)
    @staticmethod
    def End(builder): return builder.EndObject()


    @staticmethod
    def AddEventContentId(builder, EventContentId): builder.PrependInt64Slot(0, EventContentId, 0)


    @staticmethod
    def AddOriginalEventContentId(builder, OriginalEventContentId): builder.PrependInt64Slot(1, OriginalEventContentId, 0)


    @staticmethod
    def AddIsReturn(builder, IsReturn): builder.PrependBoolSlot(2, IsReturn, 0)


    @staticmethod
    def AddName(builder, Name): builder.PrependUOffsetTRelativeSlot(3, flatbuffers.number_types.UOffsetTFlags.py_type(Name), 0)

    @staticmethod
    def AddEventContentType(builder, EventContentType): builder.PrependInt32Slot(4, EventContentType, 0)


    @staticmethod
    def AddOpenConditionContent(builder, OpenConditionContent): builder.PrependInt32Slot(5, OpenConditionContent, 0)


    @staticmethod
    def AddEventDisplay(builder, EventDisplay): builder.PrependBoolSlot(6, EventDisplay, 0)


    @staticmethod
    def AddIconOrder(builder, IconOrder): builder.PrependInt32Slot(7, IconOrder, 0)


    @staticmethod
    def AddSubEventType(builder, SubEventType): builder.PrependInt32Slot(8, SubEventType, 0)


    @staticmethod
    def AddSubEvent(builder, SubEvent): builder.PrependBoolSlot(9, SubEvent, 0)


    @staticmethod
    def AddEventItemId(builder, EventItemId): builder.PrependInt64Slot(10, EventItemId, 0)


    @staticmethod
    def AddMainEventId(builder, MainEventId): builder.PrependInt64Slot(11, MainEventId, 0)


    @staticmethod
    def AddEventChangeOpenCondition(builder, EventChangeOpenCondition): builder.PrependInt64Slot(12, EventChangeOpenCondition, 0)


    @staticmethod
    def AddBeforehandExposedTime(builder, BeforehandExposedTime): builder.PrependUOffsetTRelativeSlot(13, flatbuffers.number_types.UOffsetTFlags.py_type(BeforehandExposedTime), 0)

    @staticmethod
    def AddEventContentOpenTime(builder, EventContentOpenTime): builder.PrependUOffsetTRelativeSlot(14, flatbuffers.number_types.UOffsetTFlags.py_type(EventContentOpenTime), 0)

    @staticmethod
    def AddEventContentCloseTime(builder, EventContentCloseTime): builder.PrependUOffsetTRelativeSlot(15, flatbuffers.number_types.UOffsetTFlags.py_type(EventContentCloseTime), 0)

    @staticmethod
    def AddExtensionTime(builder, ExtensionTime): builder.PrependUOffsetTRelativeSlot(16, flatbuffers.number_types.UOffsetTFlags.py_type(ExtensionTime), 0)

    @staticmethod
    def AddMainIconParcelPath(builder, MainIconParcelPath): builder.PrependUOffsetTRelativeSlot(17, flatbuffers.number_types.UOffsetTFlags.py_type(MainIconParcelPath), 0)

    @staticmethod
    def AddSubIconParcelPath(builder, SubIconParcelPath): builder.PrependUOffsetTRelativeSlot(18, flatbuffers.number_types.UOffsetTFlags.py_type(SubIconParcelPath), 0)

    @staticmethod
    def AddBeforehandBgImagePath(builder, BeforehandBgImagePath): builder.PrependUOffsetTRelativeSlot(19, flatbuffers.number_types.UOffsetTFlags.py_type(BeforehandBgImagePath), 0)

    @staticmethod
    def AddMinigamePrologScenarioGroupId(builder, MinigamePrologScenarioGroupId): builder.PrependInt64Slot(20, MinigamePrologScenarioGroupId, 0)


    @staticmethod
    def AddBeforehandScenarioGroupId(builder, BeforehandScenarioGroupId): builder.PrependUOffsetTRelativeSlot(21, flatbuffers.number_types.UOffsetTFlags.py_type(BeforehandScenarioGroupId), 0)
    @staticmethod
    def StartBeforehandScenarioGroupIdVector(builder, numElems): return builder.StartVector(8, numElems, 8)


    @staticmethod
    def AddMainBannerImagePath(builder, MainBannerImagePath): builder.PrependUOffsetTRelativeSlot(22, flatbuffers.number_types.UOffsetTFlags.py_type(MainBannerImagePath), 0)

    @staticmethod
    def AddMainBgImagePath(builder, MainBgImagePath): builder.PrependUOffsetTRelativeSlot(23, flatbuffers.number_types.UOffsetTFlags.py_type(MainBgImagePath), 0)

    @staticmethod
    def AddShiftTriggerStageId(builder, ShiftTriggerStageId): builder.PrependInt64Slot(24, ShiftTriggerStageId, 0)


    @staticmethod
    def AddShiftMainBgImagePath(builder, ShiftMainBgImagePath): builder.PrependUOffsetTRelativeSlot(25, flatbuffers.number_types.UOffsetTFlags.py_type(ShiftMainBgImagePath), 0)

    @staticmethod
    def AddMinigameLobbyPrefabName(builder, MinigameLobbyPrefabName): builder.PrependUOffsetTRelativeSlot(26, flatbuffers.number_types.UOffsetTFlags.py_type(MinigameLobbyPrefabName), 0)

    @staticmethod
    def AddMinigameVictoryPrefabName(builder, MinigameVictoryPrefabName): builder.PrependUOffsetTRelativeSlot(27, flatbuffers.number_types.UOffsetTFlags.py_type(MinigameVictoryPrefabName), 0)

    @staticmethod
    def AddMinigameMissionBgPrefabName(builder, MinigameMissionBgPrefabName): builder.PrependUOffsetTRelativeSlot(28, flatbuffers.number_types.UOffsetTFlags.py_type(MinigameMissionBgPrefabName), 0)

    @staticmethod
    def AddMinigameMissionBgImagePath(builder, MinigameMissionBgImagePath): builder.PrependUOffsetTRelativeSlot(29, flatbuffers.number_types.UOffsetTFlags.py_type(MinigameMissionBgImagePath), 0)

    @staticmethod
    def AddCardBgImagePath(builder, CardBgImagePath): builder.PrependUOffsetTRelativeSlot(30, flatbuffers.number_types.UOffsetTFlags.py_type(CardBgImagePath), 0)

    @staticmethod
    def AddEventAssist(builder, EventAssist): builder.PrependBoolSlot(31, EventAssist, 0)


    @staticmethod
    def AddEventContentReleaseType(builder, EventContentReleaseType): builder.PrependInt32Slot(32, EventContentReleaseType, 0)


    @staticmethod
    def AddEventContentStageRewardIdPermanent(builder, EventContentStageRewardIdPermanent): builder.PrependInt64Slot(33, EventContentStageRewardIdPermanent, 0)


    @staticmethod
    def AddRewardTagPermanent(builder, RewardTagPermanent): builder.PrependInt32Slot(34, RewardTagPermanent, 0)


    @staticmethod
    def AddMiniEventShortCutScenarioModeId(builder, MiniEventShortCutScenarioModeId): builder.PrependInt64Slot(35, MiniEventShortCutScenarioModeId, 0)


    @staticmethod
    def AddScenarioContentCollectionGroupId(builder, ScenarioContentCollectionGroupId): builder.PrependInt64Slot(36, ScenarioContentCollectionGroupId, 0)

