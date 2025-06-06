
import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class MiniGameRhythmBgmExcel:
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = MiniGameRhythmBgmExcel()
        x.Init(buf, n + offset)
        return x

    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)


    def RhythmBgmId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def EventContentId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def StageSelectImagePath(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def Bpm(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def Bgm(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def BgmNameText(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def BgmArtistText(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def HasLyricist(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0


    def BgmComposerText(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def BgmLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0




    @staticmethod
    def Start(builder): builder.StartObject(10)
    @staticmethod
    def End(builder): return builder.EndObject()


    @staticmethod
    def AddRhythmBgmId(builder, RhythmBgmId): builder.PrependInt64Slot(0, RhythmBgmId, 0)


    @staticmethod
    def AddEventContentId(builder, EventContentId): builder.PrependInt64Slot(1, EventContentId, 0)


    @staticmethod
    def AddStageSelectImagePath(builder, StageSelectImagePath): builder.PrependUOffsetTRelativeSlot(2, flatbuffers.number_types.UOffsetTFlags.py_type(StageSelectImagePath), 0)

    @staticmethod
    def AddBpm(builder, Bpm): builder.PrependInt64Slot(3, Bpm, 0)


    @staticmethod
    def AddBgm(builder, Bgm): builder.PrependInt64Slot(4, Bgm, 0)


    @staticmethod
    def AddBgmNameText(builder, BgmNameText): builder.PrependUOffsetTRelativeSlot(5, flatbuffers.number_types.UOffsetTFlags.py_type(BgmNameText), 0)

    @staticmethod
    def AddBgmArtistText(builder, BgmArtistText): builder.PrependUOffsetTRelativeSlot(6, flatbuffers.number_types.UOffsetTFlags.py_type(BgmArtistText), 0)

    @staticmethod
    def AddHasLyricist(builder, HasLyricist): builder.PrependBoolSlot(7, HasLyricist, 0)


    @staticmethod
    def AddBgmComposerText(builder, BgmComposerText): builder.PrependUOffsetTRelativeSlot(8, flatbuffers.number_types.UOffsetTFlags.py_type(BgmComposerText), 0)

    @staticmethod
    def AddBgmLength(builder, BgmLength): builder.PrependInt32Slot(9, BgmLength, 0)

