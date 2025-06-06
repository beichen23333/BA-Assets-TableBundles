
import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class FieldSeasonExcel:
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = FieldSeasonExcel()
        x.Init(buf, n + offset)
        return x

    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)


    def UniqueId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def EventContentId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def EntryDateId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def InstantEntryDateId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def StartDate(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def EndDate(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def LobbyBGMChangeStageId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def FieldPrefabControlID(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def FieldGetKeywordCallDialogEnum(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def MasteryImagePath(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def FieldLobbyTitleImagePath(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def KeywordLogoImagePath(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None




    @staticmethod
    def Start(builder): builder.StartObject(12)
    @staticmethod
    def End(builder): return builder.EndObject()


    @staticmethod
    def AddUniqueId(builder, UniqueId): builder.PrependInt64Slot(0, UniqueId, 0)


    @staticmethod
    def AddEventContentId(builder, EventContentId): builder.PrependInt64Slot(1, EventContentId, 0)


    @staticmethod
    def AddEntryDateId(builder, EntryDateId): builder.PrependInt64Slot(2, EntryDateId, 0)


    @staticmethod
    def AddInstantEntryDateId(builder, InstantEntryDateId): builder.PrependInt64Slot(3, InstantEntryDateId, 0)


    @staticmethod
    def AddStartDate(builder, StartDate): builder.PrependUOffsetTRelativeSlot(4, flatbuffers.number_types.UOffsetTFlags.py_type(StartDate), 0)

    @staticmethod
    def AddEndDate(builder, EndDate): builder.PrependUOffsetTRelativeSlot(5, flatbuffers.number_types.UOffsetTFlags.py_type(EndDate), 0)

    @staticmethod
    def AddLobbyBGMChangeStageId(builder, LobbyBGMChangeStageId): builder.PrependInt64Slot(6, LobbyBGMChangeStageId, 0)


    @staticmethod
    def AddFieldPrefabControlID(builder, FieldPrefabControlID): builder.PrependInt64Slot(7, FieldPrefabControlID, 0)


    @staticmethod
    def AddFieldGetKeywordCallDialogEnum(builder, FieldGetKeywordCallDialogEnum): builder.PrependInt32Slot(8, FieldGetKeywordCallDialogEnum, 0)


    @staticmethod
    def AddMasteryImagePath(builder, MasteryImagePath): builder.PrependUOffsetTRelativeSlot(9, flatbuffers.number_types.UOffsetTFlags.py_type(MasteryImagePath), 0)

    @staticmethod
    def AddFieldLobbyTitleImagePath(builder, FieldLobbyTitleImagePath): builder.PrependUOffsetTRelativeSlot(10, flatbuffers.number_types.UOffsetTFlags.py_type(FieldLobbyTitleImagePath), 0)

    @staticmethod
    def AddKeywordLogoImagePath(builder, KeywordLogoImagePath): builder.PrependUOffsetTRelativeSlot(11, flatbuffers.number_types.UOffsetTFlags.py_type(KeywordLogoImagePath), 0)
