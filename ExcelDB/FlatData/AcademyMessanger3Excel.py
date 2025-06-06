
import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class AcademyMessanger3Excel:
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = AcademyMessanger3Excel()
        x.Init(buf, n + offset)
        return x

    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)


    def MessageGroupId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def Id(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def CharacterId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def MessageCondition(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def ConditionValue(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def PreConditionGroupId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def PreConditionFavorScheduleId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def FavorScheduleId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def NextGroupId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def FeedbackTimeMillisec(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def MessageType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def ImagePath(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def MessageKR(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(28))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def MessageJP(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(30))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None




    @staticmethod
    def Start(builder): builder.StartObject(14)
    @staticmethod
    def End(builder): return builder.EndObject()


    @staticmethod
    def AddMessageGroupId(builder, MessageGroupId): builder.PrependInt64Slot(0, MessageGroupId, 0)


    @staticmethod
    def AddId(builder, Id): builder.PrependInt64Slot(1, Id, 0)


    @staticmethod
    def AddCharacterId(builder, CharacterId): builder.PrependInt64Slot(2, CharacterId, 0)


    @staticmethod
    def AddMessageCondition(builder, MessageCondition): builder.PrependInt32Slot(3, MessageCondition, 0)


    @staticmethod
    def AddConditionValue(builder, ConditionValue): builder.PrependInt64Slot(4, ConditionValue, 0)


    @staticmethod
    def AddPreConditionGroupId(builder, PreConditionGroupId): builder.PrependInt64Slot(5, PreConditionGroupId, 0)


    @staticmethod
    def AddPreConditionFavorScheduleId(builder, PreConditionFavorScheduleId): builder.PrependInt64Slot(6, PreConditionFavorScheduleId, 0)


    @staticmethod
    def AddFavorScheduleId(builder, FavorScheduleId): builder.PrependInt64Slot(7, FavorScheduleId, 0)


    @staticmethod
    def AddNextGroupId(builder, NextGroupId): builder.PrependInt64Slot(8, NextGroupId, 0)


    @staticmethod
    def AddFeedbackTimeMillisec(builder, FeedbackTimeMillisec): builder.PrependInt64Slot(9, FeedbackTimeMillisec, 0)


    @staticmethod
    def AddMessageType(builder, MessageType): builder.PrependInt32Slot(10, MessageType, 0)


    @staticmethod
    def AddImagePath(builder, ImagePath): builder.PrependUOffsetTRelativeSlot(11, flatbuffers.number_types.UOffsetTFlags.py_type(ImagePath), 0)

    @staticmethod
    def AddMessageKR(builder, MessageKR): builder.PrependUOffsetTRelativeSlot(12, flatbuffers.number_types.UOffsetTFlags.py_type(MessageKR), 0)

    @staticmethod
    def AddMessageJP(builder, MessageJP): builder.PrependUOffsetTRelativeSlot(13, flatbuffers.number_types.UOffsetTFlags.py_type(MessageJP), 0)
