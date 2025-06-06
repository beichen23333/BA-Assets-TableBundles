
import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class AcademyTicketExcel:
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = AcademyTicketExcel()
        x.Init(buf, n + offset)
        return x

    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)


    def LocationRankSum(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def ScheduleTicktetMax(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0




    @staticmethod
    def Start(builder): builder.StartObject(2)
    @staticmethod
    def End(builder): return builder.EndObject()


    @staticmethod
    def AddLocationRankSum(builder, LocationRankSum): builder.PrependInt64Slot(0, LocationRankSum, 0)


    @staticmethod
    def AddScheduleTicktetMax(builder, ScheduleTicktetMax): builder.PrependInt64Slot(1, ScheduleTicktetMax, 0)

