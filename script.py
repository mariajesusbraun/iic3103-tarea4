import requests
from requests.structures import CaseInsensitiveDict
import xml.etree.ElementTree as ET
import pandas as pd
import numpy as np
import gspread

d = []

# Australia (AUS)
url_aus = 'https://storage.googleapis.com/tarea-4.2021-1.tallerdeintegracion.cl/gho_AUS.xml'
headers_aus = CaseInsensitiveDict()
headers_aus["Accept"] = "application/xml"
r_aus = requests.get(url_aus, headers=headers_aus)
f_aus = open("gho_aus.xml", "w")
f_aus.write(r_aus.text)
f_aus.close()
tree_aus = ET.parse('gho_aus.xml'.format('country'))
root_aus = tree_aus.getroot()
for fact in root_aus.findall('Fact'):
    gho_aus = fact.find('GHO')
    if (gho_aus != None):
        gho_aus = fact.find('GHO').text
        if (gho_aus == 'Number of deaths' or gho_aus == 'Number of infant deaths' or gho_aus == 'Number of under-five deaths' or gho_aus == 'Mortality rate for 5-14 year-olds (probability of dying per 1000 children aged 5-14 years)' or gho_aus == 'Adult mortality rate (probability of dying between 15 and 60 years per 1000 population)' or gho_aus == 'Estimates of number of homicides' or gho_aus == 'Crude suicide rates (per 100 000 population)' or gho_aus == 'Mortality rate attributed to unintentional poisoning (per 100 000 population)' or gho_aus == 'Number of deaths attributed to non-communicable diseases, by type of disease and sex' or gho_aus == 'Estimated road traffic death rate (per 100 000 population)' or gho_aus == 'Estimated number of road traffic deaths' or gho_aus == 'Mean BMI (kg/m&#xb2;) (crude estimate)' or gho_aus == 'Mean BMI (kg/m&#xb2;) (age-standardized estimate)' or gho_aus == 'Prevalence of obesity among adults, BMI > 30 (age-standardized estimate) (%)' or gho_aus == 'Prevalence of obesity among children and adolescents, BMI > +2 standard deviations above the median (crude estimate) (%)' or gho_aus == 'Prevalence of overweight among adults, BMI > 25 (age-standardized estimate) (%)' or gho_aus == 'Prevalence of overweight among children and adolescents, BMI > +1 standard deviations above the median (crude estimate) (%)' or gho_aus == 'Prevalence of underweight among adults, BMI < 18.5 (age-standardized estimate) (%)' or gho_aus == 'Prevalence of thinness among children and adolescents, BMI < -2 standard deviations below the median (crude estimate) (%)' or gho_aus == 'Alcohol, recorded per capita (15+) consumption (in litres of pure alcohol)' or gho_aus == 'Estimate of daily cigarette smoking prevalence (%)' or gho_aus == 'Estimate of daily tobacco smoking prevalence (%)' or gho_aus == 'Estimate of current cigarette smoking prevalence (%)' or gho_aus == 'Estimate of current tobacco smoking prevalence (%)' or gho_aus == 'Mean systolic blood pressure (crude estimate)' or gho_aus == 'Mean fasting blood glucose (mmol/l) (crude estimate)' or gho_aus == 'Mean Total Cholesterol (crude estimate)'):
            country_aus = fact.find('COUNTRY')
            if (country_aus != None):
                country_aus = fact.find('COUNTRY').text
            sex_aus = fact.find('SEX')
            if (sex_aus != None):
                sex_aus = fact.find('SEX').text
            year_aus = fact.find('YEAR')
            if (year_aus != None):
                year_aus = fact.find('YEAR').text
                if ('-' in year_aus):
                    year_aus = year_aus[0:4]
                year_aus = int(year_aus)
            ghecauses_aus = fact.find('GHECAUSES')
            if (ghecauses_aus != None):
                ghecauses_aus = fact.find('GHECAUSES').text
            agegroup_aus = fact.find('AGEGROUP')
            if (agegroup_aus != None):
                agegroup_aus = fact.find('AGEGROUP').text
            display_aus = fact.find('Display')
            if (display_aus != None):
                display_aus = fact.find('Display').text
            numeric_aus = fact.find('Numeric')
            if (numeric_aus != None):
                numeric_aus = float(fact.find('Numeric').text)
            low_aus = fact.find('Low')
            if (low_aus != None):
                low_aus = float(fact.find('Low').text)
            high_aus = fact.find('High')
            if (high_aus != None):
                high_aus = float(fact.find('High').text)
            lista_aus = [gho_aus, country_aus, sex_aus, year_aus, ghecauses_aus, agegroup_aus, display_aus, numeric_aus, low_aus, high_aus]
            d.append(lista_aus)

# Brasil (BRA)
url_bra = 'https://storage.googleapis.com/tarea-4.2021-1.tallerdeintegracion.cl/gho_BRA.xml'
headers_bra = CaseInsensitiveDict()
headers_bra["Accept"] = "application/xml"
r_bra = requests.get(url_bra, headers=headers_bra)
f_bra = open("gho_bra.xml", "w")
f_bra.write(r_bra.text)
f_bra.close()
tree_bra = ET.parse('gho_bra.xml'.format('country'))
root_bra = tree_bra.getroot()
for fact in root_bra.findall('Fact'):
    gho_bra = fact.find('GHO')
    if (gho_bra != None):
        gho_bra = fact.find('GHO').text
        if (gho_bra == 'Number of deaths' or gho_bra == 'Number of infant deaths' or gho_bra == 'Number of under-five deaths' or gho_bra == 'Mortality rate for 5-14 year-olds (probability of dying per 1000 children aged 5-14 years)' or gho_bra == 'Adult mortality rate (probability of dying between 15 and 60 years per 1000 population)' or gho_bra == 'Estimates of number of homicides' or gho_bra == 'Crude suicide rates (per 100 000 population)' or gho_bra == 'Mortality rate attributed to unintentional poisoning (per 100 000 population)' or gho_bra == 'Number of deaths attributed to non-communicable diseases, by type of disease and sex' or gho_bra == 'Estimated road traffic death rate (per 100 000 population)' or gho_bra == 'Estimated number of road traffic deaths' or gho_bra == 'Mean BMI (kg/m&#xb2;) (crude estimate)' or gho_bra == 'Mean BMI (kg/m&#xb2;) (age-standardized estimate)' or gho_bra == 'Prevalence of obesity among adults, BMI > 30 (age-standardized estimate) (%)' or gho_bra == 'Prevalence of obesity among children and adolescents, BMI > +2 standard deviations above the median (crude estimate) (%)' or gho_bra == 'Prevalence of overweight among adults, BMI > 25 (age-standardized estimate) (%)' or gho_bra == 'Prevalence of overweight among children and adolescents, BMI > +1 standard deviations above the median (crude estimate) (%)' or gho_bra == 'Prevalence of underweight among adults, BMI < 18.5 (age-standardized estimate) (%)' or gho_bra == 'Prevalence of thinness among children and adolescents, BMI < -2 standard deviations below the median (crude estimate) (%)' or gho_bra == 'Alcohol, recorded per capita (15+) consumption (in litres of pure alcohol)' or gho_bra == 'Estimate of daily cigarette smoking prevalence (%)' or gho_bra == 'Estimate of daily tobacco smoking prevalence (%)' or gho_bra == 'Estimate of current cigarette smoking prevalence (%)' or gho_bra == 'Estimate of current tobacco smoking prevalence (%)' or gho_bra == 'Mean systolic blood pressure (crude estimate)' or gho_bra == 'Mean fasting blood glucose (mmol/l) (crude estimate)' or gho_bra == 'Mean Total Cholesterol (crude estimate)'):
            country_bra = fact.find('COUNTRY')
            if (country_bra != None):
                country_bra = fact.find('COUNTRY').text
            sex_bra = fact.find('SEX')
            if (sex_bra != None):
                sex_bra = fact.find('SEX').text
            year_bra = fact.find('YEAR')
            if (year_bra != None):
                year_bra = fact.find('YEAR').text
                if ('-' in year_bra):
                    year_bra = year_bra[0:4]
                year_bra = int(year_bra)
            ghecauses_bra = fact.find('GHECAUSES')
            if (ghecauses_bra != None):
                ghecauses_bra = fact.find('GHECAUSES').text
            agegroup_bra = fact.find('AGEGROUP')
            if (agegroup_bra != None):
                agegroup_bra = fact.find('AGEGROUP').text
            display_bra = fact.find('Display')
            if (display_bra != None):
                display_bra = fact.find('Display').text
            numeric_bra = fact.find('Numeric')
            if (numeric_bra != None):
                numeric_bra = float(fact.find('Numeric').text)
            low_bra = fact.find('Low')
            if (low_bra != None):
                low_bra = float(fact.find('Low').text)
            high_bra = fact.find('High')
            if (high_bra != None):
                high_bra = float(fact.find('High').text)
            lista_bra = [gho_bra, country_bra, sex_bra, year_bra, ghecauses_bra, agegroup_bra, display_bra, numeric_bra, low_bra, high_bra]
            d.append(lista_bra)

# Chile (CHL)
url_chl = 'https://storage.googleapis.com/tarea-4.2021-1.tallerdeintegracion.cl/gho_CHL.xml'
headers_chl = CaseInsensitiveDict()
headers_chl["Accept"] = "application/xml"
r_chl = requests.get(url_chl, headers=headers_chl)
f_chl = open("gho_chl.xml", "w")
f_chl.write(r_chl.text)
f_chl.close()
tree_chl = ET.parse('gho_chl.xml'.format('country'))
root_chl = tree_chl.getroot()
for fact in root_chl.findall('Fact'):
    gho_chl = fact.find('GHO')
    if (gho_chl != None):
        gho_chl = fact.find('GHO').text
        if (gho_chl == 'Number of deaths' or gho_chl == 'Number of infant deaths' or gho_chl == 'Number of under-five deaths' or gho_chl == 'Mortality rate for 5-14 year-olds (probability of dying per 1000 children aged 5-14 years)' or gho_chl == 'Adult mortality rate (probability of dying between 15 and 60 years per 1000 population)' or gho_chl == 'Estimates of number of homicides' or gho_chl == 'Crude suicide rates (per 100 000 population)' or gho_chl == 'Mortality rate attributed to unintentional poisoning (per 100 000 population)' or gho_chl == 'Number of deaths attributed to non-communicable diseases, by type of disease and sex' or gho_chl == 'Estimated road traffic death rate (per 100 000 population)' or gho_chl == 'Estimated number of road traffic deaths' or gho_chl == 'Mean BMI (kg/m&#xb2;) (crude estimate)' or gho_chl == 'Mean BMI (kg/m&#xb2;) (age-standardized estimate)' or gho_chl == 'Prevalence of obesity among adults, BMI > 30 (age-standardized estimate) (%)' or gho_chl == 'Prevalence of obesity among children and adolescents, BMI > +2 standard deviations above the median (crude estimate) (%)' or gho_chl == 'Prevalence of overweight among adults, BMI > 25 (age-standardized estimate) (%)' or gho_chl == 'Prevalence of overweight among children and adolescents, BMI > +1 standard deviations above the median (crude estimate) (%)' or gho_chl == 'Prevalence of underweight among adults, BMI < 18.5 (age-standardized estimate) (%)' or gho_chl == 'Prevalence of thinness among children and adolescents, BMI < -2 standard deviations below the median (crude estimate) (%)' or gho_chl == 'Alcohol, recorded per capita (15+) consumption (in litres of pure alcohol)' or gho_chl == 'Estimate of daily cigarette smoking prevalence (%)' or gho_chl == 'Estimate of daily tobacco smoking prevalence (%)' or gho_chl == 'Estimate of current cigarette smoking prevalence (%)' or gho_chl == 'Estimate of current tobacco smoking prevalence (%)' or gho_chl == 'Mean systolic blood pressure (crude estimate)' or gho_chl == 'Mean fasting blood glucose (mmol/l) (crude estimate)' or gho_chl == 'Mean Total Cholesterol (crude estimate)'):
            country_chl = fact.find('COUNTRY')
            if (country_chl != None):
                country_chl = fact.find('COUNTRY').text
            sex_chl = fact.find('SEX')
            if (sex_chl != None):
                sex_chl = fact.find('SEX').text
            year_chl = fact.find('YEAR')
            if (year_chl != None):
                year_chl = fact.find('YEAR').text
                if ('-' in year_chl):
                    year_chl = year_chl[0:4]
                year_chl = int(year_chl)
            ghecauses_chl = fact.find('GHECAUSES')
            if (ghecauses_chl != None):
                ghecauses_chl = fact.find('GHECAUSES').text
            agegroup_chl = fact.find('AGEGROUP')
            if (agegroup_chl != None):
                agegroup_chl = fact.find('AGEGROUP').text
            display_chl = fact.find('Display')
            if (display_chl != None):
                display_chl = fact.find('Display').text
            numeric_chl = fact.find('Numeric')
            if (numeric_chl != None):
                numeric_chl = float(fact.find('Numeric').text)
            low_chl = fact.find('Low')
            if (low_chl != None):
                low_chl = float(fact.find('Low').text)
            high_chl = fact.find('High')
            if (high_chl != None):
                high_chl = float(fact.find('High').text)
            lista_chl = [gho_chl, country_chl, sex_chl, year_chl, ghecauses_chl, agegroup_chl, display_chl, numeric_chl, low_chl, high_chl]
            d.append(lista_chl)

# Costa Rica (CRI)
url_cri = 'https://storage.googleapis.com/tarea-4.2021-1.tallerdeintegracion.cl/gho_CRI.xml'
headers_cri = CaseInsensitiveDict()
headers_cri["Accept"] = "application/xml"
r_cri = requests.get(url_cri, headers=headers_cri)
f_cri = open("gho_cri.xml", "w")
f_cri.write(r_cri.text)
f_cri.close()
tree_cri = ET.parse('gho_cri.xml'.format('country'))
root_cri = tree_cri.getroot()
for fact in root_cri.findall('Fact'):
    gho_cri = fact.find('GHO')
    if (gho_cri != None):
        gho_cri = fact.find('GHO').text
        if (gho_cri == 'Number of deaths' or gho_cri == 'Number of infant deaths' or gho_cri == 'Number of under-five deaths' or gho_cri == 'Mortality rate for 5-14 year-olds (probability of dying per 1000 children aged 5-14 years)' or gho_cri == 'Adult mortality rate (probability of dying between 15 and 60 years per 1000 population)' or gho_cri == 'Estimates of number of homicides' or gho_cri == 'Crude suicide rates (per 100 000 population)' or gho_cri == 'Mortality rate attributed to unintentional poisoning (per 100 000 population)' or gho_cri == 'Number of deaths attributed to non-communicable diseases, by type of disease and sex' or gho_cri == 'Estimated road traffic death rate (per 100 000 population)' or gho_cri == 'Estimated number of road traffic deaths' or gho_cri == 'Mean BMI (kg/m&#xb2;) (crude estimate)' or gho_cri == 'Mean BMI (kg/m&#xb2;) (age-standardized estimate)' or gho_cri == 'Prevalence of obesity among adults, BMI > 30 (age-standardized estimate) (%)' or gho_cri == 'Prevalence of obesity among children and adolescents, BMI > +2 standard deviations above the median (crude estimate) (%)' or gho_cri == 'Prevalence of overweight among adults, BMI > 25 (age-standardized estimate) (%)' or gho_cri == 'Prevalence of overweight among children and adolescents, BMI > +1 standard deviations above the median (crude estimate) (%)' or gho_cri == 'Prevalence of underweight among adults, BMI < 18.5 (age-standardized estimate) (%)' or gho_cri == 'Prevalence of thinness among children and adolescents, BMI < -2 standard deviations below the median (crude estimate) (%)' or gho_cri == 'Alcohol, recorded per capita (15+) consumption (in litres of pure alcohol)' or gho_cri == 'Estimate of daily cigarette smoking prevalence (%)' or gho_cri == 'Estimate of daily tobacco smoking prevalence (%)' or gho_cri == 'Estimate of current cigarette smoking prevalence (%)' or gho_cri == 'Estimate of current tobacco smoking prevalence (%)' or gho_cri == 'Mean systolic blood pressure (crude estimate)' or gho_cri == 'Mean fasting blood glucose (mmol/l) (crude estimate)' or gho_cri == 'Mean Total Cholesterol (crude estimate)'):
            country_cri = fact.find('COUNTRY')
            if (country_cri != None):
                country_cri = fact.find('COUNTRY').text
            sex_cri = fact.find('SEX')
            if (sex_cri != None):
                sex_cri = fact.find('SEX').text
            year_cri = fact.find('YEAR')
            if (year_cri != None):
                year_cri = fact.find('YEAR').text
                if ('-' in year_cri):
                    year_cri = year_cri[0:4]
                year_cri = int(year_cri)
            ghecauses_cri = fact.find('GHECAUSES')
            if (ghecauses_cri != None):
                ghecauses_cri = fact.find('GHECAUSES').text
            agegroup_cri = fact.find('AGEGROUP')
            if (agegroup_cri != None):
                agegroup_cri = fact.find('AGEGROUP').text
            display_cri = fact.find('Display')
            if (display_cri != None):
                display_cri = fact.find('Display').text
            numeric_cri = fact.find('Numeric')
            if (numeric_cri != None):
                numeric_cri = float(fact.find('Numeric').text)
            low_cri = fact.find('Low')
            if (low_cri != None):
                low_cri = float(fact.find('Low').text)
            high_cri = fact.find('High')
            if (high_cri != None):
                high_cri = float(fact.find('High').text)
            lista_cri = [gho_cri, country_cri, sex_cri, year_cri, ghecauses_cri, agegroup_cri, display_cri, numeric_cri, low_cri, high_cri]
            d.append(lista_cri)

# Sufáfrica (ZAF)
url_zaf = 'https://storage.googleapis.com/tarea-4.2021-1.tallerdeintegracion.cl/gho_ZAF.xml'
headers_zaf = CaseInsensitiveDict()
headers_zaf["Accept"] = "application/xml"
r_zaf = requests.get(url_zaf, headers=headers_zaf)
f_zaf = open("gho_zaf.xml", "w")
f_zaf.write(r_zaf.text)
f_zaf.close()
tree_zaf = ET.parse('gho_zaf.xml'.format('country'))
root_zaf = tree_zaf.getroot()
for fact in root_zaf.findall('Fact'):
    gho_zaf = fact.find('GHO')
    if (gho_zaf != None):
        gho_zaf = fact.find('GHO').text
        if (gho_zaf == 'Number of deaths' or gho_zaf == 'Number of infant deaths' or gho_zaf == 'Number of under-five deaths' or gho_zaf == 'Mortality rate for 5-14 year-olds (probability of dying per 1000 children aged 5-14 years)' or gho_zaf == 'Adult mortality rate (probability of dying between 15 and 60 years per 1000 population)' or gho_zaf == 'Estimates of number of homicides' or gho_zaf == 'Crude suicide rates (per 100 000 population)' or gho_zaf == 'Mortality rate attributed to unintentional poisoning (per 100 000 population)' or gho_zaf == 'Number of deaths attributed to non-communicable diseases, by type of disease and sex' or gho_zaf == 'Estimated road traffic death rate (per 100 000 population)' or gho_zaf == 'Estimated number of road traffic deaths' or gho_zaf == 'Mean BMI (kg/m&#xb2;) (crude estimate)' or gho_zaf == 'Mean BMI (kg/m&#xb2;) (age-standardized estimate)' or gho_zaf == 'Prevalence of obesity among adults, BMI > 30 (age-standardized estimate) (%)' or gho_zaf == 'Prevalence of obesity among children and adolescents, BMI > +2 standard deviations above the median (crude estimate) (%)' or gho_zaf == 'Prevalence of overweight among adults, BMI > 25 (age-standardized estimate) (%)' or gho_zaf == 'Prevalence of overweight among children and adolescents, BMI > +1 standard deviations above the median (crude estimate) (%)' or gho_zaf == 'Prevalence of underweight among adults, BMI < 18.5 (age-standardized estimate) (%)' or gho_zaf == 'Prevalence of thinness among children and adolescents, BMI < -2 standard deviations below the median (crude estimate) (%)' or gho_zaf == 'Alcohol, recorded per capita (15+) consumption (in litres of pure alcohol)' or gho_zaf == 'Estimate of daily cigarette smoking prevalence (%)' or gho_zaf == 'Estimate of daily tobacco smoking prevalence (%)' or gho_zaf == 'Estimate of current cigarette smoking prevalence (%)' or gho_zaf == 'Estimate of current tobacco smoking prevalence (%)' or gho_zaf == 'Mean systolic blood pressure (crude estimate)' or gho_zaf == 'Mean fasting blood glucose (mmol/l) (crude estimate)' or gho_zaf == 'Mean Total Cholesterol (crude estimate)'):
            country_zaf = fact.find('COUNTRY')
            if (country_zaf != None):
                country_zaf = fact.find('COUNTRY').text
            sex_zaf = fact.find('SEX')
            if (sex_zaf != None):
                sex_zaf = fact.find('SEX').text
            year_zaf = fact.find('YEAR')
            if (year_zaf != None):
                year_zaf = fact.find('YEAR').text
                if ('-' in year_zaf):
                    year_zaf = year_zaf[0:4]
                year_zaf = int(year_zaf)
            ghecauses_zaf = fact.find('GHECAUSES')
            if (ghecauses_zaf != None):
                ghecauses_zaf = fact.find('GHECAUSES').text
            agegroup_zaf = fact.find('AGEGROUP')
            if (agegroup_zaf != None):
                agegroup_zaf = fact.find('AGEGROUP').text
            display_zaf = fact.find('Display')
            if (display_zaf != None):
                display_zaf = fact.find('Display').text
            numeric_zaf = fact.find('Numeric')
            if (numeric_zaf != None):
                numeric_zaf = float(fact.find('Numeric').text)
            low_zaf = fact.find('Low')
            if (low_zaf != None):
                low_zaf = float(fact.find('Low').text)
            high_zaf = fact.find('High')
            if (high_zaf != None):
                high_zaf = float(fact.find('High').text)
            lista_zaf = [gho_zaf, country_zaf, sex_zaf, year_zaf, ghecauses_zaf, agegroup_zaf, display_zaf, numeric_zaf, low_zaf, high_zaf]
            d.append(lista_zaf)

# Suiza (CHE)
url_che = 'https://storage.googleapis.com/tarea-4.2021-1.tallerdeintegracion.cl/gho_CHE.xml'
headers_che = CaseInsensitiveDict()
headers_che["Accept"] = "application/xml"
r_che = requests.get(url_che, headers=headers_che)
f_che = open("gho_che.xml", "w")
f_che.write(r_che.text)
f_che.close()
tree_che = ET.parse('gho_che.xml'.format('country'))
root_che = tree_che.getroot()
for fact in root_che.findall('Fact'):
    gho_che = fact.find('GHO')
    if (gho_che != None):
        gho_che = fact.find('GHO').text
        if (gho_che == 'Number of deaths' or gho_che == 'Number of infant deaths' or gho_che == 'Number of under-five deaths' or gho_che == 'Mortality rate for 5-14 year-olds (probability of dying per 1000 children aged 5-14 years)' or gho_che == 'Adult mortality rate (probability of dying between 15 and 60 years per 1000 population)' or gho_che == 'Estimates of number of homicides' or gho_che == 'Crude suicide rates (per 100 000 population)' or gho_che == 'Mortality rate attributed to unintentional poisoning (per 100 000 population)' or gho_che == 'Number of deaths attributed to non-communicable diseases, by type of disease and sex' or gho_che == 'Estimated road traffic death rate (per 100 000 population)' or gho_che == 'Estimated number of road traffic deaths' or gho_che == 'Mean BMI (kg/m&#xb2;) (crude estimate)' or gho_che == 'Mean BMI (kg/m&#xb2;) (age-standardized estimate)' or gho_che == 'Prevalence of obesity among adults, BMI > 30 (age-standardized estimate) (%)' or gho_che == 'Prevalence of obesity among children and adolescents, BMI > +2 standard deviations above the median (crude estimate) (%)' or gho_che == 'Prevalence of overweight among adults, BMI > 25 (age-standardized estimate) (%)' or gho_che == 'Prevalence of overweight among children and adolescents, BMI > +1 standard deviations above the median (crude estimate) (%)' or gho_che == 'Prevalence of underweight among adults, BMI < 18.5 (age-standardized estimate) (%)' or gho_che == 'Prevalence of thinness among children and adolescents, BMI < -2 standard deviations below the median (crude estimate) (%)' or gho_che == 'Alcohol, recorded per capita (15+) consumption (in litres of pure alcohol)' or gho_che == 'Estimate of daily cigarette smoking prevalence (%)' or gho_che == 'Estimate of daily tobacco smoking prevalence (%)' or gho_che == 'Estimate of current cigarette smoking prevalence (%)' or gho_che == 'Estimate of current tobacco smoking prevalence (%)' or gho_che == 'Mean systolic blood pressure (crude estimate)' or gho_che == 'Mean fasting blood glucose (mmol/l) (crude estimate)' or gho_che == 'Mean Total Cholesterol (crude estimate)'):
            country_che = fact.find('COUNTRY')
            if (country_che != None):
                country_che = fact.find('COUNTRY').text
            sex_che = fact.find('SEX')
            if (sex_che != None):
                sex_che = fact.find('SEX').text
            year_che = fact.find('YEAR')
            if (year_che != None):
                year_che = fact.find('YEAR').text
                if ('-' in year_che):
                    year_che = year_che[0:4]
                year_che = int(year_che)
            ghecauses_che = fact.find('GHECAUSES')
            if (ghecauses_che != None):
                ghecauses_che = fact.find('GHECAUSES').text
            agegroup_che = fact.find('AGEGROUP')
            if (agegroup_che != None):
                agegroup_che = fact.find('AGEGROUP').text
            display_che = fact.find('Display')
            if (display_che != None):
                display_che = fact.find('Display').text
            numeric_che = fact.find('Numeric')
            if (numeric_che != None):
                numeric_che = float(fact.find('Numeric').text)
            low_che = fact.find('Low')
            if (low_che != None):
                low_che = float(fact.find('Low').text)
            high_che = fact.find('High')
            if (high_che != None):
                high_che = float(fact.find('High').text)
            lista_che = [gho_che, country_che, sex_che, year_che, ghecauses_che, agegroup_che, display_che, numeric_che, low_che, high_che]
            d.append(lista_che)

df = pd.DataFrame(np.array(d), columns=['GHO', 'COUNTRY', 'SEX', 'YEAR', 'GHECAUSES', 'AGEGROUP','Display', 'Numeric', 'Low', 'High'])

gc = gspread.service_account()
sh = gc.open('Tarea 4 IIC3103')
worksheet = sh.worksheet("Datos")
worksheet.update([df.columns.values.tolist()] + df.values.tolist()) 