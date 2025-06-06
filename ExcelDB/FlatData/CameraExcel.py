
import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class CameraExcel:
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = CameraExcel()
        x.Init(buf, n + offset)
        return x

    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)


    def UniqueId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def MinDistance(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0


    def MaxDistance(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0


    def RotationX(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0


    def RotationY(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0


    def MoveInstantly(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0


    def MoveInstantlyRotationSave(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0


    def LeftMargin(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0


    def BottomMargin(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0


    def IgnoreEnemies(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0


    def UseRailPointCompensation(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0




    @staticmethod
    def Start(builder): builder.StartObject(11)
    @staticmethod
    def End(builder): return builder.EndObject()


    @staticmethod
    def AddUniqueId(builder, UniqueId): builder.PrependInt64Slot(0, UniqueId, 0)


    @staticmethod
    def AddMinDistance(builder, MinDistance): builder.PrependFloat32Slot(1, MinDistance, 0)


    @staticmethod
    def AddMaxDistance(builder, MaxDistance): builder.PrependFloat32Slot(2, MaxDistance, 0)


    @staticmethod
    def AddRotationX(builder, RotationX): builder.PrependFloat32Slot(3, RotationX, 0)


    @staticmethod
    def AddRotationY(builder, RotationY): builder.PrependFloat32Slot(4, RotationY, 0)


    @staticmethod
    def AddMoveInstantly(builder, MoveInstantly): builder.PrependBoolSlot(5, MoveInstantly, 0)


    @staticmethod
    def AddMoveInstantlyRotationSave(builder, MoveInstantlyRotationSave): builder.PrependBoolSlot(6, MoveInstantlyRotationSave, 0)


    @staticmethod
    def AddLeftMargin(builder, LeftMargin): builder.PrependFloat32Slot(7, LeftMargin, 0)


    @staticmethod
    def AddBottomMargin(builder, BottomMargin): builder.PrependFloat32Slot(8, BottomMargin, 0)


    @staticmethod
    def AddIgnoreEnemies(builder, IgnoreEnemies): builder.PrependBoolSlot(9, IgnoreEnemies, 0)


    @staticmethod
    def AddUseRailPointCompensation(builder, UseRailPointCompensation): builder.PrependBoolSlot(10, UseRailPointCompensation, 0)

