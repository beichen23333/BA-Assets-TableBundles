
import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class MinigameTBGEncounterOptionExcel:
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = MinigameTBGEncounterOptionExcel()
        x.Init(buf, n + offset)
        return x

    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)


    def OptionGroupId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def UniqueId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def SlotIndex(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def OptionTitleLocalize(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def OptionSuccessLocalize(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def OptionSuccessRewardGroupId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def OptionSuccessOrHigherDiceCount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def OptionGreatSuccessOrHigherDiceCount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def OptionFailLocalize(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def OptionFailLessDiceCount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def RunawayOrHigherDiceCount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def RewardHide(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0




    @staticmethod
    def Start(builder): builder.StartObject(12)
    @staticmethod
    def End(builder): return builder.EndObject()


    @staticmethod
    def AddOptionGroupId(builder, OptionGroupId): builder.PrependInt64Slot(0, OptionGroupId, 0)


    @staticmethod
    def AddUniqueId(builder, UniqueId): builder.PrependInt64Slot(1, UniqueId, 0)


    @staticmethod
    def AddSlotIndex(builder, SlotIndex): builder.PrependInt32Slot(2, SlotIndex, 0)


    @staticmethod
    def AddOptionTitleLocalize(builder, OptionTitleLocalize): builder.PrependUOffsetTRelativeSlot(3, flatbuffers.number_types.UOffsetTFlags.py_type(OptionTitleLocalize), 0)

    @staticmethod
    def AddOptionSuccessLocalize(builder, OptionSuccessLocalize): builder.PrependUOffsetTRelativeSlot(4, flatbuffers.number_types.UOffsetTFlags.py_type(OptionSuccessLocalize), 0)

    @staticmethod
    def AddOptionSuccessRewardGroupId(builder, OptionSuccessRewardGroupId): builder.PrependInt64Slot(5, OptionSuccessRewardGroupId, 0)


    @staticmethod
    def AddOptionSuccessOrHigherDiceCount(builder, OptionSuccessOrHigherDiceCount): builder.PrependInt32Slot(6, OptionSuccessOrHigherDiceCount, 0)


    @staticmethod
    def AddOptionGreatSuccessOrHigherDiceCount(builder, OptionGreatSuccessOrHigherDiceCount): builder.PrependInt32Slot(7, OptionGreatSuccessOrHigherDiceCount, 0)


    @staticmethod
    def AddOptionFailLocalize(builder, OptionFailLocalize): builder.PrependUOffsetTRelativeSlot(8, flatbuffers.number_types.UOffsetTFlags.py_type(OptionFailLocalize), 0)

    @staticmethod
    def AddOptionFailLessDiceCount(builder, OptionFailLessDiceCount): builder.PrependInt32Slot(9, OptionFailLessDiceCount, 0)


    @staticmethod
    def AddRunawayOrHigherDiceCount(builder, RunawayOrHigherDiceCount): builder.PrependInt32Slot(10, RunawayOrHigherDiceCount, 0)


    @staticmethod
    def AddRewardHide(builder, RewardHide): builder.PrependBoolSlot(11, RewardHide, 0)

