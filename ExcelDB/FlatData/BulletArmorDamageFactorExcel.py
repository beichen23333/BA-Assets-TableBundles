
import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class BulletArmorDamageFactorExcel:
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = BulletArmorDamageFactorExcel()
        x.Init(buf, n + offset)
        return x

    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)


    def DamageFactorGroupId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def BulletType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def ArmorType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def DamageRate(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def DamageAttribute(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def MinDamageRate(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def MaxDamageRate(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def ShowHighlightFloater(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0




    @staticmethod
    def Start(builder): builder.StartObject(8)
    @staticmethod
    def End(builder): return builder.EndObject()


    @staticmethod
    def AddDamageFactorGroupId(builder, DamageFactorGroupId): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(DamageFactorGroupId), 0)

    @staticmethod
    def AddBulletType(builder, BulletType): builder.PrependInt32Slot(1, BulletType, 0)


    @staticmethod
    def AddArmorType(builder, ArmorType): builder.PrependInt32Slot(2, ArmorType, 0)


    @staticmethod
    def AddDamageRate(builder, DamageRate): builder.PrependInt64Slot(3, DamageRate, 0)


    @staticmethod
    def AddDamageAttribute(builder, DamageAttribute): builder.PrependInt32Slot(4, DamageAttribute, 0)


    @staticmethod
    def AddMinDamageRate(builder, MinDamageRate): builder.PrependInt64Slot(5, MinDamageRate, 0)


    @staticmethod
    def AddMaxDamageRate(builder, MaxDamageRate): builder.PrependInt64Slot(6, MaxDamageRate, 0)


    @staticmethod
    def AddShowHighlightFloater(builder, ShowHighlightFloater): builder.PrependBoolSlot(7, ShowHighlightFloater, 0)

