from DataModel.EU.sanction_EU_generic import SanctionEUGeneric


class SanctionEU(SanctionEUGeneric):

    def __init__(self, code='', classificationCode='P', nameAlias=None, citizenship=None, birthdate=None,
                 address=None,
                 identification=None, delistingDate='', designationDate='', unitedNationId='', euReferenceNumber='', id = 0):
        super().__init__()
        self.id = id
        if identification is None:
            identification = [] #list of sactionEUIdentificationType
        if address is None:
            address = [] #list of sanctionEUAddress
        if birthdate is None:
            birthdate = [] #list of sanctionEUBirthdate
        if citizenship is None:
            citizenship = [] #list of sanctionEUCitizenship
        if nameAlias is None:
            nameAlias = [] #list of sanctionEUName
        self.euReferenceNumber = euReferenceNumber
        self.unitedNationId = unitedNationId
        self.designationDate = designationDate
        self.delistingDate = delistingDate
        self.identification = identification
        self.address = address
        self.birthdate = birthdate
        self.citizenship = citizenship
        self.nameAlias = nameAlias
        self.classificationCode = classificationCode
        self.code = code
