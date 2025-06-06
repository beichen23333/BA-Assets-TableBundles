
import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class ConstCombatExcel:
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = ConstCombatExcel()
        x.Init(buf, n + offset)
        return x

    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)


    def SkillHandCount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def DyingTime(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def BuffIconBlinkTime(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def ShowBufficonEXSkill(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0


    def ShowBufficonPassiveSkill(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0


    def ShowBufficonExtraPassiveSkill(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0


    def ShowBufficonLeaderSkill(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0


    def ShowBufficonGroundPassiveSkill(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0


    def SuppliesConditionStringId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def PublicSpeechBubbleOffsetX(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0


    def PublicSpeechBubbleOffsetY(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0


    def PublicSpeechBubbleOffsetZ(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0


    def ShowRaidListCount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(28))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def MaxRaidTicketCount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(30))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def MaxRaidBossSkillSlot(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(32))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def EngageTimelinePath(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(34))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def EngageWithSupporterTimelinePath(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(36))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def VictoryTimelinePath(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(38))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def TimeLimitAlarm(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(40))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def EchelonMaxCommonCost(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(42))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def EchelonInitCommonCost(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(44))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def SkillSlotCoolTime(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(46))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def EnemyRegenCost(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(48))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def ChampionRegenCost(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(50))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def PlayerRegenCostDelay(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(52))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def CrowdControlFactor(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(54))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def RaidOpenScenarioId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(56))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def EliminateRaidOpenScenarioId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(58))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def DefenceConstA(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(60))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def DefenceConstB(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(62))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def DefenceConstC(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(64))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def DefenceConstD(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(66))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def AccuracyConstA(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(68))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def AccuracyConstB(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(70))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def AccuracyConstC(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(72))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def AccuracyConstD(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(74))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def CriticalConstA(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(76))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def CriticalConstB(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(78))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def CriticalConstC(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(80))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def CriticalConstD(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(82))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def MaxGroupBuffLevel(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(84))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def EmojiDefaultTime(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(86))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def TimeLineActionRotateSpeed(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(88))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def BodyRotateSpeed(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(90))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def NormalTimeScale(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(92))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def FastTimeScale(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(94))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def BulletTimeScale(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(96))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def UIDisplayDelayAfterSkillCutIn(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(98))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def UseInitialRangeForCoverMove(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(100))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0


    def SlowTimeScale(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(102))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def AimIKMinDegree(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(104))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0


    def AimIKMaxDegree(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(106))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0


    def MinimumClearTime(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(108))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def MinimumClearLevelGap(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(110))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def CheckCheaterMaxUseCostNonArena(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(112))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def CheckCheaterMaxUseCostArena(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(114))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def AllowedMaxTimeScale(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(116))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def RandomAnimationOutput(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(118))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def SummonedTeleportDistance(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(120))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def ArenaMinimumClearTime(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(122))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def WORLDBOSSBATTLELITTLE(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(124))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def WORLDBOSSBATTLEMIDDLE(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(126))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def WORLDBOSSBATTLEHIGH(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(128))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def WORLDBOSSBATTLEVERYHIGH(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(130))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def WorldRaidAutoSyncTermSecond(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(132))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def WorldRaidBossHpDecreaseTerm(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(134))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def WorldRaidBossParcelReactionDelay(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(136))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def RaidRankingJumpMinimumWaitingTime(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(138))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def EffectTeleportDistance(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(140))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0


    def AuraExitThresholdMargin(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(142))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def TSAInteractionDamageFactor(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(144))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def VictoryInteractionRate(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(146))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def EchelonExtensionEngageTimelinePath(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(148))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def EchelonExtensionEngageWithSupporterTimelinePath(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(150))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def EchelonExtensionVictoryTimelinePath(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(152))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def EchelonExtensionEchelonMaxCommonCost(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(154))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def EchelonExtensionEchelonInitCommonCost(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(156))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def EchelonExtensionCostRegenRatio(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(158))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def CheckCheaterMaxUseCostMultiFloorRaid(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(160))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def ExcessiveTouchCheckTime(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(162))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0


    def ExcessiveTouchCheckCount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(164))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def CampaignAlertPopupLevelGap(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(166))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0




    @staticmethod
    def Start(builder): builder.StartObject(82)
    @staticmethod
    def End(builder): return builder.EndObject()


    @staticmethod
    def AddSkillHandCount(builder, SkillHandCount): builder.PrependInt32Slot(0, SkillHandCount, 0)


    @staticmethod
    def AddDyingTime(builder, DyingTime): builder.PrependInt32Slot(1, DyingTime, 0)


    @staticmethod
    def AddBuffIconBlinkTime(builder, BuffIconBlinkTime): builder.PrependInt32Slot(2, BuffIconBlinkTime, 0)


    @staticmethod
    def AddShowBufficonEXSkill(builder, ShowBufficonEXSkill): builder.PrependBoolSlot(3, ShowBufficonEXSkill, 0)


    @staticmethod
    def AddShowBufficonPassiveSkill(builder, ShowBufficonPassiveSkill): builder.PrependBoolSlot(4, ShowBufficonPassiveSkill, 0)


    @staticmethod
    def AddShowBufficonExtraPassiveSkill(builder, ShowBufficonExtraPassiveSkill): builder.PrependBoolSlot(5, ShowBufficonExtraPassiveSkill, 0)


    @staticmethod
    def AddShowBufficonLeaderSkill(builder, ShowBufficonLeaderSkill): builder.PrependBoolSlot(6, ShowBufficonLeaderSkill, 0)


    @staticmethod
    def AddShowBufficonGroundPassiveSkill(builder, ShowBufficonGroundPassiveSkill): builder.PrependBoolSlot(7, ShowBufficonGroundPassiveSkill, 0)


    @staticmethod
    def AddSuppliesConditionStringId(builder, SuppliesConditionStringId): builder.PrependUOffsetTRelativeSlot(8, flatbuffers.number_types.UOffsetTFlags.py_type(SuppliesConditionStringId), 0)

    @staticmethod
    def AddPublicSpeechBubbleOffsetX(builder, PublicSpeechBubbleOffsetX): builder.PrependFloat32Slot(9, PublicSpeechBubbleOffsetX, 0)


    @staticmethod
    def AddPublicSpeechBubbleOffsetY(builder, PublicSpeechBubbleOffsetY): builder.PrependFloat32Slot(10, PublicSpeechBubbleOffsetY, 0)


    @staticmethod
    def AddPublicSpeechBubbleOffsetZ(builder, PublicSpeechBubbleOffsetZ): builder.PrependFloat32Slot(11, PublicSpeechBubbleOffsetZ, 0)


    @staticmethod
    def AddShowRaidListCount(builder, ShowRaidListCount): builder.PrependInt32Slot(12, ShowRaidListCount, 0)


    @staticmethod
    def AddMaxRaidTicketCount(builder, MaxRaidTicketCount): builder.PrependInt64Slot(13, MaxRaidTicketCount, 0)


    @staticmethod
    def AddMaxRaidBossSkillSlot(builder, MaxRaidBossSkillSlot): builder.PrependInt64Slot(14, MaxRaidBossSkillSlot, 0)


    @staticmethod
    def AddEngageTimelinePath(builder, EngageTimelinePath): builder.PrependUOffsetTRelativeSlot(15, flatbuffers.number_types.UOffsetTFlags.py_type(EngageTimelinePath), 0)

    @staticmethod
    def AddEngageWithSupporterTimelinePath(builder, EngageWithSupporterTimelinePath): builder.PrependUOffsetTRelativeSlot(16, flatbuffers.number_types.UOffsetTFlags.py_type(EngageWithSupporterTimelinePath), 0)

    @staticmethod
    def AddVictoryTimelinePath(builder, VictoryTimelinePath): builder.PrependUOffsetTRelativeSlot(17, flatbuffers.number_types.UOffsetTFlags.py_type(VictoryTimelinePath), 0)

    @staticmethod
    def AddTimeLimitAlarm(builder, TimeLimitAlarm): builder.PrependInt64Slot(18, TimeLimitAlarm, 0)


    @staticmethod
    def AddEchelonMaxCommonCost(builder, EchelonMaxCommonCost): builder.PrependInt32Slot(19, EchelonMaxCommonCost, 0)


    @staticmethod
    def AddEchelonInitCommonCost(builder, EchelonInitCommonCost): builder.PrependInt32Slot(20, EchelonInitCommonCost, 0)


    @staticmethod
    def AddSkillSlotCoolTime(builder, SkillSlotCoolTime): builder.PrependInt64Slot(21, SkillSlotCoolTime, 0)


    @staticmethod
    def AddEnemyRegenCost(builder, EnemyRegenCost): builder.PrependInt64Slot(22, EnemyRegenCost, 0)


    @staticmethod
    def AddChampionRegenCost(builder, ChampionRegenCost): builder.PrependInt64Slot(23, ChampionRegenCost, 0)


    @staticmethod
    def AddPlayerRegenCostDelay(builder, PlayerRegenCostDelay): builder.PrependInt64Slot(24, PlayerRegenCostDelay, 0)


    @staticmethod
    def AddCrowdControlFactor(builder, CrowdControlFactor): builder.PrependInt64Slot(25, CrowdControlFactor, 0)


    @staticmethod
    def AddRaidOpenScenarioId(builder, RaidOpenScenarioId): builder.PrependUOffsetTRelativeSlot(26, flatbuffers.number_types.UOffsetTFlags.py_type(RaidOpenScenarioId), 0)

    @staticmethod
    def AddEliminateRaidOpenScenarioId(builder, EliminateRaidOpenScenarioId): builder.PrependUOffsetTRelativeSlot(27, flatbuffers.number_types.UOffsetTFlags.py_type(EliminateRaidOpenScenarioId), 0)

    @staticmethod
    def AddDefenceConstA(builder, DefenceConstA): builder.PrependInt64Slot(28, DefenceConstA, 0)


    @staticmethod
    def AddDefenceConstB(builder, DefenceConstB): builder.PrependInt64Slot(29, DefenceConstB, 0)


    @staticmethod
    def AddDefenceConstC(builder, DefenceConstC): builder.PrependInt64Slot(30, DefenceConstC, 0)


    @staticmethod
    def AddDefenceConstD(builder, DefenceConstD): builder.PrependInt64Slot(31, DefenceConstD, 0)


    @staticmethod
    def AddAccuracyConstA(builder, AccuracyConstA): builder.PrependInt64Slot(32, AccuracyConstA, 0)


    @staticmethod
    def AddAccuracyConstB(builder, AccuracyConstB): builder.PrependInt64Slot(33, AccuracyConstB, 0)


    @staticmethod
    def AddAccuracyConstC(builder, AccuracyConstC): builder.PrependInt64Slot(34, AccuracyConstC, 0)


    @staticmethod
    def AddAccuracyConstD(builder, AccuracyConstD): builder.PrependInt64Slot(35, AccuracyConstD, 0)


    @staticmethod
    def AddCriticalConstA(builder, CriticalConstA): builder.PrependInt64Slot(36, CriticalConstA, 0)


    @staticmethod
    def AddCriticalConstB(builder, CriticalConstB): builder.PrependInt64Slot(37, CriticalConstB, 0)


    @staticmethod
    def AddCriticalConstC(builder, CriticalConstC): builder.PrependInt64Slot(38, CriticalConstC, 0)


    @staticmethod
    def AddCriticalConstD(builder, CriticalConstD): builder.PrependInt64Slot(39, CriticalConstD, 0)


    @staticmethod
    def AddMaxGroupBuffLevel(builder, MaxGroupBuffLevel): builder.PrependInt32Slot(40, MaxGroupBuffLevel, 0)


    @staticmethod
    def AddEmojiDefaultTime(builder, EmojiDefaultTime): builder.PrependInt32Slot(41, EmojiDefaultTime, 0)


    @staticmethod
    def AddTimeLineActionRotateSpeed(builder, TimeLineActionRotateSpeed): builder.PrependInt64Slot(42, TimeLineActionRotateSpeed, 0)


    @staticmethod
    def AddBodyRotateSpeed(builder, BodyRotateSpeed): builder.PrependInt64Slot(43, BodyRotateSpeed, 0)


    @staticmethod
    def AddNormalTimeScale(builder, NormalTimeScale): builder.PrependInt64Slot(44, NormalTimeScale, 0)


    @staticmethod
    def AddFastTimeScale(builder, FastTimeScale): builder.PrependInt64Slot(45, FastTimeScale, 0)


    @staticmethod
    def AddBulletTimeScale(builder, BulletTimeScale): builder.PrependInt64Slot(46, BulletTimeScale, 0)


    @staticmethod
    def AddUIDisplayDelayAfterSkillCutIn(builder, UIDisplayDelayAfterSkillCutIn): builder.PrependInt64Slot(47, UIDisplayDelayAfterSkillCutIn, 0)


    @staticmethod
    def AddUseInitialRangeForCoverMove(builder, UseInitialRangeForCoverMove): builder.PrependBoolSlot(48, UseInitialRangeForCoverMove, 0)


    @staticmethod
    def AddSlowTimeScale(builder, SlowTimeScale): builder.PrependInt64Slot(49, SlowTimeScale, 0)


    @staticmethod
    def AddAimIKMinDegree(builder, AimIKMinDegree): builder.PrependFloat32Slot(50, AimIKMinDegree, 0)


    @staticmethod
    def AddAimIKMaxDegree(builder, AimIKMaxDegree): builder.PrependFloat32Slot(51, AimIKMaxDegree, 0)


    @staticmethod
    def AddMinimumClearTime(builder, MinimumClearTime): builder.PrependInt32Slot(52, MinimumClearTime, 0)


    @staticmethod
    def AddMinimumClearLevelGap(builder, MinimumClearLevelGap): builder.PrependInt32Slot(53, MinimumClearLevelGap, 0)


    @staticmethod
    def AddCheckCheaterMaxUseCostNonArena(builder, CheckCheaterMaxUseCostNonArena): builder.PrependInt32Slot(54, CheckCheaterMaxUseCostNonArena, 0)


    @staticmethod
    def AddCheckCheaterMaxUseCostArena(builder, CheckCheaterMaxUseCostArena): builder.PrependInt32Slot(55, CheckCheaterMaxUseCostArena, 0)


    @staticmethod
    def AddAllowedMaxTimeScale(builder, AllowedMaxTimeScale): builder.PrependInt64Slot(56, AllowedMaxTimeScale, 0)


    @staticmethod
    def AddRandomAnimationOutput(builder, RandomAnimationOutput): builder.PrependInt64Slot(57, RandomAnimationOutput, 0)


    @staticmethod
    def AddSummonedTeleportDistance(builder, SummonedTeleportDistance): builder.PrependInt64Slot(58, SummonedTeleportDistance, 0)


    @staticmethod
    def AddArenaMinimumClearTime(builder, ArenaMinimumClearTime): builder.PrependInt32Slot(59, ArenaMinimumClearTime, 0)


    @staticmethod
    def AddWORLDBOSSBATTLELITTLE(builder, WORLDBOSSBATTLELITTLE): builder.PrependInt64Slot(60, WORLDBOSSBATTLELITTLE, 0)


    @staticmethod
    def AddWORLDBOSSBATTLEMIDDLE(builder, WORLDBOSSBATTLEMIDDLE): builder.PrependInt64Slot(61, WORLDBOSSBATTLEMIDDLE, 0)


    @staticmethod
    def AddWORLDBOSSBATTLEHIGH(builder, WORLDBOSSBATTLEHIGH): builder.PrependInt64Slot(62, WORLDBOSSBATTLEHIGH, 0)


    @staticmethod
    def AddWORLDBOSSBATTLEVERYHIGH(builder, WORLDBOSSBATTLEVERYHIGH): builder.PrependInt64Slot(63, WORLDBOSSBATTLEVERYHIGH, 0)


    @staticmethod
    def AddWorldRaidAutoSyncTermSecond(builder, WorldRaidAutoSyncTermSecond): builder.PrependInt64Slot(64, WorldRaidAutoSyncTermSecond, 0)


    @staticmethod
    def AddWorldRaidBossHpDecreaseTerm(builder, WorldRaidBossHpDecreaseTerm): builder.PrependInt64Slot(65, WorldRaidBossHpDecreaseTerm, 0)


    @staticmethod
    def AddWorldRaidBossParcelReactionDelay(builder, WorldRaidBossParcelReactionDelay): builder.PrependInt64Slot(66, WorldRaidBossParcelReactionDelay, 0)


    @staticmethod
    def AddRaidRankingJumpMinimumWaitingTime(builder, RaidRankingJumpMinimumWaitingTime): builder.PrependInt64Slot(67, RaidRankingJumpMinimumWaitingTime, 0)


    @staticmethod
    def AddEffectTeleportDistance(builder, EffectTeleportDistance): builder.PrependFloat32Slot(68, EffectTeleportDistance, 0)


    @staticmethod
    def AddAuraExitThresholdMargin(builder, AuraExitThresholdMargin): builder.PrependInt64Slot(69, AuraExitThresholdMargin, 0)


    @staticmethod
    def AddTSAInteractionDamageFactor(builder, TSAInteractionDamageFactor): builder.PrependInt64Slot(70, TSAInteractionDamageFactor, 0)


    @staticmethod
    def AddVictoryInteractionRate(builder, VictoryInteractionRate): builder.PrependInt64Slot(71, VictoryInteractionRate, 0)


    @staticmethod
    def AddEchelonExtensionEngageTimelinePath(builder, EchelonExtensionEngageTimelinePath): builder.PrependUOffsetTRelativeSlot(72, flatbuffers.number_types.UOffsetTFlags.py_type(EchelonExtensionEngageTimelinePath), 0)

    @staticmethod
    def AddEchelonExtensionEngageWithSupporterTimelinePath(builder, EchelonExtensionEngageWithSupporterTimelinePath): builder.PrependUOffsetTRelativeSlot(73, flatbuffers.number_types.UOffsetTFlags.py_type(EchelonExtensionEngageWithSupporterTimelinePath), 0)

    @staticmethod
    def AddEchelonExtensionVictoryTimelinePath(builder, EchelonExtensionVictoryTimelinePath): builder.PrependUOffsetTRelativeSlot(74, flatbuffers.number_types.UOffsetTFlags.py_type(EchelonExtensionVictoryTimelinePath), 0)

    @staticmethod
    def AddEchelonExtensionEchelonMaxCommonCost(builder, EchelonExtensionEchelonMaxCommonCost): builder.PrependInt32Slot(75, EchelonExtensionEchelonMaxCommonCost, 0)


    @staticmethod
    def AddEchelonExtensionEchelonInitCommonCost(builder, EchelonExtensionEchelonInitCommonCost): builder.PrependInt32Slot(76, EchelonExtensionEchelonInitCommonCost, 0)


    @staticmethod
    def AddEchelonExtensionCostRegenRatio(builder, EchelonExtensionCostRegenRatio): builder.PrependInt64Slot(77, EchelonExtensionCostRegenRatio, 0)


    @staticmethod
    def AddCheckCheaterMaxUseCostMultiFloorRaid(builder, CheckCheaterMaxUseCostMultiFloorRaid): builder.PrependInt32Slot(78, CheckCheaterMaxUseCostMultiFloorRaid, 0)


    @staticmethod
    def AddExcessiveTouchCheckTime(builder, ExcessiveTouchCheckTime): builder.PrependFloat32Slot(79, ExcessiveTouchCheckTime, 0)


    @staticmethod
    def AddExcessiveTouchCheckCount(builder, ExcessiveTouchCheckCount): builder.PrependInt32Slot(80, ExcessiveTouchCheckCount, 0)


    @staticmethod
    def AddCampaignAlertPopupLevelGap(builder, CampaignAlertPopupLevelGap): builder.PrependInt32Slot(81, CampaignAlertPopupLevelGap, 0)

