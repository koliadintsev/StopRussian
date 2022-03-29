from DataImport import import_companies_ua, import_sanctions_usa, import_sanctions_uk, import_from_russia, import_sanctions_eu
from Search import elasticsearch_handler

def main():
    #import_companies_ua.find_russian_data_from_xml()
    #import_companies_ua.import_data_from_xml()
    #result = import_sanctions_usa.import_data_from_xml()
    #result = import_sanctions_uk.import_data_from_xml()
    #import_from_russia.find_founders_from_crimea()
    #result = import_sanctions_eu.import_data_from_xml()
    #elasticsearch_handler.create_index()
    elasticsearch_handler.delete_index()
    #p, t, n = elasticsearch_handler.search_match_request('vladimir putin')
    #s, h, l = elasticsearch_handler.search_fuzzy_request('vladimir putin')

    print('a')

    
main()
