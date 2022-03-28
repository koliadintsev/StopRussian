class SanctionUK:

    def __init__(self, LastUpdated='', DateDesignated='', UniqueID='', OFSIGroupID='', UNReferenceNumber='', RegimeName='',
                 Names=None, NonLatinNames=None, IndividualEntityShip='', DesignationSource='', SanctionsImposed='',
                 SanctionsImposedIndicators=None, OtherInformation='', UKStatementofReasons='', Addresses=None,
                 PhoneNumbers=None, EmailAddresses=None, IndividualDetails=None, EntityDetails=None, id = 0):
        self.id = id
        if EntityDetails is None:
            EntityDetails = []
        self.EntityDetails = EntityDetails
        self.SanctionsImposed = SanctionsImposed
        if IndividualDetails is None:
            IndividualDetails = [] #list of sanction_UK_individual
        self.IndividualDetails = IndividualDetails
        if EmailAddresses is None:
            EmailAddresses = [] #list of strings
        self.EmailAddresses = EmailAddresses
        if PhoneNumbers is None:
            PhoneNumbers = [] #list of strings
        self.PhoneNumbers = PhoneNumbers
        if Addresses is None:
            Addresses = [] #list of sanction_UK_address
        self.Addresses = Addresses
        self.UKStatementofReasons = UKStatementofReasons
        self.OtherInformation = OtherInformation
        if SanctionsImposedIndicators is None:
            SanctionsImposedIndicators = [] #list of sanction_UK_indicator
        self.SanctionsImposedIndicators = SanctionsImposedIndicators
        self.DesignationSource = DesignationSource
        self.IndividualEntityShip = IndividualEntityShip
        if NonLatinNames is None:
            NonLatinNames = [] #list of strings
        self.NonLatinNames = NonLatinNames
        if Names is None:
            Names = [] #list of sanction_UK_name
        self.Names = Names
        self.RegimeName = RegimeName
        self.UNReferenceNumber = UNReferenceNumber
        self.OFSIGroupID = OFSIGroupID
        self.UniqueID = UniqueID
        self.DateDesignated = DateDesignated
        self.LastUpdated = LastUpdated