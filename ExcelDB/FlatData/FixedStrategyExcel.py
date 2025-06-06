
import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class FixedStrategyExcel:
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = FixedStrategyExcel()
        x.Init(buf, n + offset)
        return x

    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)


    def Id(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def StageEnterEchelon01FixedEchelonId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def StageEnterEchelon01Starttile(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def StageEnterEchelon02FixedEchelonId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def StageEnterEchelon02Starttile(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def StageEnterEchelon03FixedEchelonId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def StageEnterEchelon03Starttile(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def StageEnterEchelon04FixedEchelonId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def StageEnterEchelon04Starttile(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0




    @staticmethod
    def Start(builder): builder.StartObject(9)
    @staticmethod
    def End(builder): return builder.EndObject()


    @staticmethod
    def AddId(builder, Id): builder.PrependInt64Slot(0, Id, 0)


    @staticmethod
    def AddStageEnterEchelon01FixedEchelonId(builder, StageEnterEchelon01FixedEchelonId): builder.PrependInt64Slot(1, StageEnterEchelon01FixedEchelonId, 0)


    @staticmethod
    def AddStageEnterEchelon01Starttile(builder, StageEnterEchelon01Starttile): builder.PrependInt64Slot(2, StageEnterEchelon01Starttile, 0)


    @staticmethod
    def AddStageEnterEchelon02FixedEchelonId(builder, StageEnterEchelon02FixedEchelonId): builder.PrependInt64Slot(3, StageEnterEchelon02FixedEchelonId, 0)


    @staticmethod
    def AddStageEnterEchelon02Starttile(builder, StageEnterEchelon02Starttile): builder.PrependInt64Slot(4, StageEnterEchelon02Starttile, 0)


    @staticmethod
    def AddStageEnterEchelon03FixedEchelonId(builder, StageEnterEchelon03FixedEchelonId): builder.PrependInt64Slot(5, StageEnterEchelon03FixedEchelonId, 0)


    @staticmethod
    def AddStageEnterEchelon03Starttile(builder, StageEnterEchelon03Starttile): builder.PrependInt64Slot(6, StageEnterEchelon03Starttile, 0)


    @staticmethod
    def AddStageEnterEchelon04FixedEchelonId(builder, StageEnterEchelon04FixedEchelonId): builder.PrependInt64Slot(7, StageEnterEchelon04FixedEchelonId, 0)


    @staticmethod
    def AddStageEnterEchelon04Starttile(builder, StageEnterEchelon04Starttile): builder.PrependInt64Slot(8, StageEnterEchelon04Starttile, 0)

