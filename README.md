# Spreadsheet Analysis
A little assignment to practice finding data, munging it, and analyzing it in a spreadsheet program.


### Data set details

This dataset comes from the [New York City Open Data site](https://data.cityofnewyork.us/Public-Safety/NYPD-Arrest-Data-Year-to-Date-/uip8-fykc/about_data) and is composed of data regarding arrests in New York City, across its various boroughs. We download this data through directly from the web and then being munging it. Columns and data include descriptions of the crime committed, the borrough where the arrest occurred, age, race, gender, etc. The original format of the dataset was a CSV / Excel file. This is a very large data set with 226873 rows.

| ARREST_KEY | ARREST_DATE | PD_DESC                          | LAW_CAT_CD | ARREST_BORO | JURISDICTION_CODE | AGE_GROUP | PERP_SEX | PERP_RACE | X_COORD_CD,Y_COORD_CD | Latitude         | Longitude         | SEASON | CRIME_TYPE |
| ---------- | ----------- | -------------------------------- | ---------- | ----------- | ----------------- | --------- | -------- | --------- | --------------------- | ---------------- | ----------------- | ------ | ---------- |
| 261271301  | 01/03/2023  | STRANGULATION 1ST                | F          | S           | 0                 | 25-44     | M        | WHITE     | 962808,174275         | 40.644996        | -74.077263        | WINTER | VIOLENT    |
| 261336449  | 01/04/2023  | "ROBBERY-OPEN AREA UNCLASSIFIED" | F          | K           | 0                 | <18       | M        | BLACK     | 995118,155708         | 40.594054        | -73.960866        | WINTER | PROPERTY   |
| 261328047  | 01/04/2023  | STRANGULATION 1ST                | F          | Q           | 0                 | 18-24     | M        | BLACK     | 1007694,219656        | 40.769552        | -73.915361        | WINTER | VIOLENT    |
| 261417496  | 01/05/2023  | "BURGLARY-UNCLASSIFIED-UNKNOWN"  | F          | B           | 0                 | 25-44     | F        | BLACK     | 1007174,239542        | 40.824135        | -73.91717         | WINTER | PROPERTY   |
| 261583093  | 01/08/2023  | "ASSAULT 2-1-UNCLASSIFIED"       | F          | K           | 0                 | 25-44     | M        | BLACK     | 984110,188363         | 40.683691        | -74.000504        | WINTER | VIOLENT    |
| 261611504  | 01/09/2023  | "ARSON 2-3-4"                    | F          | B           | 71                | 25-44     | M        | WHITE     | 1028555,246897        | 40.84424         | -73.839868        | WINTER | PROPERTY   |
| 261892107  | 01/14/2023  | "ASSAULT 2-1-UNCLASSIFIED"       | F          | K           | 0                 | 25-44     | M        | BLACK     | 996541,199439         | 40.714082        | -73.955662        | WINTER | VIOLENT    |
| 261926460  | 01/14/2023  | "ARSON 2-3-4"                    | F          | K           | 0                 | 25-44     | M        | BLACK     | 1000520,168264        | 40.628508        | -73.941384        | WINTER | PROPERTY   |
| 262973934  | 02/03/2023  | STRANGULATION 1ST                | F          | M           | 0                 | 25-44     | M        | BLACK     | 1003818,253167        | 40.861538        | -73.929256        | WINTER | VIOLENT    |
| 263113943  | 02/06/2023  | "ASSAULT 2-1-UNCLASSIFIED"       | F          | B           | 0                 | 45-64     | F        | BLACK     | 1010036,246475        | 40.843155        | -73.906802        | WINTER | VIOLENT    |
| 264092077  | 02/23/2023  | STRANGULATION 1ST                | F          | Q           | 0                 | 25-44     | F        | BLACK     | 1057766,203992        | 40.726284        | -73.73476         | WINTER | VIOLENT    |
| 261635779  | 01/10/2023  | STRANGULATION 1ST                | F          | Q           | 0                 | 18-24     | M        | BLACK     | 1050620,157860        | 40.599718        | -73.760999        | WINTER | VIOLENT    |
| 261739896  | 01/11/2023  | "TRESPASS 2- CRIMINAL"           | M          | K           | 0                 | 18-24     | F        | BLACK     | 991150,192509         | 40.695068        | -73.975116        | WINTER | PROPERTY   |
| 264206386  | 02/25/2023  | STRANGULATION 1ST                | F          | K           | 0                 | 45-64     | M        | BLACK     | 1000520,168264        | 40.628508        | -73.941384        | WINTER | VIOLENT    |
| 261361209  | 01/04/2023  | ASSAULT 3                        | M          | B           | 0                 | 18-24     | F        | BLACK     | 1007528,234117        | 40.809243        | -73.915909        | WINTER | VIOLENT    |
| 264544903  | 03/04/2023  | STRANGULATION 1ST                | F          | Q           | 0                 | 25-44     | M        | BLACK     | 1007694,219656        | 40.769552        | -73.915361        | SPRING | VIOLENT    |
| 262362107  | 01/23/2023  | "ROBBERY-OPEN AREA UNCLASSIFIED" | F          | B           | 0                 | 25-44     | M        | BLACK     | 1026486,262591        | 40.887325        | -73.847247        | WINTER | PROPERTY   |
| 262497973  | 01/25/2023  | RAPE 3                           | F          | B           | 0                 | <18       | M        | BLACK     | 1017478,256069        | 40.8694704770483 | -73.8798608037303 | WINTER | SEXUAL     |

The dataset was pretty clean already.

The column that caused the most trouble was of the police descriptions of the crimes because there were commas in them which made splitting up the data in the CSV by commas using the `.split()` function into a list challenging. I had to replace any commas in that column with dashes so that I could proceed with the scrubbing.

There were also a few missing values, usually noted as `null` or `0` in our dataset. I replaced them all with the string "NaN" for consistency. Even then, there were not many missing values present in our data.

To further clean and organize our data, I deleted and added several columns. I deleted columns such as "PD_CD", "LAW CODE", etc which contained codes that are most likely useful to police departments but not so much to the general public. I also deleted a column called "OFSC_DESC" with categorizations of the crime types since there is also a "PD_DESC" column with the police's descriptions of the arrests, likely done by the police department. But even then, there were 63 different categories of crimes in the "OFSC_DESC" column. While useful surely to the police, I decided to re-organize these crime types into 8 broader categories instead: violent, property, sexual, financial, weapon-related, drug-related, vehicle-related, and miscellaneous crimes. I also added a column with the season in which the arrest occurred to categorize the column with the exact dates of arrest in each row.

Below are the links to our data files:

[Original Raw Data](https://github.com/dbdesign-students-spring2024/3-spreadsheet-analysis-VideoStorms/blob/main/data/NYPD_Arrest_Data__Year_to_Date__20240213.csv)

[Munged Data](https://github.com/dbdesign-students-spring2024/3-spreadsheet-analysis-VideoStorms/blob/main/data/clean_data.csv)

[Spreadsheet File](https://github.com/dbdesign-students-spring2024/3-spreadsheet-analysis-VideoStorms/blob/main/data/clean_data.xlsx)

# Analysis

Performing analysis on the data was challenging as there are no strict numbers, so what we did instead was we looked at the common crime that leads to an arrest. using an COUNTIF function along with a max function to effectively calculate the MODE of the data. We did this for season, borough and age. Another way this could have been achieved is through a pivot table which is also used for the most common crime that leads to an arrest. This analysis gains the additional insight that shows that property is the common crime that leads to an arrest, which is interesting to note. It also shows that most arrests happen in Brooklyn, and it shows that crimes are relatively spread-out during seasons with a light dip in winter as seen by the graph. For age not surprisingly the largest age range is 25-44 has the highest arrests.

This is the attached pivot table.

| Row Labels      | Count of CRIME_TYPE |
|-----------------|---------------------|
| PROPERTY        | 66525               |
| VIOLENT         | 58648               |
| MISC            | 41883               |
| VEHICLE-RELATED | 18160               |
| DRUG-RELATED    | 16297               |
| FINANCIAL       | 9651                |
| WEAPON          | 9614                |
| SEXUAL          | 6094                |
| (blank)         |                     |
| Grand Total     | 226872              |

Here is the attached graph

![Graph](https://github.com/dbdesign-students-spring2024/3-spreadsheet-analysis-VideoStorms/blob/main/graph.jpeg)

And here are the attached Pie Charts that can allow you to asertain which crime was most commited, where the most arrests occur, what age ranges commit the most crimes and in what seasons are the most crimes commited.

![Graph2](https://github.com/dbdesign-students-spring2024/3-spreadsheet-analysis-VideoStorms/blob/main/graph2.png)


