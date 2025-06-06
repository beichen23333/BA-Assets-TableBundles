
import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class CharacterExcel:
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = CharacterExcel()
        x.Init(buf, n + offset)
        return x

    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)


    def Id(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def DevName(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def CostumeGroupId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def IsPlayable(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0


    def ProductionStep(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
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


    def IsPlayableCharacter(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0


    def LocalizeEtcId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0


    def Rarity(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def IsNPC(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(28))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0


    def TacticEntityType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(30))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def CanSurvive(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(32))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0


    def IsDummy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(34))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0


    def SubPartsCount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(36))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def TacticRole(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(38))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def WeaponType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(40))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def TacticRange(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(42))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def BulletType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(44))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def ArmorType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(46))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def AimIKType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(48))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def School(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(50))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def Club(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(52))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def DefaultStarGrade(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(54))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def MaxStarGrade(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(56))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def StatLevelUpType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(58))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def SquadType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(60))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def Jumpable(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(62))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0


    def PersonalityId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(64))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def CharacterAIId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(66))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def ExternalBTId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(68))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def MainCombatStyleId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(70))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def CombatStyleIndex(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(72))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def ScenarioCharacter(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(74))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def SpawnTemplateId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(76))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0


    def FavorLevelupType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(78))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def EquipmentSlot(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(80))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int32Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return 0

    def EquipmentSlotAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(80))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int32Flags, o)
        return 0

    def EquipmentSlotLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(80))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    def EquipmentSlotIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(80))
        return o == 0


    def WeaponLocalizeId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(82))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0


    def DisplayEnemyInfo(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(84))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0


    def BodyRadius(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(86))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def RandomEffectRadius(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(88))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def HPBarHide(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(90))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0


    def HpBarHeight(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(92))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0


    def HighlightFloaterHeight(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(94))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0


    def EmojiOffsetX(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(96))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0


    def EmojiOffsetY(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(98))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0


    def MoveStartFrame(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(100))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def MoveEndFrame(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(102))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def JumpMotionFrame(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(104))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def AppearFrame(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(106))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def CanMove(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(108))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0


    def CanFix(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(110))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0


    def CanCrowdControl(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(112))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0


    def CanBattleItemMove(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(114))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0


    def IgnoreObstacle(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(116))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0


    def IsAirUnit(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(118))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0


    def AirUnitHeight(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(120))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def Tags(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(122))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int32Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return 0

    def TagsAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(122))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int32Flags, o)
        return 0

    def TagsLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(122))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    def TagsIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(122))
        return o == 0


    def SecretStoneItemId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(124))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def SecretStoneItemAmount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(126))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def CharacterPieceItemId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(128))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def CharacterPieceItemAmount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(130))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def CombineRecipeId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(132))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0




    @staticmethod
    def Start(builder): builder.StartObject(65)
    @staticmethod
    def End(builder): return builder.EndObject()


    @staticmethod
    def AddId(builder, Id): builder.PrependInt64Slot(0, Id, 0)


    @staticmethod
    def AddDevName(builder, DevName): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(DevName), 0)

    @staticmethod
    def AddCostumeGroupId(builder, CostumeGroupId): builder.PrependInt64Slot(2, CostumeGroupId, 0)


    @staticmethod
    def AddIsPlayable(builder, IsPlayable): builder.PrependBoolSlot(3, IsPlayable, 0)


    @staticmethod
    def AddProductionStep(builder, ProductionStep): builder.PrependInt32Slot(4, ProductionStep, 0)


    @staticmethod
    def AddCollectionVisible(builder, CollectionVisible): builder.PrependBoolSlot(5, CollectionVisible, 0)


    @staticmethod
    def AddReleaseDate(builder, ReleaseDate): builder.PrependUOffsetTRelativeSlot(6, flatbuffers.number_types.UOffsetTFlags.py_type(ReleaseDate), 0)

    @staticmethod
    def AddCollectionVisibleStartDate(builder, CollectionVisibleStartDate): builder.PrependUOffsetTRelativeSlot(7, flatbuffers.number_types.UOffsetTFlags.py_type(CollectionVisibleStartDate), 0)

    @staticmethod
    def AddCollectionVisibleEndDate(builder, CollectionVisibleEndDate): builder.PrependUOffsetTRelativeSlot(8, flatbuffers.number_types.UOffsetTFlags.py_type(CollectionVisibleEndDate), 0)

    @staticmethod
    def AddIsPlayableCharacter(builder, IsPlayableCharacter): builder.PrependBoolSlot(9, IsPlayableCharacter, 0)


    @staticmethod
    def AddLocalizeEtcId(builder, LocalizeEtcId): builder.PrependUint32Slot(10, LocalizeEtcId, 0)


    @staticmethod
    def AddRarity(builder, Rarity): builder.PrependInt32Slot(11, Rarity, 0)


    @staticmethod
    def AddIsNPC(builder, IsNPC): builder.PrependBoolSlot(12, IsNPC, 0)


    @staticmethod
    def AddTacticEntityType(builder, TacticEntityType): builder.PrependInt32Slot(13, TacticEntityType, 0)


    @staticmethod
    def AddCanSurvive(builder, CanSurvive): builder.PrependBoolSlot(14, CanSurvive, 0)


    @staticmethod
    def AddIsDummy(builder, IsDummy): builder.PrependBoolSlot(15, IsDummy, 0)


    @staticmethod
    def AddSubPartsCount(builder, SubPartsCount): builder.PrependInt32Slot(16, SubPartsCount, 0)


    @staticmethod
    def AddTacticRole(builder, TacticRole): builder.PrependInt32Slot(17, TacticRole, 0)


    @staticmethod
    def AddWeaponType(builder, WeaponType): builder.PrependInt32Slot(18, WeaponType, 0)


    @staticmethod
    def AddTacticRange(builder, TacticRange): builder.PrependInt32Slot(19, TacticRange, 0)


    @staticmethod
    def AddBulletType(builder, BulletType): builder.PrependInt32Slot(20, BulletType, 0)


    @staticmethod
    def AddArmorType(builder, ArmorType): builder.PrependInt32Slot(21, ArmorType, 0)


    @staticmethod
    def AddAimIKType(builder, AimIKType): builder.PrependInt32Slot(22, AimIKType, 0)


    @staticmethod
    def AddSchool(builder, School): builder.PrependInt32Slot(23, School, 0)


    @staticmethod
    def AddClub(builder, Club): builder.PrependInt32Slot(24, Club, 0)


    @staticmethod
    def AddDefaultStarGrade(builder, DefaultStarGrade): builder.PrependInt32Slot(25, DefaultStarGrade, 0)


    @staticmethod
    def AddMaxStarGrade(builder, MaxStarGrade): builder.PrependInt32Slot(26, MaxStarGrade, 0)


    @staticmethod
    def AddStatLevelUpType(builder, StatLevelUpType): builder.PrependInt32Slot(27, StatLevelUpType, 0)


    @staticmethod
    def AddSquadType(builder, SquadType): builder.PrependInt32Slot(28, SquadType, 0)


    @staticmethod
    def AddJumpable(builder, Jumpable): builder.PrependBoolSlot(29, Jumpable, 0)


    @staticmethod
    def AddPersonalityId(builder, PersonalityId): builder.PrependInt64Slot(30, PersonalityId, 0)


    @staticmethod
    def AddCharacterAIId(builder, CharacterAIId): builder.PrependInt64Slot(31, CharacterAIId, 0)


    @staticmethod
    def AddExternalBTId(builder, ExternalBTId): builder.PrependInt64Slot(32, ExternalBTId, 0)


    @staticmethod
    def AddMainCombatStyleId(builder, MainCombatStyleId): builder.PrependInt64Slot(33, MainCombatStyleId, 0)


    @staticmethod
    def AddCombatStyleIndex(builder, CombatStyleIndex): builder.PrependInt32Slot(34, CombatStyleIndex, 0)


    @staticmethod
    def AddScenarioCharacter(builder, ScenarioCharacter): builder.PrependUOffsetTRelativeSlot(35, flatbuffers.number_types.UOffsetTFlags.py_type(ScenarioCharacter), 0)

    @staticmethod
    def AddSpawnTemplateId(builder, SpawnTemplateId): builder.PrependUint32Slot(36, SpawnTemplateId, 0)


    @staticmethod
    def AddFavorLevelupType(builder, FavorLevelupType): builder.PrependInt32Slot(37, FavorLevelupType, 0)


    @staticmethod
    def AddEquipmentSlot(builder, EquipmentSlot): builder.PrependUOffsetTRelativeSlot(38, flatbuffers.number_types.UOffsetTFlags.py_type(EquipmentSlot), 0)
    @staticmethod
    def StartEquipmentSlotVector(builder, numElems): return builder.StartVector(4, numElems, 4)


    @staticmethod
    def AddWeaponLocalizeId(builder, WeaponLocalizeId): builder.PrependUint32Slot(39, WeaponLocalizeId, 0)


    @staticmethod
    def AddDisplayEnemyInfo(builder, DisplayEnemyInfo): builder.PrependBoolSlot(40, DisplayEnemyInfo, 0)


    @staticmethod
    def AddBodyRadius(builder, BodyRadius): builder.PrependInt64Slot(41, BodyRadius, 0)


    @staticmethod
    def AddRandomEffectRadius(builder, RandomEffectRadius): builder.PrependInt64Slot(42, RandomEffectRadius, 0)


    @staticmethod
    def AddHPBarHide(builder, HPBarHide): builder.PrependBoolSlot(43, HPBarHide, 0)


    @staticmethod
    def AddHpBarHeight(builder, HpBarHeight): builder.PrependFloat32Slot(44, HpBarHeight, 0)


    @staticmethod
    def AddHighlightFloaterHeight(builder, HighlightFloaterHeight): builder.PrependFloat32Slot(45, HighlightFloaterHeight, 0)


    @staticmethod
    def AddEmojiOffsetX(builder, EmojiOffsetX): builder.PrependFloat32Slot(46, EmojiOffsetX, 0)


    @staticmethod
    def AddEmojiOffsetY(builder, EmojiOffsetY): builder.PrependFloat32Slot(47, EmojiOffsetY, 0)


    @staticmethod
    def AddMoveStartFrame(builder, MoveStartFrame): builder.PrependInt32Slot(48, MoveStartFrame, 0)


    @staticmethod
    def AddMoveEndFrame(builder, MoveEndFrame): builder.PrependInt32Slot(49, MoveEndFrame, 0)


    @staticmethod
    def AddJumpMotionFrame(builder, JumpMotionFrame): builder.PrependInt32Slot(50, JumpMotionFrame, 0)


    @staticmethod
    def AddAppearFrame(builder, AppearFrame): builder.PrependInt32Slot(51, AppearFrame, 0)


    @staticmethod
    def AddCanMove(builder, CanMove): builder.PrependBoolSlot(52, CanMove, 0)


    @staticmethod
    def AddCanFix(builder, CanFix): builder.PrependBoolSlot(53, CanFix, 0)


    @staticmethod
    def AddCanCrowdControl(builder, CanCrowdControl): builder.PrependBoolSlot(54, CanCrowdControl, 0)


    @staticmethod
    def AddCanBattleItemMove(builder, CanBattleItemMove): builder.PrependBoolSlot(55, CanBattleItemMove, 0)


    @staticmethod
    def AddIgnoreObstacle(builder, IgnoreObstacle): builder.PrependBoolSlot(56, IgnoreObstacle, 0)


    @staticmethod
    def AddIsAirUnit(builder, IsAirUnit): builder.PrependBoolSlot(57, IsAirUnit, 0)


    @staticmethod
    def AddAirUnitHeight(builder, AirUnitHeight): builder.PrependInt64Slot(58, AirUnitHeight, 0)


    @staticmethod
    def AddTags(builder, Tags): builder.PrependUOffsetTRelativeSlot(59, flatbuffers.number_types.UOffsetTFlags.py_type(Tags), 0)
    @staticmethod
    def StartTagsVector(builder, numElems): return builder.StartVector(4, numElems, 4)


    @staticmethod
    def AddSecretStoneItemId(builder, SecretStoneItemId): builder.PrependInt64Slot(60, SecretStoneItemId, 0)


    @staticmethod
    def AddSecretStoneItemAmount(builder, SecretStoneItemAmount): builder.PrependInt32Slot(61, SecretStoneItemAmount, 0)


    @staticmethod
    def AddCharacterPieceItemId(builder, CharacterPieceItemId): builder.PrependInt64Slot(62, CharacterPieceItemId, 0)


    @staticmethod
    def AddCharacterPieceItemAmount(builder, CharacterPieceItemAmount): builder.PrependInt32Slot(63, CharacterPieceItemAmount, 0)


    @staticmethod
    def AddCombineRecipeId(builder, CombineRecipeId): builder.PrependInt64Slot(64, CombineRecipeId, 0)

