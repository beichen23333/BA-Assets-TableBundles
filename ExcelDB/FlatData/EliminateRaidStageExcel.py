
import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class EliminateRaidStageExcel:
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = EliminateRaidStageExcel()
        x.Init(buf, n + offset)
        return x

    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)


    def Id(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def UseBossIndex(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0


    def UseBossAIPhaseSync(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0


    def RaidBossGroup(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def RaidEnterCostType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def RaidEnterCostId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def RaidEnterCostAmount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def BossSpinePath(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def PortraitPath(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def BGPath(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def RaidCharacterId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def BossCharacterId(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int64Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 8))
        return 0

    def BossCharacterIdAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int64Flags, o)
        return 0

    def BossCharacterIdLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    def BossCharacterIdIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        return o == 0


    def Difficulty(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(28))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def IsOpen(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(30))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0


    def MaxPlayerCount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(32))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def RaidRoomLifeTime(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(34))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


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


    def GroundDevName(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(40))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def EnterTimeLine(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(42))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def TacticEnvironment(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(44))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def DefaultClearScore(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(46))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def MaximumScore(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(48))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def PerSecondMinusScore(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(50))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def HPPercentScore(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(52))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def MinimumAcquisitionScore(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(54))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def MaximumAcquisitionScore(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(56))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def RaidRewardGroupId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(58))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def BattleReadyTimelinePath(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(60))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.String(a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return ""

    def BattleReadyTimelinePathLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(60))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    def BattleReadyTimelinePathIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(60))
        return o == 0


    def BattleReadyTimelinePhaseStart(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(62))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int32Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return 0

    def BattleReadyTimelinePhaseStartAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(62))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int32Flags, o)
        return 0

    def BattleReadyTimelinePhaseStartLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(62))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    def BattleReadyTimelinePhaseStartIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(62))
        return o == 0


    def BattleReadyTimelinePhaseEnd(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(64))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int32Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return 0

    def BattleReadyTimelinePhaseEndAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(64))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int32Flags, o)
        return 0

    def BattleReadyTimelinePhaseEndLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(64))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    def BattleReadyTimelinePhaseEndIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(64))
        return o == 0


    def VictoryTimelinePath(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(66))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def PhaseChangeTimelinePath(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(68))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def TimeLinePhase(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(70))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def EnterScenarioKey(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(72))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0


    def ClearScenarioKey(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(74))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0


    def ShowSkillCard(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(76))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0


    def BossBGInfoKey(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(78))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0


    def EchelonExtensionType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(80))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0




    @staticmethod
    def Start(builder): builder.StartObject(39)
    @staticmethod
    def End(builder): return builder.EndObject()


    @staticmethod
    def AddId(builder, Id): builder.PrependInt64Slot(0, Id, 0)


    @staticmethod
    def AddUseBossIndex(builder, UseBossIndex): builder.PrependBoolSlot(1, UseBossIndex, 0)


    @staticmethod
    def AddUseBossAIPhaseSync(builder, UseBossAIPhaseSync): builder.PrependBoolSlot(2, UseBossAIPhaseSync, 0)


    @staticmethod
    def AddRaidBossGroup(builder, RaidBossGroup): builder.PrependUOffsetTRelativeSlot(3, flatbuffers.number_types.UOffsetTFlags.py_type(RaidBossGroup), 0)

    @staticmethod
    def AddRaidEnterCostType(builder, RaidEnterCostType): builder.PrependInt32Slot(4, RaidEnterCostType, 0)


    @staticmethod
    def AddRaidEnterCostId(builder, RaidEnterCostId): builder.PrependInt64Slot(5, RaidEnterCostId, 0)


    @staticmethod
    def AddRaidEnterCostAmount(builder, RaidEnterCostAmount): builder.PrependInt32Slot(6, RaidEnterCostAmount, 0)


    @staticmethod
    def AddBossSpinePath(builder, BossSpinePath): builder.PrependUOffsetTRelativeSlot(7, flatbuffers.number_types.UOffsetTFlags.py_type(BossSpinePath), 0)

    @staticmethod
    def AddPortraitPath(builder, PortraitPath): builder.PrependUOffsetTRelativeSlot(8, flatbuffers.number_types.UOffsetTFlags.py_type(PortraitPath), 0)

    @staticmethod
    def AddBGPath(builder, BGPath): builder.PrependUOffsetTRelativeSlot(9, flatbuffers.number_types.UOffsetTFlags.py_type(BGPath), 0)

    @staticmethod
    def AddRaidCharacterId(builder, RaidCharacterId): builder.PrependInt64Slot(10, RaidCharacterId, 0)


    @staticmethod
    def AddBossCharacterId(builder, BossCharacterId): builder.PrependUOffsetTRelativeSlot(11, flatbuffers.number_types.UOffsetTFlags.py_type(BossCharacterId), 0)
    @staticmethod
    def StartBossCharacterIdVector(builder, numElems): return builder.StartVector(8, numElems, 8)


    @staticmethod
    def AddDifficulty(builder, Difficulty): builder.PrependInt32Slot(12, Difficulty, 0)


    @staticmethod
    def AddIsOpen(builder, IsOpen): builder.PrependBoolSlot(13, IsOpen, 0)


    @staticmethod
    def AddMaxPlayerCount(builder, MaxPlayerCount): builder.PrependInt64Slot(14, MaxPlayerCount, 0)


    @staticmethod
    def AddRaidRoomLifeTime(builder, RaidRoomLifeTime): builder.PrependInt32Slot(15, RaidRoomLifeTime, 0)


    @staticmethod
    def AddBattleDuration(builder, BattleDuration): builder.PrependInt64Slot(16, BattleDuration, 0)


    @staticmethod
    def AddGroundId(builder, GroundId): builder.PrependInt64Slot(17, GroundId, 0)


    @staticmethod
    def AddGroundDevName(builder, GroundDevName): builder.PrependUOffsetTRelativeSlot(18, flatbuffers.number_types.UOffsetTFlags.py_type(GroundDevName), 0)

    @staticmethod
    def AddEnterTimeLine(builder, EnterTimeLine): builder.PrependUOffsetTRelativeSlot(19, flatbuffers.number_types.UOffsetTFlags.py_type(EnterTimeLine), 0)

    @staticmethod
    def AddTacticEnvironment(builder, TacticEnvironment): builder.PrependInt32Slot(20, TacticEnvironment, 0)


    @staticmethod
    def AddDefaultClearScore(builder, DefaultClearScore): builder.PrependInt64Slot(21, DefaultClearScore, 0)


    @staticmethod
    def AddMaximumScore(builder, MaximumScore): builder.PrependInt64Slot(22, MaximumScore, 0)


    @staticmethod
    def AddPerSecondMinusScore(builder, PerSecondMinusScore): builder.PrependInt64Slot(23, PerSecondMinusScore, 0)


    @staticmethod
    def AddHPPercentScore(builder, HPPercentScore): builder.PrependInt64Slot(24, HPPercentScore, 0)


    @staticmethod
    def AddMinimumAcquisitionScore(builder, MinimumAcquisitionScore): builder.PrependInt64Slot(25, MinimumAcquisitionScore, 0)


    @staticmethod
    def AddMaximumAcquisitionScore(builder, MaximumAcquisitionScore): builder.PrependInt64Slot(26, MaximumAcquisitionScore, 0)


    @staticmethod
    def AddRaidRewardGroupId(builder, RaidRewardGroupId): builder.PrependInt64Slot(27, RaidRewardGroupId, 0)


    @staticmethod
    def AddBattleReadyTimelinePath(builder, BattleReadyTimelinePath): builder.PrependUOffsetTRelativeSlot(28, flatbuffers.number_types.UOffsetTFlags.py_type(BattleReadyTimelinePath), 0)
    @staticmethod
    def StartBattleReadyTimelinePathVector(builder, numElems): return builder.StartVector(4, numElems, 4)


    @staticmethod
    def AddBattleReadyTimelinePhaseStart(builder, BattleReadyTimelinePhaseStart): builder.PrependUOffsetTRelativeSlot(29, flatbuffers.number_types.UOffsetTFlags.py_type(BattleReadyTimelinePhaseStart), 0)
    @staticmethod
    def StartBattleReadyTimelinePhaseStartVector(builder, numElems): return builder.StartVector(4, numElems, 4)


    @staticmethod
    def AddBattleReadyTimelinePhaseEnd(builder, BattleReadyTimelinePhaseEnd): builder.PrependUOffsetTRelativeSlot(30, flatbuffers.number_types.UOffsetTFlags.py_type(BattleReadyTimelinePhaseEnd), 0)
    @staticmethod
    def StartBattleReadyTimelinePhaseEndVector(builder, numElems): return builder.StartVector(4, numElems, 4)


    @staticmethod
    def AddVictoryTimelinePath(builder, VictoryTimelinePath): builder.PrependUOffsetTRelativeSlot(31, flatbuffers.number_types.UOffsetTFlags.py_type(VictoryTimelinePath), 0)

    @staticmethod
    def AddPhaseChangeTimelinePath(builder, PhaseChangeTimelinePath): builder.PrependUOffsetTRelativeSlot(32, flatbuffers.number_types.UOffsetTFlags.py_type(PhaseChangeTimelinePath), 0)

    @staticmethod
    def AddTimeLinePhase(builder, TimeLinePhase): builder.PrependInt64Slot(33, TimeLinePhase, 0)


    @staticmethod
    def AddEnterScenarioKey(builder, EnterScenarioKey): builder.PrependUint32Slot(34, EnterScenarioKey, 0)


    @staticmethod
    def AddClearScenarioKey(builder, ClearScenarioKey): builder.PrependUint32Slot(35, ClearScenarioKey, 0)


    @staticmethod
    def AddShowSkillCard(builder, ShowSkillCard): builder.PrependBoolSlot(36, ShowSkillCard, 0)


    @staticmethod
    def AddBossBGInfoKey(builder, BossBGInfoKey): builder.PrependUint32Slot(37, BossBGInfoKey, 0)


    @staticmethod
    def AddEchelonExtensionType(builder, EchelonExtensionType): builder.PrependInt32Slot(38, EchelonExtensionType, 0)

