
import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class ConstNewbieContentExcel:
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = ConstNewbieContentExcel()
        x.Init(buf, n + offset)
        return x

    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)


    def NewbieGachaReleaseDate(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def NewbieGachaCheckDays(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def NewbieGachaTokenGraceTime(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def NewbieAttendanceReleaseDate(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def NewbieAttendanceStartableEndDay(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def NewbieAttendanceEndDay(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0




    @staticmethod
    def Start(builder): builder.StartObject(6)
    @staticmethod
    def End(builder): return builder.EndObject()


    @staticmethod
    def AddNewbieGachaReleaseDate(builder, NewbieGachaReleaseDate): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(NewbieGachaReleaseDate), 0)

    @staticmethod
    def AddNewbieGachaCheckDays(builder, NewbieGachaCheckDays): builder.PrependInt32Slot(1, NewbieGachaCheckDays, 0)


    @staticmethod
    def AddNewbieGachaTokenGraceTime(builder, NewbieGachaTokenGraceTime): builder.PrependInt32Slot(2, NewbieGachaTokenGraceTime, 0)


    @staticmethod
    def AddNewbieAttendanceReleaseDate(builder, NewbieAttendanceReleaseDate): builder.PrependUOffsetTRelativeSlot(3, flatbuffers.number_types.UOffsetTFlags.py_type(NewbieAttendanceReleaseDate), 0)

    @staticmethod
    def AddNewbieAttendanceStartableEndDay(builder, NewbieAttendanceStartableEndDay): builder.PrependInt32Slot(4, NewbieAttendanceStartableEndDay, 0)


    @staticmethod
    def AddNewbieAttendanceEndDay(builder, NewbieAttendanceEndDay): builder.PrependInt32Slot(5, NewbieAttendanceEndDay, 0)

