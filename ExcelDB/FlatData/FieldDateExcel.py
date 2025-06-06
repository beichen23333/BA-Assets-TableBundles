
import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class FieldDateExcel:
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = FieldDateExcel()
        x.Init(buf, n + offset)
        return x

    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)


    def SeasonId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def UniqueId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def OpenDate(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def DateLocalizeKey(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def EntrySceneId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def StartConditionType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def StartConditionId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def EndConditionType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def EndConditionId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def EndReadyConditionType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def EndReadyConditionId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def OpenConditionStage(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def CharacterIconPath(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(28))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def DateResultBGPath(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(30))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def DateResultSpinePath(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(32))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def DateResultSpineOffsetX(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(34))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0




    @staticmethod
    def Start(builder): builder.StartObject(16)
    @staticmethod
    def End(builder): return builder.EndObject()


    @staticmethod
    def AddSeasonId(builder, SeasonId): builder.PrependInt64Slot(0, SeasonId, 0)


    @staticmethod
    def AddUniqueId(builder, UniqueId): builder.PrependInt64Slot(1, UniqueId, 0)


    @staticmethod
    def AddOpenDate(builder, OpenDate): builder.PrependInt64Slot(2, OpenDate, 0)


    @staticmethod
    def AddDateLocalizeKey(builder, DateLocalizeKey): builder.PrependUOffsetTRelativeSlot(3, flatbuffers.number_types.UOffsetTFlags.py_type(DateLocalizeKey), 0)

    @staticmethod
    def AddEntrySceneId(builder, EntrySceneId): builder.PrependInt64Slot(4, EntrySceneId, 0)


    @staticmethod
    def AddStartConditionType(builder, StartConditionType): builder.PrependInt32Slot(5, StartConditionType, 0)


    @staticmethod
    def AddStartConditionId(builder, StartConditionId): builder.PrependInt64Slot(6, StartConditionId, 0)


    @staticmethod
    def AddEndConditionType(builder, EndConditionType): builder.PrependInt32Slot(7, EndConditionType, 0)


    @staticmethod
    def AddEndConditionId(builder, EndConditionId): builder.PrependInt64Slot(8, EndConditionId, 0)


    @staticmethod
    def AddEndReadyConditionType(builder, EndReadyConditionType): builder.PrependInt32Slot(9, EndReadyConditionType, 0)


    @staticmethod
    def AddEndReadyConditionId(builder, EndReadyConditionId): builder.PrependInt64Slot(10, EndReadyConditionId, 0)


    @staticmethod
    def AddOpenConditionStage(builder, OpenConditionStage): builder.PrependInt64Slot(11, OpenConditionStage, 0)


    @staticmethod
    def AddCharacterIconPath(builder, CharacterIconPath): builder.PrependUOffsetTRelativeSlot(12, flatbuffers.number_types.UOffsetTFlags.py_type(CharacterIconPath), 0)

    @staticmethod
    def AddDateResultBGPath(builder, DateResultBGPath): builder.PrependUOffsetTRelativeSlot(13, flatbuffers.number_types.UOffsetTFlags.py_type(DateResultBGPath), 0)

    @staticmethod
    def AddDateResultSpinePath(builder, DateResultSpinePath): builder.PrependUOffsetTRelativeSlot(14, flatbuffers.number_types.UOffsetTFlags.py_type(DateResultSpinePath), 0)

    @staticmethod
    def AddDateResultSpineOffsetX(builder, DateResultSpineOffsetX): builder.PrependFloat32Slot(15, DateResultSpineOffsetX, 0)

