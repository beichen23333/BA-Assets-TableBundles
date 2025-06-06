
import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class MiniGameDefenseStageExcel:
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = MiniGameDefenseStageExcel()
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


    def EventContentId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def StageDifficulty(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def StageDifficultyLocalize(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0


    def StageNumber(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def StageDisplay(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def PrevStageId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def EchelonExtensionType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
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


    def EventContentStageRewardId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(30))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def EnterScenarioGroupId(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(32))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int64Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 8))
        return 0

    def EnterScenarioGroupIdAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(32))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int64Flags, o)
        return 0

    def EnterScenarioGroupIdLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(32))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    def EnterScenarioGroupIdIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(32))
        return o == 0


    def ClearScenarioGroupId(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(34))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int64Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 8))
        return 0

    def ClearScenarioGroupIdAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(34))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int64Flags, o)
        return 0

    def ClearScenarioGroupIdLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(34))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    def ClearScenarioGroupIdIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(34))
        return o == 0


    def StageTopography(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(36))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def RecommandLevel(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(38))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def GroundID(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(40))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def ContentType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(42))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def StarGoal(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(44))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int32Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return 0

    def StarGoalAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(44))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int32Flags, o)
        return 0

    def StarGoalLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(44))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    def StarGoalIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(44))
        return o == 0


    def StarGoalAmount(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(46))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int32Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return 0

    def StarGoalAmountAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(46))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int32Flags, o)
        return 0

    def StarGoalAmountLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(46))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    def StarGoalAmountIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(46))
        return o == 0


    def DefenseFormationBGPrefab(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(48))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def DefenseFormationBGPrefabScale(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(50))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0


    def FixedEchelon(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(52))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def MininageDefenseFixedStatId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(54))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def StageHint(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(56))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0




    @staticmethod
    def Start(builder): builder.StartObject(27)
    @staticmethod
    def End(builder): return builder.EndObject()


    @staticmethod
    def AddId(builder, Id): builder.PrependInt64Slot(0, Id, 0)


    @staticmethod
    def AddName(builder, Name): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(Name), 0)

    @staticmethod
    def AddEventContentId(builder, EventContentId): builder.PrependInt64Slot(2, EventContentId, 0)


    @staticmethod
    def AddStageDifficulty(builder, StageDifficulty): builder.PrependInt32Slot(3, StageDifficulty, 0)


    @staticmethod
    def AddStageDifficultyLocalize(builder, StageDifficultyLocalize): builder.PrependUint32Slot(4, StageDifficultyLocalize, 0)


    @staticmethod
    def AddStageNumber(builder, StageNumber): builder.PrependInt32Slot(5, StageNumber, 0)


    @staticmethod
    def AddStageDisplay(builder, StageDisplay): builder.PrependInt32Slot(6, StageDisplay, 0)


    @staticmethod
    def AddPrevStageId(builder, PrevStageId): builder.PrependInt64Slot(7, PrevStageId, 0)


    @staticmethod
    def AddEchelonExtensionType(builder, EchelonExtensionType): builder.PrependInt32Slot(8, EchelonExtensionType, 0)


    @staticmethod
    def AddBattleDuration(builder, BattleDuration): builder.PrependInt64Slot(9, BattleDuration, 0)


    @staticmethod
    def AddStageEnterCostType(builder, StageEnterCostType): builder.PrependInt32Slot(10, StageEnterCostType, 0)


    @staticmethod
    def AddStageEnterCostId(builder, StageEnterCostId): builder.PrependInt64Slot(11, StageEnterCostId, 0)


    @staticmethod
    def AddStageEnterCostAmount(builder, StageEnterCostAmount): builder.PrependInt32Slot(12, StageEnterCostAmount, 0)


    @staticmethod
    def AddEventContentStageRewardId(builder, EventContentStageRewardId): builder.PrependInt64Slot(13, EventContentStageRewardId, 0)


    @staticmethod
    def AddEnterScenarioGroupId(builder, EnterScenarioGroupId): builder.PrependUOffsetTRelativeSlot(14, flatbuffers.number_types.UOffsetTFlags.py_type(EnterScenarioGroupId), 0)
    @staticmethod
    def StartEnterScenarioGroupIdVector(builder, numElems): return builder.StartVector(8, numElems, 8)


    @staticmethod
    def AddClearScenarioGroupId(builder, ClearScenarioGroupId): builder.PrependUOffsetTRelativeSlot(15, flatbuffers.number_types.UOffsetTFlags.py_type(ClearScenarioGroupId), 0)
    @staticmethod
    def StartClearScenarioGroupIdVector(builder, numElems): return builder.StartVector(8, numElems, 8)


    @staticmethod
    def AddStageTopography(builder, StageTopography): builder.PrependInt32Slot(16, StageTopography, 0)


    @staticmethod
    def AddRecommandLevel(builder, RecommandLevel): builder.PrependInt32Slot(17, RecommandLevel, 0)


    @staticmethod
    def AddGroundID(builder, GroundID): builder.PrependInt64Slot(18, GroundID, 0)


    @staticmethod
    def AddContentType(builder, ContentType): builder.PrependInt32Slot(19, ContentType, 0)


    @staticmethod
    def AddStarGoal(builder, StarGoal): builder.PrependUOffsetTRelativeSlot(20, flatbuffers.number_types.UOffsetTFlags.py_type(StarGoal), 0)
    @staticmethod
    def StartStarGoalVector(builder, numElems): return builder.StartVector(4, numElems, 4)


    @staticmethod
    def AddStarGoalAmount(builder, StarGoalAmount): builder.PrependUOffsetTRelativeSlot(21, flatbuffers.number_types.UOffsetTFlags.py_type(StarGoalAmount), 0)
    @staticmethod
    def StartStarGoalAmountVector(builder, numElems): return builder.StartVector(4, numElems, 4)


    @staticmethod
    def AddDefenseFormationBGPrefab(builder, DefenseFormationBGPrefab): builder.PrependUOffsetTRelativeSlot(22, flatbuffers.number_types.UOffsetTFlags.py_type(DefenseFormationBGPrefab), 0)

    @staticmethod
    def AddDefenseFormationBGPrefabScale(builder, DefenseFormationBGPrefabScale): builder.PrependFloat32Slot(23, DefenseFormationBGPrefabScale, 0)


    @staticmethod
    def AddFixedEchelon(builder, FixedEchelon): builder.PrependInt64Slot(24, FixedEchelon, 0)


    @staticmethod
    def AddMininageDefenseFixedStatId(builder, MininageDefenseFixedStatId): builder.PrependInt64Slot(25, MininageDefenseFixedStatId, 0)


    @staticmethod
    def AddStageHint(builder, StageHint): builder.PrependUint32Slot(26, StageHint, 0)

