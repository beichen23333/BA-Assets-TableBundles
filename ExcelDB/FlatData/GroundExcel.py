
import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class GroundExcel:
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = GroundExcel()
        x.Init(buf, n + offset)
        return x

    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)


    def Id(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def StageFileName(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.String(a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return ""

    def StageFileNameLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    def StageFileNameIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        return o == 0


    def GroundSceneName(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def FormationGroupId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def StageTopography(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def EnemyBulletType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def EnemyArmorType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def LevelNPC(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def LevelMinion(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def LevelElite(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def LevelChampion(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def LevelBoss(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def ObstacleLevel(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(28))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def GradeNPC(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(30))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def GradeMinion(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(32))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def GradeElite(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(34))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def GradeChampion(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(36))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def GradeBoss(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(38))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def PlayerSightPointAdd(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(40))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def PlayerSightPointRate(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(42))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def PlayerAttackRangeAdd(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(44))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def PlayerAttackRangeRate(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(46))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def EnemySightPointAdd(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(48))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def EnemySightPointRate(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(50))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def EnemyAttackRangeAdd(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(52))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def EnemyAttackRangeRate(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(54))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def PlayerSkillRangeAdd(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(56))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def PlayerSkillRangeRate(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(58))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def EnemySkillRangeAdd(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(60))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def EnemySkillRangeRate(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(62))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def PlayerMinimumPositionGapRate(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(64))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def EnemyMinimumPositionGapRate(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(66))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def PlayerSightRangeMax(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(68))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0


    def EnemySightRangeMax(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(70))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0


    def TSSAirUnitHeight(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(72))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def IsPhaseBGM(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(74))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0


    def BGMId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(76))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def WarningUI(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(78))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0


    def TSSHatchOpen(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(80))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0


    def ForcedTacticSpeed(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(82))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def ForcedSkillUse(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(84))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def ShowNPCSkillCutIn(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(86))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def ImmuneHitBeforeTimeOutEnd(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(88))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0


    def UIBattleHideFromScratch(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(90))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0


    def BattleReadyTimelinePath(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(92))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def BeforeVictoryTimelinePath(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(94))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def SkipBattleEnd(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(96))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0


    def HideNPCWhenBattleEnd(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(98))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0


    def CoverPointOff(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(100))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0


    def UIHpScale(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(102))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0


    def UIEmojiScale(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(104))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0


    def UISkillMainLogScale(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(106))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0


    def EffectCountLimit(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(108))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def AllyPassiveSkillId(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(110))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.String(a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return ""

    def AllyPassiveSkillIdLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(110))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    def AllyPassiveSkillIdIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(110))
        return o == 0


    def AllyPassiveSkillLevel(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(112))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int32Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return 0

    def AllyPassiveSkillLevelAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(112))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int32Flags, o)
        return 0

    def AllyPassiveSkillLevelLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(112))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    def AllyPassiveSkillLevelIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(112))
        return o == 0


    def EnemyPassiveSkillId(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(114))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.String(a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return ""

    def EnemyPassiveSkillIdLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(114))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    def EnemyPassiveSkillIdIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(114))
        return o == 0


    def EnemyPassiveSkillLevel(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(116))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int32Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return 0

    def EnemyPassiveSkillLevelAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(116))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int32Flags, o)
        return 0

    def EnemyPassiveSkillLevelLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(116))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    def EnemyPassiveSkillLevelIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(116))
        return o == 0




    @staticmethod
    def Start(builder): builder.StartObject(57)
    @staticmethod
    def End(builder): return builder.EndObject()


    @staticmethod
    def AddId(builder, Id): builder.PrependInt64Slot(0, Id, 0)


    @staticmethod
    def AddStageFileName(builder, StageFileName): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(StageFileName), 0)
    @staticmethod
    def StartStageFileNameVector(builder, numElems): return builder.StartVector(4, numElems, 4)


    @staticmethod
    def AddGroundSceneName(builder, GroundSceneName): builder.PrependUOffsetTRelativeSlot(2, flatbuffers.number_types.UOffsetTFlags.py_type(GroundSceneName), 0)

    @staticmethod
    def AddFormationGroupId(builder, FormationGroupId): builder.PrependInt64Slot(3, FormationGroupId, 0)


    @staticmethod
    def AddStageTopography(builder, StageTopography): builder.PrependInt32Slot(4, StageTopography, 0)


    @staticmethod
    def AddEnemyBulletType(builder, EnemyBulletType): builder.PrependInt32Slot(5, EnemyBulletType, 0)


    @staticmethod
    def AddEnemyArmorType(builder, EnemyArmorType): builder.PrependInt32Slot(6, EnemyArmorType, 0)


    @staticmethod
    def AddLevelNPC(builder, LevelNPC): builder.PrependInt64Slot(7, LevelNPC, 0)


    @staticmethod
    def AddLevelMinion(builder, LevelMinion): builder.PrependInt64Slot(8, LevelMinion, 0)


    @staticmethod
    def AddLevelElite(builder, LevelElite): builder.PrependInt64Slot(9, LevelElite, 0)


    @staticmethod
    def AddLevelChampion(builder, LevelChampion): builder.PrependInt64Slot(10, LevelChampion, 0)


    @staticmethod
    def AddLevelBoss(builder, LevelBoss): builder.PrependInt64Slot(11, LevelBoss, 0)


    @staticmethod
    def AddObstacleLevel(builder, ObstacleLevel): builder.PrependInt64Slot(12, ObstacleLevel, 0)


    @staticmethod
    def AddGradeNPC(builder, GradeNPC): builder.PrependInt64Slot(13, GradeNPC, 0)


    @staticmethod
    def AddGradeMinion(builder, GradeMinion): builder.PrependInt64Slot(14, GradeMinion, 0)


    @staticmethod
    def AddGradeElite(builder, GradeElite): builder.PrependInt64Slot(15, GradeElite, 0)


    @staticmethod
    def AddGradeChampion(builder, GradeChampion): builder.PrependInt64Slot(16, GradeChampion, 0)


    @staticmethod
    def AddGradeBoss(builder, GradeBoss): builder.PrependInt64Slot(17, GradeBoss, 0)


    @staticmethod
    def AddPlayerSightPointAdd(builder, PlayerSightPointAdd): builder.PrependInt64Slot(18, PlayerSightPointAdd, 0)


    @staticmethod
    def AddPlayerSightPointRate(builder, PlayerSightPointRate): builder.PrependInt64Slot(19, PlayerSightPointRate, 0)


    @staticmethod
    def AddPlayerAttackRangeAdd(builder, PlayerAttackRangeAdd): builder.PrependInt64Slot(20, PlayerAttackRangeAdd, 0)


    @staticmethod
    def AddPlayerAttackRangeRate(builder, PlayerAttackRangeRate): builder.PrependInt64Slot(21, PlayerAttackRangeRate, 0)


    @staticmethod
    def AddEnemySightPointAdd(builder, EnemySightPointAdd): builder.PrependInt64Slot(22, EnemySightPointAdd, 0)


    @staticmethod
    def AddEnemySightPointRate(builder, EnemySightPointRate): builder.PrependInt64Slot(23, EnemySightPointRate, 0)


    @staticmethod
    def AddEnemyAttackRangeAdd(builder, EnemyAttackRangeAdd): builder.PrependInt64Slot(24, EnemyAttackRangeAdd, 0)


    @staticmethod
    def AddEnemyAttackRangeRate(builder, EnemyAttackRangeRate): builder.PrependInt64Slot(25, EnemyAttackRangeRate, 0)


    @staticmethod
    def AddPlayerSkillRangeAdd(builder, PlayerSkillRangeAdd): builder.PrependInt64Slot(26, PlayerSkillRangeAdd, 0)


    @staticmethod
    def AddPlayerSkillRangeRate(builder, PlayerSkillRangeRate): builder.PrependInt64Slot(27, PlayerSkillRangeRate, 0)


    @staticmethod
    def AddEnemySkillRangeAdd(builder, EnemySkillRangeAdd): builder.PrependInt64Slot(28, EnemySkillRangeAdd, 0)


    @staticmethod
    def AddEnemySkillRangeRate(builder, EnemySkillRangeRate): builder.PrependInt64Slot(29, EnemySkillRangeRate, 0)


    @staticmethod
    def AddPlayerMinimumPositionGapRate(builder, PlayerMinimumPositionGapRate): builder.PrependInt64Slot(30, PlayerMinimumPositionGapRate, 0)


    @staticmethod
    def AddEnemyMinimumPositionGapRate(builder, EnemyMinimumPositionGapRate): builder.PrependInt64Slot(31, EnemyMinimumPositionGapRate, 0)


    @staticmethod
    def AddPlayerSightRangeMax(builder, PlayerSightRangeMax): builder.PrependBoolSlot(32, PlayerSightRangeMax, 0)


    @staticmethod
    def AddEnemySightRangeMax(builder, EnemySightRangeMax): builder.PrependBoolSlot(33, EnemySightRangeMax, 0)


    @staticmethod
    def AddTSSAirUnitHeight(builder, TSSAirUnitHeight): builder.PrependInt64Slot(34, TSSAirUnitHeight, 0)


    @staticmethod
    def AddIsPhaseBGM(builder, IsPhaseBGM): builder.PrependBoolSlot(35, IsPhaseBGM, 0)


    @staticmethod
    def AddBGMId(builder, BGMId): builder.PrependInt64Slot(36, BGMId, 0)


    @staticmethod
    def AddWarningUI(builder, WarningUI): builder.PrependBoolSlot(37, WarningUI, 0)


    @staticmethod
    def AddTSSHatchOpen(builder, TSSHatchOpen): builder.PrependBoolSlot(38, TSSHatchOpen, 0)


    @staticmethod
    def AddForcedTacticSpeed(builder, ForcedTacticSpeed): builder.PrependInt32Slot(39, ForcedTacticSpeed, 0)


    @staticmethod
    def AddForcedSkillUse(builder, ForcedSkillUse): builder.PrependInt32Slot(40, ForcedSkillUse, 0)


    @staticmethod
    def AddShowNPCSkillCutIn(builder, ShowNPCSkillCutIn): builder.PrependInt32Slot(41, ShowNPCSkillCutIn, 0)


    @staticmethod
    def AddImmuneHitBeforeTimeOutEnd(builder, ImmuneHitBeforeTimeOutEnd): builder.PrependBoolSlot(42, ImmuneHitBeforeTimeOutEnd, 0)


    @staticmethod
    def AddUIBattleHideFromScratch(builder, UIBattleHideFromScratch): builder.PrependBoolSlot(43, UIBattleHideFromScratch, 0)


    @staticmethod
    def AddBattleReadyTimelinePath(builder, BattleReadyTimelinePath): builder.PrependUOffsetTRelativeSlot(44, flatbuffers.number_types.UOffsetTFlags.py_type(BattleReadyTimelinePath), 0)

    @staticmethod
    def AddBeforeVictoryTimelinePath(builder, BeforeVictoryTimelinePath): builder.PrependUOffsetTRelativeSlot(45, flatbuffers.number_types.UOffsetTFlags.py_type(BeforeVictoryTimelinePath), 0)

    @staticmethod
    def AddSkipBattleEnd(builder, SkipBattleEnd): builder.PrependBoolSlot(46, SkipBattleEnd, 0)


    @staticmethod
    def AddHideNPCWhenBattleEnd(builder, HideNPCWhenBattleEnd): builder.PrependBoolSlot(47, HideNPCWhenBattleEnd, 0)


    @staticmethod
    def AddCoverPointOff(builder, CoverPointOff): builder.PrependBoolSlot(48, CoverPointOff, 0)


    @staticmethod
    def AddUIHpScale(builder, UIHpScale): builder.PrependFloat32Slot(49, UIHpScale, 0)


    @staticmethod
    def AddUIEmojiScale(builder, UIEmojiScale): builder.PrependFloat32Slot(50, UIEmojiScale, 0)


    @staticmethod
    def AddUISkillMainLogScale(builder, UISkillMainLogScale): builder.PrependFloat32Slot(51, UISkillMainLogScale, 0)


    @staticmethod
    def AddEffectCountLimit(builder, EffectCountLimit): builder.PrependInt32Slot(52, EffectCountLimit, 0)


    @staticmethod
    def AddAllyPassiveSkillId(builder, AllyPassiveSkillId): builder.PrependUOffsetTRelativeSlot(53, flatbuffers.number_types.UOffsetTFlags.py_type(AllyPassiveSkillId), 0)
    @staticmethod
    def StartAllyPassiveSkillIdVector(builder, numElems): return builder.StartVector(4, numElems, 4)


    @staticmethod
    def AddAllyPassiveSkillLevel(builder, AllyPassiveSkillLevel): builder.PrependUOffsetTRelativeSlot(54, flatbuffers.number_types.UOffsetTFlags.py_type(AllyPassiveSkillLevel), 0)
    @staticmethod
    def StartAllyPassiveSkillLevelVector(builder, numElems): return builder.StartVector(4, numElems, 4)


    @staticmethod
    def AddEnemyPassiveSkillId(builder, EnemyPassiveSkillId): builder.PrependUOffsetTRelativeSlot(55, flatbuffers.number_types.UOffsetTFlags.py_type(EnemyPassiveSkillId), 0)
    @staticmethod
    def StartEnemyPassiveSkillIdVector(builder, numElems): return builder.StartVector(4, numElems, 4)


    @staticmethod
    def AddEnemyPassiveSkillLevel(builder, EnemyPassiveSkillLevel): builder.PrependUOffsetTRelativeSlot(56, flatbuffers.number_types.UOffsetTFlags.py_type(EnemyPassiveSkillLevel), 0)
    @staticmethod
    def StartEnemyPassiveSkillLevelVector(builder, numElems): return builder.StartVector(4, numElems, 4)

