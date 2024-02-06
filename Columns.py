class MSZoning:
    values = [
        "A",
        "C",
        "FV",
        "I",
        "RH",
        "RL",
        "RP",
        "RM"]


class Street:
    values = ["Grvl", "Pave"]


class Alley:
    values = ["Grvl", "Pave", "NA"]


class LotShape:
    values = ["Reg", "IR1", "IR2", "IR3"]


class LandContour:
    values = ["Lvl", "Bnk", "HLS", "Low"]


class Utilities:
    values = ["AllPub", "NoSewr", "NoSeWa", "ELO"]


class LotConfig:
    values = [
        "Inside",
        "Corner",
        "CulDSac",
        "FR2",
        "FR3"
    ]


class LandSlope:
    values = [
        "Gtl",
        "Mod",
        "Sev",
    ]


class Neighborhood:
    values = [
        "Blmngtn",
        "Blueste",
        "BrDale",
        "BrkSide",
        "ClearCr",
        "CollgCr",
        "Crawfor",
        "Edwards",
        "Gilbert",
        "IDOTRR",
        "MeadowV",
        "Mitchel",
        "Names",
        "NoRidge",
        "NPkVill",
        "NridgHt",
        "NWAmes",
        "OldTown",
        "SWISU",
        "Sawyer",
        "SawyerW",
        "Somerst",
        "StoneBr",
        "Timber",
        "Veenker",
    ]


class Condition1:
    values = [
        "Artery",
        "Feedr",
        "Norm",
        "RRNn",
        "RRAn",
        "PosN",
        "PosA",
        "RRNe",
        "RRAe",
    ]


class Condition2:
    values = [
        "Artery",
        "Feedr",
        "Norm",
        "RRNn",
        "RRAn",
        "PosN",
        "PosA",
        "RRNe",
        "RRAe",
    ]


class BldgType:
    values = [
        "1Fam",
        "2FmCon",
        "Duplx",
        "TwnhsE",
        "TwnhsI",
    ]


class HouseStyle:
    values = [
        "1Story",
        "1.5Fin",
        "1.5Unf",
        "2Story",
        "2.5Fin",
        "2.5Unf",
        "SFoyer",
        "SLvl",
    ]


class RoofStyle:
    values = [
        "Flat",
        "Gable",
        "Gambrel",
        "Hip",
        "Mansard",
        "Shed",
    ]


class RoofMatl:
    values = [
        "ClyTile",
        "CompShg",
        "Membran",
        "Metal",
        "Roll",
        "Tar&Grv",
        "WdShake",
        "WdShngl",
    ]


class Exterior1st:
    values = [
        "AsbShng",
        "AsphShn",
        "BrkComm",
        "BrkFace",
        "CBlock",
        "CemntBd",
        "HdBoard",
        "ImStucc",
        "MetalSd",
        "Other",
        "Plywood",
        "PreCast",
        "Stone",
        "Stucco",
        "VinylSd",
        "Wd Sdng",
        "WdShing",
    ]


class Exterior2nd:
    values = [
        "AsbShng",
        "AsphShn",
        "BrkComm",
        "BrkFace",
        "CBlock",
        "CemntBd",
        "HdBoard",
        "ImStucc",
        "MetalSd",
        "Other",
        "Plywood",
        "PreCast",
        "Stone",
        "Stucco",
        "VinylSd",
        "Wd Sdng",
        "WdShing",
    ]


class MasVnrType:
    values = [
        "BrkCmn",
        "BrkFace",
        "CBlock",
        "None",
        "Stone",
    ]


class ExterQual:
    values = [
        "Ex",
        "Gd",
        "TA",
        "Fa",
        "Po",
    ]


class ExterCond:
    values = [
        "Ex",
        "Gd",
        "TA",
        "Fa",
        "Po",
    ]


class Foundation:
    values = [
        "BrkTil",
        "CBlock",
        "PConc",
        "Slab",
        "Stone",
        "Wood",
    ]

class BsmtQual:
    values = [
        "Ex",
        "Gd",
        "TA",
        "Fa",
        "Po",
        "NA",
    ]

class BsmtCond:
    values = [
        "Ex",
        "Gd",
        "TA",
        "Fa",
        "Po",
        "NA",
    ]

class BsmtExposure:
    values = [
       "Gd",
       "Av",
       "Mn",
       "No",
       "NA",
    ]


class BsmtFinType1:
    values = [
       "GLQ",
       "ALQ",
       "BLQ",
       "Rec",
       "LwQ",
       "Unf",
       "NA",
    ]

class BsmtFinType2:
    values = [
       "GLQ",
       "ALQ",
       "BLQ",
       "Rec",
       "LwQ",
       "Unf",
       "NA",
    ]


class Heating:
    values = [
       "Floor",
       "GasA",
       "GasW",
       "Grav",
       "OthW",
       "Wall",
    ]


class HeatingQC:
    values = [
        "Ex",
        "Gd",
        "TA",
        "Fa",
        "Po",
    ]


class CentralAir:
    values = [
        "N",
        "Y"
    ]


class Electrical:
    values = [
       "SBrkr",
       "FuseA",
       "FuseF",
       "FuseP",
       "Mix",
    ]


class KitchenQual:
    values = [
        "Ex",
        "Gd",
        "TA",
        "Fa",
        "Po",
    ]


class Functional:
    values = [
       "Typ",
       "Min1",
       "Min2",
       "Mod",
       "Maj1",
       "Maj2",
       "Sev",
       "Sal",
    ]


class FireplaceQu:
    values = [
        "Ex",
        "Gd",
        "TA",
        "Fa",
        "Po",
        "NA",
    ]


class GarageType:
    values = [
       "2Types",
       "Attchd",
       "Basment",
       "BuiltIn",
       "CarPort",
       "Detchd",
       "NA",
    ]

class GarageFinish:
    values = [
       "Fin",
       "RFn",
       "Unf",
       "NA",
    ]


class GarageQual:
    values = [
        "Ex",
        "Gd",
        "TA",
        "Fa",
        "Po",
        "NA",
    ]


class GarageCond:
    values = [
        "Ex",
        "Gd",
        "TA",
        "Fa",
        "Po",
        "NA",
    ]


class PavedDrive:
    values = [
        "Y",
        "P",
        "N",
    ]


class PoolQC:
    values = [
       "Ex",
       "Gd",
       "TA",
       "Fa",
       "NA",
    ]


class Fence:
    values = [
       "GdPrv",
       "MnPrv",
       "GdWo",
       "MnWw",
       "NA",
    ]


class MiscFeature:
    values = [
       "Elev",
       "Gar2",
       "Othr",
       "Shed",
       "TenC",
       "NA",
    ]


class SaleType:
    values = [
       "WD",
       "CWD",
       "VWD",
       "New",
       "COD",
       "Con",
       "ConLw",
       "ConLI",
       "ConLD",
       "Oth",
    ]


class SaleCondition:
    values = [
       "Normal",
       "Abnorml",
       "AdjLand",
       "Alloca",
       "Family",
       "Partial",
    ]


class Columns:
    columns = {
        "MSZoning": MSZoning(),
        "Street": Street(),
        "Alley": Alley(),
        "LotShape": LotShape(),
        "LandContour": LandContour(),
        "Utilities": Utilities(),
        "LotConfig": LotConfig(),
        "LandSlope": LandSlope(),
        "Neighborhood": Neighborhood(),
        "Condition1": Condition1(),
        "Condition2": Condition2(),
        "BldgType": BldgType(),
        "HouseStyle": HouseStyle(),
        "RoofStyle": RoofStyle(),
        "RoofMatl": RoofMatl(),
        "Exterior1st": Exterior1st(),
        "Exterior2nd": Exterior2nd(),
        "MasVnrType": MasVnrType(),
        "ExterQual": ExterQual(),
        "ExterCond": ExterCond(),
        "Foundation": Foundation(),
        "BsmtQual": BsmtQual(),
        "BsmtCond": BsmtCond(),
        "BsmtExposure": BsmtExposure(),
        "BsmtFinType1": BsmtFinType1(),
        "BsmtFinType2": BsmtFinType2(),
        "Heating": Heating(),
        "HeatingQC": HeatingQC(),
        "CentralAir": CentralAir(),
        "Electrical": Electrical(),
        "KitchenQual": KitchenQual(),
        "Functional": Functional(),
        "FireplaceQu": FireplaceQu(),
        "GarageType": GarageType(),
        "GarageFinish": GarageFinish(),
        "GarageQual": GarageQual(),
        "GarageCond": GarageCond(),
        "PavedDrive": PavedDrive(),
        "PoolQC": PoolQC(),
        "Fence": Fence(),
        "MiscFeature": MiscFeature(),
        "SaleType": SaleType(),
        "SaleCondition": SaleCondition(),


}














