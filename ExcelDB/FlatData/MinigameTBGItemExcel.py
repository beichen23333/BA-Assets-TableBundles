
import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class MinigameTBGItemExcel:
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = MinigameTBGItemExcel()
        x.Init(buf, n + offset)
        return x

    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)


    def UniqueId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def ItemType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def TBGItemEffectType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def ItemParameter(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def LocalizeETCId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def Icon(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def BuffIcon(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def EncounterCount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def DiceEffectAniClip(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def BuffIconHUDVisible(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0




    @staticmethod
    def Start(builder): builder.StartObject(10)
    @staticmethod
    def End(builder): return builder.EndObject()


    @staticmethod
    def AddUniqueId(builder, UniqueId): builder.PrependInt64Slot(0, UniqueId, 0)


    @staticmethod
    def AddItemType(builder, ItemType): builder.PrependInt32Slot(1, ItemType, 0)


    @staticmethod
    def AddTBGItemEffectType(builder, TBGItemEffectType): builder.PrependInt32Slot(2, TBGItemEffectType, 0)


    @staticmethod
    def AddItemParameter(builder, ItemParameter): builder.PrependInt32Slot(3, ItemParameter, 0)


    @staticmethod
    def AddLocalizeETCId(builder, LocalizeETCId): builder.PrependUOffsetTRelativeSlot(4, flatbuffers.number_types.UOffsetTFlags.py_type(LocalizeETCId), 0)

    @staticmethod
    def AddIcon(builder, Icon): builder.PrependUOffsetTRelativeSlot(5, flatbuffers.number_types.UOffsetTFlags.py_type(Icon), 0)

    @staticmethod
    def AddBuffIcon(builder, BuffIcon): builder.PrependUOffsetTRelativeSlot(6, flatbuffers.number_types.UOffsetTFlags.py_type(BuffIcon), 0)

    @staticmethod
    def AddEncounterCount(builder, EncounterCount): builder.PrependInt32Slot(7, EncounterCount, 0)


    @staticmethod
    def AddDiceEffectAniClip(builder, DiceEffectAniClip): builder.PrependUOffsetTRelativeSlot(8, flatbuffers.number_types.UOffsetTFlags.py_type(DiceEffectAniClip), 0)

    @staticmethod
    def AddBuffIconHUDVisible(builder, BuffIconHUDVisible): builder.PrependBoolSlot(9, BuffIconHUDVisible, 0)

