import csv
file = open('Liver.TXT', 'r')
Patient_data= {}

for char in file:

    key = char[0:8]
    year = char[38:42]
    primary_site = char[43:46]
    #if int(primary_site) >=340 and int(primary_site) <= 349:
    #identify the cancer type in the txt file
    if int(primary_site) == 220:
        if int(year) <= 2010 and int(year)>= 1995:
            if key not in Patient_data.keys():
                # ignore data with death due to selected cancer
                if char[254:259] != '21071':
                    Patient_data[key] = {}
                    Patient_data_id = Patient_data[key]

                    Patient_data_id['MARITAL_STATUS_AT_DX'] = char[18:19]
                    Patient_data_id['RACE_ETHNICITY'] = char[19:21]
                    Patient_data_id['AGE_AT_DIAGNOSIS'] = char[24:27]
                    Patient_data_id['PRIMARY_SITE'] = char[42:46]
                    Patient_data_id['LATERALITY'] = char[46:47]
                    Patient_data_id['BEHAVIOUR_CODE_ICD03'] = char[56:57]
                    Patient_data_id['GRADE'] = char[57:58]
                    Patient_data_id['EOD_TUMOR_SIZE'] = char[60:63]
                    Patient_data_id['EOD_EXTENSION'] = char[63:65]
                    Patient_data_id['EOD_LYMPH_NODE_INV'] = char[67:68]
                    Patient_data_id['REASON_FOR_NO_SURG'] = char[165:166]
                    Patient_data_id['RX_SUMM_SURG_TYPE'] = char[169:171]
                    Patient_data_id['SEQUENCE_NUMBER_CENTRAL'] = char[34:36]
                    Patient_data_id['CAUSE_OF_DEATH_TO_SEER_SITE_RECODE'] = char[254:259]
                    Patient_data_id['DIAGNOSTIC_CONFIRMATION'] = char[58:59]
                    Patient_data_id['SEER_TYPE_OF_FOLLOWUP'] = char[190:191]
                    Patient_data_id['SEX'] = char[23:24]
                    Patient_data_id['YEAR_OF_DIAGNOSIS'] = char[38:42]
                    Patient_data_id['TARGET'] = 'NO RECURRENCE'

            else:
                Patient_data_year_of_diagnosis = Patient_data[key]['YEAR_OF_DIAGNOSIS'];
                next_year_of_diagnosis = char[38:42]
                diff = int(next_year_of_diagnosis) - int(Patient_data_year_of_diagnosis)

                if diff <= 5:
                    Patient_data[key]['TARGET'] = "RECURRENCE"

csv_columns = ['SEQUENCE_NUMBER_CENTRAL','MARITAL_STATUS_AT_DX', 'RACE_ETHNICITY',
               'CAUSE_OF_DEATH_TO_SEER_SITE_RECODE', 'SEER_TYPE_OF_FOLLOWUP', 'GRADE',
               'LATERALITY', 'EOD_TUMOR_SIZE', 'RX_SUMM_SURG_TYPE', 'YEAR_OF_DIAGNOSIS', 'SEX', 'DIAGNOSTIC_CONFIRMATION',
               'REASON_FOR_NO_SURG', 'PRIMARY_SITE', 'AGE_AT_DIAGNOSIS', 'TARGET',
               'EOD_LYMPH_NODE_INV', 'EOD_EXTENSION', 'BEHAVIOUR_CODE_ICD03'];
with open("data_test.csv", "w") as fp:
    wr = csv.writer(fp, dialect='excel')
    wr.writerow(csv_columns)


for key in Patient_data.keys():

    with open("data_test.csv", "a") as fp:
        wr = csv.writer(fp, dialect='excel')
        wr.writerow(Patient_data[key].values())







