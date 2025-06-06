
import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class EventContentBuffGroupExcel:
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = EventContentBuffGroupExcel()
        x.Init(buf, n + offset)
        return x

    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)


    def EventContentId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def BuffContentId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def BuffGroupId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def BuffGroupNameLocalizeCodeId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def EventContentBuffId1(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def BuffNameLocalizeCodeId1(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def BuffDescriptionIconPath1(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def EventContentBuffId2(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def BuffNameLocalizeCodeId2(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def BuffDescriptionIconPath2(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def EventContentDebuffId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def DebuffNameLocalizeCodeId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def DeBuffDescriptionIconPath(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(28))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def BuffGroupProb(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(30))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0




    @staticmethod
    def Start(builder): builder.StartObject(14)
    @staticmethod
    def End(builder): return builder.EndObject()


    @staticmethod
    def AddEventContentId(builder, EventContentId): builder.PrependInt64Slot(0, EventContentId, 0)


    @staticmethod
    def AddBuffContentId(builder, BuffContentId): builder.PrependInt64Slot(1, BuffContentId, 0)


    @staticmethod
    def AddBuffGroupId(builder, BuffGroupId): builder.PrependInt64Slot(2, BuffGroupId, 0)


    @staticmethod
    def AddBuffGroupNameLocalizeCodeId(builder, BuffGroupNameLocalizeCodeId): builder.PrependUOffsetTRelativeSlot(3, flatbuffers.number_types.UOffsetTFlags.py_type(BuffGroupNameLocalizeCodeId), 0)

    @staticmethod
    def AddEventContentBuffId1(builder, EventContentBuffId1): builder.PrependInt64Slot(4, EventContentBuffId1, 0)


    @staticmethod
    def AddBuffNameLocalizeCodeId1(builder, BuffNameLocalizeCodeId1): builder.PrependUOffsetTRelativeSlot(5, flatbuffers.number_types.UOffsetTFlags.py_type(BuffNameLocalizeCodeId1), 0)

    @staticmethod
    def AddBuffDescriptionIconPath1(builder, BuffDescriptionIconPath1): builder.PrependUOffsetTRelativeSlot(6, flatbuffers.number_types.UOffsetTFlags.py_type(BuffDescriptionIconPath1), 0)

    @staticmethod
    def AddEventContentBuffId2(builder, EventContentBuffId2): builder.PrependInt64Slot(7, EventContentBuffId2, 0)


    @staticmethod
    def AddBuffNameLocalizeCodeId2(builder, BuffNameLocalizeCodeId2): builder.PrependUOffsetTRelativeSlot(8, flatbuffers.number_types.UOffsetTFlags.py_type(BuffNameLocalizeCodeId2), 0)

    @staticmethod
    def AddBuffDescriptionIconPath2(builder, BuffDescriptionIconPath2): builder.PrependUOffsetTRelativeSlot(9, flatbuffers.number_types.UOffsetTFlags.py_type(BuffDescriptionIconPath2), 0)

    @staticmethod
    def AddEventContentDebuffId(builder, EventContentDebuffId): builder.PrependInt64Slot(10, EventContentDebuffId, 0)


    @staticmethod
    def AddDebuffNameLocalizeCodeId(builder, DebuffNameLocalizeCodeId): builder.PrependUOffsetTRelativeSlot(11, flatbuffers.number_types.UOffsetTFlags.py_type(DebuffNameLocalizeCodeId), 0)

    @staticmethod
    def AddDeBuffDescriptionIconPath(builder, DeBuffDescriptionIconPath): builder.PrependUOffsetTRelativeSlot(12, flatbuffers.number_types.UOffsetTFlags.py_type(DeBuffDescriptionIconPath), 0)

    @staticmethod
    def AddBuffGroupProb(builder, BuffGroupProb): builder.PrependInt64Slot(13, BuffGroupProb, 0)

