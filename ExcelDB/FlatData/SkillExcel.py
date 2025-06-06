
import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class SkillExcel:
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = SkillExcel()
        x.Init(buf, n + offset)
        return x

    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)


    def Id(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def LocalizeSkillId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0


    def GroupId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def SkillDataKey(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def VisualDataKey(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def Level(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def SkillCost(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def ExtraSkillCost(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def EnemySkillCost(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def ExtraEnemySkillCost(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def NPCSkillCost(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def ExtraNPCSkillCost(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def BulletType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(28))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def StartCoolTime(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(30))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def CoolTime(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(32))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def EnemyStartCoolTime(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(34))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def EnemyCoolTime(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(36))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def NPCStartCoolTime(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(38))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def NPCCoolTime(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(40))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def UseAtg(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(42))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def RequireCharacterLevel(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(44))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def RequireLevelUpMaterial(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(46))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def IconName(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(48))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def IsShowInfo(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(50))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0


    def IsShowSpeechbubble(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(52))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0


    def PublicSpeechDuration(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(54))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def AdditionalToolTipId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(56))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def TextureSkillCardForFormConversion(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(58))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def SkillCardLabelPath(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(60))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None




    @staticmethod
    def Start(builder): builder.StartObject(29)
    @staticmethod
    def End(builder): return builder.EndObject()


    @staticmethod
    def AddId(builder, Id): builder.PrependInt64Slot(0, Id, 0)


    @staticmethod
    def AddLocalizeSkillId(builder, LocalizeSkillId): builder.PrependUint32Slot(1, LocalizeSkillId, 0)


    @staticmethod
    def AddGroupId(builder, GroupId): builder.PrependUOffsetTRelativeSlot(2, flatbuffers.number_types.UOffsetTFlags.py_type(GroupId), 0)

    @staticmethod
    def AddSkillDataKey(builder, SkillDataKey): builder.PrependUOffsetTRelativeSlot(3, flatbuffers.number_types.UOffsetTFlags.py_type(SkillDataKey), 0)

    @staticmethod
    def AddVisualDataKey(builder, VisualDataKey): builder.PrependUOffsetTRelativeSlot(4, flatbuffers.number_types.UOffsetTFlags.py_type(VisualDataKey), 0)

    @staticmethod
    def AddLevel(builder, Level): builder.PrependInt32Slot(5, Level, 0)


    @staticmethod
    def AddSkillCost(builder, SkillCost): builder.PrependInt32Slot(6, SkillCost, 0)


    @staticmethod
    def AddExtraSkillCost(builder, ExtraSkillCost): builder.PrependInt32Slot(7, ExtraSkillCost, 0)


    @staticmethod
    def AddEnemySkillCost(builder, EnemySkillCost): builder.PrependInt32Slot(8, EnemySkillCost, 0)


    @staticmethod
    def AddExtraEnemySkillCost(builder, ExtraEnemySkillCost): builder.PrependInt32Slot(9, ExtraEnemySkillCost, 0)


    @staticmethod
    def AddNPCSkillCost(builder, NPCSkillCost): builder.PrependInt32Slot(10, NPCSkillCost, 0)


    @staticmethod
    def AddExtraNPCSkillCost(builder, ExtraNPCSkillCost): builder.PrependInt32Slot(11, ExtraNPCSkillCost, 0)


    @staticmethod
    def AddBulletType(builder, BulletType): builder.PrependInt32Slot(12, BulletType, 0)


    @staticmethod
    def AddStartCoolTime(builder, StartCoolTime): builder.PrependInt32Slot(13, StartCoolTime, 0)


    @staticmethod
    def AddCoolTime(builder, CoolTime): builder.PrependInt32Slot(14, CoolTime, 0)


    @staticmethod
    def AddEnemyStartCoolTime(builder, EnemyStartCoolTime): builder.PrependInt32Slot(15, EnemyStartCoolTime, 0)


    @staticmethod
    def AddEnemyCoolTime(builder, EnemyCoolTime): builder.PrependInt32Slot(16, EnemyCoolTime, 0)


    @staticmethod
    def AddNPCStartCoolTime(builder, NPCStartCoolTime): builder.PrependInt32Slot(17, NPCStartCoolTime, 0)


    @staticmethod
    def AddNPCCoolTime(builder, NPCCoolTime): builder.PrependInt32Slot(18, NPCCoolTime, 0)


    @staticmethod
    def AddUseAtg(builder, UseAtg): builder.PrependInt32Slot(19, UseAtg, 0)


    @staticmethod
    def AddRequireCharacterLevel(builder, RequireCharacterLevel): builder.PrependInt32Slot(20, RequireCharacterLevel, 0)


    @staticmethod
    def AddRequireLevelUpMaterial(builder, RequireLevelUpMaterial): builder.PrependInt64Slot(21, RequireLevelUpMaterial, 0)


    @staticmethod
    def AddIconName(builder, IconName): builder.PrependUOffsetTRelativeSlot(22, flatbuffers.number_types.UOffsetTFlags.py_type(IconName), 0)

    @staticmethod
    def AddIsShowInfo(builder, IsShowInfo): builder.PrependBoolSlot(23, IsShowInfo, 0)


    @staticmethod
    def AddIsShowSpeechbubble(builder, IsShowSpeechbubble): builder.PrependBoolSlot(24, IsShowSpeechbubble, 0)


    @staticmethod
    def AddPublicSpeechDuration(builder, PublicSpeechDuration): builder.PrependInt32Slot(25, PublicSpeechDuration, 0)


    @staticmethod
    def AddAdditionalToolTipId(builder, AdditionalToolTipId): builder.PrependInt64Slot(26, AdditionalToolTipId, 0)


    @staticmethod
    def AddTextureSkillCardForFormConversion(builder, TextureSkillCardForFormConversion): builder.PrependUOffsetTRelativeSlot(27, flatbuffers.number_types.UOffsetTFlags.py_type(TextureSkillCardForFormConversion), 0)

    @staticmethod
    def AddSkillCardLabelPath(builder, SkillCardLabelPath): builder.PrependUOffsetTRelativeSlot(28, flatbuffers.number_types.UOffsetTFlags.py_type(SkillCardLabelPath), 0)
