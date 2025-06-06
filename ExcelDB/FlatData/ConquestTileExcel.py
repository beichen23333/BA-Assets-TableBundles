
import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class ConquestTileExcel:
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = ConquestTileExcel()
        x.Init(buf, n + offset)
        return x

    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)


    def Id(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def Name(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def EventId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def Step(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def PrefabName(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def TileNameLocalize(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def TileImageName(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def Playable(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0


    def TileType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def NotMapFog(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0


    def GroupBonusId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def ConquestCostType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def ConquestCostId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(28))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def ConquestCostAmount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(30))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def ManageCostType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(32))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def ManageCostId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(34))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def ManageCostAmount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(36))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def ConquestRewardId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(38))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def MassErosionId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(40))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def Upgrade2CostType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(42))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def Upgrade2CostId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(44))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def Upgrade2CostAmount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(46))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def Upgrade3CostType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(48))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def Upgrade3CostId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(50))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def Upgrade3CostAmount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(52))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0




    @staticmethod
    def Start(builder): builder.StartObject(25)
    @staticmethod
    def End(builder): return builder.EndObject()


    @staticmethod
    def AddId(builder, Id): builder.PrependInt64Slot(0, Id, 0)


    @staticmethod
    def AddName(builder, Name): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(Name), 0)

    @staticmethod
    def AddEventId(builder, EventId): builder.PrependInt64Slot(2, EventId, 0)


    @staticmethod
    def AddStep(builder, Step): builder.PrependInt32Slot(3, Step, 0)


    @staticmethod
    def AddPrefabName(builder, PrefabName): builder.PrependUOffsetTRelativeSlot(4, flatbuffers.number_types.UOffsetTFlags.py_type(PrefabName), 0)

    @staticmethod
    def AddTileNameLocalize(builder, TileNameLocalize): builder.PrependUOffsetTRelativeSlot(5, flatbuffers.number_types.UOffsetTFlags.py_type(TileNameLocalize), 0)

    @staticmethod
    def AddTileImageName(builder, TileImageName): builder.PrependUOffsetTRelativeSlot(6, flatbuffers.number_types.UOffsetTFlags.py_type(TileImageName), 0)

    @staticmethod
    def AddPlayable(builder, Playable): builder.PrependBoolSlot(7, Playable, 0)


    @staticmethod
    def AddTileType(builder, TileType): builder.PrependInt32Slot(8, TileType, 0)


    @staticmethod
    def AddNotMapFog(builder, NotMapFog): builder.PrependBoolSlot(9, NotMapFog, 0)


    @staticmethod
    def AddGroupBonusId(builder, GroupBonusId): builder.PrependInt64Slot(10, GroupBonusId, 0)


    @staticmethod
    def AddConquestCostType(builder, ConquestCostType): builder.PrependInt32Slot(11, ConquestCostType, 0)


    @staticmethod
    def AddConquestCostId(builder, ConquestCostId): builder.PrependInt64Slot(12, ConquestCostId, 0)


    @staticmethod
    def AddConquestCostAmount(builder, ConquestCostAmount): builder.PrependInt32Slot(13, ConquestCostAmount, 0)


    @staticmethod
    def AddManageCostType(builder, ManageCostType): builder.PrependInt32Slot(14, ManageCostType, 0)


    @staticmethod
    def AddManageCostId(builder, ManageCostId): builder.PrependInt64Slot(15, ManageCostId, 0)


    @staticmethod
    def AddManageCostAmount(builder, ManageCostAmount): builder.PrependInt32Slot(16, ManageCostAmount, 0)


    @staticmethod
    def AddConquestRewardId(builder, ConquestRewardId): builder.PrependInt64Slot(17, ConquestRewardId, 0)


    @staticmethod
    def AddMassErosionId(builder, MassErosionId): builder.PrependInt64Slot(18, MassErosionId, 0)


    @staticmethod
    def AddUpgrade2CostType(builder, Upgrade2CostType): builder.PrependInt32Slot(19, Upgrade2CostType, 0)


    @staticmethod
    def AddUpgrade2CostId(builder, Upgrade2CostId): builder.PrependInt64Slot(20, Upgrade2CostId, 0)


    @staticmethod
    def AddUpgrade2CostAmount(builder, Upgrade2CostAmount): builder.PrependInt32Slot(21, Upgrade2CostAmount, 0)


    @staticmethod
    def AddUpgrade3CostType(builder, Upgrade3CostType): builder.PrependInt32Slot(22, Upgrade3CostType, 0)


    @staticmethod
    def AddUpgrade3CostId(builder, Upgrade3CostId): builder.PrependInt64Slot(23, Upgrade3CostId, 0)


    @staticmethod
    def AddUpgrade3CostAmount(builder, Upgrade3CostAmount): builder.PrependInt32Slot(24, Upgrade3CostAmount, 0)

