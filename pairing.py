from numpy.lib.function_base import append
import pandas as pd
import sys
import os
import glob
import numpy as np
import shutil
from matplotlib import pyplot as plt

destination = str(os.getcwd())+'/output'

if os.path.isdir("output") == True:
    shutil.rmtree(destination)
    os.mkdir(destination)
else:
    os.mkdir(destination)

if len(sys.argv) == 2:
    input_file_gov = pd.read_csv(sys.argv[1])
    print("Please include additional pairing data...")

elif len(sys.argv) == 3:
    input_file_gov = pd.read_csv(sys.argv[1])
    input_file_trustee = pd.read_csv(sys.argv[2])
    print("Proper input recieved... Beginning to process data...")

else:
    print("Invalid input, please supple governor and trustee pairing data...")

df = input_file_gov[['Name',
'District',
'Please answer the following questions about you, your district, and trustee wants as honestly as you can [I would like an international trustee that focuses heavily on helping you to perform more service]',
'Please answer the following questions about you, your district, and trustee wants as honestly as you can [You would like an international trustee that is geared towards helping you plan your district events]',
'Please answer the following questions about you, your district, and trustee wants as honestly as you can [You would like a trustee thats geared toward help you fundraise for district projects or goals]',
'Please answer the following questions about you, your district, and trustee wants as honestly as you can [My district does a poor job networking and managing Kiwanis Family Relations]',
'Please answer the following questions about you, your district, and trustee wants as honestly as you can [You would like a trustee that communicates multiple times a week, about CKI related and non-related topics]',
'Please answer the following questions about you, your district, and trustee wants as honestly as you can [Fundraising for a cause is very important to your term as governor]',
'Please answer the following questions about you, your district, and trustee wants as honestly as you can [You would like an international trustee to have extensive knowledge on governing documents.]',
"Please answer the following questions about you, your district, and trustee wants as honestly as you can [Clubs in my district don’t have signature service projects and don't do enough service]",
'Please answer the following questions about you, your district, and trustee wants as honestly as you can [I would like an international trustee that takes on initiatives like an additional board member]',
'Please answer the following questions about you, your district, and trustee wants as honestly as you can [Chartering and establishing new clubs is at the utmost priority for our district this year]',
'Please answer the following questions about you, your district, and trustee wants as honestly as you can [You want an international trustee to send out updates to not just your board but clubs]',
'Please answer the following questions about you, your district, and trustee wants as honestly as you can [The clubs in our district don’t know how to recruit members]',
'Please answer the following questions about you, your district, and trustee wants as honestly as you can [You are currently not satisfied with the amount of service currently being done within your district]',
'Please answer the following questions about you, your district, and trustee wants as honestly as you can [Our district board has a large number of vacancies this year]',
'Please answer the following questions about you, your district, and trustee wants as honestly as you can [You are not experienced working with CKI alumni and/or dont feel comfortable doing so]',
'Please answer the following questions about you, your district, and trustee wants as honestly as you can [Applying for international awards is very important to you]',
'Please answer the following questions about you, your district, and trustee wants as honestly as you can [Having a trustee that is good with networking within the Kiwanis family is very important to you]',
'Please answer the following questions about you, your district, and trustee wants as honestly as you can [Our district has no new charters or potential charters that we are working with]',
'Please answer the following questions about you, your district, and trustee wants as honestly as you can [More than half of our clubs are below charter strength (15 members)]',
'Please answer the following questions about you, your district, and trustee wants as honestly as you can [You feel as though your district does a poor job at fundraising]',
'Please answer the following questions about you, your district, and trustee wants as honestly as you can [Generation and creation of a strategic plan for your district is of the utmost importance to you in your term as governor]',
'Please answer the following questions about you, your district, and trustee wants as honestly as you can [You would like a trustee that is there to excite members about service]',
'Please answer the following questions about you, your district, and trustee wants as honestly as you can [It is a priority for our district to increase the amount of interest in leadership opportunities that we have]',
'Please answer the following questions about you, your district, and trustee wants as honestly as you can [You would like an international trustee that has extensive knowledge on Strategic Planning for clubs and districts]',
'Please answer the following questions about you, your district, and trustee wants as honestly as you can [Our service hour goal is one of the most important goals to me as a governor]',
'Please answer the following questions about you, your district, and trustee wants as honestly as you can [Communication from international directly to clubs is very important to you as a governor]',
'Please answer the following questions about you, your district, and trustee wants as honestly as you can [I want my board to be in constant communication with their international trustee for advice]',
'Please answer the following questions about you, your district, and trustee wants as honestly as you can [A majority of our clubs have difficulty electing officers]',
'Please answer the following questions about you, your district, and trustee wants as honestly as you can [Kiwanis-family relations is one of your top priorities as governor this year]',
'Please answer the following questions about you, your district, and trustee wants as honestly as you can [You would like a trustee that plans to host inter-district events or initiatives for your members to meet and interact with other members]',
'Please answer the following questions about you, your district, and trustee wants as honestly as you can [Increasing district event attendance is of the utmost importance to you in your term as governor]',
'Please answer the following questions about you, your district, and trustee wants as honestly as you can [Our district does not work directly with clubs to help them with recruitment and retention efforts year round]',
'Please answer the following questions about you, your district, and trustee wants as honestly as you can [Redoing your governing documents is of the utmost importance to you and your district]',
'Please answer the following questions about you, your district, and trustee wants as honestly as you can [Your district or clubs are not likely to apply for the Tomorrow Fund]',
'Please answer the following questions about you, your district, and trustee wants as honestly as you can [Our current strategic plan for my district is weak]',
'Please answer the following questions about you, your district, and trustee wants as honestly as you can [Our district has made little effort to implement new recruitment initiatives this year]',
'Please answer the following questions about you, your district, and trustee wants as honestly as you can [You would like to attend other districts events within your sister district pairings]',
'Please answer the following questions about you, your district, and trustee wants as honestly as you can [Working with other governors in your term would be very useful to you as a governor]',
'Please answer the following questions about you, your district, and trustee wants as honestly as you can [You want a trustee that is comfortable facilitating Diversity, Equity, and Inclusion (DEI) programs and activities]',
'Please answer the following questions about you, your district, and trustee wants as honestly as you can [It is difficult to find candidates for district office during District Conference season]',
'Please answer the following questions about you, your district, and trustee wants as honestly as you can [My clubs do not engage heavily with the CKI Service Initiatives and partners]',
'Please answer the following questions about you, your district, and trustee wants as honestly as you can [Having an international trustee attend most/all events is very important to me as a governor]',
'Please answer the following questions about you, your district, and trustee wants as honestly as you can [You would like a trustee experienced working with CKI alumni and would like their help in this area]',
'Please answer the following questions about you, your district, and trustee wants as honestly as you can [It is important for our district to have an International Trustee that understands the charter process]',
'Please answer the following questions about you, your district, and trustee wants as honestly as you can [The clubs in our district do not know how to retain members]',
'Please answer the following questions about you, your district, and trustee wants as honestly as you can [In the last five years, my district has experienced a decrease in membership numbers]',
'Please answer the following questions about you, your district, and trustee wants as honestly as you can [Fellowship is the most important tenant to you in your term as governor]',
'Please answer the following questions about you, your district, and trustee wants as honestly as you can [You would like a trustee that wants to facilitate strong inter-district connections between your sister districts]',
'Please answer the following questions about you, your district, and trustee wants as honestly as you can [In the last five years, my district has experienced a decrease in the total number of active clubs]',
'Please answer the following questions about you, your district, and trustee wants as honestly as you can [You feel as though your district has weak district events]']]

df.columns = ['Name', 'District','Q_3_2_3','Q_4_3_1','Q_4_4_2','Q_3_3_3','Q_1_3_1','Q_4_4_1','Q_4_1_1','Q_3_1_2','Q_1_4_1','Q_2_3_1','Q_1_3_2','Q_2_2_3','Q_3_2_1','Q_2_4_1','Q_3_4_2','Q_4_1_3','Q_3_3_2','Q_2_3_3','Q_2_1_3','Q_4_4_3','Q_4_2_2','Q_1_1_2','Q_2_4_4','Q_4_2_1','Q_3_2_2','Q_1_3_3','Q_1_4_3','Q_2_4_2','Q_3_3_1','Q_1_1_3','Q_4_3_2','Q_2_2_2','Q_4_1_2','Q_3_1_3','Q_4_2_3','Q_2_2_1','Q_1_2_2','Q_1_2_1','Q_3_4_1','Q_2_4_3','Q_3_1_1','Q_1_4_2','Q_3_4_3','Q_2_3_2','Q_2_2_4','Q_2_1_1','Q_1_1_1','Q_1_2_3','Q_2_1_2','Q_4_3_3',]
column_names = ['Name', 'District','Q_3_2_3','Q_4_3_1','Q_4_4_2','Q_3_3_3','Q_1_3_1','Q_4_4_1','Q_4_1_1','Q_3_1_2','Q_1_4_1','Q_2_3_1','Q_1_3_2','Q_2_2_3','Q_3_2_1','Q_2_4_1','Q_3_4_2','Q_4_1_3','Q_3_3_2','Q_2_3_3','Q_2_1_3','Q_4_4_3','Q_4_2_2','Q_1_1_2','Q_2_4_4','Q_4_2_1','Q_3_2_2','Q_1_3_3','Q_1_4_3','Q_2_4_2','Q_3_3_1','Q_1_1_3','Q_4_3_2','Q_2_2_2','Q_4_1_2','Q_3_1_3','Q_4_2_3','Q_2_2_1','Q_1_2_2','Q_1_2_1','Q_3_4_1','Q_2_4_3','Q_3_1_1','Q_1_4_2','Q_3_4_3','Q_2_3_2','Q_2_2_4','Q_2_1_1','Q_1_1_1','Q_1_2_3','Q_2_1_2','Q_4_3_3',]

District = list(df['District'])

df = df.replace(['Strongly Disagree','Disagree','Slightly Disagree','Neutral','Slightly Agree','Agree','Strongly Agree'],[1,2,3,4,5,6,7])
df = df.sort_index (axis = 1)

names = ['District','Q_1_1', 'Q_1_2','Q_1_3','Q_1_4','Q_2_1','Q_2_2','Q_2_3','Q_2_4','Q_3_1','Q_3_2','Q_3_3','Q_3_4','Q_4_1','Q_4_2','Q_4_3','Q_4_4','Trustee Involvment Need Score','Membership Need Score','Interntional Intativates and Service Need Score','District Operations Need Score']

empty = []
values = []
district_totals_final = []
for index,row in df.iterrows():
    empty_2 = []
    empty_3 = []
    outta_100 = []
    for y in range(1,5):
        stepup = []
        stepup_2 = []
        for n in range(1,5):
            questions = []
            if y == 2 and n == 2:
                x = (int(row[str('Q_'+ str(y) + '_'+ str(n) + '_1')]) + int(row[str('Q_'+ str(y) + '_'+ str(n) + '_2')]) + int(row[str('Q_'+ str(y) + '_'+ str(n) + '_3')]) + int(row[str('Q_'+ str(y) + '_'+ str(n) + '_4')]))
                z = round((x/28)*25,2)
            elif y == 2 and n == 4:
                x = (int(row[str('Q_'+ str(y) + '_'+ str(n) + '_1')]) + int(row[str('Q_'+ str(y) + '_'+ str(n) + '_2')]) + int(row[str('Q_'+ str(y) + '_'+ str(n) + '_3')]) + int(row[str('Q_'+ str(y) + '_'+ str(n) + '_4')]))
                z = round((x/28)*25,2)
            else:
                x = (int(row[str('Q_'+ str(y) + '_'+ str(n) + '_1')]) + int(row[str('Q_'+ str(y) + '_'+ str(n) + '_2')]) + int(row[str('Q_'+ str(y) + '_'+ str(n) + '_3')]))
                z = round((x/21)*25,2)
            stepup.append(z)
            empty_3.append(x)
        empty_2.append(stepup)
    empty.append(empty_2)
    values.append(empty_3)
    outta_100_list = empty_2
    district_totals = 100-np.sum(outta_100_list,0)
    district_totals = district_totals.tolist()
    district_totals_final.append(district_totals)

totals_df = pd.DataFrame(district_totals_final)
values_df = pd.DataFrame(values)
district_df = pd.DataFrame(District)
output_df = pd.concat([district_df,values_df,totals_df], axis=1)
output_df.columns=names

output_df.to_csv('District_Assessment.csv')
source = str(os.getcwd())+'/District_Assessment.csv'
shutil.move(source,destination)

df_1 = input_file_trustee[['Name',
"Please answer the following questions as honestly as you can [As an international trustee I would like to focus heavily on helping districts to perform more service]",
"Please answer the following questions as honestly as you can [My prior experince has geared me towards helping plan district events]",
"Please answer the following questions as honestly as you can [As an international trustee, a main goal of mine is to help districts fundraise for district projects or goals]",
"Please answer the following questions as honestly as you can [I have worked with networking and managing Kiwanis Family Relations and consider myself an expert in this area]",
"Please answer the following questions as honestly as you can [I would likw to communicate with my governors multiple times a week, about CKI related and non-related topics]",
"Please answer the following questions as honestly as you can [Planning and organizing new fundraising for a cause is very important to your term as international trustee]",
"Please answer the following questions as honestly as you can [I have extensive knowledge on governing documents and would be able to help districts in extensive detaill]",
"Please answer the following questions as honestly as you can [As international trustee a main goal of mine would be to help clubs create signature service projects and do more service]",
"Please answer the following questions as honestly as you can [As an international trustee I would like to take on initiatives like an additional board member for my districts]",
"Please answer the following questions as honestly as you can [Chartering and establishing new clubs is at the utmost priority for me in my term]",
"Please answer the following questions as honestly as you can [I would like to be able to engauge with and send out updates to clubs as well as district boards]",
"Please answer the following questions as honestly as you can [I have experience in recruiting members and would like to teach others how to do so]",
"Please answer the following questions as honestly as you can [I would like to be able to engauge with and send out updates to clubs as well as district boards]",
"Please answer the following questions as honestly as you can [I feel very comfortable working and mentoring individuals in priorizing workload]",
"Please answer the following questions as honestly as you can [I am experienced working with CKI alumni and/or feel comfortable doing so]",
"Please answer the following questions as honestly as you can [I have experience applying for international awards and think my districts should apply for every award]",
"Please answer the following questions as honestly as you can [I consider myself well connected within the relmn of Kiwanis and feel confortable asking Kiwanians for assistance]",
"Please answer the following questions as honestly as you can [Finding new charters or potential charters is something that I would be intrested in doing as an international trustee]",
"Please answer the following questions as honestly as you can [I prefer to work with smaller clubs of less than 15 members than larger clubs]",
"Please answer the following questions as honestly as you can [I enjoy the challege of helping a district plan and organize new fundraising techniques]",
"Please answer the following questions as honestly as you can [Helping generate and create a strategic plan for your districts is of the utmost importance to you in your term]",
"Please answer the following questions as honestly as you can [I think that one of my greatest abilities is to excite members about CKI]",
"Please answer the following questions as honestly as you can [One of the most important things I can do as international trustee is increase the amount of interest in leadership opportunities that we have in the org]",
"Please answer the following questions as honestly as you can [I have extensive knowledge on Strategic Planning for clubs and districts]",
"Please answer the following questions as honestly as you can [The most important metric for success a district can hit is the service hour goal]",
"Please answer the following questions as honestly as you can [I would like to be able to engauge with clubs and speak to them on a 1 on 1 basis with little oversight]",
"Please answer the following questions as honestly as you can [I would like the ability to mentor district boards more so than working with clubs]",
"Please answer the following questions as honestly as you can [I come from a small club that has a tough time filling officer positions]",
"Please answer the following questions as honestly as you can [Kiwanis-family relations is one of your top priorities as trustee this year]",
"Please answer the following questions as honestly as you can [I would like to host inter-district events or initiatives for district members to meet and interact with other members]",
"Please answer the following questions as honestly as you can [Helping increasing district event attendance is of the utmost importance to you in your term as international trustee]",
"Please answer the following questions as honestly as you can [the most important thing I can do as trustee is help districts work directly with clubs to on recruitment and retention efforts year round]",
"Please answer the following questions as honestly as you can [I would like to help redo my districts governing documents this year]",
"Please answer the following questions as honestly as you can [I would like to help my districts or clubs apply for the Tomorrow Fund]",
"Please answer the following questions as honestly as you can [I find it enjoyable creating and updating strategic plans]",
"Please answer the following questions as honestly as you can [I have new ideas for recruitment initiatives this year and want to implement them into my districts]",
"Please answer the following questions as honestly as you can [You would like your members to attend other districts events within your sister district pairings]",
"Please answer the following questions as honestly as you can [It's important that your governors want to communicate and work with eachother]",
"Please answer the following questions as honestly as you can [I feel comfortable facilitating Diversity, Equity, and Inclusion (DEI) programs and activities]",
"Please answer the following questions as honestly as you can [I am an expert at building up peoples confidence to run for higher office]",
"Please answer the following questions as honestly as you can [The mark I would like to leave on my districts is by helpping clubs engauge with CKI Service Initiatives and partners]",
"Please answer the following questions as honestly as you can [I plan to visit my districts multiple times a year, offically and unoffically]",
"Please answer the following questions as honestly as you can [I take pride in my experience working with CKI alumni and would like to help build alumni societies in my districts]",
"Please answer the following questions as honestly as you can [I understand the charter process and feel confrotable teaching others how the process works]",
"Please answer the following questions as honestly as you can [The ability to retaining members, new and old, is something that I am known for]",
"Please answer the following questions as honestly as you can [I come from a club that has experienced growth within my time in CKI and want to help other achievee said growth]",
"Please answer the following questions as honestly as you can [If I had to describe my role as international trustee in one word, I would use the word fellowship]",
"Please answer the following questions as honestly as you can [I want to facilitate strong inter-district connections between my sister districts]",
"Please answer the following questions as honestly as you can [I feel comfortable and have experience bringing clubs back from suspended/inactive status]",
"Please answer the following questions as honestly as you can [I have attended a large number of district events and know what works and what does not]"]]

df_1.columns = ['Name','Q_3_2_3','Q_4_3_1','Q_4_4_2','Q_3_3_3','Q_1_3_1','Q_4_4_1','Q_4_1_1','Q_3_1_2','Q_1_4_1','Q_2_3_1','Q_1_3_2','Q_2_2_3','Q_3_2_1','Q_2_4_1','Q_3_4_2','Q_4_1_3','Q_3_3_2','Q_2_3_3','Q_2_1_3','Q_4_4_3','Q_4_2_2','Q_1_1_2','Q_2_4_4','Q_4_2_1','Q_3_2_2','Q_1_3_3','Q_1_4_3','Q_2_4_2','Q_3_3_1','Q_1_1_3','Q_4_3_2','Q_2_2_2','Q_4_1_2','Q_3_1_3','Q_4_2_3','Q_2_2_1','Q_1_2_2','Q_1_2_1','Q_3_4_1','Q_2_4_3','Q_3_1_1','Q_1_4_2','Q_3_4_3','Q_2_3_2','Q_2_2_4','Q_2_1_1','Q_1_1_1','Q_1_2_3','Q_2_1_2','Q_4_3_3',]
column_names = ['Name','Q_3_2_3','Q_4_3_1','Q_4_4_2','Q_3_3_3','Q_1_3_1','Q_4_4_1','Q_4_1_1','Q_3_1_2','Q_1_4_1','Q_2_3_1','Q_1_3_2','Q_2_2_3','Q_3_2_1','Q_2_4_1','Q_3_4_2','Q_4_1_3','Q_3_3_2','Q_2_3_3','Q_2_1_3','Q_4_4_3','Q_4_2_2','Q_1_1_2','Q_2_4_4','Q_4_2_1','Q_3_2_2','Q_1_3_3','Q_1_4_3','Q_2_4_2','Q_3_3_1','Q_1_1_3','Q_4_3_2','Q_2_2_2','Q_4_1_2','Q_3_1_3','Q_4_2_3','Q_2_2_1','Q_1_2_2','Q_1_2_1','Q_3_4_1','Q_2_4_3','Q_3_1_1','Q_1_4_2','Q_3_4_3','Q_2_3_2','Q_2_2_4','Q_2_1_1','Q_1_1_1','Q_1_2_3','Q_2_1_2','Q_4_3_3',]

df_1 = df_1.replace(['Strongly Disagree','Disagree','Slightly Disagree','Neutral','Slightly Agree','Agree','Strongly Agree'],[1,2,3,4,5,6,7])
df_1 = df_1.sort_index (axis = 1)

names_1 = ['Name','Q_1_1', 'Q_1_2','Q_1_3','Q_1_4','Q_2_1','Q_2_2','Q_2_3','Q_2_4','Q_3_1','Q_3_2','Q_3_3','Q_3_4','Q_4_1','Q_4_2','Q_4_3','Q_4_4','Trustee Involvment Strength Score','Membership Strength Score','Interntional Intativates and Service Strength Score','District Operations Strength Score']

Trustee_names = list(df_1['Name'])

empty_1 = []
values_1 = []
trustee_totals_final = []
for index,row in df_1.iterrows():
    empty_2_1 = []
    empty_3_1 = []
    outta_100_1 = []
    for y in range(1,5):
        stepup_1 = []
        stepup_2_1 = []
        for n in range(1,5):
            questions_1 = []
            if y == 2 and n == 2:
                x = (int(row[str('Q_'+ str(y) + '_'+ str(n) + '_1')]) + int(row[str('Q_'+ str(y) + '_'+ str(n) + '_2')]) + int(row[str('Q_'+ str(y) + '_'+ str(n) + '_3')]) + int(row[str('Q_'+ str(y) + '_'+ str(n) + '_4')]))
                z = round((x/28)*25,2)
            elif y == 2 and n == 4:
                x = (int(row[str('Q_'+ str(y) + '_'+ str(n) + '_1')]) + int(row[str('Q_'+ str(y) + '_'+ str(n) + '_2')]) + int(row[str('Q_'+ str(y) + '_'+ str(n) + '_3')]) + int(row[str('Q_'+ str(y) + '_'+ str(n) + '_4')]))
                z = round((x/28)*25,2)
            else:
                x = (int(row[str('Q_'+ str(y) + '_'+ str(n) + '_1')]) + int(row[str('Q_'+ str(y) + '_'+ str(n) + '_2')]) + int(row[str('Q_'+ str(y) + '_'+ str(n) + '_3')]))
                z = round((x/21)*25,2)
            stepup_1.append(z)
            empty_3_1.append(x)
        empty_2_1.append(stepup_1)
    empty_1.append(empty_2_1)
    values_1.append(empty_3_1)
    outta_100_list_1 = empty_2_1
    trustee_totals = np.sum(outta_100_list_1,0)
    trustee_totals = trustee_totals.tolist()
    trustee_totals_final.append(trustee_totals)

totals_df_1 = pd.DataFrame(trustee_totals_final)
values_df_1 = pd.DataFrame(values_1)
Trustee_names_1 = pd.DataFrame(Trustee_names)
output_df_1 = pd.concat([Trustee_names_1,values_df_1,totals_df_1], axis=1)
output_df_1.columns=names_1

output_df_1.to_csv('Trustee_Strength.csv')
source = str(os.getcwd())+'/Trustee_Strength.csv'
shutil.move(source,destination)

print(output_df_1)
trustee_truth = output_df_1[['Q_1_1', 'Q_1_2','Q_1_3','Q_1_4','Q_2_1','Q_2_2','Q_2_3','Q_2_4','Q_3_1','Q_3_2','Q_3_3','Q_3_4','Q_4_1','Q_4_2','Q_4_3','Q_4_4']]
district_truth = output_df[['Q_1_1', 'Q_1_2','Q_1_3','Q_1_4','Q_2_1','Q_2_2','Q_2_3','Q_2_4','Q_3_1','Q_3_2','Q_3_3','Q_3_4','Q_4_1','Q_4_2','Q_4_3','Q_4_4']]


tuples_dis = district_truth.to_records(index=False)

district_truth_1 = district_truth.T
district_truth_1.columns = District
trustee_truth_1 = trustee_truth.T
trustee_truth_1.columns = Trustee_names

output_scores = []
for x in District:
    district_pair = []
    for y in Trustee_names:
        df_mix = trustee_truth_1.copy()
        #df_mix = df_mix.set_index('Name')
        lists_mix = df_mix[y].tolist()
        trustee_variable_1 = np.array(lists_mix)
        #print(lists_mix)
        df_mix_1 = district_truth_1[x].tolist()
        district_variable_1 = np.array(df_mix_1)
        diff = trustee_variable_1 - district_variable_1
        diff = np.abs(diff)
        diff = np.sum(diff)
        district_pair.append(diff)
    array = np.array(district_pair)
    temp = array.argsort()
    district_pair = np.arange(len(array))[temp.argsort()]
    district_pair = np.array(district_pair)
    district_pair = district_pair + 1
    district_pair = [x] + list(district_pair)
    output_scores.append(district_pair)

final_names = ['District'] + Trustee_names
output_values_final = pd.DataFrame(output_scores,columns=final_names)
print(output_values_final)

output_values_final.to_csv('Recommended_Ranking.csv')
source = str(os.getcwd())+'/Recommended_Ranking.csv'
shutil.move(source,destination)
    