class SanctionUSA:

    def __init__(self, uid=0, firstName='', lastName='', title='', sdnType='', remarks='', programList=None,
                 idList=None, akaList=None, addressList=None, nationalityList=None, citizenshipList=None,
                 dateOfBirthList=None, placeOfBirthList=None, vesselInfo=None, id = 0):
        self.id = id
        if vesselInfo is None:
            vesselInfo = []
        self.vesselInfo = vesselInfo #list of SanctionUSAVessel
        if placeOfBirthList is None:
            placeOfBirthList = []
        self.placeOfBirthList = placeOfBirthList #list of SanctionUSAPlaceOfBirth
        if dateOfBirthList is None:
            dateOfBirthList = []
        self.dateOfBirthList = dateOfBirthList #list of SanctionUSADateOfBirth
        if citizenshipList is None:
            citizenshipList = []
        self.citizenshipList = citizenshipList #list of SanctionUSANationality
        if nationalityList is None:
            nationalityList = []
        self.nationalityList = nationalityList #list of SanctionUSANationality
        if addressList is None:
            addressList = []
        self.addressList = addressList #list of SanctionUSAAddress
        if akaList is None:
            akaList = []
        self.akaList = akaList #list of SanctionUSAAka
        if idList is None:
            idList = []
        if programList is None:
            programList = []
        self.idList = idList #list of SanctionUSADocument
        self.programList = programList #list of strings
        self.remarks = remarks
        self.sdnType = sdnType
        self.title = title
        self.lastName = lastName
        self.firstName = firstName
        self.uid = uid
        name = ''
        if not firstName:
            name = lastName
        else:
            name = firstName + ' ' + lastName
        self.wholeName = name

