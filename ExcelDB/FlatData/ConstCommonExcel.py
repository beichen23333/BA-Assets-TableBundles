
import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class ConstCommonExcel:
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = ConstCommonExcel()
        x.Init(buf, n + offset)
        return x

    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)


    def CampaignMainStageMaxRank(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def CampaignMainStageBestRecord(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def HardAdventurePlayCountRecoverDailyNumber(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def HardStageCount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def TacticRankClearTime(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def BaseTimeScale(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def GachaPercentage(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def AcademyFavorZoneId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def CafePresetSlotCount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def CafeMonologueIntervalMillisec(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def CafeMonologueDefaultDuration(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def CafeBubbleIdleDurationMilliSec(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def FindGiftTimeLimit(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(28))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def CafeAutoChargePeriodInMsc(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(30))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def CafeProductionDecimalPosition(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(32))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def CafeSetGroupApplyCount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(34))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def WeekDungeonFindGiftRewardLimitCount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(36))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def StageFailedCurrencyRefundRate(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(38))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def EnterDeposit(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(40))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def AccountMaxLevel(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(42))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def MainSquadExpBonus(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(44))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def SupportSquadExpBonus(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(46))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def AccountExpRatio(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(48))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def MissionToastLifeTime(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(50))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def ExpItemInsertLimit(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(52))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def ExpItemInsertAccelTime(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(54))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def CharacterLvUpCoefficient(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(56))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def EquipmentLvUpCoefficient(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(58))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def ExpEquipInsertLimit(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(60))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def EquipLvUpCoefficient(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(62))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def NicknameLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(64))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def CraftDuration(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(66))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int32Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return 0

    def CraftDurationAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(66))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int32Flags, o)
        return 0

    def CraftDurationLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(66))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    def CraftDurationIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(66))
        return o == 0


    def CraftLimitTime(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(68))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def ShiftingCraftDuration(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(70))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int32Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return 0

    def ShiftingCraftDurationAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(70))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int32Flags, o)
        return 0

    def ShiftingCraftDurationLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(70))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    def ShiftingCraftDurationIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(70))
        return o == 0


    def ShiftingCraftTicketConsumeAmount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(72))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def ShiftingCraftSlotMaxCapacity(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(74))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def CraftTicketItemUniqueId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(76))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def CraftTicketConsumeAmount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(78))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def AcademyEnterCostType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(80))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def AcademyEnterCostId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(82))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def AcademyTicketCost(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(84))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def MassangerMessageExpireDay(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(86))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def CraftLeafNodeGenerateLv1Count(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(88))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def CraftLeafNodeGenerateLv2Count(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(90))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def TutorialGachaShopId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(92))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def BeforehandGachaShopId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(94))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def TutorialGachaGoodsId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(96))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def EquipmentSlotOpenLevel(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(98))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int32Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return 0

    def EquipmentSlotOpenLevelAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(98))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int32Flags, o)
        return 0

    def EquipmentSlotOpenLevelLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(98))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    def EquipmentSlotOpenLevelIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(98))
        return o == 0


    def ScenarioAutoDelayMillisec(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(100))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0


    def JoinOrCreateClanCoolTimeFromHour(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(102))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def ClanMaxMember(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(104))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def ClanSearchResultCount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(106))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def ClanMaxApplicant(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(108))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def ClanRejoinCoolTimeFromSecond(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(110))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def ClanWordBalloonMaxCharacter(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(112))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def CallNameRenameCoolTimeFromHour(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(114))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def CallNameMinimumLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(116))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def CallNameMaximumLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(118))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def LobbyToScreenModeWaitTime(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(120))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def ScreenshotToLobbyButtonHideDelay(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(122))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def PrologueScenarioID01(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(124))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def PrologueScenarioID02(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(126))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def TutorialHardStage11(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(128))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def TutorialSpeedButtonStage(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(130))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def TutorialCharacterDefaultCount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(132))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def TutorialShopCategoryType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(134))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def AdventureStrategyPlayTimeLimitInSeconds(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(136))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def WeekDungoenTacticPlayTimeLimitInSeconds(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(138))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def RaidTacticPlayTimeLimitInSeconds(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(140))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def RaidOpponentListAmount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(142))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def CraftBaseGoldRequired(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(144))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int64Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 8))
        return 0

    def CraftBaseGoldRequiredAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(144))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int64Flags, o)
        return 0

    def CraftBaseGoldRequiredLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(144))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    def CraftBaseGoldRequiredIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(144))
        return o == 0


    def PostExpiredDayAttendance(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(146))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def PostExpiredDayInventoryOverflow(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(148))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def PostExpiredDayGameManager(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(150))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def UILabelCharacterWrap(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(152))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def RequestTimeOut(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(154))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0


    def MailStorageSoftCap(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(156))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def MailStorageHardCap(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(158))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def ClearDeckStorageSize(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(160))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def ClearDeckNoStarViewCount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(162))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def ClearDeck1StarViewCount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(164))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def ClearDeck2StarViewCount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(166))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def ClearDeck3StarViewCount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(168))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def ExSkillLevelMax(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(170))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def PublicSkillLevelMax(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(172))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def PassiveSkillLevelMax(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(174))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def ExtraPassiveSkillLevelMax(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(176))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def AccountCommentMaxLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(178))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def CafeSummonCoolTimeFromHour(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(180))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def LimitedStageDailyClearCount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(182))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def LimitedStageEntryTimeLimit(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(184))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def LimitedStageEntryTimeBuffer(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(186))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def LimitedStagePointAmount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(188))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def LimitedStagePointPerApMin(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(190))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def LimitedStagePointPerApMax(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(192))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def AccountLinkReward(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(194))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def MonthlyProductCheckDays(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(196))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def WeaponLvUpCoefficient(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(198))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def ShowRaidMyListCount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(200))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def MaxLevelExpMasterCoinRatio(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(202))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def RaidEnterCostType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(204))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def RaidEnterCostId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(206))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def RaidTicketCost(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(208))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def TimeAttackDungeonScenarioId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(210))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def TimeAttackDungoenPlayCountPerTicket(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(212))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def TimeAttackDungeonEnterCostType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(214))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def TimeAttackDungeonEnterCostId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(216))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def TimeAttackDungeonEnterCost(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(218))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def ClanLeaderTransferLastLoginLimit(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(220))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def MonthlyProductRepurchasePopupLimit(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(222))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def CommonFavorItemTags(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(224))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int32Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return 0

    def CommonFavorItemTagsAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(224))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int32Flags, o)
        return 0

    def CommonFavorItemTagsLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(224))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    def CommonFavorItemTagsIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(224))
        return o == 0


    def MaxApMasterCoinPerWeek(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(226))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def CraftOpenExpTier1(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(228))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def CraftOpenExpTier2(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(230))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def CraftOpenExpTier3(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(232))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def CharacterEquipmentGearSlot(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(234))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def BirthDayDDay(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(236))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def RecommendedFriendsLvDifferenceLimit(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(238))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def DDosDetectCount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(240))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def DDosCheckIntervalInSeconds(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(242))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def MaxFriendsCount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(244))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def MaxFriendsRequest(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(246))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def FriendsSearchRequestCount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(248))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def FriendsMaxApplicant(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(250))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def IdCardDefaultCharacterId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(252))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def IdCardDefaultBgId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(254))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def WorldRaidGemEnterCost(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(256))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def WorldRaidGemEnterAmout(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(258))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def FriendIdCardCommentMaxLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(260))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def FormationPresetNumberOfEchelonTab(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(262))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def FormationPresetNumberOfEchelon(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(264))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def FormationPresetRecentNumberOfEchelon(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(266))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def FormationPresetEchelonTabTextLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(268))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def FormationPresetEchelonSlotTextLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(270))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def CharProfileRowIntervalKr(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(272))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def CharProfileRowIntervalJp(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(274))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def CharProfilePopupRowIntervalKr(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(276))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def CharProfilePopupRowIntervalJp(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(278))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def BeforehandGachaCount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(280))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def BeforehandGachaGroupId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(282))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def RenewalDisplayOrderDay(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(284))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def EmblemDefaultId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(286))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def BirthdayMailStartDate(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(288))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def BirthdayMailRemainDate(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(290))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def BirthdayMailParcelType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(292))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def BirthdayMailParcelId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(294))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def BirthdayMailParcelAmount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(296))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def ClearDeckAverageDeckCount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(298))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def ClearDeckWorldRaidSaveConditionCoefficient(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(300))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def ClearDeckShowCount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(302))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def CharacterMaxLevel(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(304))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def PotentialBonusStatMaxLevelMaxHP(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(306))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def PotentialBonusStatMaxLevelAttackPower(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(308))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def PotentialBonusStatMaxLevelHealPower(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(310))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def PotentialOpenConditionCharacterLevel(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(312))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def AssistStrangerMinLevel(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(314))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def AssistStrangerMaxLevel(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(316))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def MaxBlockedUserCount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(318))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def CafeRandomVisitMinComfortBonus(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(320))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def CafeRandomVisitMinLastLogin(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(322))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def CafeTravelSyncIntervalByMillisec(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(324))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0




    @staticmethod
    def Start(builder): builder.StartObject(161)
    @staticmethod
    def End(builder): return builder.EndObject()


    @staticmethod
    def AddCampaignMainStageMaxRank(builder, CampaignMainStageMaxRank): builder.PrependInt32Slot(0, CampaignMainStageMaxRank, 0)


    @staticmethod
    def AddCampaignMainStageBestRecord(builder, CampaignMainStageBestRecord): builder.PrependInt32Slot(1, CampaignMainStageBestRecord, 0)


    @staticmethod
    def AddHardAdventurePlayCountRecoverDailyNumber(builder, HardAdventurePlayCountRecoverDailyNumber): builder.PrependInt32Slot(2, HardAdventurePlayCountRecoverDailyNumber, 0)


    @staticmethod
    def AddHardStageCount(builder, HardStageCount): builder.PrependInt32Slot(3, HardStageCount, 0)


    @staticmethod
    def AddTacticRankClearTime(builder, TacticRankClearTime): builder.PrependInt32Slot(4, TacticRankClearTime, 0)


    @staticmethod
    def AddBaseTimeScale(builder, BaseTimeScale): builder.PrependInt64Slot(5, BaseTimeScale, 0)


    @staticmethod
    def AddGachaPercentage(builder, GachaPercentage): builder.PrependInt32Slot(6, GachaPercentage, 0)


    @staticmethod
    def AddAcademyFavorZoneId(builder, AcademyFavorZoneId): builder.PrependInt64Slot(7, AcademyFavorZoneId, 0)


    @staticmethod
    def AddCafePresetSlotCount(builder, CafePresetSlotCount): builder.PrependInt32Slot(8, CafePresetSlotCount, 0)


    @staticmethod
    def AddCafeMonologueIntervalMillisec(builder, CafeMonologueIntervalMillisec): builder.PrependInt64Slot(9, CafeMonologueIntervalMillisec, 0)


    @staticmethod
    def AddCafeMonologueDefaultDuration(builder, CafeMonologueDefaultDuration): builder.PrependInt64Slot(10, CafeMonologueDefaultDuration, 0)


    @staticmethod
    def AddCafeBubbleIdleDurationMilliSec(builder, CafeBubbleIdleDurationMilliSec): builder.PrependInt64Slot(11, CafeBubbleIdleDurationMilliSec, 0)


    @staticmethod
    def AddFindGiftTimeLimit(builder, FindGiftTimeLimit): builder.PrependInt32Slot(12, FindGiftTimeLimit, 0)


    @staticmethod
    def AddCafeAutoChargePeriodInMsc(builder, CafeAutoChargePeriodInMsc): builder.PrependInt32Slot(13, CafeAutoChargePeriodInMsc, 0)


    @staticmethod
    def AddCafeProductionDecimalPosition(builder, CafeProductionDecimalPosition): builder.PrependInt32Slot(14, CafeProductionDecimalPosition, 0)


    @staticmethod
    def AddCafeSetGroupApplyCount(builder, CafeSetGroupApplyCount): builder.PrependInt32Slot(15, CafeSetGroupApplyCount, 0)


    @staticmethod
    def AddWeekDungeonFindGiftRewardLimitCount(builder, WeekDungeonFindGiftRewardLimitCount): builder.PrependInt32Slot(16, WeekDungeonFindGiftRewardLimitCount, 0)


    @staticmethod
    def AddStageFailedCurrencyRefundRate(builder, StageFailedCurrencyRefundRate): builder.PrependInt32Slot(17, StageFailedCurrencyRefundRate, 0)


    @staticmethod
    def AddEnterDeposit(builder, EnterDeposit): builder.PrependInt32Slot(18, EnterDeposit, 0)


    @staticmethod
    def AddAccountMaxLevel(builder, AccountMaxLevel): builder.PrependInt32Slot(19, AccountMaxLevel, 0)


    @staticmethod
    def AddMainSquadExpBonus(builder, MainSquadExpBonus): builder.PrependInt32Slot(20, MainSquadExpBonus, 0)


    @staticmethod
    def AddSupportSquadExpBonus(builder, SupportSquadExpBonus): builder.PrependInt32Slot(21, SupportSquadExpBonus, 0)


    @staticmethod
    def AddAccountExpRatio(builder, AccountExpRatio): builder.PrependInt32Slot(22, AccountExpRatio, 0)


    @staticmethod
    def AddMissionToastLifeTime(builder, MissionToastLifeTime): builder.PrependInt32Slot(23, MissionToastLifeTime, 0)


    @staticmethod
    def AddExpItemInsertLimit(builder, ExpItemInsertLimit): builder.PrependInt32Slot(24, ExpItemInsertLimit, 0)


    @staticmethod
    def AddExpItemInsertAccelTime(builder, ExpItemInsertAccelTime): builder.PrependInt32Slot(25, ExpItemInsertAccelTime, 0)


    @staticmethod
    def AddCharacterLvUpCoefficient(builder, CharacterLvUpCoefficient): builder.PrependInt32Slot(26, CharacterLvUpCoefficient, 0)


    @staticmethod
    def AddEquipmentLvUpCoefficient(builder, EquipmentLvUpCoefficient): builder.PrependInt32Slot(27, EquipmentLvUpCoefficient, 0)


    @staticmethod
    def AddExpEquipInsertLimit(builder, ExpEquipInsertLimit): builder.PrependInt32Slot(28, ExpEquipInsertLimit, 0)


    @staticmethod
    def AddEquipLvUpCoefficient(builder, EquipLvUpCoefficient): builder.PrependInt32Slot(29, EquipLvUpCoefficient, 0)


    @staticmethod
    def AddNicknameLength(builder, NicknameLength): builder.PrependInt32Slot(30, NicknameLength, 0)


    @staticmethod
    def AddCraftDuration(builder, CraftDuration): builder.PrependUOffsetTRelativeSlot(31, flatbuffers.number_types.UOffsetTFlags.py_type(CraftDuration), 0)
    @staticmethod
    def StartCraftDurationVector(builder, numElems): return builder.StartVector(4, numElems, 4)


    @staticmethod
    def AddCraftLimitTime(builder, CraftLimitTime): builder.PrependInt32Slot(32, CraftLimitTime, 0)


    @staticmethod
    def AddShiftingCraftDuration(builder, ShiftingCraftDuration): builder.PrependUOffsetTRelativeSlot(33, flatbuffers.number_types.UOffsetTFlags.py_type(ShiftingCraftDuration), 0)
    @staticmethod
    def StartShiftingCraftDurationVector(builder, numElems): return builder.StartVector(4, numElems, 4)


    @staticmethod
    def AddShiftingCraftTicketConsumeAmount(builder, ShiftingCraftTicketConsumeAmount): builder.PrependInt32Slot(34, ShiftingCraftTicketConsumeAmount, 0)


    @staticmethod
    def AddShiftingCraftSlotMaxCapacity(builder, ShiftingCraftSlotMaxCapacity): builder.PrependInt32Slot(35, ShiftingCraftSlotMaxCapacity, 0)


    @staticmethod
    def AddCraftTicketItemUniqueId(builder, CraftTicketItemUniqueId): builder.PrependInt32Slot(36, CraftTicketItemUniqueId, 0)


    @staticmethod
    def AddCraftTicketConsumeAmount(builder, CraftTicketConsumeAmount): builder.PrependInt32Slot(37, CraftTicketConsumeAmount, 0)


    @staticmethod
    def AddAcademyEnterCostType(builder, AcademyEnterCostType): builder.PrependInt32Slot(38, AcademyEnterCostType, 0)


    @staticmethod
    def AddAcademyEnterCostId(builder, AcademyEnterCostId): builder.PrependInt64Slot(39, AcademyEnterCostId, 0)


    @staticmethod
    def AddAcademyTicketCost(builder, AcademyTicketCost): builder.PrependInt32Slot(40, AcademyTicketCost, 0)


    @staticmethod
    def AddMassangerMessageExpireDay(builder, MassangerMessageExpireDay): builder.PrependInt32Slot(41, MassangerMessageExpireDay, 0)


    @staticmethod
    def AddCraftLeafNodeGenerateLv1Count(builder, CraftLeafNodeGenerateLv1Count): builder.PrependInt32Slot(42, CraftLeafNodeGenerateLv1Count, 0)


    @staticmethod
    def AddCraftLeafNodeGenerateLv2Count(builder, CraftLeafNodeGenerateLv2Count): builder.PrependInt32Slot(43, CraftLeafNodeGenerateLv2Count, 0)


    @staticmethod
    def AddTutorialGachaShopId(builder, TutorialGachaShopId): builder.PrependInt32Slot(44, TutorialGachaShopId, 0)


    @staticmethod
    def AddBeforehandGachaShopId(builder, BeforehandGachaShopId): builder.PrependInt32Slot(45, BeforehandGachaShopId, 0)


    @staticmethod
    def AddTutorialGachaGoodsId(builder, TutorialGachaGoodsId): builder.PrependInt32Slot(46, TutorialGachaGoodsId, 0)


    @staticmethod
    def AddEquipmentSlotOpenLevel(builder, EquipmentSlotOpenLevel): builder.PrependUOffsetTRelativeSlot(47, flatbuffers.number_types.UOffsetTFlags.py_type(EquipmentSlotOpenLevel), 0)
    @staticmethod
    def StartEquipmentSlotOpenLevelVector(builder, numElems): return builder.StartVector(4, numElems, 4)


    @staticmethod
    def AddScenarioAutoDelayMillisec(builder, ScenarioAutoDelayMillisec): builder.PrependFloat32Slot(48, ScenarioAutoDelayMillisec, 0)


    @staticmethod
    def AddJoinOrCreateClanCoolTimeFromHour(builder, JoinOrCreateClanCoolTimeFromHour): builder.PrependInt64Slot(49, JoinOrCreateClanCoolTimeFromHour, 0)


    @staticmethod
    def AddClanMaxMember(builder, ClanMaxMember): builder.PrependInt64Slot(50, ClanMaxMember, 0)


    @staticmethod
    def AddClanSearchResultCount(builder, ClanSearchResultCount): builder.PrependInt64Slot(51, ClanSearchResultCount, 0)


    @staticmethod
    def AddClanMaxApplicant(builder, ClanMaxApplicant): builder.PrependInt64Slot(52, ClanMaxApplicant, 0)


    @staticmethod
    def AddClanRejoinCoolTimeFromSecond(builder, ClanRejoinCoolTimeFromSecond): builder.PrependInt64Slot(53, ClanRejoinCoolTimeFromSecond, 0)


    @staticmethod
    def AddClanWordBalloonMaxCharacter(builder, ClanWordBalloonMaxCharacter): builder.PrependInt32Slot(54, ClanWordBalloonMaxCharacter, 0)


    @staticmethod
    def AddCallNameRenameCoolTimeFromHour(builder, CallNameRenameCoolTimeFromHour): builder.PrependInt64Slot(55, CallNameRenameCoolTimeFromHour, 0)


    @staticmethod
    def AddCallNameMinimumLength(builder, CallNameMinimumLength): builder.PrependInt64Slot(56, CallNameMinimumLength, 0)


    @staticmethod
    def AddCallNameMaximumLength(builder, CallNameMaximumLength): builder.PrependInt64Slot(57, CallNameMaximumLength, 0)


    @staticmethod
    def AddLobbyToScreenModeWaitTime(builder, LobbyToScreenModeWaitTime): builder.PrependInt64Slot(58, LobbyToScreenModeWaitTime, 0)


    @staticmethod
    def AddScreenshotToLobbyButtonHideDelay(builder, ScreenshotToLobbyButtonHideDelay): builder.PrependInt64Slot(59, ScreenshotToLobbyButtonHideDelay, 0)


    @staticmethod
    def AddPrologueScenarioID01(builder, PrologueScenarioID01): builder.PrependInt64Slot(60, PrologueScenarioID01, 0)


    @staticmethod
    def AddPrologueScenarioID02(builder, PrologueScenarioID02): builder.PrependInt64Slot(61, PrologueScenarioID02, 0)


    @staticmethod
    def AddTutorialHardStage11(builder, TutorialHardStage11): builder.PrependInt64Slot(62, TutorialHardStage11, 0)


    @staticmethod
    def AddTutorialSpeedButtonStage(builder, TutorialSpeedButtonStage): builder.PrependInt64Slot(63, TutorialSpeedButtonStage, 0)


    @staticmethod
    def AddTutorialCharacterDefaultCount(builder, TutorialCharacterDefaultCount): builder.PrependInt64Slot(64, TutorialCharacterDefaultCount, 0)


    @staticmethod
    def AddTutorialShopCategoryType(builder, TutorialShopCategoryType): builder.PrependInt32Slot(65, TutorialShopCategoryType, 0)


    @staticmethod
    def AddAdventureStrategyPlayTimeLimitInSeconds(builder, AdventureStrategyPlayTimeLimitInSeconds): builder.PrependInt64Slot(66, AdventureStrategyPlayTimeLimitInSeconds, 0)


    @staticmethod
    def AddWeekDungoenTacticPlayTimeLimitInSeconds(builder, WeekDungoenTacticPlayTimeLimitInSeconds): builder.PrependInt64Slot(67, WeekDungoenTacticPlayTimeLimitInSeconds, 0)


    @staticmethod
    def AddRaidTacticPlayTimeLimitInSeconds(builder, RaidTacticPlayTimeLimitInSeconds): builder.PrependInt64Slot(68, RaidTacticPlayTimeLimitInSeconds, 0)


    @staticmethod
    def AddRaidOpponentListAmount(builder, RaidOpponentListAmount): builder.PrependInt64Slot(69, RaidOpponentListAmount, 0)


    @staticmethod
    def AddCraftBaseGoldRequired(builder, CraftBaseGoldRequired): builder.PrependUOffsetTRelativeSlot(70, flatbuffers.number_types.UOffsetTFlags.py_type(CraftBaseGoldRequired), 0)
    @staticmethod
    def StartCraftBaseGoldRequiredVector(builder, numElems): return builder.StartVector(8, numElems, 8)


    @staticmethod
    def AddPostExpiredDayAttendance(builder, PostExpiredDayAttendance): builder.PrependInt32Slot(71, PostExpiredDayAttendance, 0)


    @staticmethod
    def AddPostExpiredDayInventoryOverflow(builder, PostExpiredDayInventoryOverflow): builder.PrependInt32Slot(72, PostExpiredDayInventoryOverflow, 0)


    @staticmethod
    def AddPostExpiredDayGameManager(builder, PostExpiredDayGameManager): builder.PrependInt32Slot(73, PostExpiredDayGameManager, 0)


    @staticmethod
    def AddUILabelCharacterWrap(builder, UILabelCharacterWrap): builder.PrependUOffsetTRelativeSlot(74, flatbuffers.number_types.UOffsetTFlags.py_type(UILabelCharacterWrap), 0)

    @staticmethod
    def AddRequestTimeOut(builder, RequestTimeOut): builder.PrependFloat32Slot(75, RequestTimeOut, 0)


    @staticmethod
    def AddMailStorageSoftCap(builder, MailStorageSoftCap): builder.PrependInt32Slot(76, MailStorageSoftCap, 0)


    @staticmethod
    def AddMailStorageHardCap(builder, MailStorageHardCap): builder.PrependInt32Slot(77, MailStorageHardCap, 0)


    @staticmethod
    def AddClearDeckStorageSize(builder, ClearDeckStorageSize): builder.PrependInt32Slot(78, ClearDeckStorageSize, 0)


    @staticmethod
    def AddClearDeckNoStarViewCount(builder, ClearDeckNoStarViewCount): builder.PrependInt32Slot(79, ClearDeckNoStarViewCount, 0)


    @staticmethod
    def AddClearDeck1StarViewCount(builder, ClearDeck1StarViewCount): builder.PrependInt32Slot(80, ClearDeck1StarViewCount, 0)


    @staticmethod
    def AddClearDeck2StarViewCount(builder, ClearDeck2StarViewCount): builder.PrependInt32Slot(81, ClearDeck2StarViewCount, 0)


    @staticmethod
    def AddClearDeck3StarViewCount(builder, ClearDeck3StarViewCount): builder.PrependInt32Slot(82, ClearDeck3StarViewCount, 0)


    @staticmethod
    def AddExSkillLevelMax(builder, ExSkillLevelMax): builder.PrependInt32Slot(83, ExSkillLevelMax, 0)


    @staticmethod
    def AddPublicSkillLevelMax(builder, PublicSkillLevelMax): builder.PrependInt32Slot(84, PublicSkillLevelMax, 0)


    @staticmethod
    def AddPassiveSkillLevelMax(builder, PassiveSkillLevelMax): builder.PrependInt32Slot(85, PassiveSkillLevelMax, 0)


    @staticmethod
    def AddExtraPassiveSkillLevelMax(builder, ExtraPassiveSkillLevelMax): builder.PrependInt32Slot(86, ExtraPassiveSkillLevelMax, 0)


    @staticmethod
    def AddAccountCommentMaxLength(builder, AccountCommentMaxLength): builder.PrependInt32Slot(87, AccountCommentMaxLength, 0)


    @staticmethod
    def AddCafeSummonCoolTimeFromHour(builder, CafeSummonCoolTimeFromHour): builder.PrependInt32Slot(88, CafeSummonCoolTimeFromHour, 0)


    @staticmethod
    def AddLimitedStageDailyClearCount(builder, LimitedStageDailyClearCount): builder.PrependInt64Slot(89, LimitedStageDailyClearCount, 0)


    @staticmethod
    def AddLimitedStageEntryTimeLimit(builder, LimitedStageEntryTimeLimit): builder.PrependInt64Slot(90, LimitedStageEntryTimeLimit, 0)


    @staticmethod
    def AddLimitedStageEntryTimeBuffer(builder, LimitedStageEntryTimeBuffer): builder.PrependInt64Slot(91, LimitedStageEntryTimeBuffer, 0)


    @staticmethod
    def AddLimitedStagePointAmount(builder, LimitedStagePointAmount): builder.PrependInt64Slot(92, LimitedStagePointAmount, 0)


    @staticmethod
    def AddLimitedStagePointPerApMin(builder, LimitedStagePointPerApMin): builder.PrependInt64Slot(93, LimitedStagePointPerApMin, 0)


    @staticmethod
    def AddLimitedStagePointPerApMax(builder, LimitedStagePointPerApMax): builder.PrependInt64Slot(94, LimitedStagePointPerApMax, 0)


    @staticmethod
    def AddAccountLinkReward(builder, AccountLinkReward): builder.PrependInt32Slot(95, AccountLinkReward, 0)


    @staticmethod
    def AddMonthlyProductCheckDays(builder, MonthlyProductCheckDays): builder.PrependInt32Slot(96, MonthlyProductCheckDays, 0)


    @staticmethod
    def AddWeaponLvUpCoefficient(builder, WeaponLvUpCoefficient): builder.PrependInt32Slot(97, WeaponLvUpCoefficient, 0)


    @staticmethod
    def AddShowRaidMyListCount(builder, ShowRaidMyListCount): builder.PrependInt32Slot(98, ShowRaidMyListCount, 0)


    @staticmethod
    def AddMaxLevelExpMasterCoinRatio(builder, MaxLevelExpMasterCoinRatio): builder.PrependInt32Slot(99, MaxLevelExpMasterCoinRatio, 0)


    @staticmethod
    def AddRaidEnterCostType(builder, RaidEnterCostType): builder.PrependInt32Slot(100, RaidEnterCostType, 0)


    @staticmethod
    def AddRaidEnterCostId(builder, RaidEnterCostId): builder.PrependInt64Slot(101, RaidEnterCostId, 0)


    @staticmethod
    def AddRaidTicketCost(builder, RaidTicketCost): builder.PrependInt64Slot(102, RaidTicketCost, 0)


    @staticmethod
    def AddTimeAttackDungeonScenarioId(builder, TimeAttackDungeonScenarioId): builder.PrependUOffsetTRelativeSlot(103, flatbuffers.number_types.UOffsetTFlags.py_type(TimeAttackDungeonScenarioId), 0)

    @staticmethod
    def AddTimeAttackDungoenPlayCountPerTicket(builder, TimeAttackDungoenPlayCountPerTicket): builder.PrependInt32Slot(104, TimeAttackDungoenPlayCountPerTicket, 0)


    @staticmethod
    def AddTimeAttackDungeonEnterCostType(builder, TimeAttackDungeonEnterCostType): builder.PrependInt32Slot(105, TimeAttackDungeonEnterCostType, 0)


    @staticmethod
    def AddTimeAttackDungeonEnterCostId(builder, TimeAttackDungeonEnterCostId): builder.PrependInt64Slot(106, TimeAttackDungeonEnterCostId, 0)


    @staticmethod
    def AddTimeAttackDungeonEnterCost(builder, TimeAttackDungeonEnterCost): builder.PrependInt64Slot(107, TimeAttackDungeonEnterCost, 0)


    @staticmethod
    def AddClanLeaderTransferLastLoginLimit(builder, ClanLeaderTransferLastLoginLimit): builder.PrependInt64Slot(108, ClanLeaderTransferLastLoginLimit, 0)


    @staticmethod
    def AddMonthlyProductRepurchasePopupLimit(builder, MonthlyProductRepurchasePopupLimit): builder.PrependInt32Slot(109, MonthlyProductRepurchasePopupLimit, 0)


    @staticmethod
    def AddCommonFavorItemTags(builder, CommonFavorItemTags): builder.PrependUOffsetTRelativeSlot(110, flatbuffers.number_types.UOffsetTFlags.py_type(CommonFavorItemTags), 0)
    @staticmethod
    def StartCommonFavorItemTagsVector(builder, numElems): return builder.StartVector(4, numElems, 4)


    @staticmethod
    def AddMaxApMasterCoinPerWeek(builder, MaxApMasterCoinPerWeek): builder.PrependInt64Slot(111, MaxApMasterCoinPerWeek, 0)


    @staticmethod
    def AddCraftOpenExpTier1(builder, CraftOpenExpTier1): builder.PrependInt64Slot(112, CraftOpenExpTier1, 0)


    @staticmethod
    def AddCraftOpenExpTier2(builder, CraftOpenExpTier2): builder.PrependInt64Slot(113, CraftOpenExpTier2, 0)


    @staticmethod
    def AddCraftOpenExpTier3(builder, CraftOpenExpTier3): builder.PrependInt64Slot(114, CraftOpenExpTier3, 0)


    @staticmethod
    def AddCharacterEquipmentGearSlot(builder, CharacterEquipmentGearSlot): builder.PrependInt64Slot(115, CharacterEquipmentGearSlot, 0)


    @staticmethod
    def AddBirthDayDDay(builder, BirthDayDDay): builder.PrependInt32Slot(116, BirthDayDDay, 0)


    @staticmethod
    def AddRecommendedFriendsLvDifferenceLimit(builder, RecommendedFriendsLvDifferenceLimit): builder.PrependInt32Slot(117, RecommendedFriendsLvDifferenceLimit, 0)


    @staticmethod
    def AddDDosDetectCount(builder, DDosDetectCount): builder.PrependInt32Slot(118, DDosDetectCount, 0)


    @staticmethod
    def AddDDosCheckIntervalInSeconds(builder, DDosCheckIntervalInSeconds): builder.PrependInt32Slot(119, DDosCheckIntervalInSeconds, 0)


    @staticmethod
    def AddMaxFriendsCount(builder, MaxFriendsCount): builder.PrependInt32Slot(120, MaxFriendsCount, 0)


    @staticmethod
    def AddMaxFriendsRequest(builder, MaxFriendsRequest): builder.PrependInt32Slot(121, MaxFriendsRequest, 0)


    @staticmethod
    def AddFriendsSearchRequestCount(builder, FriendsSearchRequestCount): builder.PrependInt32Slot(122, FriendsSearchRequestCount, 0)


    @staticmethod
    def AddFriendsMaxApplicant(builder, FriendsMaxApplicant): builder.PrependInt32Slot(123, FriendsMaxApplicant, 0)


    @staticmethod
    def AddIdCardDefaultCharacterId(builder, IdCardDefaultCharacterId): builder.PrependInt64Slot(124, IdCardDefaultCharacterId, 0)


    @staticmethod
    def AddIdCardDefaultBgId(builder, IdCardDefaultBgId): builder.PrependInt64Slot(125, IdCardDefaultBgId, 0)


    @staticmethod
    def AddWorldRaidGemEnterCost(builder, WorldRaidGemEnterCost): builder.PrependInt64Slot(126, WorldRaidGemEnterCost, 0)


    @staticmethod
    def AddWorldRaidGemEnterAmout(builder, WorldRaidGemEnterAmout): builder.PrependInt64Slot(127, WorldRaidGemEnterAmout, 0)


    @staticmethod
    def AddFriendIdCardCommentMaxLength(builder, FriendIdCardCommentMaxLength): builder.PrependInt64Slot(128, FriendIdCardCommentMaxLength, 0)


    @staticmethod
    def AddFormationPresetNumberOfEchelonTab(builder, FormationPresetNumberOfEchelonTab): builder.PrependInt32Slot(129, FormationPresetNumberOfEchelonTab, 0)


    @staticmethod
    def AddFormationPresetNumberOfEchelon(builder, FormationPresetNumberOfEchelon): builder.PrependInt32Slot(130, FormationPresetNumberOfEchelon, 0)


    @staticmethod
    def AddFormationPresetRecentNumberOfEchelon(builder, FormationPresetRecentNumberOfEchelon): builder.PrependInt32Slot(131, FormationPresetRecentNumberOfEchelon, 0)


    @staticmethod
    def AddFormationPresetEchelonTabTextLength(builder, FormationPresetEchelonTabTextLength): builder.PrependInt32Slot(132, FormationPresetEchelonTabTextLength, 0)


    @staticmethod
    def AddFormationPresetEchelonSlotTextLength(builder, FormationPresetEchelonSlotTextLength): builder.PrependInt32Slot(133, FormationPresetEchelonSlotTextLength, 0)


    @staticmethod
    def AddCharProfileRowIntervalKr(builder, CharProfileRowIntervalKr): builder.PrependInt32Slot(134, CharProfileRowIntervalKr, 0)


    @staticmethod
    def AddCharProfileRowIntervalJp(builder, CharProfileRowIntervalJp): builder.PrependInt32Slot(135, CharProfileRowIntervalJp, 0)


    @staticmethod
    def AddCharProfilePopupRowIntervalKr(builder, CharProfilePopupRowIntervalKr): builder.PrependInt32Slot(136, CharProfilePopupRowIntervalKr, 0)


    @staticmethod
    def AddCharProfilePopupRowIntervalJp(builder, CharProfilePopupRowIntervalJp): builder.PrependInt32Slot(137, CharProfilePopupRowIntervalJp, 0)


    @staticmethod
    def AddBeforehandGachaCount(builder, BeforehandGachaCount): builder.PrependInt32Slot(138, BeforehandGachaCount, 0)


    @staticmethod
    def AddBeforehandGachaGroupId(builder, BeforehandGachaGroupId): builder.PrependInt32Slot(139, BeforehandGachaGroupId, 0)


    @staticmethod
    def AddRenewalDisplayOrderDay(builder, RenewalDisplayOrderDay): builder.PrependInt32Slot(140, RenewalDisplayOrderDay, 0)


    @staticmethod
    def AddEmblemDefaultId(builder, EmblemDefaultId): builder.PrependInt64Slot(141, EmblemDefaultId, 0)


    @staticmethod
    def AddBirthdayMailStartDate(builder, BirthdayMailStartDate): builder.PrependUOffsetTRelativeSlot(142, flatbuffers.number_types.UOffsetTFlags.py_type(BirthdayMailStartDate), 0)

    @staticmethod
    def AddBirthdayMailRemainDate(builder, BirthdayMailRemainDate): builder.PrependInt32Slot(143, BirthdayMailRemainDate, 0)


    @staticmethod
    def AddBirthdayMailParcelType(builder, BirthdayMailParcelType): builder.PrependInt32Slot(144, BirthdayMailParcelType, 0)


    @staticmethod
    def AddBirthdayMailParcelId(builder, BirthdayMailParcelId): builder.PrependInt64Slot(145, BirthdayMailParcelId, 0)


    @staticmethod
    def AddBirthdayMailParcelAmount(builder, BirthdayMailParcelAmount): builder.PrependInt32Slot(146, BirthdayMailParcelAmount, 0)


    @staticmethod
    def AddClearDeckAverageDeckCount(builder, ClearDeckAverageDeckCount): builder.PrependInt32Slot(147, ClearDeckAverageDeckCount, 0)


    @staticmethod
    def AddClearDeckWorldRaidSaveConditionCoefficient(builder, ClearDeckWorldRaidSaveConditionCoefficient): builder.PrependInt32Slot(148, ClearDeckWorldRaidSaveConditionCoefficient, 0)


    @staticmethod
    def AddClearDeckShowCount(builder, ClearDeckShowCount): builder.PrependInt32Slot(149, ClearDeckShowCount, 0)


    @staticmethod
    def AddCharacterMaxLevel(builder, CharacterMaxLevel): builder.PrependInt32Slot(150, CharacterMaxLevel, 0)


    @staticmethod
    def AddPotentialBonusStatMaxLevelMaxHP(builder, PotentialBonusStatMaxLevelMaxHP): builder.PrependInt32Slot(151, PotentialBonusStatMaxLevelMaxHP, 0)


    @staticmethod
    def AddPotentialBonusStatMaxLevelAttackPower(builder, PotentialBonusStatMaxLevelAttackPower): builder.PrependInt32Slot(152, PotentialBonusStatMaxLevelAttackPower, 0)


    @staticmethod
    def AddPotentialBonusStatMaxLevelHealPower(builder, PotentialBonusStatMaxLevelHealPower): builder.PrependInt32Slot(153, PotentialBonusStatMaxLevelHealPower, 0)


    @staticmethod
    def AddPotentialOpenConditionCharacterLevel(builder, PotentialOpenConditionCharacterLevel): builder.PrependInt32Slot(154, PotentialOpenConditionCharacterLevel, 0)


    @staticmethod
    def AddAssistStrangerMinLevel(builder, AssistStrangerMinLevel): builder.PrependInt32Slot(155, AssistStrangerMinLevel, 0)


    @staticmethod
    def AddAssistStrangerMaxLevel(builder, AssistStrangerMaxLevel): builder.PrependInt32Slot(156, AssistStrangerMaxLevel, 0)


    @staticmethod
    def AddMaxBlockedUserCount(builder, MaxBlockedUserCount): builder.PrependInt32Slot(157, MaxBlockedUserCount, 0)


    @staticmethod
    def AddCafeRandomVisitMinComfortBonus(builder, CafeRandomVisitMinComfortBonus): builder.PrependInt64Slot(158, CafeRandomVisitMinComfortBonus, 0)


    @staticmethod
    def AddCafeRandomVisitMinLastLogin(builder, CafeRandomVisitMinLastLogin): builder.PrependInt32Slot(159, CafeRandomVisitMinLastLogin, 0)


    @staticmethod
    def AddCafeTravelSyncIntervalByMillisec(builder, CafeTravelSyncIntervalByMillisec): builder.PrependInt32Slot(160, CafeTravelSyncIntervalByMillisec, 0)

