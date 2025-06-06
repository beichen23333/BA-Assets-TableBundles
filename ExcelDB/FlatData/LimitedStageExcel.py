
import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class LimitedStageExcel:
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = LimitedStageExcel()
        x.Init(buf, n + offset)
        return x

    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)


    def Id(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def Name(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def SeasonId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def StageDifficulty(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def StageNumber(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def StageDisplay(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def PrevStageId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def OpenDate(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def OpenEventPoint(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def BattleDuration(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def StageEnterCostType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def StageEnterCostId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def StageEnterCostAmount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(28))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def StageEnterEchelonCount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(30))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def StarConditionTacticRankSCount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(32))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def StarConditionTurnCount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(34))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def EnterScenarioGroupId(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(36))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int64Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 8))
        return 0

    def EnterScenarioGroupIdAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(36))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int64Flags, o)
        return 0

    def EnterScenarioGroupIdLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(36))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    def EnterScenarioGroupIdIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(36))
        return o == 0


    def ClearScenarioGroupId(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(38))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int64Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 8))
        return 0

    def ClearScenarioGroupIdAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(38))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int64Flags, o)
        return 0

    def ClearScenarioGroupIdLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(38))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    def ClearScenarioGroupIdIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(38))
        return o == 0


    def StrategyMap(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(40))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def StrategyMapBG(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(42))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def StageRewardId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(44))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def MaxTurn(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(46))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def StageTopography(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(48))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def RecommandLevel(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(50))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def BgmId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(52))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def StrategyEnvironment(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(54))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def GroundID(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(56))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def ContentType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(58))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def BGMId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(60))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def InstantClear(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(62))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0


    def BuffContentId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(64))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def ChallengeDisplay(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(66))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0




    @staticmethod
    def Start(builder): builder.StartObject(32)
    @staticmethod
    def End(builder): return builder.EndObject()


    @staticmethod
    def AddId(builder, Id): builder.PrependInt64Slot(0, Id, 0)


    @staticmethod
    def AddName(builder, Name): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(Name), 0)

    @staticmethod
    def AddSeasonId(builder, SeasonId): builder.PrependInt64Slot(2, SeasonId, 0)


    @staticmethod
    def AddStageDifficulty(builder, StageDifficulty): builder.PrependInt32Slot(3, StageDifficulty, 0)


    @staticmethod
    def AddStageNumber(builder, StageNumber): builder.PrependUOffsetTRelativeSlot(4, flatbuffers.number_types.UOffsetTFlags.py_type(StageNumber), 0)

    @staticmethod
    def AddStageDisplay(builder, StageDisplay): builder.PrependInt32Slot(5, StageDisplay, 0)


    @staticmethod
    def AddPrevStageId(builder, PrevStageId): builder.PrependInt64Slot(6, PrevStageId, 0)


    @staticmethod
    def AddOpenDate(builder, OpenDate): builder.PrependInt64Slot(7, OpenDate, 0)


    @staticmethod
    def AddOpenEventPoint(builder, OpenEventPoint): builder.PrependInt64Slot(8, OpenEventPoint, 0)


    @staticmethod
    def AddBattleDuration(builder, BattleDuration): builder.PrependInt64Slot(9, BattleDuration, 0)


    @staticmethod
    def AddStageEnterCostType(builder, StageEnterCostType): builder.PrependInt32Slot(10, StageEnterCostType, 0)


    @staticmethod
    def AddStageEnterCostId(builder, StageEnterCostId): builder.PrependInt64Slot(11, StageEnterCostId, 0)


    @staticmethod
    def AddStageEnterCostAmount(builder, StageEnterCostAmount): builder.PrependInt32Slot(12, StageEnterCostAmount, 0)


    @staticmethod
    def AddStageEnterEchelonCount(builder, StageEnterEchelonCount): builder.PrependInt32Slot(13, StageEnterEchelonCount, 0)


    @staticmethod
    def AddStarConditionTacticRankSCount(builder, StarConditionTacticRankSCount): builder.PrependInt64Slot(14, StarConditionTacticRankSCount, 0)


    @staticmethod
    def AddStarConditionTurnCount(builder, StarConditionTurnCount): builder.PrependInt64Slot(15, StarConditionTurnCount, 0)


    @staticmethod
    def AddEnterScenarioGroupId(builder, EnterScenarioGroupId): builder.PrependUOffsetTRelativeSlot(16, flatbuffers.number_types.UOffsetTFlags.py_type(EnterScenarioGroupId), 0)
    @staticmethod
    def StartEnterScenarioGroupIdVector(builder, numElems): return builder.StartVector(8, numElems, 8)


    @staticmethod
    def AddClearScenarioGroupId(builder, ClearScenarioGroupId): builder.PrependUOffsetTRelativeSlot(17, flatbuffers.number_types.UOffsetTFlags.py_type(ClearScenarioGroupId), 0)
    @staticmethod
    def StartClearScenarioGroupIdVector(builder, numElems): return builder.StartVector(8, numElems, 8)


    @staticmethod
    def AddStrategyMap(builder, StrategyMap): builder.PrependUOffsetTRelativeSlot(18, flatbuffers.number_types.UOffsetTFlags.py_type(StrategyMap), 0)

    @staticmethod
    def AddStrategyMapBG(builder, StrategyMapBG): builder.PrependUOffsetTRelativeSlot(19, flatbuffers.number_types.UOffsetTFlags.py_type(StrategyMapBG), 0)

    @staticmethod
    def AddStageRewardId(builder, StageRewardId): builder.PrependInt64Slot(20, StageRewardId, 0)


    @staticmethod
    def AddMaxTurn(builder, MaxTurn): builder.PrependInt32Slot(21, MaxTurn, 0)


    @staticmethod
    def AddStageTopography(builder, StageTopography): builder.PrependInt32Slot(22, StageTopography, 0)


    @staticmethod
    def AddRecommandLevel(builder, RecommandLevel): builder.PrependInt32Slot(23, RecommandLevel, 0)


    @staticmethod
    def AddBgmId(builder, BgmId): builder.PrependUOffsetTRelativeSlot(24, flatbuffers.number_types.UOffsetTFlags.py_type(BgmId), 0)

    @staticmethod
    def AddStrategyEnvironment(builder, StrategyEnvironment): builder.PrependInt32Slot(25, StrategyEnvironment, 0)


    @staticmethod
    def AddGroundID(builder, GroundID): builder.PrependInt64Slot(26, GroundID, 0)


    @staticmethod
    def AddContentType(builder, ContentType): builder.PrependInt32Slot(27, ContentType, 0)


    @staticmethod
    def AddBGMId(builder, BGMId): builder.PrependInt64Slot(28, BGMId, 0)


    @staticmethod
    def AddInstantClear(builder, InstantClear): builder.PrependBoolSlot(29, InstantClear, 0)


    @staticmethod
    def AddBuffContentId(builder, BuffContentId): builder.PrependInt64Slot(30, BuffContentId, 0)


    @staticmethod
    def AddChallengeDisplay(builder, ChallengeDisplay): builder.PrependBoolSlot(31, ChallengeDisplay, 0)

