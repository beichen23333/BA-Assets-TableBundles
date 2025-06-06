
import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class RootMotionFlat:
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = RootMotionFlat()
        x.Init(buf, n + offset)
        return x

    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)


    def Forms(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            x = self._tab.Vector(o)
            x += flatbuffers.number_types.UOffsetTFlags.py_type(j) * 4
            x = self._tab.Indirect(x)
            from .Form import Form
            obj = Form()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    def FormsLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    def FormsIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        return o == 0


    def ExSkills(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            x = self._tab.Vector(o)
            x += flatbuffers.number_types.UOffsetTFlags.py_type(j) * 4
            x = self._tab.Indirect(x)
            from .Motion import Motion
            obj = Motion()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    def ExSkillsLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    def ExSkillsIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        return o == 0


    def MoveLeft(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            x = self._tab.Indirect(o + self._tab.Pos)
            from .Motion import Motion
            obj = Motion()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None


    def MoveRight(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            x = self._tab.Indirect(o + self._tab.Pos)
            from .Motion import Motion
            obj = Motion()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None




    @staticmethod
    def Start(builder): builder.StartObject(4)
    @staticmethod
    def End(builder): return builder.EndObject()


    @staticmethod
    def AddForms(builder, Forms): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(Forms), 0)
    @staticmethod
    def StartFormsVector(builder, numElems): return builder.StartVector(4, numElems, 4)


    @staticmethod
    def AddExSkills(builder, ExSkills): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(ExSkills), 0)
    @staticmethod
    def StartExSkillsVector(builder, numElems): return builder.StartVector(4, numElems, 4)


    @staticmethod
    def AddMoveLeft(builder, MoveLeft): builder.PrependUOffsetTRelativeSlot(2, flatbuffers.number_types.UOffsetTFlags.py_type(MoveLeft), 0)

    @staticmethod
    def AddMoveRight(builder, MoveRight): builder.PrependUOffsetTRelativeSlot(3, flatbuffers.number_types.UOffsetTFlags.py_type(MoveRight), 0)
