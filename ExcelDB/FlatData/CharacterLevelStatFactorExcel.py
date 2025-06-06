
import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class CharacterLevelStatFactorExcel:
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = CharacterLevelStatFactorExcel()
        x.Init(buf, n + offset)
        return x

    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)


    def Level(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def CriticalFactor(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def StabilityFactor(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def DefenceFactor(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def AccuracyFactor(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0




    @staticmethod
    def Start(builder): builder.StartObject(5)
    @staticmethod
    def End(builder): return builder.EndObject()


    @staticmethod
    def AddLevel(builder, Level): builder.PrependInt64Slot(0, Level, 0)


    @staticmethod
    def AddCriticalFactor(builder, CriticalFactor): builder.PrependInt64Slot(1, CriticalFactor, 0)


    @staticmethod
    def AddStabilityFactor(builder, StabilityFactor): builder.PrependInt64Slot(2, StabilityFactor, 0)


    @staticmethod
    def AddDefenceFactor(builder, DefenceFactor): builder.PrependInt64Slot(3, DefenceFactor, 0)


    @staticmethod
    def AddAccuracyFactor(builder, AccuracyFactor): builder.PrependInt64Slot(4, AccuracyFactor, 0)

