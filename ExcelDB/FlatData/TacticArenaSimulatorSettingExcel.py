
import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class TacticArenaSimulatorSettingExcel:
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = TacticArenaSimulatorSettingExcel()
        x.Init(buf, n + offset)
        return x

    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)


    def Order(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def Repeat(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def AttackerFrom(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def AttackerUserArenaGroup(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def AttackerUserArenaRank(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def AttackerPresetGroupId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def AttackerStrikerNum(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def AttackerSpecialNum(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def DefenderFrom(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def DefenderUserArenaGroup(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def DefenderUserArenaRank(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def DefenderPresetGroupId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def DefenderStrikerNum(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(28))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def DefenderSpecialNum(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(30))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def GroundId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(32))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0




    @staticmethod
    def Start(builder): builder.StartObject(15)
    @staticmethod
    def End(builder): return builder.EndObject()


    @staticmethod
    def AddOrder(builder, Order): builder.PrependInt64Slot(0, Order, 0)


    @staticmethod
    def AddRepeat(builder, Repeat): builder.PrependInt64Slot(1, Repeat, 0)


    @staticmethod
    def AddAttackerFrom(builder, AttackerFrom): builder.PrependInt32Slot(2, AttackerFrom, 0)


    @staticmethod
    def AddAttackerUserArenaGroup(builder, AttackerUserArenaGroup): builder.PrependInt64Slot(3, AttackerUserArenaGroup, 0)


    @staticmethod
    def AddAttackerUserArenaRank(builder, AttackerUserArenaRank): builder.PrependInt64Slot(4, AttackerUserArenaRank, 0)


    @staticmethod
    def AddAttackerPresetGroupId(builder, AttackerPresetGroupId): builder.PrependInt64Slot(5, AttackerPresetGroupId, 0)


    @staticmethod
    def AddAttackerStrikerNum(builder, AttackerStrikerNum): builder.PrependInt64Slot(6, AttackerStrikerNum, 0)


    @staticmethod
    def AddAttackerSpecialNum(builder, AttackerSpecialNum): builder.PrependInt64Slot(7, AttackerSpecialNum, 0)


    @staticmethod
    def AddDefenderFrom(builder, DefenderFrom): builder.PrependInt32Slot(8, DefenderFrom, 0)


    @staticmethod
    def AddDefenderUserArenaGroup(builder, DefenderUserArenaGroup): builder.PrependInt64Slot(9, DefenderUserArenaGroup, 0)


    @staticmethod
    def AddDefenderUserArenaRank(builder, DefenderUserArenaRank): builder.PrependInt64Slot(10, DefenderUserArenaRank, 0)


    @staticmethod
    def AddDefenderPresetGroupId(builder, DefenderPresetGroupId): builder.PrependInt64Slot(11, DefenderPresetGroupId, 0)


    @staticmethod
    def AddDefenderStrikerNum(builder, DefenderStrikerNum): builder.PrependInt64Slot(12, DefenderStrikerNum, 0)


    @staticmethod
    def AddDefenderSpecialNum(builder, DefenderSpecialNum): builder.PrependInt64Slot(13, DefenderSpecialNum, 0)


    @staticmethod
    def AddGroundId(builder, GroundId): builder.PrependInt64Slot(14, GroundId, 0)

