
import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class CharacterSkillListExcel:
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = CharacterSkillListExcel()
        x.Init(buf, n + offset)
        return x

    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)


    def CharacterSkillListGroupId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def MinimumGradeCharacterWeapon(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def MinimumTierCharacterGear(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def FormIndex(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def IsRootMotion(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0


    def IsMoveLeftRight(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0


    def UseRandomExSkillTimeline(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0


    def TSAInteractionId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def NormalSkillGroupId(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.String(a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return ""

    def NormalSkillGroupIdLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    def NormalSkillGroupIdIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        return o == 0


    def NormalSkillTimeLineIndex(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int32Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return 0

    def NormalSkillTimeLineIndexAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int32Flags, o)
        return 0

    def NormalSkillTimeLineIndexLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    def NormalSkillTimeLineIndexIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        return o == 0


    def ExSkillGroupId(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.String(a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return ""

    def ExSkillGroupIdLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    def ExSkillGroupIdIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        return o == 0


    def ExSkillCutInTimeLineIndex(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.String(a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return ""

    def ExSkillCutInTimeLineIndexLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    def ExSkillCutInTimeLineIndexIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        return o == 0


    def ExSkillLevelTimeLineIndex(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(28))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.String(a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return ""

    def ExSkillLevelTimeLineIndexLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(28))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    def ExSkillLevelTimeLineIndexIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(28))
        return o == 0


    def PublicSkillGroupId(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(30))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.String(a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return ""

    def PublicSkillGroupIdLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(30))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    def PublicSkillGroupIdIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(30))
        return o == 0


    def PublicSkillTimeLineIndex(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(32))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int32Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return 0

    def PublicSkillTimeLineIndexAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(32))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int32Flags, o)
        return 0

    def PublicSkillTimeLineIndexLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(32))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    def PublicSkillTimeLineIndexIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(32))
        return o == 0


    def PassiveSkillGroupId(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(34))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.String(a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return ""

    def PassiveSkillGroupIdLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(34))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    def PassiveSkillGroupIdIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(34))
        return o == 0


    def LeaderSkillGroupId(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(36))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.String(a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return ""

    def LeaderSkillGroupIdLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(36))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    def LeaderSkillGroupIdIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(36))
        return o == 0


    def ExtraPassiveSkillGroupId(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(38))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.String(a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return ""

    def ExtraPassiveSkillGroupIdLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(38))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    def ExtraPassiveSkillGroupIdIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(38))
        return o == 0


    def HiddenPassiveSkillGroupId(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(40))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.String(a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return ""

    def HiddenPassiveSkillGroupIdLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(40))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    def HiddenPassiveSkillGroupIdIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(40))
        return o == 0




    @staticmethod
    def Start(builder): builder.StartObject(19)
    @staticmethod
    def End(builder): return builder.EndObject()


    @staticmethod
    def AddCharacterSkillListGroupId(builder, CharacterSkillListGroupId): builder.PrependInt64Slot(0, CharacterSkillListGroupId, 0)


    @staticmethod
    def AddMinimumGradeCharacterWeapon(builder, MinimumGradeCharacterWeapon): builder.PrependInt32Slot(1, MinimumGradeCharacterWeapon, 0)


    @staticmethod
    def AddMinimumTierCharacterGear(builder, MinimumTierCharacterGear): builder.PrependInt32Slot(2, MinimumTierCharacterGear, 0)


    @staticmethod
    def AddFormIndex(builder, FormIndex): builder.PrependInt32Slot(3, FormIndex, 0)


    @staticmethod
    def AddIsRootMotion(builder, IsRootMotion): builder.PrependBoolSlot(4, IsRootMotion, 0)


    @staticmethod
    def AddIsMoveLeftRight(builder, IsMoveLeftRight): builder.PrependBoolSlot(5, IsMoveLeftRight, 0)


    @staticmethod
    def AddUseRandomExSkillTimeline(builder, UseRandomExSkillTimeline): builder.PrependBoolSlot(6, UseRandomExSkillTimeline, 0)


    @staticmethod
    def AddTSAInteractionId(builder, TSAInteractionId): builder.PrependInt64Slot(7, TSAInteractionId, 0)


    @staticmethod
    def AddNormalSkillGroupId(builder, NormalSkillGroupId): builder.PrependUOffsetTRelativeSlot(8, flatbuffers.number_types.UOffsetTFlags.py_type(NormalSkillGroupId), 0)
    @staticmethod
    def StartNormalSkillGroupIdVector(builder, numElems): return builder.StartVector(4, numElems, 4)


    @staticmethod
    def AddNormalSkillTimeLineIndex(builder, NormalSkillTimeLineIndex): builder.PrependUOffsetTRelativeSlot(9, flatbuffers.number_types.UOffsetTFlags.py_type(NormalSkillTimeLineIndex), 0)
    @staticmethod
    def StartNormalSkillTimeLineIndexVector(builder, numElems): return builder.StartVector(4, numElems, 4)


    @staticmethod
    def AddExSkillGroupId(builder, ExSkillGroupId): builder.PrependUOffsetTRelativeSlot(10, flatbuffers.number_types.UOffsetTFlags.py_type(ExSkillGroupId), 0)
    @staticmethod
    def StartExSkillGroupIdVector(builder, numElems): return builder.StartVector(4, numElems, 4)


    @staticmethod
    def AddExSkillCutInTimeLineIndex(builder, ExSkillCutInTimeLineIndex): builder.PrependUOffsetTRelativeSlot(11, flatbuffers.number_types.UOffsetTFlags.py_type(ExSkillCutInTimeLineIndex), 0)
    @staticmethod
    def StartExSkillCutInTimeLineIndexVector(builder, numElems): return builder.StartVector(4, numElems, 4)


    @staticmethod
    def AddExSkillLevelTimeLineIndex(builder, ExSkillLevelTimeLineIndex): builder.PrependUOffsetTRelativeSlot(12, flatbuffers.number_types.UOffsetTFlags.py_type(ExSkillLevelTimeLineIndex), 0)
    @staticmethod
    def StartExSkillLevelTimeLineIndexVector(builder, numElems): return builder.StartVector(4, numElems, 4)


    @staticmethod
    def AddPublicSkillGroupId(builder, PublicSkillGroupId): builder.PrependUOffsetTRelativeSlot(13, flatbuffers.number_types.UOffsetTFlags.py_type(PublicSkillGroupId), 0)
    @staticmethod
    def StartPublicSkillGroupIdVector(builder, numElems): return builder.StartVector(4, numElems, 4)


    @staticmethod
    def AddPublicSkillTimeLineIndex(builder, PublicSkillTimeLineIndex): builder.PrependUOffsetTRelativeSlot(14, flatbuffers.number_types.UOffsetTFlags.py_type(PublicSkillTimeLineIndex), 0)
    @staticmethod
    def StartPublicSkillTimeLineIndexVector(builder, numElems): return builder.StartVector(4, numElems, 4)


    @staticmethod
    def AddPassiveSkillGroupId(builder, PassiveSkillGroupId): builder.PrependUOffsetTRelativeSlot(15, flatbuffers.number_types.UOffsetTFlags.py_type(PassiveSkillGroupId), 0)
    @staticmethod
    def StartPassiveSkillGroupIdVector(builder, numElems): return builder.StartVector(4, numElems, 4)


    @staticmethod
    def AddLeaderSkillGroupId(builder, LeaderSkillGroupId): builder.PrependUOffsetTRelativeSlot(16, flatbuffers.number_types.UOffsetTFlags.py_type(LeaderSkillGroupId), 0)
    @staticmethod
    def StartLeaderSkillGroupIdVector(builder, numElems): return builder.StartVector(4, numElems, 4)


    @staticmethod
    def AddExtraPassiveSkillGroupId(builder, ExtraPassiveSkillGroupId): builder.PrependUOffsetTRelativeSlot(17, flatbuffers.number_types.UOffsetTFlags.py_type(ExtraPassiveSkillGroupId), 0)
    @staticmethod
    def StartExtraPassiveSkillGroupIdVector(builder, numElems): return builder.StartVector(4, numElems, 4)


    @staticmethod
    def AddHiddenPassiveSkillGroupId(builder, HiddenPassiveSkillGroupId): builder.PrependUOffsetTRelativeSlot(18, flatbuffers.number_types.UOffsetTFlags.py_type(HiddenPassiveSkillGroupId), 0)
    @staticmethod
    def StartHiddenPassiveSkillGroupIdVector(builder, numElems): return builder.StartVector(4, numElems, 4)

