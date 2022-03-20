class SanctionUSA:

    def __init__(self, LastUpdated='', DateDesignated='', UniqueID='', OFSIGroupID='', UNReferenceNumber='', RegimeName='',
                 Names=None, NonLatinNames=None, IndividualEntityShip='', DesignationSource='',
                 SanctionsImposedIndicators=None, OtherInformation='', UKStatementofReasons='', Addresses=None,
                 PhoneNumbers=None, EmailAddresses=None):
        if EmailAddresses is None:
            EmailAddresses = [] #list of strings
        self.EmailAddresses = EmailAddresses
        if PhoneNumbers is None:
            PhoneNumbers = [] #list of strings
        self.PhoneNumbers = PhoneNumbers
        if Addresses is None:
            Addresses = []
        self.Addresses = Addresses
        self.UKStatementofReasons = UKStatementofReasons
        self.OtherInformation = OtherInformation
        if SanctionsImposedIndicators is None:
            SanctionsImposedIndicators = []
        self.SanctionsImposedIndicators = SanctionsImposedIndicators
        self.DesignationSource = DesignationSource
        self.IndividualEntityShip = IndividualEntityShip
        if NonLatinNames is None:
            NonLatinNames = [] #list of strings
        self.NonLatinNames = NonLatinNames
        if Names is None:
            Names = []
        self.Names = Names
        self.RegimeName = RegimeName
        self.UNReferenceNumber = UNReferenceNumber
        self.OFSIGroupID = OFSIGroupID
        self.UniqueID = UniqueID
        self.DateDesignated = DateDesignated
        self.LastUpdated = LastUpdated