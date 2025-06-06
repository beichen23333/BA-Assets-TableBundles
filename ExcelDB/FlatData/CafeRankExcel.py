
import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class CafeRankExcel:
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = CafeRankExcel()
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


    def RecipeId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def ComfortMax(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def TagCountMax(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def CharacterVisitMin(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def CharacterVisitMax(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def CafeVisitWeightBase(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def CafeVisitWeightTagBonusStep(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int32Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return 0

    def CafeVisitWeightTagBonusStepAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int32Flags, o)
        return 0

    def CafeVisitWeightTagBonusStepLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    def CafeVisitWeightTagBonusStepIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        return o == 0


    def CafeVisitWeightTagBonus(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int32Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return 0

    def CafeVisitWeightTagBonusAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int32Flags, o)
        return 0

    def CafeVisitWeightTagBonusLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    def CafeVisitWeightTagBonusIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        return o == 0




    @staticmethod
    def Start(builder): builder.StartObject(10)
    @staticmethod
    def End(builder): return builder.EndObject()


    @staticmethod
    def AddCafeId(builder, CafeId): builder.PrependInt64Slot(0, CafeId, 0)


    @staticmethod
    def AddRank(builder, Rank): builder.PrependInt64Slot(1, Rank, 0)


    @staticmethod
    def AddRecipeId(builder, RecipeId): builder.PrependInt64Slot(2, RecipeId, 0)


    @staticmethod
    def AddComfortMax(builder, ComfortMax): builder.PrependInt64Slot(3, ComfortMax, 0)


    @staticmethod
    def AddTagCountMax(builder, TagCountMax): builder.PrependInt64Slot(4, TagCountMax, 0)


    @staticmethod
    def AddCharacterVisitMin(builder, CharacterVisitMin): builder.PrependInt32Slot(5, CharacterVisitMin, 0)


    @staticmethod
    def AddCharacterVisitMax(builder, CharacterVisitMax): builder.PrependInt32Slot(6, CharacterVisitMax, 0)


    @staticmethod
    def AddCafeVisitWeightBase(builder, CafeVisitWeightBase): builder.PrependInt32Slot(7, CafeVisitWeightBase, 0)


    @staticmethod
    def AddCafeVisitWeightTagBonusStep(builder, CafeVisitWeightTagBonusStep): builder.PrependUOffsetTRelativeSlot(8, flatbuffers.number_types.UOffsetTFlags.py_type(CafeVisitWeightTagBonusStep), 0)
    @staticmethod
    def StartCafeVisitWeightTagBonusStepVector(builder, numElems): return builder.StartVector(4, numElems, 4)


    @staticmethod
    def AddCafeVisitWeightTagBonus(builder, CafeVisitWeightTagBonus): builder.PrependUOffsetTRelativeSlot(9, flatbuffers.number_types.UOffsetTFlags.py_type(CafeVisitWeightTagBonus), 0)
    @staticmethod
    def StartCafeVisitWeightTagBonusVector(builder, numElems): return builder.StartVector(4, numElems, 4)

