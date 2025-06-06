
import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class MiniGameDefenseFixedStatExcel:
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = MiniGameDefenseFixedStatExcel()
        x.Init(buf, n + offset)
        return x

    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)


    def MinigameDefenseFixedStatId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def Level(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def Grade(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def ExSkillLevel(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def NoneExSkillLevel(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def Equipment1Tier(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def Equipment1Level(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def Equipment2Tier(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def Equipment2Level(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def Equipment3Tier(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def Equipment3Level(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def CharacterWeaponGrade(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def CharacterWeaponLevel(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(28))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def CharacterGearTier(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(30))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def CharacterGearLevel(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(32))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0




    @staticmethod
    def Start(builder): builder.StartObject(15)
    @staticmethod
    def End(builder): return builder.EndObject()


    @staticmethod
    def AddMinigameDefenseFixedStatId(builder, MinigameDefenseFixedStatId): builder.PrependInt64Slot(0, MinigameDefenseFixedStatId, 0)


    @staticmethod
    def AddLevel(builder, Level): builder.PrependInt32Slot(1, Level, 0)


    @staticmethod
    def AddGrade(builder, Grade): builder.PrependInt32Slot(2, Grade, 0)


    @staticmethod
    def AddExSkillLevel(builder, ExSkillLevel): builder.PrependInt32Slot(3, ExSkillLevel, 0)


    @staticmethod
    def AddNoneExSkillLevel(builder, NoneExSkillLevel): builder.PrependInt32Slot(4, NoneExSkillLevel, 0)


    @staticmethod
    def AddEquipment1Tier(builder, Equipment1Tier): builder.PrependInt32Slot(5, Equipment1Tier, 0)


    @staticmethod
    def AddEquipment1Level(builder, Equipment1Level): builder.PrependInt32Slot(6, Equipment1Level, 0)


    @staticmethod
    def AddEquipment2Tier(builder, Equipment2Tier): builder.PrependInt32Slot(7, Equipment2Tier, 0)


    @staticmethod
    def AddEquipment2Level(builder, Equipment2Level): builder.PrependInt32Slot(8, Equipment2Level, 0)


    @staticmethod
    def AddEquipment3Tier(builder, Equipment3Tier): builder.PrependInt32Slot(9, Equipment3Tier, 0)


    @staticmethod
    def AddEquipment3Level(builder, Equipment3Level): builder.PrependInt32Slot(10, Equipment3Level, 0)


    @staticmethod
    def AddCharacterWeaponGrade(builder, CharacterWeaponGrade): builder.PrependInt32Slot(11, CharacterWeaponGrade, 0)


    @staticmethod
    def AddCharacterWeaponLevel(builder, CharacterWeaponLevel): builder.PrependInt32Slot(12, CharacterWeaponLevel, 0)


    @staticmethod
    def AddCharacterGearTier(builder, CharacterGearTier): builder.PrependInt32Slot(13, CharacterGearTier, 0)


    @staticmethod
    def AddCharacterGearLevel(builder, CharacterGearLevel): builder.PrependInt32Slot(14, CharacterGearLevel, 0)

