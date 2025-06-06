
import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class ConstStrategyExcel:
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = ConstStrategyExcel()
        x.Init(buf, n + offset)
        return x

    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)


    def HexaMapBoundaryOffset(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0


    def HexaMapStartCameraOffset(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0


    def CameraZoomMax(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0


    def CameraZoomMin(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0


    def CameraZoomDefault(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0


    def HealCostType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def HealCostAmount(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int64Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 8))
        return 0

    def HealCostAmountAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int64Flags, o)
        return 0

    def HealCostAmountLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    def HealCostAmountIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        return o == 0


    def CanHealHpRate(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def PlayTimeLimitInSeconds(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def AdventureEchelonCount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def RaidEchelonCount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def DefaultEchelonCount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def EventContentEchelonCount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(28))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def TimeAttackDungeonEchelonCount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(30))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def WorldRaidEchelonCount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(32))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def TacticSkipClearTimeSeconds(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(34))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def TacticSkipFramePerSecond(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(36))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def ConquestEchelonCount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(38))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def StoryEchelonCount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(40))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def MultiSweepPresetCount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(42))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def MultiSweepPresetNameMaxLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(44))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def MultiSweepPresetSelectStageMaxCount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(46))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def MultiSweepPresetMaxSweepCount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(48))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def MultiSweepPresetSelectParcelMaxCount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(50))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0




    @staticmethod
    def Start(builder): builder.StartObject(24)
    @staticmethod
    def End(builder): return builder.EndObject()


    @staticmethod
    def AddHexaMapBoundaryOffset(builder, HexaMapBoundaryOffset): builder.PrependFloat32Slot(0, HexaMapBoundaryOffset, 0)


    @staticmethod
    def AddHexaMapStartCameraOffset(builder, HexaMapStartCameraOffset): builder.PrependFloat32Slot(1, HexaMapStartCameraOffset, 0)


    @staticmethod
    def AddCameraZoomMax(builder, CameraZoomMax): builder.PrependFloat32Slot(2, CameraZoomMax, 0)


    @staticmethod
    def AddCameraZoomMin(builder, CameraZoomMin): builder.PrependFloat32Slot(3, CameraZoomMin, 0)


    @staticmethod
    def AddCameraZoomDefault(builder, CameraZoomDefault): builder.PrependFloat32Slot(4, CameraZoomDefault, 0)


    @staticmethod
    def AddHealCostType(builder, HealCostType): builder.PrependInt32Slot(5, HealCostType, 0)


    @staticmethod
    def AddHealCostAmount(builder, HealCostAmount): builder.PrependUOffsetTRelativeSlot(6, flatbuffers.number_types.UOffsetTFlags.py_type(HealCostAmount), 0)
    @staticmethod
    def StartHealCostAmountVector(builder, numElems): return builder.StartVector(8, numElems, 8)


    @staticmethod
    def AddCanHealHpRate(builder, CanHealHpRate): builder.PrependInt32Slot(7, CanHealHpRate, 0)


    @staticmethod
    def AddPlayTimeLimitInSeconds(builder, PlayTimeLimitInSeconds): builder.PrependInt64Slot(8, PlayTimeLimitInSeconds, 0)


    @staticmethod
    def AddAdventureEchelonCount(builder, AdventureEchelonCount): builder.PrependInt32Slot(9, AdventureEchelonCount, 0)


    @staticmethod
    def AddRaidEchelonCount(builder, RaidEchelonCount): builder.PrependInt32Slot(10, RaidEchelonCount, 0)


    @staticmethod
    def AddDefaultEchelonCount(builder, DefaultEchelonCount): builder.PrependInt32Slot(11, DefaultEchelonCount, 0)


    @staticmethod
    def AddEventContentEchelonCount(builder, EventContentEchelonCount): builder.PrependInt32Slot(12, EventContentEchelonCount, 0)


    @staticmethod
    def AddTimeAttackDungeonEchelonCount(builder, TimeAttackDungeonEchelonCount): builder.PrependInt32Slot(13, TimeAttackDungeonEchelonCount, 0)


    @staticmethod
    def AddWorldRaidEchelonCount(builder, WorldRaidEchelonCount): builder.PrependInt32Slot(14, WorldRaidEchelonCount, 0)


    @staticmethod
    def AddTacticSkipClearTimeSeconds(builder, TacticSkipClearTimeSeconds): builder.PrependInt32Slot(15, TacticSkipClearTimeSeconds, 0)


    @staticmethod
    def AddTacticSkipFramePerSecond(builder, TacticSkipFramePerSecond): builder.PrependInt32Slot(16, TacticSkipFramePerSecond, 0)


    @staticmethod
    def AddConquestEchelonCount(builder, ConquestEchelonCount): builder.PrependInt32Slot(17, ConquestEchelonCount, 0)


    @staticmethod
    def AddStoryEchelonCount(builder, StoryEchelonCount): builder.PrependInt32Slot(18, StoryEchelonCount, 0)


    @staticmethod
    def AddMultiSweepPresetCount(builder, MultiSweepPresetCount): builder.PrependInt32Slot(19, MultiSweepPresetCount, 0)


    @staticmethod
    def AddMultiSweepPresetNameMaxLength(builder, MultiSweepPresetNameMaxLength): builder.PrependInt32Slot(20, MultiSweepPresetNameMaxLength, 0)


    @staticmethod
    def AddMultiSweepPresetSelectStageMaxCount(builder, MultiSweepPresetSelectStageMaxCount): builder.PrependInt32Slot(21, MultiSweepPresetSelectStageMaxCount, 0)


    @staticmethod
    def AddMultiSweepPresetMaxSweepCount(builder, MultiSweepPresetMaxSweepCount): builder.PrependInt32Slot(22, MultiSweepPresetMaxSweepCount, 0)


    @staticmethod
    def AddMultiSweepPresetSelectParcelMaxCount(builder, MultiSweepPresetSelectParcelMaxCount): builder.PrependInt32Slot(23, MultiSweepPresetSelectParcelMaxCount, 0)

