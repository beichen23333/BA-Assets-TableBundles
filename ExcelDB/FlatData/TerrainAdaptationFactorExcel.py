
import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class TerrainAdaptationFactorExcel:
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = TerrainAdaptationFactorExcel()
        x.Init(buf, n + offset)
        return x

    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)


    def TerrainAdaptation(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def TerrainAdaptationStat(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def ShotFactor(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def BlockFactor(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def AccuracyFactor(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def DodgeFactor(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def AttackPowerFactor(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0




    @staticmethod
    def Start(builder): builder.StartObject(7)
    @staticmethod
    def End(builder): return builder.EndObject()


    @staticmethod
    def AddTerrainAdaptation(builder, TerrainAdaptation): builder.PrependInt32Slot(0, TerrainAdaptation, 0)


    @staticmethod
    def AddTerrainAdaptationStat(builder, TerrainAdaptationStat): builder.PrependInt32Slot(1, TerrainAdaptationStat, 0)


    @staticmethod
    def AddShotFactor(builder, ShotFactor): builder.PrependInt64Slot(2, ShotFactor, 0)


    @staticmethod
    def AddBlockFactor(builder, BlockFactor): builder.PrependInt64Slot(3, BlockFactor, 0)


    @staticmethod
    def AddAccuracyFactor(builder, AccuracyFactor): builder.PrependInt64Slot(4, AccuracyFactor, 0)


    @staticmethod
    def AddDodgeFactor(builder, DodgeFactor): builder.PrependInt64Slot(5, DodgeFactor, 0)


    @staticmethod
    def AddAttackPowerFactor(builder, AttackPowerFactor): builder.PrependInt64Slot(6, AttackPowerFactor, 0)

