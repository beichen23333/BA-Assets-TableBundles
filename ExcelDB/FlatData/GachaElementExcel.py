
import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class GachaElementExcel:
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = GachaElementExcel()
        x.Init(buf, n + offset)
        return x

    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)


    def ID(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def GachaGroupID(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def ParcelType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def ParcelID(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def Rarity(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def ParcelAmountMin(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def ParcelAmountMax(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def Prob(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def State(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0




    @staticmethod
    def Start(builder): builder.StartObject(9)
    @staticmethod
    def End(builder): return builder.EndObject()


    @staticmethod
    def AddID(builder, ID): builder.PrependInt64Slot(0, ID, 0)


    @staticmethod
    def AddGachaGroupID(builder, GachaGroupID): builder.PrependInt64Slot(1, GachaGroupID, 0)


    @staticmethod
    def AddParcelType(builder, ParcelType): builder.PrependInt32Slot(2, ParcelType, 0)


    @staticmethod
    def AddParcelID(builder, ParcelID): builder.PrependInt64Slot(3, ParcelID, 0)


    @staticmethod
    def AddRarity(builder, Rarity): builder.PrependInt32Slot(4, Rarity, 0)


    @staticmethod
    def AddParcelAmountMin(builder, ParcelAmountMin): builder.PrependInt32Slot(5, ParcelAmountMin, 0)


    @staticmethod
    def AddParcelAmountMax(builder, ParcelAmountMax): builder.PrependInt32Slot(6, ParcelAmountMax, 0)


    @staticmethod
    def AddProb(builder, Prob): builder.PrependInt32Slot(7, Prob, 0)


    @staticmethod
    def AddState(builder, State): builder.PrependInt32Slot(8, State, 0)

