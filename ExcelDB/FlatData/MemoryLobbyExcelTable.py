
import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class MemoryLobbyExcelTable:
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = MemoryLobbyExcelTable()
        x.Init(buf, n + offset)
        return x

    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)


    def DataList(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            x = self._tab.Vector(o)
            x += flatbuffers.number_types.UOffsetTFlags.py_type(j) * 4
            x = self._tab.Indirect(x)
            from .MemoryLobbyExcel import MemoryLobbyExcel
            obj = MemoryLobbyExcel()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    def DataListLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    def DataListIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        return o == 0




    @staticmethod
    def Start(builder): builder.StartObject(1)
    @staticmethod
    def End(builder): return builder.EndObject()


    @staticmethod
    def AddDataList(builder, DataList): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(DataList), 0)
    @staticmethod
    def StartDataListVector(builder, numElems): return builder.StartVector(4, numElems, 4)

