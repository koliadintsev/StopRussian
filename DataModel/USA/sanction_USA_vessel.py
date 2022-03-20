class SanctionUSAVessel:

    def __init__(self, callSign='', vesselType='', vesselFlag='', vesselOwner='', tonnage=0, grossRegisteredTonnage=0):
        self.grossRegisteredTonnage = grossRegisteredTonnage
        self.tonnage = tonnage
        self.vesselOwner = vesselOwner
        self.vesselFlag = vesselFlag
        self.vesselType = vesselType
        self.callSign = callSign
