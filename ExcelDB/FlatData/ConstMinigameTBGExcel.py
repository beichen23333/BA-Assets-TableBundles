
import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class ConstMinigameTBGExcel:
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = ConstMinigameTBGExcel()
        x.Init(buf, n + offset)
        return x

    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)


    def ConquestMapBoundaryOffsetLeft(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0


    def ConquestMapBoundaryOffsetRight(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0


    def ConquestMapBoundaryOffsetTop(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0


    def ConquestMapBoundaryOffsetBottom(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0


    def ConquestMapCenterOffsetX(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0


    def ConquestMapCenterOffsetY(self):
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


    def ThemaLoadingProgressTime(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0


    def MapAllyRotation(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0


    def AniAllyBattleAttack(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(28))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def EffectAllyBattleAttack(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(30))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def EffectAllyBattleDamage(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(32))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def AniEnemyBattleAttack(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(34))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def EffectEnemyBattleAttack(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(36))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def EffectEnemyBattleDamage(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(38))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def EncounterAllyRotation(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(40))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0


    def EncounterEnemyRotation(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(42))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0


    def EncounterRewardReceiveIndex(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(44))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0




    @staticmethod
    def Start(builder): builder.StartObject(21)
    @staticmethod
    def End(builder): return builder.EndObject()


    @staticmethod
    def AddConquestMapBoundaryOffsetLeft(builder, ConquestMapBoundaryOffsetLeft): builder.PrependFloat32Slot(0, ConquestMapBoundaryOffsetLeft, 0)


    @staticmethod
    def AddConquestMapBoundaryOffsetRight(builder, ConquestMapBoundaryOffsetRight): builder.PrependFloat32Slot(1, ConquestMapBoundaryOffsetRight, 0)


    @staticmethod
    def AddConquestMapBoundaryOffsetTop(builder, ConquestMapBoundaryOffsetTop): builder.PrependFloat32Slot(2, ConquestMapBoundaryOffsetTop, 0)


    @staticmethod
    def AddConquestMapBoundaryOffsetBottom(builder, ConquestMapBoundaryOffsetBottom): builder.PrependFloat32Slot(3, ConquestMapBoundaryOffsetBottom, 0)


    @staticmethod
    def AddConquestMapCenterOffsetX(builder, ConquestMapCenterOffsetX): builder.PrependFloat32Slot(4, ConquestMapCenterOffsetX, 0)


    @staticmethod
    def AddConquestMapCenterOffsetY(builder, ConquestMapCenterOffsetY): builder.PrependFloat32Slot(5, ConquestMapCenterOffsetY, 0)


    @staticmethod
    def AddCameraAngle(builder, CameraAngle): builder.PrependFloat32Slot(6, CameraAngle, 0)


    @staticmethod
    def AddCameraZoomMax(builder, CameraZoomMax): builder.PrependFloat32Slot(7, CameraZoomMax, 0)


    @staticmethod
    def AddCameraZoomMin(builder, CameraZoomMin): builder.PrependFloat32Slot(8, CameraZoomMin, 0)


    @staticmethod
    def AddCameraZoomDefault(builder, CameraZoomDefault): builder.PrependFloat32Slot(9, CameraZoomDefault, 0)


    @staticmethod
    def AddThemaLoadingProgressTime(builder, ThemaLoadingProgressTime): builder.PrependFloat32Slot(10, ThemaLoadingProgressTime, 0)


    @staticmethod
    def AddMapAllyRotation(builder, MapAllyRotation): builder.PrependFloat32Slot(11, MapAllyRotation, 0)


    @staticmethod
    def AddAniAllyBattleAttack(builder, AniAllyBattleAttack): builder.PrependUOffsetTRelativeSlot(12, flatbuffers.number_types.UOffsetTFlags.py_type(AniAllyBattleAttack), 0)

    @staticmethod
    def AddEffectAllyBattleAttack(builder, EffectAllyBattleAttack): builder.PrependUOffsetTRelativeSlot(13, flatbuffers.number_types.UOffsetTFlags.py_type(EffectAllyBattleAttack), 0)

    @staticmethod
    def AddEffectAllyBattleDamage(builder, EffectAllyBattleDamage): builder.PrependUOffsetTRelativeSlot(14, flatbuffers.number_types.UOffsetTFlags.py_type(EffectAllyBattleDamage), 0)

    @staticmethod
    def AddAniEnemyBattleAttack(builder, AniEnemyBattleAttack): builder.PrependUOffsetTRelativeSlot(15, flatbuffers.number_types.UOffsetTFlags.py_type(AniEnemyBattleAttack), 0)

    @staticmethod
    def AddEffectEnemyBattleAttack(builder, EffectEnemyBattleAttack): builder.PrependUOffsetTRelativeSlot(16, flatbuffers.number_types.UOffsetTFlags.py_type(EffectEnemyBattleAttack), 0)

    @staticmethod
    def AddEffectEnemyBattleDamage(builder, EffectEnemyBattleDamage): builder.PrependUOffsetTRelativeSlot(17, flatbuffers.number_types.UOffsetTFlags.py_type(EffectEnemyBattleDamage), 0)

    @staticmethod
    def AddEncounterAllyRotation(builder, EncounterAllyRotation): builder.PrependFloat32Slot(18, EncounterAllyRotation, 0)


    @staticmethod
    def AddEncounterEnemyRotation(builder, EncounterEnemyRotation): builder.PrependFloat32Slot(19, EncounterEnemyRotation, 0)


    @staticmethod
    def AddEncounterRewardReceiveIndex(builder, EncounterRewardReceiveIndex): builder.PrependInt32Slot(20, EncounterRewardReceiveIndex, 0)

