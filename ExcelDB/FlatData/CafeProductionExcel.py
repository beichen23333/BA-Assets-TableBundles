
import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class CafeProductionExcel:
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = CafeProductionExcel()
        x.Init(buf, n + offset)
        return x

    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)


    def CafeId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def Rank(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def CafeProductionParcelType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def CafeProductionParcelId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def ParcelProductionCoefficient(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def ParcelProductionCorrectionValue(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def ParcelStorageMax(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0




    @staticmethod
    def Start(builder): builder.StartObject(7)
    @staticmethod
    def End(builder): return builder.EndObject()


    @staticmethod
    def AddCafeId(builder, CafeId): builder.PrependInt64Slot(0, CafeId, 0)


    @staticmethod
    def AddRank(builder, Rank): builder.PrependInt64Slot(1, Rank, 0)


    @staticmethod
    def AddCafeProductionParcelType(builder, CafeProductionParcelType): builder.PrependInt32Slot(2, CafeProductionParcelType, 0)


    @staticmethod
    def AddCafeProductionParcelId(builder, CafeProductionParcelId): builder.PrependInt64Slot(3, CafeProductionParcelId, 0)


    @staticmethod
    def AddParcelProductionCoefficient(builder, ParcelProductionCoefficient): builder.PrependInt64Slot(4, ParcelProductionCoefficient, 0)


    @staticmethod
    def AddParcelProductionCorrectionValue(builder, ParcelProductionCorrectionValue): builder.PrependInt64Slot(5, ParcelProductionCorrectionValue, 0)


    @staticmethod
    def AddParcelStorageMax(builder, ParcelStorageMax): builder.PrependInt64Slot(6, ParcelStorageMax, 0)

