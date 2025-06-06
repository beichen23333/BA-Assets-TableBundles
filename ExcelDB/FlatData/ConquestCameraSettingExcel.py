
import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class ConquestCameraSettingExcel:
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = ConquestCameraSettingExcel()
        x.Init(buf, n + offset)
        return x

    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)


    def Id(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def ConquestMapBoundaryOffsetLeft(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0


    def ConquestMapBoundaryOffsetRight(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0


    def ConquestMapBoundaryOffsetTop(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0


    def ConquestMapBoundaryOffsetBottom(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0


    def ConquestMapCenterOffsetX(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0


    def ConquestMapCenterOffsetY(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0


    def CameraAngle(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0


    def CameraZoomMax(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0


    def CameraZoomMin(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0


    def CameraZoomDefault(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0




    @staticmethod
    def Start(builder): builder.StartObject(11)
    @staticmethod
    def End(builder): return builder.EndObject()


    @staticmethod
    def AddId(builder, Id): builder.PrependInt64Slot(0, Id, 0)


    @staticmethod
    def AddConquestMapBoundaryOffsetLeft(builder, ConquestMapBoundaryOffsetLeft): builder.PrependFloat32Slot(1, ConquestMapBoundaryOffsetLeft, 0)


    @staticmethod
    def AddConquestMapBoundaryOffsetRight(builder, ConquestMapBoundaryOffsetRight): builder.PrependFloat32Slot(2, ConquestMapBoundaryOffsetRight, 0)


    @staticmethod
    def AddConquestMapBoundaryOffsetTop(builder, ConquestMapBoundaryOffsetTop): builder.PrependFloat32Slot(3, ConquestMapBoundaryOffsetTop, 0)


    @staticmethod
    def AddConquestMapBoundaryOffsetBottom(builder, ConquestMapBoundaryOffsetBottom): builder.PrependFloat32Slot(4, ConquestMapBoundaryOffsetBottom, 0)


    @staticmethod
    def AddConquestMapCenterOffsetX(builder, ConquestMapCenterOffsetX): builder.PrependFloat32Slot(5, ConquestMapCenterOffsetX, 0)


    @staticmethod
    def AddConquestMapCenterOffsetY(builder, ConquestMapCenterOffsetY): builder.PrependFloat32Slot(6, ConquestMapCenterOffsetY, 0)


    @staticmethod
    def AddCameraAngle(builder, CameraAngle): builder.PrependFloat32Slot(7, CameraAngle, 0)


    @staticmethod
    def AddCameraZoomMax(builder, CameraZoomMax): builder.PrependFloat32Slot(8, CameraZoomMax, 0)


    @staticmethod
    def AddCameraZoomMin(builder, CameraZoomMin): builder.PrependFloat32Slot(9, CameraZoomMin, 0)


    @staticmethod
    def AddCameraZoomDefault(builder, CameraZoomDefault): builder.PrependFloat32Slot(10, CameraZoomDefault, 0)

