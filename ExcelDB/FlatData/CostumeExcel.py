
import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class CostumeExcel:
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = CostumeExcel()
        x.Init(buf, n + offset)
        return x

    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)


    def CostumeGroupId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def CostumeUniqueId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def DevName(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def ProductionStep(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def IsDefault(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0


    def CollectionVisible(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0


    def ReleaseDate(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def CollectionVisibleStartDate(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def CollectionVisibleEndDate(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def Rarity(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def CharacterSkillListGroupId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def SpineResourceName(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def SpineResourceNameDiorama(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(28))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def SpineResourceNameDioramaForFormConversion(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(30))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.String(a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return ""

    def SpineResourceNameDioramaForFormConversionLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(30))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    def SpineResourceNameDioramaForFormConversionIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(30))
        return o == 0


    def EntityMaterialType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(32))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def ModelPrefabName(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(34))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def CafeModelPrefabName(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(36))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def EchelonModelPrefabName(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(38))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def StrategyModelPrefabName(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(40))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def TextureDir(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(42))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def CollectionTexturePath(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(44))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def CollectionBGTexturePath(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(46))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def CombatStyleTexturePath(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(48))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def UseObjectHPBAR(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(50))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0


    def TextureBoss(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(52))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def TextureSkillCard(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(54))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.String(a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return ""

    def TextureSkillCardLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(54))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    def TextureSkillCardIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(54))
        return o == 0


    def InformationPacel(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(56))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def AnimationSSR(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(58))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def EnterStrategyAnimationName(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(60))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def AnimationValidator(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(62))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0


    def CharacterVoiceGroupId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(64))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def ShowObjectHpStatus(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(66))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0




    @staticmethod
    def Start(builder): builder.StartObject(32)
    @staticmethod
    def End(builder): return builder.EndObject()


    @staticmethod
    def AddCostumeGroupId(builder, CostumeGroupId): builder.PrependInt64Slot(0, CostumeGroupId, 0)


    @staticmethod
    def AddCostumeUniqueId(builder, CostumeUniqueId): builder.PrependInt64Slot(1, CostumeUniqueId, 0)


    @staticmethod
    def AddDevName(builder, DevName): builder.PrependUOffsetTRelativeSlot(2, flatbuffers.number_types.UOffsetTFlags.py_type(DevName), 0)

    @staticmethod
    def AddProductionStep(builder, ProductionStep): builder.PrependInt32Slot(3, ProductionStep, 0)


    @staticmethod
    def AddIsDefault(builder, IsDefault): builder.PrependBoolSlot(4, IsDefault, 0)


    @staticmethod
    def AddCollectionVisible(builder, CollectionVisible): builder.PrependBoolSlot(5, CollectionVisible, 0)


    @staticmethod
    def AddReleaseDate(builder, ReleaseDate): builder.PrependUOffsetTRelativeSlot(6, flatbuffers.number_types.UOffsetTFlags.py_type(ReleaseDate), 0)

    @staticmethod
    def AddCollectionVisibleStartDate(builder, CollectionVisibleStartDate): builder.PrependUOffsetTRelativeSlot(7, flatbuffers.number_types.UOffsetTFlags.py_type(CollectionVisibleStartDate), 0)

    @staticmethod
    def AddCollectionVisibleEndDate(builder, CollectionVisibleEndDate): builder.PrependUOffsetTRelativeSlot(8, flatbuffers.number_types.UOffsetTFlags.py_type(CollectionVisibleEndDate), 0)

    @staticmethod
    def AddRarity(builder, Rarity): builder.PrependInt32Slot(9, Rarity, 0)


    @staticmethod
    def AddCharacterSkillListGroupId(builder, CharacterSkillListGroupId): builder.PrependInt64Slot(10, CharacterSkillListGroupId, 0)


    @staticmethod
    def AddSpineResourceName(builder, SpineResourceName): builder.PrependUOffsetTRelativeSlot(11, flatbuffers.number_types.UOffsetTFlags.py_type(SpineResourceName), 0)

    @staticmethod
    def AddSpineResourceNameDiorama(builder, SpineResourceNameDiorama): builder.PrependUOffsetTRelativeSlot(12, flatbuffers.number_types.UOffsetTFlags.py_type(SpineResourceNameDiorama), 0)

    @staticmethod
    def AddSpineResourceNameDioramaForFormConversion(builder, SpineResourceNameDioramaForFormConversion): builder.PrependUOffsetTRelativeSlot(13, flatbuffers.number_types.UOffsetTFlags.py_type(SpineResourceNameDioramaForFormConversion), 0)
    @staticmethod
    def StartSpineResourceNameDioramaForFormConversionVector(builder, numElems): return builder.StartVector(4, numElems, 4)


    @staticmethod
    def AddEntityMaterialType(builder, EntityMaterialType): builder.PrependInt32Slot(14, EntityMaterialType, 0)


    @staticmethod
    def AddModelPrefabName(builder, ModelPrefabName): builder.PrependUOffsetTRelativeSlot(15, flatbuffers.number_types.UOffsetTFlags.py_type(ModelPrefabName), 0)

    @staticmethod
    def AddCafeModelPrefabName(builder, CafeModelPrefabName): builder.PrependUOffsetTRelativeSlot(16, flatbuffers.number_types.UOffsetTFlags.py_type(CafeModelPrefabName), 0)

    @staticmethod
    def AddEchelonModelPrefabName(builder, EchelonModelPrefabName): builder.PrependUOffsetTRelativeSlot(17, flatbuffers.number_types.UOffsetTFlags.py_type(EchelonModelPrefabName), 0)

    @staticmethod
    def AddStrategyModelPrefabName(builder, StrategyModelPrefabName): builder.PrependUOffsetTRelativeSlot(18, flatbuffers.number_types.UOffsetTFlags.py_type(StrategyModelPrefabName), 0)

    @staticmethod
    def AddTextureDir(builder, TextureDir): builder.PrependUOffsetTRelativeSlot(19, flatbuffers.number_types.UOffsetTFlags.py_type(TextureDir), 0)

    @staticmethod
    def AddCollectionTexturePath(builder, CollectionTexturePath): builder.PrependUOffsetTRelativeSlot(20, flatbuffers.number_types.UOffsetTFlags.py_type(CollectionTexturePath), 0)

    @staticmethod
    def AddCollectionBGTexturePath(builder, CollectionBGTexturePath): builder.PrependUOffsetTRelativeSlot(21, flatbuffers.number_types.UOffsetTFlags.py_type(CollectionBGTexturePath), 0)

    @staticmethod
    def AddCombatStyleTexturePath(builder, CombatStyleTexturePath): builder.PrependUOffsetTRelativeSlot(22, flatbuffers.number_types.UOffsetTFlags.py_type(CombatStyleTexturePath), 0)

    @staticmethod
    def AddUseObjectHPBAR(builder, UseObjectHPBAR): builder.PrependBoolSlot(23, UseObjectHPBAR, 0)


    @staticmethod
    def AddTextureBoss(builder, TextureBoss): builder.PrependUOffsetTRelativeSlot(24, flatbuffers.number_types.UOffsetTFlags.py_type(TextureBoss), 0)

    @staticmethod
    def AddTextureSkillCard(builder, TextureSkillCard): builder.PrependUOffsetTRelativeSlot(25, flatbuffers.number_types.UOffsetTFlags.py_type(TextureSkillCard), 0)
    @staticmethod
    def StartTextureSkillCardVector(builder, numElems): return builder.StartVector(4, numElems, 4)


    @staticmethod
    def AddInformationPacel(builder, InformationPacel): builder.PrependUOffsetTRelativeSlot(26, flatbuffers.number_types.UOffsetTFlags.py_type(InformationPacel), 0)

    @staticmethod
    def AddAnimationSSR(builder, AnimationSSR): builder.PrependUOffsetTRelativeSlot(27, flatbuffers.number_types.UOffsetTFlags.py_type(AnimationSSR), 0)

    @staticmethod
    def AddEnterStrategyAnimationName(builder, EnterStrategyAnimationName): builder.PrependUOffsetTRelativeSlot(28, flatbuffers.number_types.UOffsetTFlags.py_type(EnterStrategyAnimationName), 0)

    @staticmethod
    def AddAnimationValidator(builder, AnimationValidator): builder.PrependBoolSlot(29, AnimationValidator, 0)


    @staticmethod
    def AddCharacterVoiceGroupId(builder, CharacterVoiceGroupId): builder.PrependInt64Slot(30, CharacterVoiceGroupId, 0)


    @staticmethod
    def AddShowObjectHpStatus(builder, ShowObjectHpStatus): builder.PrependBoolSlot(31, ShowObjectHpStatus, 0)

