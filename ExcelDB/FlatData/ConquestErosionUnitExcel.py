
import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class ConquestErosionUnitExcel:
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = ConquestErosionUnitExcel()
        x.Init(buf, n + offset)
        return x

    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)


    def TilePrefabId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def MassErosionUnitId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def MassErosionUnitRotationY(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0


    def IndividualErosionUnitId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def IndividualErosionUnitRotationY(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0




    @staticmethod
    def Start(builder): builder.StartObject(5)
    @staticmethod
    def End(builder): return builder.EndObject()


    @staticmethod
    def AddTilePrefabId(builder, TilePrefabId): builder.PrependInt64Slot(0, TilePrefabId, 0)


    @staticmethod
    def AddMassErosionUnitId(builder, MassErosionUnitId): builder.PrependInt64Slot(1, MassErosionUnitId, 0)


    @staticmethod
    def AddMassErosionUnitRotationY(builder, MassErosionUnitRotationY): builder.PrependFloat32Slot(2, MassErosionUnitRotationY, 0)


    @staticmethod
    def AddIndividualErosionUnitId(builder, IndividualErosionUnitId): builder.PrependInt64Slot(3, IndividualErosionUnitId, 0)


    @staticmethod
    def AddIndividualErosionUnitRotationY(builder, IndividualErosionUnitRotationY): builder.PrependFloat32Slot(4, IndividualErosionUnitRotationY, 0)

