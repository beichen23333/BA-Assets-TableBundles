
import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class ObstacleStatExcel:
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = ObstacleStatExcel()
        x.Init(buf, n + offset)
        return x

    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)


    def StringID(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0


    def Name(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def MaxHP1(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def MaxHP100(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def BlockRate(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def Dodge(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def CanNotStandRange(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def HighlightFloaterHeight(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0


    def EnhanceLightArmorRate(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def EnhanceHeavyArmorRate(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def EnhanceUnarmedRate(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def EnhanceElasticArmorRate(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def EnhanceStructureRate(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(28))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def EnhanceNormalArmorRate(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(30))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def ReduceExDamagedRate(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(32))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0




    @staticmethod
    def Start(builder): builder.StartObject(15)
    @staticmethod
    def End(builder): return builder.EndObject()


    @staticmethod
    def AddStringID(builder, StringID): builder.PrependUint32Slot(0, StringID, 0)


    @staticmethod
    def AddName(builder, Name): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(Name), 0)

    @staticmethod
    def AddMaxHP1(builder, MaxHP1): builder.PrependInt64Slot(2, MaxHP1, 0)


    @staticmethod
    def AddMaxHP100(builder, MaxHP100): builder.PrependInt64Slot(3, MaxHP100, 0)


    @staticmethod
    def AddBlockRate(builder, BlockRate): builder.PrependInt64Slot(4, BlockRate, 0)


    @staticmethod
    def AddDodge(builder, Dodge): builder.PrependInt64Slot(5, Dodge, 0)


    @staticmethod
    def AddCanNotStandRange(builder, CanNotStandRange): builder.PrependInt64Slot(6, CanNotStandRange, 0)


    @staticmethod
    def AddHighlightFloaterHeight(builder, HighlightFloaterHeight): builder.PrependFloat32Slot(7, HighlightFloaterHeight, 0)


    @staticmethod
    def AddEnhanceLightArmorRate(builder, EnhanceLightArmorRate): builder.PrependInt64Slot(8, EnhanceLightArmorRate, 0)


    @staticmethod
    def AddEnhanceHeavyArmorRate(builder, EnhanceHeavyArmorRate): builder.PrependInt64Slot(9, EnhanceHeavyArmorRate, 0)


    @staticmethod
    def AddEnhanceUnarmedRate(builder, EnhanceUnarmedRate): builder.PrependInt64Slot(10, EnhanceUnarmedRate, 0)


    @staticmethod
    def AddEnhanceElasticArmorRate(builder, EnhanceElasticArmorRate): builder.PrependInt64Slot(11, EnhanceElasticArmorRate, 0)


    @staticmethod
    def AddEnhanceStructureRate(builder, EnhanceStructureRate): builder.PrependInt64Slot(12, EnhanceStructureRate, 0)


    @staticmethod
    def AddEnhanceNormalArmorRate(builder, EnhanceNormalArmorRate): builder.PrependInt64Slot(13, EnhanceNormalArmorRate, 0)


    @staticmethod
    def AddReduceExDamagedRate(builder, ReduceExDamagedRate): builder.PrependInt64Slot(14, ReduceExDamagedRate, 0)

