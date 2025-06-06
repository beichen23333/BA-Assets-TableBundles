
import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class ConstConquestExcel:
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = ConstConquestExcel()
        x.Init(buf, n + offset)
        return x

    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)


    def ManageUnitChange(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def AssistCount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def PlayTimeLimitInSeconds(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def AnimationUnitAmountMin(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def AnimationUnitAmountMax(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def AnimationUnitDelay(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0




    @staticmethod
    def Start(builder): builder.StartObject(6)
    @staticmethod
    def End(builder): return builder.EndObject()


    @staticmethod
    def AddManageUnitChange(builder, ManageUnitChange): builder.PrependInt32Slot(0, ManageUnitChange, 0)


    @staticmethod
    def AddAssistCount(builder, AssistCount): builder.PrependInt32Slot(1, AssistCount, 0)


    @staticmethod
    def AddPlayTimeLimitInSeconds(builder, PlayTimeLimitInSeconds): builder.PrependInt32Slot(2, PlayTimeLimitInSeconds, 0)


    @staticmethod
    def AddAnimationUnitAmountMin(builder, AnimationUnitAmountMin): builder.PrependInt32Slot(3, AnimationUnitAmountMin, 0)


    @staticmethod
    def AddAnimationUnitAmountMax(builder, AnimationUnitAmountMax): builder.PrependInt32Slot(4, AnimationUnitAmountMax, 0)


    @staticmethod
    def AddAnimationUnitDelay(builder, AnimationUnitDelay): builder.PrependFloat32Slot(5, AnimationUnitDelay, 0)

