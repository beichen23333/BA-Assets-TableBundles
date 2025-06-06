
import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class ParcelAutoSynthExcel:
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = ParcelAutoSynthExcel()
        x.Init(buf, n + offset)
        return x

    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)


    def RequireParcelType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def RequireParcelId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def RequireParcelAmount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def SynthStartAmount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def SynthEndAmount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def SynthMaxItem(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0


    def ResultParcelType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def ResultParcelId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def ResultParcelAmount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0




    @staticmethod
    def Start(builder): builder.StartObject(9)
    @staticmethod
    def End(builder): return builder.EndObject()


    @staticmethod
    def AddRequireParcelType(builder, RequireParcelType): builder.PrependInt32Slot(0, RequireParcelType, 0)


    @staticmethod
    def AddRequireParcelId(builder, RequireParcelId): builder.PrependInt64Slot(1, RequireParcelId, 0)


    @staticmethod
    def AddRequireParcelAmount(builder, RequireParcelAmount): builder.PrependInt64Slot(2, RequireParcelAmount, 0)


    @staticmethod
    def AddSynthStartAmount(builder, SynthStartAmount): builder.PrependInt64Slot(3, SynthStartAmount, 0)


    @staticmethod
    def AddSynthEndAmount(builder, SynthEndAmount): builder.PrependInt64Slot(4, SynthEndAmount, 0)


    @staticmethod
    def AddSynthMaxItem(builder, SynthMaxItem): builder.PrependBoolSlot(5, SynthMaxItem, 0)


    @staticmethod
    def AddResultParcelType(builder, ResultParcelType): builder.PrependInt32Slot(6, ResultParcelType, 0)


    @staticmethod
    def AddResultParcelId(builder, ResultParcelId): builder.PrependInt64Slot(7, ResultParcelId, 0)


    @staticmethod
    def AddResultParcelAmount(builder, ResultParcelAmount): builder.PrependInt64Slot(8, ResultParcelAmount, 0)

