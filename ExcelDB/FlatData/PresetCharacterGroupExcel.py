
import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class PresetCharacterGroupExcel:
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = PresetCharacterGroupExcel()
        x.Init(buf, n + offset)
        return x

    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)


    def PresetCharacterGroupId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def GetPresetType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def Level(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def Exp(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def FavorExp(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def FavorRank(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def StarGrade(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def ExSkillLevel(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def PassiveSkillLevel(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def ExtraPassiveSkillLevel(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def CommonSkillLevel(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def LeaderSkillLevel(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def EquipSlot01(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(28))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0


    def EquipSlotTier01(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(30))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def EquipSlotLevel01(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(32))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def EquipSlot02(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(34))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0


    def EquipSlotTier02(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(36))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def EquipSlotLevel02(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(38))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def EquipSlot03(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(40))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0


    def EquipSlotTier03(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(42))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def EquipSlotLevel03(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(44))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def EquipCharacterWeapon(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(46))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0


    def EquipCharacterWeaponTier(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(48))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def EquipCharacterWeaponLevel(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(50))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def EquipCharacterGear(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(52))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0


    def EquipCharacterGearTier(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(54))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def EquipCharacterGearLevel(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(56))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def PotentialType01(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(58))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def PotentialLevel01(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(60))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def PotentialType02(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(62))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def PotentialLevel02(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(64))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def PotentialType03(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(66))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def PotentialLevel03(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(68))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0




    @staticmethod
    def Start(builder): builder.StartObject(33)
    @staticmethod
    def End(builder): return builder.EndObject()


    @staticmethod
    def AddPresetCharacterGroupId(builder, PresetCharacterGroupId): builder.PrependInt64Slot(0, PresetCharacterGroupId, 0)


    @staticmethod
    def AddGetPresetType(builder, GetPresetType): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(GetPresetType), 0)

    @staticmethod
    def AddLevel(builder, Level): builder.PrependInt32Slot(2, Level, 0)


    @staticmethod
    def AddExp(builder, Exp): builder.PrependInt32Slot(3, Exp, 0)


    @staticmethod
    def AddFavorExp(builder, FavorExp): builder.PrependInt32Slot(4, FavorExp, 0)


    @staticmethod
    def AddFavorRank(builder, FavorRank): builder.PrependInt32Slot(5, FavorRank, 0)


    @staticmethod
    def AddStarGrade(builder, StarGrade): builder.PrependInt32Slot(6, StarGrade, 0)


    @staticmethod
    def AddExSkillLevel(builder, ExSkillLevel): builder.PrependInt32Slot(7, ExSkillLevel, 0)


    @staticmethod
    def AddPassiveSkillLevel(builder, PassiveSkillLevel): builder.PrependInt32Slot(8, PassiveSkillLevel, 0)


    @staticmethod
    def AddExtraPassiveSkillLevel(builder, ExtraPassiveSkillLevel): builder.PrependInt32Slot(9, ExtraPassiveSkillLevel, 0)


    @staticmethod
    def AddCommonSkillLevel(builder, CommonSkillLevel): builder.PrependInt32Slot(10, CommonSkillLevel, 0)


    @staticmethod
    def AddLeaderSkillLevel(builder, LeaderSkillLevel): builder.PrependInt32Slot(11, LeaderSkillLevel, 0)


    @staticmethod
    def AddEquipSlot01(builder, EquipSlot01): builder.PrependBoolSlot(12, EquipSlot01, 0)


    @staticmethod
    def AddEquipSlotTier01(builder, EquipSlotTier01): builder.PrependInt32Slot(13, EquipSlotTier01, 0)


    @staticmethod
    def AddEquipSlotLevel01(builder, EquipSlotLevel01): builder.PrependInt32Slot(14, EquipSlotLevel01, 0)


    @staticmethod
    def AddEquipSlot02(builder, EquipSlot02): builder.PrependBoolSlot(15, EquipSlot02, 0)


    @staticmethod
    def AddEquipSlotTier02(builder, EquipSlotTier02): builder.PrependInt32Slot(16, EquipSlotTier02, 0)


    @staticmethod
    def AddEquipSlotLevel02(builder, EquipSlotLevel02): builder.PrependInt32Slot(17, EquipSlotLevel02, 0)


    @staticmethod
    def AddEquipSlot03(builder, EquipSlot03): builder.PrependBoolSlot(18, EquipSlot03, 0)


    @staticmethod
    def AddEquipSlotTier03(builder, EquipSlotTier03): builder.PrependInt32Slot(19, EquipSlotTier03, 0)


    @staticmethod
    def AddEquipSlotLevel03(builder, EquipSlotLevel03): builder.PrependInt32Slot(20, EquipSlotLevel03, 0)


    @staticmethod
    def AddEquipCharacterWeapon(builder, EquipCharacterWeapon): builder.PrependBoolSlot(21, EquipCharacterWeapon, 0)


    @staticmethod
    def AddEquipCharacterWeaponTier(builder, EquipCharacterWeaponTier): builder.PrependInt32Slot(22, EquipCharacterWeaponTier, 0)


    @staticmethod
    def AddEquipCharacterWeaponLevel(builder, EquipCharacterWeaponLevel): builder.PrependInt32Slot(23, EquipCharacterWeaponLevel, 0)


    @staticmethod
    def AddEquipCharacterGear(builder, EquipCharacterGear): builder.PrependBoolSlot(24, EquipCharacterGear, 0)


    @staticmethod
    def AddEquipCharacterGearTier(builder, EquipCharacterGearTier): builder.PrependInt32Slot(25, EquipCharacterGearTier, 0)


    @staticmethod
    def AddEquipCharacterGearLevel(builder, EquipCharacterGearLevel): builder.PrependInt32Slot(26, EquipCharacterGearLevel, 0)


    @staticmethod
    def AddPotentialType01(builder, PotentialType01): builder.PrependInt32Slot(27, PotentialType01, 0)


    @staticmethod
    def AddPotentialLevel01(builder, PotentialLevel01): builder.PrependInt32Slot(28, PotentialLevel01, 0)


    @staticmethod
    def AddPotentialType02(builder, PotentialType02): builder.PrependInt32Slot(29, PotentialType02, 0)


    @staticmethod
    def AddPotentialLevel02(builder, PotentialLevel02): builder.PrependInt32Slot(30, PotentialLevel02, 0)


    @staticmethod
    def AddPotentialType03(builder, PotentialType03): builder.PrependInt32Slot(31, PotentialType03, 0)


    @staticmethod
    def AddPotentialLevel03(builder, PotentialLevel03): builder.PrependInt32Slot(32, PotentialLevel03, 0)

