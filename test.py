from DataImport import import_companies_ua, import_sanctions_usa, import_sanctions_uk, import_from_russia


def main():
    #import_companies_ua.find_russian_data_from_xml()
    #import_companies_ua.import_data_from_xml()
    #result = import_sanctions_usa.import_data_from_xml()
    result = import_sanctions_uk.import_data_from_xml()
    #import_from_russia.find_founders_from_crimea()
    print('a')

    
main()
