
import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class CharacterWeaponExpBonusExcel:
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = CharacterWeaponExpBonusExcel()
        x.Init(buf, n + offset)
        return x

    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)


    def WeaponType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def WeaponExpGrowthA(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def WeaponExpGrowthB(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def WeaponExpGrowthC(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def WeaponExpGrowthZ(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0




    @staticmethod
    def Start(builder): builder.StartObject(5)
    @staticmethod
    def End(builder): return builder.EndObject()


    @staticmethod
    def AddWeaponType(builder, WeaponType): builder.PrependInt32Slot(0, WeaponType, 0)


    @staticmethod
    def AddWeaponExpGrowthA(builder, WeaponExpGrowthA): builder.PrependInt32Slot(1, WeaponExpGrowthA, 0)


    @staticmethod
    def AddWeaponExpGrowthB(builder, WeaponExpGrowthB): builder.PrependInt32Slot(2, WeaponExpGrowthB, 0)


    @staticmethod
    def AddWeaponExpGrowthC(builder, WeaponExpGrowthC): builder.PrependInt32Slot(3, WeaponExpGrowthC, 0)


    @staticmethod
    def AddWeaponExpGrowthZ(builder, WeaponExpGrowthZ): builder.PrependInt32Slot(4, WeaponExpGrowthZ, 0)

