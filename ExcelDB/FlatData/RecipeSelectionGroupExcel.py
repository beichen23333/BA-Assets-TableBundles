
import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class RecipeSelectionGroupExcel:
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = RecipeSelectionGroupExcel()
        x.Init(buf, n + offset)
        return x

    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)


    def RecipeSelectionGroupId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def RecipeSelectionGroupComponentId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def ParcelType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def ParcelId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def ResultAmountMin(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def ResultAmountMax(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0




    @staticmethod
    def Start(builder): builder.StartObject(6)
    @staticmethod
    def End(builder): return builder.EndObject()


    @staticmethod
    def AddRecipeSelectionGroupId(builder, RecipeSelectionGroupId): builder.PrependInt64Slot(0, RecipeSelectionGroupId, 0)


    @staticmethod
    def AddRecipeSelectionGroupComponentId(builder, RecipeSelectionGroupComponentId): builder.PrependInt64Slot(1, RecipeSelectionGroupComponentId, 0)


    @staticmethod
    def AddParcelType(builder, ParcelType): builder.PrependInt32Slot(2, ParcelType, 0)


    @staticmethod
    def AddParcelId(builder, ParcelId): builder.PrependInt64Slot(3, ParcelId, 0)


    @staticmethod
    def AddResultAmountMin(builder, ResultAmountMin): builder.PrependInt64Slot(4, ResultAmountMin, 0)


    @staticmethod
    def AddResultAmountMax(builder, ResultAmountMax): builder.PrependInt64Slot(5, ResultAmountMax, 0)

