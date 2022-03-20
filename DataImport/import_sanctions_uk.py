from lxml import etree
from DataModel.USA import sanction_USA, sanction_USA_vessel, sanction_USA_aka, sanction_USA_address, \
    sanction_USA_document, sanction_USA_nationality, sanction_USA_placeofbirth, sanction_USA_dateofbirth
from settings import STATIC_ROOT

SANCTIONS_LIST = STATIC_ROOT + "/Sanctions/UK/UK_Sanctions_List.xml"
sanctions = []


def import_data_from_xml():
    global sanctions
    #parser = etree.XMLParser(recover=True, huge_tree=True)

    for event, element in etree.iterparse(SANCTIONS_LIST, tag="{http://tempuri.org/sdnList.xsd}sdnEntry", recover=True, huge_tree=True, ):
        import_data_from_element(element)
        element.clear()

    """
    tree = ET.fromstring(file.read().strip())
    executor = concurrent.futures.ThreadPoolExecutor(100)
    futures = [executor.submit(import_data_from_element, item, companies) for item in tree.findall('.//document')]
    concurrent.futures.wait(futures)
    """
    print('import finished')
    return sanctions


def import_data_from_element(doc):
    global sanctions

    uid = 0
    firstName = ''
    lastName = ''
    title = ''
    sdnType = ''
    remarks = ''
    programList = []
    idList = []
    akaList = []
    addressList = []
    nationalityList = []
    citizenshipList = []
    dateOfBirthList = []
    placeOfBirthList = []
    vesselInfo = []

    sanction = sanction_USA.SanctionUSA()

    for item in doc.getchildren():
        item.tag=item.tag.split('}')[-1]
        if item.tag == 'uid':
            uid = int(item.text)
        elif item.tag == 'firstName':
            firstName = item.text
        elif item.tag == 'lastName':
            lastName = item.text
        elif item.tag == 'title':
            title = item.text
        elif item.tag == 'sdnType':
            sdnType = item.text
        elif item.tag == 'remarks':
            remarks = item.text
        elif item.tag == 'programList':
            for child in item.getchildren():
                programList.append(child.text)
        elif item.tag == 'idList':
            for child in item.getchildren():
                document = sanction_USA_document.SanctionUSADocument()
                for c in child.getchildren():
                    c.tag = c.tag.split('}')[-1]
                    if c.tag == 'uid':
                        document.uid = int(c.text)
                    elif c.tag == 'idType':
                        document.idType = c.text
                    elif c.tag == 'issueDate':
                        document.issueDate = c.text
                    elif c.tag == 'expirationDate':
                        document.expirationDate = c.text
                    elif c.tag == 'idNumber':
                        document.idNumber = c.text
                    elif c.tag == 'idCountry':
                        document.idCountry = c.text
                idList.append(document)
        elif item.tag == 'akaList':
            for child in item.getchildren():
                aka = sanction_USA_aka.SanctionUSAAka()
                for c in child.getchildren():
                    c.tag = c.tag.split('}')[-1]
                    if c.tag == 'uid':
                        aka.uid = int(c.text)
                    elif c.tag == 'type':
                        aka.type = c.text
                    elif c.tag == 'lastName':
                        aka.lastName = c.text
                    elif c.tag == 'firstName':
                        aka.firstName = c.text
                    elif c.tag == 'category':
                        aka.category = c.text
                akaList.append(aka)
        elif item.tag == 'addressList':
            for child in item.getchildren():
                child.tag = child.tag.split('}')[-1]
                address = sanction_USA_address.SanctionUSAAddress()
                for c in child.getchildren():
                    c.tag = c.tag.split('}')[-1]
                    if c.tag == 'uid':
                        address.uid = int(c.text)
                    elif c.tag == 'address1':
                        address.address1 = c.text
                    elif c.tag == 'address2':
                        address.address2 = c.text
                    elif c.tag == 'address3':
                        address.address3 = c.text
                    elif c.tag == 'country':
                        address.country = c.text
                    elif c.tag == 'city':
                        address.city = c.text
                    elif c.tag == 'postalCode':
                        address.postalCode = c.text
                    elif c.tag == 'stateOrProvince':
                        address.stateOrProvince = c.text
                addressList.append(address)
        elif item.tag == 'nationalityList':
            for child in item.getchildren():
                nationality = sanction_USA_nationality.SanctionUSANationality()
                for c in child.getchildren():
                    c.tag = c.tag.split('}')[-1]
                    if c.tag == 'uid':
                        nationality.uid = int(c.text)
                    elif c.tag == 'country':
                        nationality.country = c.text
                    elif c.tag == 'mainEntry':
                        nationality.mainEntry = bool(c.text)
                nationalityList.append(nationality)
        elif item.tag == 'citizenshipList':
            for child in item.getchildren():
                citizenship = sanction_USA_nationality.SanctionUSANationality()
                for c in child.getchildren():
                    c.tag = c.tag.split('}')[-1]
                    if c.tag == 'uid':
                        citizenship.uid = int(c.text)
                    elif c.tag == 'country':
                        citizenship.country = c.text
                    elif c.tag == 'mainEntry':
                        citizenship.mainEntry = bool(c.text)
                citizenshipList.append(citizenship)
        elif item.tag == 'dateOfBirthList':
            for child in item.getchildren():
                dateOfBirth = sanction_USA_dateofbirth.SanctionUSADateOfBirth()
                for c in child.getchildren():
                    c.tag = c.tag.split('}')[-1]
                    if c.tag == 'uid':
                        dateOfBirth.uid = int(c.text)
                    elif c.tag == 'dateOfBirth':
                        dateOfBirth.dateOfBirth = c.text
                    elif c.tag == 'mainEntry':
                        dateOfBirth.mainEntry = bool(c.text)
                dateOfBirthList.append(dateOfBirth)
        elif item.tag == 'placeOfBirthList':
            for child in item.getchildren():
                placeOfBirth = sanction_USA_placeofbirth.SanctionUSAPlaceOfBirth()
                for c in child.getchildren():
                    c.tag = c.tag.split('}')[-1]
                    if c.tag == 'uid':
                        placeOfBirth.uid = int(c.text)
                    elif c.tag == 'placeOfBirth':
                        placeOfBirth.placeOfBirth = c.text
                    elif c.tag == 'mainEntry':
                        placeOfBirth.mainEntry = bool(c.text)
                placeOfBirthList.append(placeOfBirth)
        elif item.tag == 'vesselInfo':
            for child in item.getchildren():
                vessel = sanction_USA_vessel.SanctionUSAVessel()
                for c in child.getchildren():
                    c.tag = c.tag.split('}')[-1]
                    if c.tag == 'uid':
                        vessel.uid = int(c.text)
                    elif c.tag == 'vesselOwner':
                        vessel.vesselOwner = c.text
                    elif c.tag == 'vesselType':
                        vessel.vesselType = c.text
                    elif c.tag == 'vesselFlag':
                        vessel.vesselFlag = c.text
                    elif c.tag == 'tonnage':
                        vessel.tonnage = c.text
                    elif c.tag == 'callSign':
                        vessel.callSign = c.text
                    elif c.tag == 'grossRegisteredTonnage':
                        vessel.grossRegisteredTonnage = c.text
                vesselInfo.append(vessel)
    sanction = sanction_USA.SanctionUSA(uid, firstName, lastName, title, sdnType, remarks, programList, idList,
                                        akaList, addressList, nationalityList, citizenshipList, dateOfBirthList,
                                        placeOfBirthList, vesselInfo)
    sanctions.append(sanction)
    #print(str(uid) + ' added successfully')
