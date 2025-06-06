
import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class TacticDamageSimulatorSettingExcel:
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = TacticDamageSimulatorSettingExcel()
        x.Init(buf, n + offset)
        return x

    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)


    def Order(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def Repeat(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def TestPreset(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def TestBattleTime(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def StrikerSquard(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def SpecialSquard(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def ReplaceCharacterCostRegen(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0


    def ReplaceCostRegenValue(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def UseAutoSkill(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0


    def OverrideStreetAdaptation(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def OverrideOutdoorAdaptation(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def OverrideIndoorAdaptation(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def ApplyOverrideAdaptation(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(28))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0


    def OverrideFavorLevel(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(30))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def ApplyOverrideFavorLevel(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(32))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0


    def GroundId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(34))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def FixedCharacter(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(36))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int64Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 8))
        return 0

    def FixedCharacterAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(36))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int64Flags, o)
        return 0

    def FixedCharacterLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(36))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    def FixedCharacterIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(36))
        return o == 0




    @staticmethod
    def Start(builder): builder.StartObject(17)
    @staticmethod
    def End(builder): return builder.EndObject()


    @staticmethod
    def AddOrder(builder, Order): builder.PrependInt32Slot(0, Order, 0)


    @staticmethod
    def AddRepeat(builder, Repeat): builder.PrependInt32Slot(1, Repeat, 0)


    @staticmethod
    def AddTestPreset(builder, TestPreset): builder.PrependInt64Slot(2, TestPreset, 0)


    @staticmethod
    def AddTestBattleTime(builder, TestBattleTime): builder.PrependInt64Slot(3, TestBattleTime, 0)


    @staticmethod
    def AddStrikerSquard(builder, StrikerSquard): builder.PrependInt64Slot(4, StrikerSquard, 0)


    @staticmethod
    def AddSpecialSquard(builder, SpecialSquard): builder.PrependInt64Slot(5, SpecialSquard, 0)


    @staticmethod
    def AddReplaceCharacterCostRegen(builder, ReplaceCharacterCostRegen): builder.PrependBoolSlot(6, ReplaceCharacterCostRegen, 0)


    @staticmethod
    def AddReplaceCostRegenValue(builder, ReplaceCostRegenValue): builder.PrependInt32Slot(7, ReplaceCostRegenValue, 0)


    @staticmethod
    def AddUseAutoSkill(builder, UseAutoSkill): builder.PrependBoolSlot(8, UseAutoSkill, 0)


    @staticmethod
    def AddOverrideStreetAdaptation(builder, OverrideStreetAdaptation): builder.PrependInt32Slot(9, OverrideStreetAdaptation, 0)


    @staticmethod
    def AddOverrideOutdoorAdaptation(builder, OverrideOutdoorAdaptation): builder.PrependInt32Slot(10, OverrideOutdoorAdaptation, 0)


    @staticmethod
    def AddOverrideIndoorAdaptation(builder, OverrideIndoorAdaptation): builder.PrependInt32Slot(11, OverrideIndoorAdaptation, 0)


    @staticmethod
    def AddApplyOverrideAdaptation(builder, ApplyOverrideAdaptation): builder.PrependBoolSlot(12, ApplyOverrideAdaptation, 0)


    @staticmethod
    def AddOverrideFavorLevel(builder, OverrideFavorLevel): builder.PrependInt32Slot(13, OverrideFavorLevel, 0)


    @staticmethod
    def AddApplyOverrideFavorLevel(builder, ApplyOverrideFavorLevel): builder.PrependBoolSlot(14, ApplyOverrideFavorLevel, 0)


    @staticmethod
    def AddGroundId(builder, GroundId): builder.PrependInt64Slot(15, GroundId, 0)


    @staticmethod
    def AddFixedCharacter(builder, FixedCharacter): builder.PrependUOffsetTRelativeSlot(16, flatbuffers.number_types.UOffsetTFlags.py_type(FixedCharacter), 0)
    @staticmethod
    def StartFixedCharacterVector(builder, numElems): return builder.StartVector(8, numElems, 8)

