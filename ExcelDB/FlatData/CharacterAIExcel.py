
import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class CharacterAIExcel:
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = CharacterAIExcel()
        x.Init(buf, n + offset)
        return x

    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)


    def Id(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def EngageType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def Positioning(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def CheckCanUseAutoSkill(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0


    def DistanceReduceRatioObstaclePath(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def DistanceReduceObstaclePath(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def DistanceReduceRatioFormationPath(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def DistanceReduceFormationPath(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def MinimumPositionGap(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def CanUseObstacleOfKneelMotion(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0


    def CanUseObstacleOfStandMotion(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0


    def HasTargetSwitchingMotion(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0




    @staticmethod
    def Start(builder): builder.StartObject(12)
    @staticmethod
    def End(builder): return builder.EndObject()


    @staticmethod
    def AddId(builder, Id): builder.PrependInt64Slot(0, Id, 0)


    @staticmethod
    def AddEngageType(builder, EngageType): builder.PrependInt32Slot(1, EngageType, 0)


    @staticmethod
    def AddPositioning(builder, Positioning): builder.PrependInt32Slot(2, Positioning, 0)


    @staticmethod
    def AddCheckCanUseAutoSkill(builder, CheckCanUseAutoSkill): builder.PrependBoolSlot(3, CheckCanUseAutoSkill, 0)


    @staticmethod
    def AddDistanceReduceRatioObstaclePath(builder, DistanceReduceRatioObstaclePath): builder.PrependInt64Slot(4, DistanceReduceRatioObstaclePath, 0)


    @staticmethod
    def AddDistanceReduceObstaclePath(builder, DistanceReduceObstaclePath): builder.PrependInt64Slot(5, DistanceReduceObstaclePath, 0)


    @staticmethod
    def AddDistanceReduceRatioFormationPath(builder, DistanceReduceRatioFormationPath): builder.PrependInt64Slot(6, DistanceReduceRatioFormationPath, 0)


    @staticmethod
    def AddDistanceReduceFormationPath(builder, DistanceReduceFormationPath): builder.PrependInt64Slot(7, DistanceReduceFormationPath, 0)


    @staticmethod
    def AddMinimumPositionGap(builder, MinimumPositionGap): builder.PrependInt64Slot(8, MinimumPositionGap, 0)


    @staticmethod
    def AddCanUseObstacleOfKneelMotion(builder, CanUseObstacleOfKneelMotion): builder.PrependBoolSlot(9, CanUseObstacleOfKneelMotion, 0)


    @staticmethod
    def AddCanUseObstacleOfStandMotion(builder, CanUseObstacleOfStandMotion): builder.PrependBoolSlot(10, CanUseObstacleOfStandMotion, 0)


    @staticmethod
    def AddHasTargetSwitchingMotion(builder, HasTargetSwitchingMotion): builder.PrependBoolSlot(11, HasTargetSwitchingMotion, 0)

