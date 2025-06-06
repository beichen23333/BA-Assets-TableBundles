
import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class MinigameTBGEncounterExcel:
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = MinigameTBGEncounterExcel()
        x.Init(buf, n + offset)
        return x

    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)


    def EventContentId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def UniqueId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def AllThema(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0


    def ThemaIndex(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def ThemaType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def ObjectType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def EnemyImagePath(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def EnemyPrefabName(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def EnemyNameLocalize(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def OptionGroupId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def RewardHide(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0


    def EncounterTitleLocalize(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def StoryImagePath(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(28))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def BeforeStoryLocalize(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(30))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def BeforeStoryOption1Localize(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(32))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def BeforeStoryOption2Localize(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(34))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def BeforeStoryOption3Localize(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(36))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def AllyAttackLocalize(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(38))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def EnemyAttackLocalize(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(40))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def AttackDefenceLocalize(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(42))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def ClearStoryLocalize(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(44))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def DefeatStoryLocalize(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(46))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def RunawayStoryLocalize(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(48))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None




    @staticmethod
    def Start(builder): builder.StartObject(23)
    @staticmethod
    def End(builder): return builder.EndObject()


    @staticmethod
    def AddEventContentId(builder, EventContentId): builder.PrependInt64Slot(0, EventContentId, 0)


    @staticmethod
    def AddUniqueId(builder, UniqueId): builder.PrependInt64Slot(1, UniqueId, 0)


    @staticmethod
    def AddAllThema(builder, AllThema): builder.PrependBoolSlot(2, AllThema, 0)


    @staticmethod
    def AddThemaIndex(builder, ThemaIndex): builder.PrependInt32Slot(3, ThemaIndex, 0)


    @staticmethod
    def AddThemaType(builder, ThemaType): builder.PrependInt32Slot(4, ThemaType, 0)


    @staticmethod
    def AddObjectType(builder, ObjectType): builder.PrependInt32Slot(5, ObjectType, 0)


    @staticmethod
    def AddEnemyImagePath(builder, EnemyImagePath): builder.PrependUOffsetTRelativeSlot(6, flatbuffers.number_types.UOffsetTFlags.py_type(EnemyImagePath), 0)

    @staticmethod
    def AddEnemyPrefabName(builder, EnemyPrefabName): builder.PrependUOffsetTRelativeSlot(7, flatbuffers.number_types.UOffsetTFlags.py_type(EnemyPrefabName), 0)

    @staticmethod
    def AddEnemyNameLocalize(builder, EnemyNameLocalize): builder.PrependUOffsetTRelativeSlot(8, flatbuffers.number_types.UOffsetTFlags.py_type(EnemyNameLocalize), 0)

    @staticmethod
    def AddOptionGroupId(builder, OptionGroupId): builder.PrependInt64Slot(9, OptionGroupId, 0)


    @staticmethod
    def AddRewardHide(builder, RewardHide): builder.PrependBoolSlot(10, RewardHide, 0)


    @staticmethod
    def AddEncounterTitleLocalize(builder, EncounterTitleLocalize): builder.PrependUOffsetTRelativeSlot(11, flatbuffers.number_types.UOffsetTFlags.py_type(EncounterTitleLocalize), 0)

    @staticmethod
    def AddStoryImagePath(builder, StoryImagePath): builder.PrependUOffsetTRelativeSlot(12, flatbuffers.number_types.UOffsetTFlags.py_type(StoryImagePath), 0)

    @staticmethod
    def AddBeforeStoryLocalize(builder, BeforeStoryLocalize): builder.PrependUOffsetTRelativeSlot(13, flatbuffers.number_types.UOffsetTFlags.py_type(BeforeStoryLocalize), 0)

    @staticmethod
    def AddBeforeStoryOption1Localize(builder, BeforeStoryOption1Localize): builder.PrependUOffsetTRelativeSlot(14, flatbuffers.number_types.UOffsetTFlags.py_type(BeforeStoryOption1Localize), 0)

    @staticmethod
    def AddBeforeStoryOption2Localize(builder, BeforeStoryOption2Localize): builder.PrependUOffsetTRelativeSlot(15, flatbuffers.number_types.UOffsetTFlags.py_type(BeforeStoryOption2Localize), 0)

    @staticmethod
    def AddBeforeStoryOption3Localize(builder, BeforeStoryOption3Localize): builder.PrependUOffsetTRelativeSlot(16, flatbuffers.number_types.UOffsetTFlags.py_type(BeforeStoryOption3Localize), 0)

    @staticmethod
    def AddAllyAttackLocalize(builder, AllyAttackLocalize): builder.PrependUOffsetTRelativeSlot(17, flatbuffers.number_types.UOffsetTFlags.py_type(AllyAttackLocalize), 0)

    @staticmethod
    def AddEnemyAttackLocalize(builder, EnemyAttackLocalize): builder.PrependUOffsetTRelativeSlot(18, flatbuffers.number_types.UOffsetTFlags.py_type(EnemyAttackLocalize), 0)

    @staticmethod
    def AddAttackDefenceLocalize(builder, AttackDefenceLocalize): builder.PrependUOffsetTRelativeSlot(19, flatbuffers.number_types.UOffsetTFlags.py_type(AttackDefenceLocalize), 0)

    @staticmethod
    def AddClearStoryLocalize(builder, ClearStoryLocalize): builder.PrependUOffsetTRelativeSlot(20, flatbuffers.number_types.UOffsetTFlags.py_type(ClearStoryLocalize), 0)

    @staticmethod
    def AddDefeatStoryLocalize(builder, DefeatStoryLocalize): builder.PrependUOffsetTRelativeSlot(21, flatbuffers.number_types.UOffsetTFlags.py_type(DefeatStoryLocalize), 0)

    @staticmethod
    def AddRunawayStoryLocalize(builder, RunawayStoryLocalize): builder.PrependUOffsetTRelativeSlot(22, flatbuffers.number_types.UOffsetTFlags.py_type(RunawayStoryLocalize), 0)
