
import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class ConstMinigameRoadPuzzleExcel:
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = ConstMinigameRoadPuzzleExcel()
        x.Init(buf, n + offset)
        return x

    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)


    def RoadPuzzleMapBoundaryOffsetLeft(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0


    def RoadPuzzleMapBoundaryOffsetRight(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0


    def RoadPuzzleMapBoundaryOffsetTop(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0


    def RoadPuzzleMapBoundaryOffsetBottom(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0


    def RoadPuzzleMapCenterOffsetX(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0


    def RoadPuzzleMapCenterOffsetY(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0


    def CameraAngle(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0


    def CameraZoomMax(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0


    def CameraZoomMin(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0


    def CameraZoomDefault(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0


    def StageLoadingProgressTime(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0


    def TileRotationDegree(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def StartStageIndex(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(28))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def LoopStageIndex(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(30))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0




    @staticmethod
    def Start(builder): builder.StartObject(14)
    @staticmethod
    def End(builder): return builder.EndObject()


    @staticmethod
    def AddRoadPuzzleMapBoundaryOffsetLeft(builder, RoadPuzzleMapBoundaryOffsetLeft): builder.PrependFloat32Slot(0, RoadPuzzleMapBoundaryOffsetLeft, 0)


    @staticmethod
    def AddRoadPuzzleMapBoundaryOffsetRight(builder, RoadPuzzleMapBoundaryOffsetRight): builder.PrependFloat32Slot(1, RoadPuzzleMapBoundaryOffsetRight, 0)


    @staticmethod
    def AddRoadPuzzleMapBoundaryOffsetTop(builder, RoadPuzzleMapBoundaryOffsetTop): builder.PrependFloat32Slot(2, RoadPuzzleMapBoundaryOffsetTop, 0)


    @staticmethod
    def AddRoadPuzzleMapBoundaryOffsetBottom(builder, RoadPuzzleMapBoundaryOffsetBottom): builder.PrependFloat32Slot(3, RoadPuzzleMapBoundaryOffsetBottom, 0)


    @staticmethod
    def AddRoadPuzzleMapCenterOffsetX(builder, RoadPuzzleMapCenterOffsetX): builder.PrependFloat32Slot(4, RoadPuzzleMapCenterOffsetX, 0)


    @staticmethod
    def AddRoadPuzzleMapCenterOffsetY(builder, RoadPuzzleMapCenterOffsetY): builder.PrependFloat32Slot(5, RoadPuzzleMapCenterOffsetY, 0)


    @staticmethod
    def AddCameraAngle(builder, CameraAngle): builder.PrependFloat32Slot(6, CameraAngle, 0)


    @staticmethod
    def AddCameraZoomMax(builder, CameraZoomMax): builder.PrependFloat32Slot(7, CameraZoomMax, 0)


    @staticmethod
    def AddCameraZoomMin(builder, CameraZoomMin): builder.PrependFloat32Slot(8, CameraZoomMin, 0)


    @staticmethod
    def AddCameraZoomDefault(builder, CameraZoomDefault): builder.PrependFloat32Slot(9, CameraZoomDefault, 0)


    @staticmethod
    def AddStageLoadingProgressTime(builder, StageLoadingProgressTime): builder.PrependFloat32Slot(10, StageLoadingProgressTime, 0)


    @staticmethod
    def AddTileRotationDegree(builder, TileRotationDegree): builder.PrependInt32Slot(11, TileRotationDegree, 0)


    @staticmethod
    def AddStartStageIndex(builder, StartStageIndex): builder.PrependInt32Slot(12, StartStageIndex, 0)


    @staticmethod
    def AddLoopStageIndex(builder, LoopStageIndex): builder.PrependInt32Slot(13, LoopStageIndex, 0)

