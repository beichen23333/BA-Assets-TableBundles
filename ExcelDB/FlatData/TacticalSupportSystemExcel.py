
import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class TacticalSupportSystemExcel:
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = TacticalSupportSystemExcel()
        x.Init(buf, n + offset)
        return x

    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)


    def Id(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def SummonedTime(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def DefaultPersonalityId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def CanTargeting(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0


    def CanCover(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0


    def ObstacleUniqueName(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def ObstacleCoverRange(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def SummonSkilllGroupId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def CrashObstacleOBBWidth(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def CrashObstacleOBBHeight(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def IsTSSBlockedNodeCheck(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0


    def NumberOfUses(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def InventoryOffsetX(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(28))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0


    def InventoryOffsetY(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(30))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0


    def InventoryOffsetZ(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(32))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0


    def InteractionChar(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(34))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def CharacterInteractionStartDelay(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(36))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def GetOnStartEffectPath(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(38))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def GetOnEndEffectPath(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(40))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def SummonerCharacterId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(42))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def InteractionFrame(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(44))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def TSAInteractionAddDuration(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(46))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def InteractionStudentExSkillGroupId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(48))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def InteractionSkillCardTexture(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(50))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def InteractionSkillSpine(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(52))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def RetreatFrame(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(54))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def DestroyFrame(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(56))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0




    @staticmethod
    def Start(builder): builder.StartObject(27)
    @staticmethod
    def End(builder): return builder.EndObject()


    @staticmethod
    def AddId(builder, Id): builder.PrependInt64Slot(0, Id, 0)


    @staticmethod
    def AddSummonedTime(builder, SummonedTime): builder.PrependInt64Slot(1, SummonedTime, 0)


    @staticmethod
    def AddDefaultPersonalityId(builder, DefaultPersonalityId): builder.PrependInt64Slot(2, DefaultPersonalityId, 0)


    @staticmethod
    def AddCanTargeting(builder, CanTargeting): builder.PrependBoolSlot(3, CanTargeting, 0)


    @staticmethod
    def AddCanCover(builder, CanCover): builder.PrependBoolSlot(4, CanCover, 0)


    @staticmethod
    def AddObstacleUniqueName(builder, ObstacleUniqueName): builder.PrependUOffsetTRelativeSlot(5, flatbuffers.number_types.UOffsetTFlags.py_type(ObstacleUniqueName), 0)

    @staticmethod
    def AddObstacleCoverRange(builder, ObstacleCoverRange): builder.PrependInt64Slot(6, ObstacleCoverRange, 0)


    @staticmethod
    def AddSummonSkilllGroupId(builder, SummonSkilllGroupId): builder.PrependUOffsetTRelativeSlot(7, flatbuffers.number_types.UOffsetTFlags.py_type(SummonSkilllGroupId), 0)

    @staticmethod
    def AddCrashObstacleOBBWidth(builder, CrashObstacleOBBWidth): builder.PrependInt64Slot(8, CrashObstacleOBBWidth, 0)


    @staticmethod
    def AddCrashObstacleOBBHeight(builder, CrashObstacleOBBHeight): builder.PrependInt64Slot(9, CrashObstacleOBBHeight, 0)


    @staticmethod
    def AddIsTSSBlockedNodeCheck(builder, IsTSSBlockedNodeCheck): builder.PrependBoolSlot(10, IsTSSBlockedNodeCheck, 0)


    @staticmethod
    def AddNumberOfUses(builder, NumberOfUses): builder.PrependInt32Slot(11, NumberOfUses, 0)


    @staticmethod
    def AddInventoryOffsetX(builder, InventoryOffsetX): builder.PrependFloat32Slot(12, InventoryOffsetX, 0)


    @staticmethod
    def AddInventoryOffsetY(builder, InventoryOffsetY): builder.PrependFloat32Slot(13, InventoryOffsetY, 0)


    @staticmethod
    def AddInventoryOffsetZ(builder, InventoryOffsetZ): builder.PrependFloat32Slot(14, InventoryOffsetZ, 0)


    @staticmethod
    def AddInteractionChar(builder, InteractionChar): builder.PrependInt64Slot(15, InteractionChar, 0)


    @staticmethod
    def AddCharacterInteractionStartDelay(builder, CharacterInteractionStartDelay): builder.PrependInt64Slot(16, CharacterInteractionStartDelay, 0)


    @staticmethod
    def AddGetOnStartEffectPath(builder, GetOnStartEffectPath): builder.PrependUOffsetTRelativeSlot(17, flatbuffers.number_types.UOffsetTFlags.py_type(GetOnStartEffectPath), 0)

    @staticmethod
    def AddGetOnEndEffectPath(builder, GetOnEndEffectPath): builder.PrependUOffsetTRelativeSlot(18, flatbuffers.number_types.UOffsetTFlags.py_type(GetOnEndEffectPath), 0)

    @staticmethod
    def AddSummonerCharacterId(builder, SummonerCharacterId): builder.PrependInt64Slot(19, SummonerCharacterId, 0)


    @staticmethod
    def AddInteractionFrame(builder, InteractionFrame): builder.PrependInt32Slot(20, InteractionFrame, 0)


    @staticmethod
    def AddTSAInteractionAddDuration(builder, TSAInteractionAddDuration): builder.PrependInt64Slot(21, TSAInteractionAddDuration, 0)


    @staticmethod
    def AddInteractionStudentExSkillGroupId(builder, InteractionStudentExSkillGroupId): builder.PrependUOffsetTRelativeSlot(22, flatbuffers.number_types.UOffsetTFlags.py_type(InteractionStudentExSkillGroupId), 0)

    @staticmethod
    def AddInteractionSkillCardTexture(builder, InteractionSkillCardTexture): builder.PrependUOffsetTRelativeSlot(23, flatbuffers.number_types.UOffsetTFlags.py_type(InteractionSkillCardTexture), 0)

    @staticmethod
    def AddInteractionSkillSpine(builder, InteractionSkillSpine): builder.PrependUOffsetTRelativeSlot(24, flatbuffers.number_types.UOffsetTFlags.py_type(InteractionSkillSpine), 0)

    @staticmethod
    def AddRetreatFrame(builder, RetreatFrame): builder.PrependInt32Slot(25, RetreatFrame, 0)


    @staticmethod
    def AddDestroyFrame(builder, DestroyFrame): builder.PrependInt32Slot(26, DestroyFrame, 0)

