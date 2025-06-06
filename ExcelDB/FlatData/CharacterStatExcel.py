
import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class CharacterStatExcel:
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = CharacterStatExcel()
        x.Init(buf, n + offset)
        return x

    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)


    def CharacterId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def StabilityRate(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def StabilityPoint(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def AttackPower1(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def AttackPower100(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def MaxHP1(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def MaxHP100(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def DefensePower1(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def DefensePower100(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def HealPower1(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def HealPower100(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def DodgePoint(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def AccuracyPoint(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(28))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def CriticalPoint(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(30))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def CriticalResistPoint(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(32))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def CriticalDamageRate(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(34))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def CriticalDamageResistRate(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(36))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def BlockRate(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(38))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def HealEffectivenessRate(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(40))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def OppressionPower(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(42))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def OppressionResist(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(44))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def DefensePenetration1(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(46))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def DefensePenetration100(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(48))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def DefensePenetrationResist1(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(50))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def DefensePenetrationResist100(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(52))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def EnhanceExplosionRate(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(54))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def EnhancePierceRate(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(56))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def EnhanceMysticRate(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(58))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def EnhanceSonicRate(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(60))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def EnhanceSiegeRate(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(62))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def EnhanceNormalRate(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(64))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def EnhanceLightArmorRate(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(66))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def EnhanceHeavyArmorRate(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(68))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def EnhanceUnarmedRate(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(70))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def EnhanceElasticArmorRate(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(72))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def EnhanceStructureRate(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(74))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def EnhanceNormalArmorRate(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(76))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def ExtendBuffDuration(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(78))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def ExtendDebuffDuration(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(80))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def ExtendCrowdControlDuration(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(82))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def AmmoCount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(84))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def AmmoCost(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(86))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def IgnoreDelayCount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(88))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def NormalAttackSpeed(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(90))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def Range(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(92))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def InitialRangeRate(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(94))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def MoveSpeed(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(96))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def SightPoint(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(98))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def ActiveGauge(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(100))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def GroggyGauge(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(102))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def GroggyTime(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(104))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def StrategyMobility(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(106))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def ActionCount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(108))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def StrategySightRange(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(110))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def DamageRatio(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(112))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def DamagedRatio(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(114))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def DamageRatio2Increase(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(116))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def DamageRatio2Decrease(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(118))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def DamagedRatio2Increase(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(120))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def DamagedRatio2Decrease(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(122))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def ExDamagedRatioIncrease(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(124))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def ExDamagedRatioDecrease(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(126))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def EnhanceExDamageRate(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(128))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def ReduceExDamagedRate(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(130))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def HealRate(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(132))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def HealLightArmorRate(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(134))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def HealHeavyArmorRate(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(136))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def HealUnarmedRate(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(138))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def HealElasticArmorRate(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(140))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def HealNormalArmorRate(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(142))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def HealedExplosionRate(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(144))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def HealedPierceRate(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(146))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def HealedMysticRate(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(148))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def HealedSonicRate(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(150))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def HealedNormalRate(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(152))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def StreetBattleAdaptation(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(154))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def OutdoorBattleAdaptation(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(156))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def IndoorBattleAdaptation(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(158))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def RegenCost(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(160))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0




    @staticmethod
    def Start(builder): builder.StartObject(79)
    @staticmethod
    def End(builder): return builder.EndObject()


    @staticmethod
    def AddCharacterId(builder, CharacterId): builder.PrependInt64Slot(0, CharacterId, 0)


    @staticmethod
    def AddStabilityRate(builder, StabilityRate): builder.PrependInt64Slot(1, StabilityRate, 0)


    @staticmethod
    def AddStabilityPoint(builder, StabilityPoint): builder.PrependInt64Slot(2, StabilityPoint, 0)


    @staticmethod
    def AddAttackPower1(builder, AttackPower1): builder.PrependInt64Slot(3, AttackPower1, 0)


    @staticmethod
    def AddAttackPower100(builder, AttackPower100): builder.PrependInt64Slot(4, AttackPower100, 0)


    @staticmethod
    def AddMaxHP1(builder, MaxHP1): builder.PrependInt64Slot(5, MaxHP1, 0)


    @staticmethod
    def AddMaxHP100(builder, MaxHP100): builder.PrependInt64Slot(6, MaxHP100, 0)


    @staticmethod
    def AddDefensePower1(builder, DefensePower1): builder.PrependInt64Slot(7, DefensePower1, 0)


    @staticmethod
    def AddDefensePower100(builder, DefensePower100): builder.PrependInt64Slot(8, DefensePower100, 0)


    @staticmethod
    def AddHealPower1(builder, HealPower1): builder.PrependInt64Slot(9, HealPower1, 0)


    @staticmethod
    def AddHealPower100(builder, HealPower100): builder.PrependInt64Slot(10, HealPower100, 0)


    @staticmethod
    def AddDodgePoint(builder, DodgePoint): builder.PrependInt64Slot(11, DodgePoint, 0)


    @staticmethod
    def AddAccuracyPoint(builder, AccuracyPoint): builder.PrependInt64Slot(12, AccuracyPoint, 0)


    @staticmethod
    def AddCriticalPoint(builder, CriticalPoint): builder.PrependInt64Slot(13, CriticalPoint, 0)


    @staticmethod
    def AddCriticalResistPoint(builder, CriticalResistPoint): builder.PrependInt64Slot(14, CriticalResistPoint, 0)


    @staticmethod
    def AddCriticalDamageRate(builder, CriticalDamageRate): builder.PrependInt64Slot(15, CriticalDamageRate, 0)


    @staticmethod
    def AddCriticalDamageResistRate(builder, CriticalDamageResistRate): builder.PrependInt64Slot(16, CriticalDamageResistRate, 0)


    @staticmethod
    def AddBlockRate(builder, BlockRate): builder.PrependInt64Slot(17, BlockRate, 0)


    @staticmethod
    def AddHealEffectivenessRate(builder, HealEffectivenessRate): builder.PrependInt64Slot(18, HealEffectivenessRate, 0)


    @staticmethod
    def AddOppressionPower(builder, OppressionPower): builder.PrependInt64Slot(19, OppressionPower, 0)


    @staticmethod
    def AddOppressionResist(builder, OppressionResist): builder.PrependInt64Slot(20, OppressionResist, 0)


    @staticmethod
    def AddDefensePenetration1(builder, DefensePenetration1): builder.PrependInt64Slot(21, DefensePenetration1, 0)


    @staticmethod
    def AddDefensePenetration100(builder, DefensePenetration100): builder.PrependInt64Slot(22, DefensePenetration100, 0)


    @staticmethod
    def AddDefensePenetrationResist1(builder, DefensePenetrationResist1): builder.PrependInt64Slot(23, DefensePenetrationResist1, 0)


    @staticmethod
    def AddDefensePenetrationResist100(builder, DefensePenetrationResist100): builder.PrependInt64Slot(24, DefensePenetrationResist100, 0)


    @staticmethod
    def AddEnhanceExplosionRate(builder, EnhanceExplosionRate): builder.PrependInt64Slot(25, EnhanceExplosionRate, 0)


    @staticmethod
    def AddEnhancePierceRate(builder, EnhancePierceRate): builder.PrependInt64Slot(26, EnhancePierceRate, 0)


    @staticmethod
    def AddEnhanceMysticRate(builder, EnhanceMysticRate): builder.PrependInt64Slot(27, EnhanceMysticRate, 0)


    @staticmethod
    def AddEnhanceSonicRate(builder, EnhanceSonicRate): builder.PrependInt64Slot(28, EnhanceSonicRate, 0)


    @staticmethod
    def AddEnhanceSiegeRate(builder, EnhanceSiegeRate): builder.PrependInt64Slot(29, EnhanceSiegeRate, 0)


    @staticmethod
    def AddEnhanceNormalRate(builder, EnhanceNormalRate): builder.PrependInt64Slot(30, EnhanceNormalRate, 0)


    @staticmethod
    def AddEnhanceLightArmorRate(builder, EnhanceLightArmorRate): builder.PrependInt64Slot(31, EnhanceLightArmorRate, 0)


    @staticmethod
    def AddEnhanceHeavyArmorRate(builder, EnhanceHeavyArmorRate): builder.PrependInt64Slot(32, EnhanceHeavyArmorRate, 0)


    @staticmethod
    def AddEnhanceUnarmedRate(builder, EnhanceUnarmedRate): builder.PrependInt64Slot(33, EnhanceUnarmedRate, 0)


    @staticmethod
    def AddEnhanceElasticArmorRate(builder, EnhanceElasticArmorRate): builder.PrependInt64Slot(34, EnhanceElasticArmorRate, 0)


    @staticmethod
    def AddEnhanceStructureRate(builder, EnhanceStructureRate): builder.PrependInt64Slot(35, EnhanceStructureRate, 0)


    @staticmethod
    def AddEnhanceNormalArmorRate(builder, EnhanceNormalArmorRate): builder.PrependInt64Slot(36, EnhanceNormalArmorRate, 0)


    @staticmethod
    def AddExtendBuffDuration(builder, ExtendBuffDuration): builder.PrependInt64Slot(37, ExtendBuffDuration, 0)


    @staticmethod
    def AddExtendDebuffDuration(builder, ExtendDebuffDuration): builder.PrependInt64Slot(38, ExtendDebuffDuration, 0)


    @staticmethod
    def AddExtendCrowdControlDuration(builder, ExtendCrowdControlDuration): builder.PrependInt64Slot(39, ExtendCrowdControlDuration, 0)


    @staticmethod
    def AddAmmoCount(builder, AmmoCount): builder.PrependInt64Slot(40, AmmoCount, 0)


    @staticmethod
    def AddAmmoCost(builder, AmmoCost): builder.PrependInt64Slot(41, AmmoCost, 0)


    @staticmethod
    def AddIgnoreDelayCount(builder, IgnoreDelayCount): builder.PrependInt64Slot(42, IgnoreDelayCount, 0)


    @staticmethod
    def AddNormalAttackSpeed(builder, NormalAttackSpeed): builder.PrependInt64Slot(43, NormalAttackSpeed, 0)


    @staticmethod
    def AddRange(builder, Range): builder.PrependInt64Slot(44, Range, 0)


    @staticmethod
    def AddInitialRangeRate(builder, InitialRangeRate): builder.PrependInt64Slot(45, InitialRangeRate, 0)


    @staticmethod
    def AddMoveSpeed(builder, MoveSpeed): builder.PrependInt64Slot(46, MoveSpeed, 0)


    @staticmethod
    def AddSightPoint(builder, SightPoint): builder.PrependInt64Slot(47, SightPoint, 0)


    @staticmethod
    def AddActiveGauge(builder, ActiveGauge): builder.PrependInt64Slot(48, ActiveGauge, 0)


    @staticmethod
    def AddGroggyGauge(builder, GroggyGauge): builder.PrependInt32Slot(49, GroggyGauge, 0)


    @staticmethod
    def AddGroggyTime(builder, GroggyTime): builder.PrependInt32Slot(50, GroggyTime, 0)


    @staticmethod
    def AddStrategyMobility(builder, StrategyMobility): builder.PrependInt64Slot(51, StrategyMobility, 0)


    @staticmethod
    def AddActionCount(builder, ActionCount): builder.PrependInt64Slot(52, ActionCount, 0)


    @staticmethod
    def AddStrategySightRange(builder, StrategySightRange): builder.PrependInt64Slot(53, StrategySightRange, 0)


    @staticmethod
    def AddDamageRatio(builder, DamageRatio): builder.PrependInt64Slot(54, DamageRatio, 0)


    @staticmethod
    def AddDamagedRatio(builder, DamagedRatio): builder.PrependInt64Slot(55, DamagedRatio, 0)


    @staticmethod
    def AddDamageRatio2Increase(builder, DamageRatio2Increase): builder.PrependInt64Slot(56, DamageRatio2Increase, 0)


    @staticmethod
    def AddDamageRatio2Decrease(builder, DamageRatio2Decrease): builder.PrependInt64Slot(57, DamageRatio2Decrease, 0)


    @staticmethod
    def AddDamagedRatio2Increase(builder, DamagedRatio2Increase): builder.PrependInt64Slot(58, DamagedRatio2Increase, 0)


    @staticmethod
    def AddDamagedRatio2Decrease(builder, DamagedRatio2Decrease): builder.PrependInt64Slot(59, DamagedRatio2Decrease, 0)


    @staticmethod
    def AddExDamagedRatioIncrease(builder, ExDamagedRatioIncrease): builder.PrependInt64Slot(60, ExDamagedRatioIncrease, 0)


    @staticmethod
    def AddExDamagedRatioDecrease(builder, ExDamagedRatioDecrease): builder.PrependInt64Slot(61, ExDamagedRatioDecrease, 0)


    @staticmethod
    def AddEnhanceExDamageRate(builder, EnhanceExDamageRate): builder.PrependInt64Slot(62, EnhanceExDamageRate, 0)


    @staticmethod
    def AddReduceExDamagedRate(builder, ReduceExDamagedRate): builder.PrependInt64Slot(63, ReduceExDamagedRate, 0)


    @staticmethod
    def AddHealRate(builder, HealRate): builder.PrependInt64Slot(64, HealRate, 0)


    @staticmethod
    def AddHealLightArmorRate(builder, HealLightArmorRate): builder.PrependInt64Slot(65, HealLightArmorRate, 0)


    @staticmethod
    def AddHealHeavyArmorRate(builder, HealHeavyArmorRate): builder.PrependInt64Slot(66, HealHeavyArmorRate, 0)


    @staticmethod
    def AddHealUnarmedRate(builder, HealUnarmedRate): builder.PrependInt64Slot(67, HealUnarmedRate, 0)


    @staticmethod
    def AddHealElasticArmorRate(builder, HealElasticArmorRate): builder.PrependInt64Slot(68, HealElasticArmorRate, 0)


    @staticmethod
    def AddHealNormalArmorRate(builder, HealNormalArmorRate): builder.PrependInt64Slot(69, HealNormalArmorRate, 0)


    @staticmethod
    def AddHealedExplosionRate(builder, HealedExplosionRate): builder.PrependInt64Slot(70, HealedExplosionRate, 0)


    @staticmethod
    def AddHealedPierceRate(builder, HealedPierceRate): builder.PrependInt64Slot(71, HealedPierceRate, 0)


    @staticmethod
    def AddHealedMysticRate(builder, HealedMysticRate): builder.PrependInt64Slot(72, HealedMysticRate, 0)


    @staticmethod
    def AddHealedSonicRate(builder, HealedSonicRate): builder.PrependInt64Slot(73, HealedSonicRate, 0)


    @staticmethod
    def AddHealedNormalRate(builder, HealedNormalRate): builder.PrependInt64Slot(74, HealedNormalRate, 0)


    @staticmethod
    def AddStreetBattleAdaptation(builder, StreetBattleAdaptation): builder.PrependInt32Slot(75, StreetBattleAdaptation, 0)


    @staticmethod
    def AddOutdoorBattleAdaptation(builder, OutdoorBattleAdaptation): builder.PrependInt32Slot(76, OutdoorBattleAdaptation, 0)


    @staticmethod
    def AddIndoorBattleAdaptation(builder, IndoorBattleAdaptation): builder.PrependInt32Slot(77, IndoorBattleAdaptation, 0)


    @staticmethod
    def AddRegenCost(builder, RegenCost): builder.PrependInt64Slot(78, RegenCost, 0)

