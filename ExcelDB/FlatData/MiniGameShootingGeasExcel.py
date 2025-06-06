
import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class MiniGameShootingGeasExcel:
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = MiniGameShootingGeasExcel()
        x.Init(buf, n + offset)
        return x

    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)


    def UniqueId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def GeasType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def Icon(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def Probability(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def MaxOverlapCount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def GeasData(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def NeedGeasId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def HideInPausePopup(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0




    @staticmethod
    def Start(builder): builder.StartObject(8)
    @staticmethod
    def End(builder): return builder.EndObject()


    @staticmethod
    def AddUniqueId(builder, UniqueId): builder.PrependInt64Slot(0, UniqueId, 0)


    @staticmethod
    def AddGeasType(builder, GeasType): builder.PrependInt32Slot(1, GeasType, 0)


    @staticmethod
    def AddIcon(builder, Icon): builder.PrependUOffsetTRelativeSlot(2, flatbuffers.number_types.UOffsetTFlags.py_type(Icon), 0)

    @staticmethod
    def AddProbability(builder, Probability): builder.PrependInt64Slot(3, Probability, 0)


    @staticmethod
    def AddMaxOverlapCount(builder, MaxOverlapCount): builder.PrependInt32Slot(4, MaxOverlapCount, 0)


    @staticmethod
    def AddGeasData(builder, GeasData): builder.PrependUOffsetTRelativeSlot(5, flatbuffers.number_types.UOffsetTFlags.py_type(GeasData), 0)

    @staticmethod
    def AddNeedGeasId(builder, NeedGeasId): builder.PrependInt64Slot(6, NeedGeasId, 0)


    @staticmethod
    def AddHideInPausePopup(builder, HideInPausePopup): builder.PrependBoolSlot(7, HideInPausePopup, 0)

