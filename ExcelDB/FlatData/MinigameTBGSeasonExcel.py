
import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class MinigameTBGSeasonExcel:
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = MinigameTBGSeasonExcel()
        x.Init(buf, n + offset)
        return x

    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)


    def EventContentId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def ItemSlot(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def DefaultEchelonHp(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def DefaultItemDiceId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def EchelonSlot1CharacterId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def EchelonSlot2CharacterId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def EchelonSlot3CharacterId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def EchelonSlot4CharacterId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def EchelonSlot1Portrait(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def EchelonSlot2Portrait(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def EchelonSlot3Portrait(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def EchelonSlot4Portrait(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def EventUseCostType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(28))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def EventUseCostId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(30))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def EchelonRevivalCostType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(32))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def EchelonRevivalCostId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(34))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def EchelonRevivalCostAmount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(36))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def EnemyBossHP(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(38))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def EnemyMinionHP(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(40))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def AttackDamage(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(42))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def CriticalAttackDamage(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(44))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def RoundItemSelectLimit(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(46))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def InstantClearRound(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(48))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def MaxHp(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(50))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def MapImagePath(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(52))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def MapNameLocalize(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(54))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def StartThemaIndex(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(56))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def LoopThemaIndex(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(58))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def MaxDicePlus(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(60))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0




    @staticmethod
    def Start(builder): builder.StartObject(29)
    @staticmethod
    def End(builder): return builder.EndObject()


    @staticmethod
    def AddEventContentId(builder, EventContentId): builder.PrependInt64Slot(0, EventContentId, 0)


    @staticmethod
    def AddItemSlot(builder, ItemSlot): builder.PrependInt32Slot(1, ItemSlot, 0)


    @staticmethod
    def AddDefaultEchelonHp(builder, DefaultEchelonHp): builder.PrependInt32Slot(2, DefaultEchelonHp, 0)


    @staticmethod
    def AddDefaultItemDiceId(builder, DefaultItemDiceId): builder.PrependInt64Slot(3, DefaultItemDiceId, 0)


    @staticmethod
    def AddEchelonSlot1CharacterId(builder, EchelonSlot1CharacterId): builder.PrependInt64Slot(4, EchelonSlot1CharacterId, 0)


    @staticmethod
    def AddEchelonSlot2CharacterId(builder, EchelonSlot2CharacterId): builder.PrependInt64Slot(5, EchelonSlot2CharacterId, 0)


    @staticmethod
    def AddEchelonSlot3CharacterId(builder, EchelonSlot3CharacterId): builder.PrependInt64Slot(6, EchelonSlot3CharacterId, 0)


    @staticmethod
    def AddEchelonSlot4CharacterId(builder, EchelonSlot4CharacterId): builder.PrependInt64Slot(7, EchelonSlot4CharacterId, 0)


    @staticmethod
    def AddEchelonSlot1Portrait(builder, EchelonSlot1Portrait): builder.PrependUOffsetTRelativeSlot(8, flatbuffers.number_types.UOffsetTFlags.py_type(EchelonSlot1Portrait), 0)

    @staticmethod
    def AddEchelonSlot2Portrait(builder, EchelonSlot2Portrait): builder.PrependUOffsetTRelativeSlot(9, flatbuffers.number_types.UOffsetTFlags.py_type(EchelonSlot2Portrait), 0)

    @staticmethod
    def AddEchelonSlot3Portrait(builder, EchelonSlot3Portrait): builder.PrependUOffsetTRelativeSlot(10, flatbuffers.number_types.UOffsetTFlags.py_type(EchelonSlot3Portrait), 0)

    @staticmethod
    def AddEchelonSlot4Portrait(builder, EchelonSlot4Portrait): builder.PrependUOffsetTRelativeSlot(11, flatbuffers.number_types.UOffsetTFlags.py_type(EchelonSlot4Portrait), 0)

    @staticmethod
    def AddEventUseCostType(builder, EventUseCostType): builder.PrependInt32Slot(12, EventUseCostType, 0)


    @staticmethod
    def AddEventUseCostId(builder, EventUseCostId): builder.PrependInt64Slot(13, EventUseCostId, 0)


    @staticmethod
    def AddEchelonRevivalCostType(builder, EchelonRevivalCostType): builder.PrependInt32Slot(14, EchelonRevivalCostType, 0)


    @staticmethod
    def AddEchelonRevivalCostId(builder, EchelonRevivalCostId): builder.PrependInt64Slot(15, EchelonRevivalCostId, 0)


    @staticmethod
    def AddEchelonRevivalCostAmount(builder, EchelonRevivalCostAmount): builder.PrependInt32Slot(16, EchelonRevivalCostAmount, 0)


    @staticmethod
    def AddEnemyBossHP(builder, EnemyBossHP): builder.PrependInt32Slot(17, EnemyBossHP, 0)


    @staticmethod
    def AddEnemyMinionHP(builder, EnemyMinionHP): builder.PrependInt32Slot(18, EnemyMinionHP, 0)


    @staticmethod
    def AddAttackDamage(builder, AttackDamage): builder.PrependInt32Slot(19, AttackDamage, 0)


    @staticmethod
    def AddCriticalAttackDamage(builder, CriticalAttackDamage): builder.PrependInt32Slot(20, CriticalAttackDamage, 0)


    @staticmethod
    def AddRoundItemSelectLimit(builder, RoundItemSelectLimit): builder.PrependInt32Slot(21, RoundItemSelectLimit, 0)


    @staticmethod
    def AddInstantClearRound(builder, InstantClearRound): builder.PrependInt32Slot(22, InstantClearRound, 0)


    @staticmethod
    def AddMaxHp(builder, MaxHp): builder.PrependInt32Slot(23, MaxHp, 0)


    @staticmethod
    def AddMapImagePath(builder, MapImagePath): builder.PrependUOffsetTRelativeSlot(24, flatbuffers.number_types.UOffsetTFlags.py_type(MapImagePath), 0)

    @staticmethod
    def AddMapNameLocalize(builder, MapNameLocalize): builder.PrependUOffsetTRelativeSlot(25, flatbuffers.number_types.UOffsetTFlags.py_type(MapNameLocalize), 0)

    @staticmethod
    def AddStartThemaIndex(builder, StartThemaIndex): builder.PrependInt32Slot(26, StartThemaIndex, 0)


    @staticmethod
    def AddLoopThemaIndex(builder, LoopThemaIndex): builder.PrependInt32Slot(27, LoopThemaIndex, 0)


    @staticmethod
    def AddMaxDicePlus(builder, MaxDicePlus): builder.PrependInt32Slot(28, MaxDicePlus, 0)

