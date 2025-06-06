
import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class ConstMiniGameShootingExcel:
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = ConstMiniGameShootingExcel()
        x.Init(buf, n + offset)
        return x

    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)


    def NormalStageId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def NormalSectionCount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def HardStageId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def HardSectionCount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def FreeStageId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def FreeSectionCount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def PlayerCharacterId(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int64Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 8))
        return 0

    def PlayerCharacterIdAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int64Flags, o)
        return 0

    def PlayerCharacterIdLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    def PlayerCharacterIdIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        return o == 0


    def HiddenPlayerCharacterId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def CameraSmoothTime(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0


    def SpawnEffectPath(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def WaitTimeAfterSpawn(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0


    def FreeGearInterval(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0




    @staticmethod
    def Start(builder): builder.StartObject(12)
    @staticmethod
    def End(builder): return builder.EndObject()


    @staticmethod
    def AddNormalStageId(builder, NormalStageId): builder.PrependInt64Slot(0, NormalStageId, 0)


    @staticmethod
    def AddNormalSectionCount(builder, NormalSectionCount): builder.PrependInt32Slot(1, NormalSectionCount, 0)


    @staticmethod
    def AddHardStageId(builder, HardStageId): builder.PrependInt64Slot(2, HardStageId, 0)


    @staticmethod
    def AddHardSectionCount(builder, HardSectionCount): builder.PrependInt32Slot(3, HardSectionCount, 0)


    @staticmethod
    def AddFreeStageId(builder, FreeStageId): builder.PrependInt64Slot(4, FreeStageId, 0)


    @staticmethod
    def AddFreeSectionCount(builder, FreeSectionCount): builder.PrependInt32Slot(5, FreeSectionCount, 0)


    @staticmethod
    def AddPlayerCharacterId(builder, PlayerCharacterId): builder.PrependUOffsetTRelativeSlot(6, flatbuffers.number_types.UOffsetTFlags.py_type(PlayerCharacterId), 0)
    @staticmethod
    def StartPlayerCharacterIdVector(builder, numElems): return builder.StartVector(8, numElems, 8)


    @staticmethod
    def AddHiddenPlayerCharacterId(builder, HiddenPlayerCharacterId): builder.PrependInt64Slot(7, HiddenPlayerCharacterId, 0)


    @staticmethod
    def AddCameraSmoothTime(builder, CameraSmoothTime): builder.PrependFloat32Slot(8, CameraSmoothTime, 0)


    @staticmethod
    def AddSpawnEffectPath(builder, SpawnEffectPath): builder.PrependUOffsetTRelativeSlot(9, flatbuffers.number_types.UOffsetTFlags.py_type(SpawnEffectPath), 0)

    @staticmethod
    def AddWaitTimeAfterSpawn(builder, WaitTimeAfterSpawn): builder.PrependFloat32Slot(10, WaitTimeAfterSpawn, 0)


    @staticmethod
    def AddFreeGearInterval(builder, FreeGearInterval): builder.PrependInt32Slot(11, FreeGearInterval, 0)

