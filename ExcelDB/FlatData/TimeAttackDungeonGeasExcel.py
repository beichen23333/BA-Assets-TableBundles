
import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class TimeAttackDungeonGeasExcel:
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = TimeAttackDungeonGeasExcel()
        x.Init(buf, n + offset)
        return x

    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)


    def Id(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def TimeAttackDungeonType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def LocalizeEtcKey(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0


    def BattleDuration(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def ClearDefaultPoint(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def ClearTimeWeightPoint(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def TimeWeightConst(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def Difficulty(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def RecommandLevel(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def GroundId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def AllyPassiveSkillId(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.String(a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return ""

    def AllyPassiveSkillIdLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    def AllyPassiveSkillIdIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        return o == 0


    def AllyPassiveSkillLevel(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int32Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return 0

    def AllyPassiveSkillLevelAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int32Flags, o)
        return 0

    def AllyPassiveSkillLevelLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    def AllyPassiveSkillLevelIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        return o == 0


    def EnemyPassiveSkillId(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(28))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.String(a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return ""

    def EnemyPassiveSkillIdLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(28))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    def EnemyPassiveSkillIdIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(28))
        return o == 0


    def EnemyPassiveSkillLevel(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(30))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int32Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return 0

    def EnemyPassiveSkillLevelAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(30))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int32Flags, o)
        return 0

    def EnemyPassiveSkillLevelLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(30))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    def EnemyPassiveSkillLevelIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(30))
        return o == 0


    def GeasIconPath(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(32))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.String(a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return ""

    def GeasIconPathLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(32))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    def GeasIconPathIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(32))
        return o == 0


    def GeasLocalizeEtcKey(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(34))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return 0

    def GeasLocalizeEtcKeyAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(34))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Uint32Flags, o)
        return 0

    def GeasLocalizeEtcKeyLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(34))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    def GeasLocalizeEtcKeyIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(34))
        return o == 0




    @staticmethod
    def Start(builder): builder.StartObject(16)
    @staticmethod
    def End(builder): return builder.EndObject()


    @staticmethod
    def AddId(builder, Id): builder.PrependInt64Slot(0, Id, 0)


    @staticmethod
    def AddTimeAttackDungeonType(builder, TimeAttackDungeonType): builder.PrependInt32Slot(1, TimeAttackDungeonType, 0)


    @staticmethod
    def AddLocalizeEtcKey(builder, LocalizeEtcKey): builder.PrependUint32Slot(2, LocalizeEtcKey, 0)


    @staticmethod
    def AddBattleDuration(builder, BattleDuration): builder.PrependInt64Slot(3, BattleDuration, 0)


    @staticmethod
    def AddClearDefaultPoint(builder, ClearDefaultPoint): builder.PrependInt64Slot(4, ClearDefaultPoint, 0)


    @staticmethod
    def AddClearTimeWeightPoint(builder, ClearTimeWeightPoint): builder.PrependInt64Slot(5, ClearTimeWeightPoint, 0)


    @staticmethod
    def AddTimeWeightConst(builder, TimeWeightConst): builder.PrependInt64Slot(6, TimeWeightConst, 0)


    @staticmethod
    def AddDifficulty(builder, Difficulty): builder.PrependInt32Slot(7, Difficulty, 0)


    @staticmethod
    def AddRecommandLevel(builder, RecommandLevel): builder.PrependInt32Slot(8, RecommandLevel, 0)


    @staticmethod
    def AddGroundId(builder, GroundId): builder.PrependInt64Slot(9, GroundId, 0)


    @staticmethod
    def AddAllyPassiveSkillId(builder, AllyPassiveSkillId): builder.PrependUOffsetTRelativeSlot(10, flatbuffers.number_types.UOffsetTFlags.py_type(AllyPassiveSkillId), 0)
    @staticmethod
    def StartAllyPassiveSkillIdVector(builder, numElems): return builder.StartVector(4, numElems, 4)


    @staticmethod
    def AddAllyPassiveSkillLevel(builder, AllyPassiveSkillLevel): builder.PrependUOffsetTRelativeSlot(11, flatbuffers.number_types.UOffsetTFlags.py_type(AllyPassiveSkillLevel), 0)
    @staticmethod
    def StartAllyPassiveSkillLevelVector(builder, numElems): return builder.StartVector(4, numElems, 4)


    @staticmethod
    def AddEnemyPassiveSkillId(builder, EnemyPassiveSkillId): builder.PrependUOffsetTRelativeSlot(12, flatbuffers.number_types.UOffsetTFlags.py_type(EnemyPassiveSkillId), 0)
    @staticmethod
    def StartEnemyPassiveSkillIdVector(builder, numElems): return builder.StartVector(4, numElems, 4)


    @staticmethod
    def AddEnemyPassiveSkillLevel(builder, EnemyPassiveSkillLevel): builder.PrependUOffsetTRelativeSlot(13, flatbuffers.number_types.UOffsetTFlags.py_type(EnemyPassiveSkillLevel), 0)
    @staticmethod
    def StartEnemyPassiveSkillLevelVector(builder, numElems): return builder.StartVector(4, numElems, 4)


    @staticmethod
    def AddGeasIconPath(builder, GeasIconPath): builder.PrependUOffsetTRelativeSlot(14, flatbuffers.number_types.UOffsetTFlags.py_type(GeasIconPath), 0)
    @staticmethod
    def StartGeasIconPathVector(builder, numElems): return builder.StartVector(4, numElems, 4)


    @staticmethod
    def AddGeasLocalizeEtcKey(builder, GeasLocalizeEtcKey): builder.PrependUOffsetTRelativeSlot(15, flatbuffers.number_types.UOffsetTFlags.py_type(GeasLocalizeEtcKey), 0)
    @staticmethod
    def StartGeasLocalizeEtcKeyVector(builder, numElems): return builder.StartVector(4, numElems, 4)

