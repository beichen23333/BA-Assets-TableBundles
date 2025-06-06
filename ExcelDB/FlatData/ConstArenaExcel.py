
import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class ConstArenaExcel:
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = ConstArenaExcel()
        x.Init(buf, n + offset)
        return x

    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)


    def AttackCoolTime(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def BattleDuration(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def DefenseCoolTime(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def TSSStartCoolTime(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def EndAlarm(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def TimeRewardMaxAmount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def EnterCostType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def EnterCostId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def TicketCost(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def DailyRewardResetTime(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def OpenScenarioId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def CharacterSlotHideRank(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int64Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 8))
        return 0

    def CharacterSlotHideRankAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int64Flags, o)
        return 0

    def CharacterSlotHideRankLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    def CharacterSlotHideRankIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        return o == 0


    def MapSlotHideRank(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(28))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def RelativeOpponentRankStart(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(30))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int64Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 8))
        return 0

    def RelativeOpponentRankStartAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(30))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int64Flags, o)
        return 0

    def RelativeOpponentRankStartLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(30))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    def RelativeOpponentRankStartIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(30))
        return o == 0


    def RelativeOpponentRankEnd(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(32))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int64Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 8))
        return 0

    def RelativeOpponentRankEndAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(32))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int64Flags, o)
        return 0

    def RelativeOpponentRankEndLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(32))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    def RelativeOpponentRankEndIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(32))
        return o == 0


    def ModifiedStatType(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(34))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int32Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return 0

    def ModifiedStatTypeAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(34))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int32Flags, o)
        return 0

    def ModifiedStatTypeLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(34))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    def ModifiedStatTypeIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(34))
        return o == 0


    def StatMulFactor(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(36))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int64Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 8))
        return 0

    def StatMulFactorAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(36))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int64Flags, o)
        return 0

    def StatMulFactorLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(36))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    def StatMulFactorIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(36))
        return o == 0


    def StatSumFactor(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(38))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int64Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 8))
        return 0

    def StatSumFactorAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(38))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int64Flags, o)
        return 0

    def StatSumFactorLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(38))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    def StatSumFactorIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(38))
        return o == 0


    def NPCName(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(40))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.String(a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return ""

    def NPCNameLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(40))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    def NPCNameIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(40))
        return o == 0


    def NPCMainCharacterCount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(42))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def NPCSupportCharacterCount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(44))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def NPCCharacterSkillLevel(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(46))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def TimeSpanInDaysForBattleHistory(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(48))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def HiddenCharacterImagePath(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(50))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def DefenseVictoryRewardMaxCount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(52))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def TopRankerCountLimit(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(54))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def AutoRefreshIntervalMilliSeconds(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(56))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def EchelonSettingIntervalMilliSeconds(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(58))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def SkipAllowedTimeMilliSeconds(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(60))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def ShowSeasonChangeInfoStartTime(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(62))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def ShowSeasonChangeInfoEndTime(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(64))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def ShowSeasonId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(66))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def ArenaHistoryQueryLimitDays(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(68))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0




    @staticmethod
    def Start(builder): builder.StartObject(33)
    @staticmethod
    def End(builder): return builder.EndObject()


    @staticmethod
    def AddAttackCoolTime(builder, AttackCoolTime): builder.PrependInt64Slot(0, AttackCoolTime, 0)


    @staticmethod
    def AddBattleDuration(builder, BattleDuration): builder.PrependInt64Slot(1, BattleDuration, 0)


    @staticmethod
    def AddDefenseCoolTime(builder, DefenseCoolTime): builder.PrependInt64Slot(2, DefenseCoolTime, 0)


    @staticmethod
    def AddTSSStartCoolTime(builder, TSSStartCoolTime): builder.PrependInt64Slot(3, TSSStartCoolTime, 0)


    @staticmethod
    def AddEndAlarm(builder, EndAlarm): builder.PrependInt64Slot(4, EndAlarm, 0)


    @staticmethod
    def AddTimeRewardMaxAmount(builder, TimeRewardMaxAmount): builder.PrependInt64Slot(5, TimeRewardMaxAmount, 0)


    @staticmethod
    def AddEnterCostType(builder, EnterCostType): builder.PrependInt32Slot(6, EnterCostType, 0)


    @staticmethod
    def AddEnterCostId(builder, EnterCostId): builder.PrependInt64Slot(7, EnterCostId, 0)


    @staticmethod
    def AddTicketCost(builder, TicketCost): builder.PrependInt64Slot(8, TicketCost, 0)


    @staticmethod
    def AddDailyRewardResetTime(builder, DailyRewardResetTime): builder.PrependUOffsetTRelativeSlot(9, flatbuffers.number_types.UOffsetTFlags.py_type(DailyRewardResetTime), 0)

    @staticmethod
    def AddOpenScenarioId(builder, OpenScenarioId): builder.PrependUOffsetTRelativeSlot(10, flatbuffers.number_types.UOffsetTFlags.py_type(OpenScenarioId), 0)

    @staticmethod
    def AddCharacterSlotHideRank(builder, CharacterSlotHideRank): builder.PrependUOffsetTRelativeSlot(11, flatbuffers.number_types.UOffsetTFlags.py_type(CharacterSlotHideRank), 0)
    @staticmethod
    def StartCharacterSlotHideRankVector(builder, numElems): return builder.StartVector(8, numElems, 8)


    @staticmethod
    def AddMapSlotHideRank(builder, MapSlotHideRank): builder.PrependInt64Slot(12, MapSlotHideRank, 0)


    @staticmethod
    def AddRelativeOpponentRankStart(builder, RelativeOpponentRankStart): builder.PrependUOffsetTRelativeSlot(13, flatbuffers.number_types.UOffsetTFlags.py_type(RelativeOpponentRankStart), 0)
    @staticmethod
    def StartRelativeOpponentRankStartVector(builder, numElems): return builder.StartVector(8, numElems, 8)


    @staticmethod
    def AddRelativeOpponentRankEnd(builder, RelativeOpponentRankEnd): builder.PrependUOffsetTRelativeSlot(14, flatbuffers.number_types.UOffsetTFlags.py_type(RelativeOpponentRankEnd), 0)
    @staticmethod
    def StartRelativeOpponentRankEndVector(builder, numElems): return builder.StartVector(8, numElems, 8)


    @staticmethod
    def AddModifiedStatType(builder, ModifiedStatType): builder.PrependUOffsetTRelativeSlot(15, flatbuffers.number_types.UOffsetTFlags.py_type(ModifiedStatType), 0)
    @staticmethod
    def StartModifiedStatTypeVector(builder, numElems): return builder.StartVector(4, numElems, 4)


    @staticmethod
    def AddStatMulFactor(builder, StatMulFactor): builder.PrependUOffsetTRelativeSlot(16, flatbuffers.number_types.UOffsetTFlags.py_type(StatMulFactor), 0)
    @staticmethod
    def StartStatMulFactorVector(builder, numElems): return builder.StartVector(8, numElems, 8)


    @staticmethod
    def AddStatSumFactor(builder, StatSumFactor): builder.PrependUOffsetTRelativeSlot(17, flatbuffers.number_types.UOffsetTFlags.py_type(StatSumFactor), 0)
    @staticmethod
    def StartStatSumFactorVector(builder, numElems): return builder.StartVector(8, numElems, 8)


    @staticmethod
    def AddNPCName(builder, NPCName): builder.PrependUOffsetTRelativeSlot(18, flatbuffers.number_types.UOffsetTFlags.py_type(NPCName), 0)
    @staticmethod
    def StartNPCNameVector(builder, numElems): return builder.StartVector(4, numElems, 4)


    @staticmethod
    def AddNPCMainCharacterCount(builder, NPCMainCharacterCount): builder.PrependInt64Slot(19, NPCMainCharacterCount, 0)


    @staticmethod
    def AddNPCSupportCharacterCount(builder, NPCSupportCharacterCount): builder.PrependInt64Slot(20, NPCSupportCharacterCount, 0)


    @staticmethod
    def AddNPCCharacterSkillLevel(builder, NPCCharacterSkillLevel): builder.PrependInt64Slot(21, NPCCharacterSkillLevel, 0)


    @staticmethod
    def AddTimeSpanInDaysForBattleHistory(builder, TimeSpanInDaysForBattleHistory): builder.PrependInt64Slot(22, TimeSpanInDaysForBattleHistory, 0)


    @staticmethod
    def AddHiddenCharacterImagePath(builder, HiddenCharacterImagePath): builder.PrependUOffsetTRelativeSlot(23, flatbuffers.number_types.UOffsetTFlags.py_type(HiddenCharacterImagePath), 0)

    @staticmethod
    def AddDefenseVictoryRewardMaxCount(builder, DefenseVictoryRewardMaxCount): builder.PrependInt64Slot(24, DefenseVictoryRewardMaxCount, 0)


    @staticmethod
    def AddTopRankerCountLimit(builder, TopRankerCountLimit): builder.PrependInt64Slot(25, TopRankerCountLimit, 0)


    @staticmethod
    def AddAutoRefreshIntervalMilliSeconds(builder, AutoRefreshIntervalMilliSeconds): builder.PrependInt64Slot(26, AutoRefreshIntervalMilliSeconds, 0)


    @staticmethod
    def AddEchelonSettingIntervalMilliSeconds(builder, EchelonSettingIntervalMilliSeconds): builder.PrependInt64Slot(27, EchelonSettingIntervalMilliSeconds, 0)


    @staticmethod
    def AddSkipAllowedTimeMilliSeconds(builder, SkipAllowedTimeMilliSeconds): builder.PrependInt64Slot(28, SkipAllowedTimeMilliSeconds, 0)


    @staticmethod
    def AddShowSeasonChangeInfoStartTime(builder, ShowSeasonChangeInfoStartTime): builder.PrependUOffsetTRelativeSlot(29, flatbuffers.number_types.UOffsetTFlags.py_type(ShowSeasonChangeInfoStartTime), 0)

    @staticmethod
    def AddShowSeasonChangeInfoEndTime(builder, ShowSeasonChangeInfoEndTime): builder.PrependUOffsetTRelativeSlot(30, flatbuffers.number_types.UOffsetTFlags.py_type(ShowSeasonChangeInfoEndTime), 0)

    @staticmethod
    def AddShowSeasonId(builder, ShowSeasonId): builder.PrependInt64Slot(31, ShowSeasonId, 0)


    @staticmethod
    def AddArenaHistoryQueryLimitDays(builder, ArenaHistoryQueryLimitDays): builder.PrependInt32Slot(32, ArenaHistoryQueryLimitDays, 0)

