
import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class MultiFloorRaidStageExcel:
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = MultiFloorRaidStageExcel()
        x.Init(buf, n + offset)
        return x

    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)


    def Id(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def EchelonExtensionType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def BossGroupId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def AssistSlot(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def StageOpenCondition(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def FloorListSection(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0


    def FloorListSectionOpenCondition(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def FloorListSectionLabel(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0


    def Difficulty(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def UseBossIndex(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0


    def UseBossAIPhaseSync(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0


    def FloorListImgPath(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def FloorImgPath(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(28))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def RaidCharacterId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(30))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def BossCharacterId(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(32))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int64Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 8))
        return 0

    def BossCharacterIdAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(32))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int64Flags, o)
        return 0

    def BossCharacterIdLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(32))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    def BossCharacterIdIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(32))
        return o == 0


    def StatChangeId(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(34))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int64Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 8))
        return 0

    def StatChangeIdAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(34))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int64Flags, o)
        return 0

    def StatChangeIdLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(34))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    def StatChangeIdIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(34))
        return o == 0


    def BattleDuration(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(36))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def GroundId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(38))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def RecommendLevel(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(40))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def RewardGroupId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(42))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def BattleReadyTimelinePath(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(44))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.String(a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return ""

    def BattleReadyTimelinePathLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(44))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    def BattleReadyTimelinePathIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(44))
        return o == 0


    def BattleReadyTimelinePhaseStart(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(46))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int32Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return 0

    def BattleReadyTimelinePhaseStartAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(46))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int32Flags, o)
        return 0

    def BattleReadyTimelinePhaseStartLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(46))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    def BattleReadyTimelinePhaseStartIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(46))
        return o == 0


    def BattleReadyTimelinePhaseEnd(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(48))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int32Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return 0

    def BattleReadyTimelinePhaseEndAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(48))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int32Flags, o)
        return 0

    def BattleReadyTimelinePhaseEndLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(48))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    def BattleReadyTimelinePhaseEndIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(48))
        return o == 0


    def VictoryTimelinePath(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(50))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def ShowSkillCard(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(52))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0




    @staticmethod
    def Start(builder): builder.StartObject(25)
    @staticmethod
    def End(builder): return builder.EndObject()


    @staticmethod
    def AddId(builder, Id): builder.PrependInt64Slot(0, Id, 0)


    @staticmethod
    def AddEchelonExtensionType(builder, EchelonExtensionType): builder.PrependInt32Slot(1, EchelonExtensionType, 0)


    @staticmethod
    def AddBossGroupId(builder, BossGroupId): builder.PrependUOffsetTRelativeSlot(2, flatbuffers.number_types.UOffsetTFlags.py_type(BossGroupId), 0)

    @staticmethod
    def AddAssistSlot(builder, AssistSlot): builder.PrependInt32Slot(3, AssistSlot, 0)


    @staticmethod
    def AddStageOpenCondition(builder, StageOpenCondition): builder.PrependInt64Slot(4, StageOpenCondition, 0)


    @staticmethod
    def AddFloorListSection(builder, FloorListSection): builder.PrependBoolSlot(5, FloorListSection, 0)


    @staticmethod
    def AddFloorListSectionOpenCondition(builder, FloorListSectionOpenCondition): builder.PrependInt64Slot(6, FloorListSectionOpenCondition, 0)


    @staticmethod
    def AddFloorListSectionLabel(builder, FloorListSectionLabel): builder.PrependUint32Slot(7, FloorListSectionLabel, 0)


    @staticmethod
    def AddDifficulty(builder, Difficulty): builder.PrependInt32Slot(8, Difficulty, 0)


    @staticmethod
    def AddUseBossIndex(builder, UseBossIndex): builder.PrependBoolSlot(9, UseBossIndex, 0)


    @staticmethod
    def AddUseBossAIPhaseSync(builder, UseBossAIPhaseSync): builder.PrependBoolSlot(10, UseBossAIPhaseSync, 0)


    @staticmethod
    def AddFloorListImgPath(builder, FloorListImgPath): builder.PrependUOffsetTRelativeSlot(11, flatbuffers.number_types.UOffsetTFlags.py_type(FloorListImgPath), 0)

    @staticmethod
    def AddFloorImgPath(builder, FloorImgPath): builder.PrependUOffsetTRelativeSlot(12, flatbuffers.number_types.UOffsetTFlags.py_type(FloorImgPath), 0)

    @staticmethod
    def AddRaidCharacterId(builder, RaidCharacterId): builder.PrependInt64Slot(13, RaidCharacterId, 0)


    @staticmethod
    def AddBossCharacterId(builder, BossCharacterId): builder.PrependUOffsetTRelativeSlot(14, flatbuffers.number_types.UOffsetTFlags.py_type(BossCharacterId), 0)
    @staticmethod
    def StartBossCharacterIdVector(builder, numElems): return builder.StartVector(8, numElems, 8)


    @staticmethod
    def AddStatChangeId(builder, StatChangeId): builder.PrependUOffsetTRelativeSlot(15, flatbuffers.number_types.UOffsetTFlags.py_type(StatChangeId), 0)
    @staticmethod
    def StartStatChangeIdVector(builder, numElems): return builder.StartVector(8, numElems, 8)


    @staticmethod
    def AddBattleDuration(builder, BattleDuration): builder.PrependInt64Slot(16, BattleDuration, 0)


    @staticmethod
    def AddGroundId(builder, GroundId): builder.PrependInt64Slot(17, GroundId, 0)


    @staticmethod
    def AddRecommendLevel(builder, RecommendLevel): builder.PrependInt64Slot(18, RecommendLevel, 0)


    @staticmethod
    def AddRewardGroupId(builder, RewardGroupId): builder.PrependInt64Slot(19, RewardGroupId, 0)


    @staticmethod
    def AddBattleReadyTimelinePath(builder, BattleReadyTimelinePath): builder.PrependUOffsetTRelativeSlot(20, flatbuffers.number_types.UOffsetTFlags.py_type(BattleReadyTimelinePath), 0)
    @staticmethod
    def StartBattleReadyTimelinePathVector(builder, numElems): return builder.StartVector(4, numElems, 4)


    @staticmethod
    def AddBattleReadyTimelinePhaseStart(builder, BattleReadyTimelinePhaseStart): builder.PrependUOffsetTRelativeSlot(21, flatbuffers.number_types.UOffsetTFlags.py_type(BattleReadyTimelinePhaseStart), 0)
    @staticmethod
    def StartBattleReadyTimelinePhaseStartVector(builder, numElems): return builder.StartVector(4, numElems, 4)


    @staticmethod
    def AddBattleReadyTimelinePhaseEnd(builder, BattleReadyTimelinePhaseEnd): builder.PrependUOffsetTRelativeSlot(22, flatbuffers.number_types.UOffsetTFlags.py_type(BattleReadyTimelinePhaseEnd), 0)
    @staticmethod
    def StartBattleReadyTimelinePhaseEndVector(builder, numElems): return builder.StartVector(4, numElems, 4)


    @staticmethod
    def AddVictoryTimelinePath(builder, VictoryTimelinePath): builder.PrependUOffsetTRelativeSlot(23, flatbuffers.number_types.UOffsetTFlags.py_type(VictoryTimelinePath), 0)

    @staticmethod
    def AddShowSkillCard(builder, ShowSkillCard): builder.PrependBoolSlot(24, ShowSkillCard, 0)

