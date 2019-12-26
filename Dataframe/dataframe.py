import pandas as pd
import numpy as np

# to display whole dataframe in console 
pd.set_option('display.max_rows', 100)
pd.set_option('display.max_columns', 100)
pd.set_option('display.width', 227)

# to create dataframe from CSV file
df1=pd.read_csv('flights_data_dataframe.csv')
print(df1)

print("filter data")
print("**filter with = ")
#method 1
Equalto=df1[df1.flt_num==3314]
print(Equalto)

print("***")
#mwthod 2
Equalto=df1[df1['flt_num']==3314]
print(Equalto)

print("***filter with & ")
print("method 1")
filter_and=df1[(df1.origin=='ATL') & (df1.Price==201.2)]
print(filter_and)

print("method 2")
filter_and=df1[(df1['origin']=='ATL') & (df1['Price']==201.2)]
print(filter_and.iloc[:,1])

print("***IMP: filter with or")
#method 1
filter_or=df1[(df1.destination == 'ATL')|(df1.destination == 'FLL')]
print(filter_or)

#method2
filter_or=df1[(df1['destination'] == 'ATL')|(df1['destination'] == 'FLL')]
print(filter_or)

print("*** filter with <,>,<=,>= ")
filter_lessthan=df1[(df1.Price >= 100) & (df1.Price < 400)]
print(filter_lessthan.iloc[:,-4:-1])

print("*** see -filter with  Like")
# https://www.tutorialspoint.com/python/string_startswith.htm
# https://www.tutorialspoint.com/python/string_endswith.htm

print("*** IN ")
isin=df1[df1.scheduled_origin_gate.isin(['B22','B25',2,'Any'])]
print(isin.loc[:,['id','scheduled_origin_gate','created_at','updated_at','flight_identifier','flt_num']])

print("***IMP - not in ")
#https://stackoverflow.com/questions/19960077/how-to-filter-pandas-dataframe-using-in-and-not-in-like-in-sql
isnotin=df1[~df1.scheduled_origin_gate.isin(['B22','B25',2,'Any'])]
print(isnotin.loc[:,['id','scheduled_origin_gate','created_at','updated_at','flight_identifier','flt_num']])

print("*** is null")
ISnull=df1.isna()
print(ISnull)

print("*** is not null")
ISnotnull=df1.notna()
print(ISnotnull)

print(" *** between")
#between=df[(df.a<4) & (df.a> 2)] 
#print(between) 

print("*** Left")
Left=df1.created_at.str[:4]
print(Left.iloc[:10])

print("*** Right")
Right=df1.origin_full_name.str[-4:-1]
print(Right.iloc[:10])

print("***see -trim")
#trim=df1.flight_identifier.str.strip()
#print(trim)


#Method 2 see
#df[df.columns] = df.apply(lambda x: x.str.strip())
print("***see - LTRIM")
#LTRIM=df.b.str.strip()
#print(LTRIM)

print("***see - RTRIM")
#RTRIM=df.b.str.strip()
#print(RTRIM)

print("*** upper case")
Upper_case=df1.scheduled_destination_gate.str.upper()
print(Upper_case.iloc[:10])

print("*** lower case")
Lower_case=df1.origin.str.lower()
print(Lower_case.iloc[:10])

print("*** see - replace")

print("*** see - reverse(not imp)")

print("*** If/case ")
print("*** update with if...than ")
df1.loc[df1.Price > 201,['Price_level']] = 'costly'
print(df1.iloc[:5,-4:])

print("*** update with if...than...else")
df1.Price_level = np.where(df1.Price > 201,'costly','cheaper')
print(df1.iloc[:5,-4:])

#method 2
#df['new column name'] = df['column name'].apply(lambda x: 'value if condition is met' if x condition else 'value if condition is not met')

print("see - if ...multiple conidition")
#https://stackoverflow.com/questions/48569166/multiple-if-else-conditions-in-pandas-dataframe-and-derive-multiple-columns/48569899

print("sort")
print("*** sort by values ***")
sort_values=df1.sort_values('Price')
print(sort_values.loc[:,['destination_full_name','origin_full_name','Price']])

print("*** sort by alphabet -- capital letters pahela and small letters pachi ***")
sort_alphabet=df1.sort_values('destination_full_name')
print(sort_alphabet.loc[:,['destination_full_name','origin_full_name','Price']])

print("***group by")
print("*** group by - sum")
groupby_sum=df1.groupby(['Price']).sum()
print(groupby_sum)

print("*** group by - mean")
groupby_mean=df1.groupby(['Price']).mean()
print(groupby_mean)

print("***see- Group by - having")

print("*** sub string")
substring=df1.destination_full_name.str[-5:]
print(substring)

print("*** count")
count=df1.count()
print(count)

print("*** get first 2 rows **")
head=df1.head(2)
print(head)

print("*** get last 2 rows**")
tail=df1.tail(2)
print(tail)

print("*** keep column as index column ***")
index_column=df1.set_index('Coreid')
print(index_column)

print("*** df2")
df2=pd.read_csv('flights_data_dataframe2.csv')
print(df2)

print("***Union all")
Union_all=pd.concat([df1,df2]) 
print(Union_all)

print("*** Union")
Union=pd.concat([df1,df2]).drop_duplicates()
print(Union)

print("*** intersect")
#intersect= pd.merge(df1, df2, how='inner', on=['Score'])
#print(intersect)

print("*** see - merge **")
print("*** Inner Join ***")
inner_join=pd.merge(df1,df2,left_on='Coreid',right_on='Coreid_2',how='inner')
print(inner_join.loc[:,['Coreid','Coreid_2']])

print("*** Outer Join ***")
Outer_join=pd.merge(df1,df2,left_on='Coreid',right_on='Coreid_2',how='outer')
print(Outer_join.loc[:,['Coreid','Coreid_2']])

print("*** Left Join")
Left_join=pd.merge(df1,df2,left_on='Coreid',right_on='Coreid_2',how='left')
print(Left_join.loc[:,['Coreid','Coreid_2']])

print("*** Right Join")
Right_join=pd.merge(df1,df2,left_on='Coreid',right_on='Coreid_2',how='right')
print(Right_join.loc[:,['Coreid','Coreid_2']])


print("*** concatenation between 2 columns")
df1['flight_fulldetail']=df1['origin_full_name'] + ' TO ' + df1['destination_full_name']
print(df1.loc[:,['origin_full_name','destination_full_name','flight_fulldetail']])

print("*** IMP: to get second column")
#https://www.shanelynn.ie/select-pandas-dataframe-rows-and-columns-using-iloc-loc-and-ix/
#List25={'Name':['Tom', 'Jack', 'Steve','John','akhil','khan'],
#'Age':[25,40,35,90,14,92]}
#df25=pd.DataFrame(List25)
#print(df25.iloc[:,1])
print("*** to get second row")
#print(df25.iloc[1])

print("*** IMP: to get by column names")
#use loc ... 

print("*** calculation between 2 columns")
#df10["ab"] = 25
df1['Plus']=df1['Price']+df1['Points']
df1['Minus']=df1['Price']-df1['Points']
df1['Muliply']=df1['Price']*df1['Points']
df1['Divide']=df1['Price']/df1['Points']
print(df1.loc[:,['Price','Points','Plus','Minus','Muliply','Divide']])

print("***see - look for and / or ")

print("***delete row based on condition")
deleterow=df1[df1.Coreid==25].index
df1.drop(deleterow, inplace=True)
print(df1.iloc[:,-7:-1])

print("***see - delete row based on location") 

print("*** delete all rows")
df1.drop(df1.index , inplace=True)
print(df1)

print("***see- to delete table")
del df2
print(df2)

print("***")
#df29=pd.read_csv('flights_data.csv')
#print(df29.dtypes)

#df29['concat1']= df29['updated_at']+'*'+df29['destination_full_name']
#print(df29['concat1'].head(10))

print("-------------------------")
print("*** to create DataFrame")
print("***empty DataFrame***")
df = pd.DataFrame()
print(df)

print("***DataFrame from list- 1column without column name**")
List1=[34,63,85,14,96]
df1=pd.DataFrame(List1)
print(df1)

print("***DataFrame from list- 2columns without column name*")
List2=[['alex',10],['bob',20],['mike',30]]
df2=pd.DataFrame(List2)
print(df2)

print("***give data type,row names,columns names***")
List3=[['shah',25],['patel',28],['kumar',11]]
df3=pd.DataFrame(List3,dtype=float,
  index=['city1','city2','city3'],
  columns=['last_name','birth_day'])
print(df3)

print("*** DataFrame from dictionry ***")
List4 = {'Name':['Tom'],'Age':[28]}
df4=pd.DataFrame(List4)
print(df4) 

print("**To create 1 column with column name**")
lst= {"city":["baroda","bangalore"],
    "state":["GJ","KA"]}
df=pd.DataFrame(lst)
print(df)

print("***")
List5={'Name':['Tom', 'Jack', 'Steve'],'Age':[28,34,29]}
df5=pd.DataFrame(List5)
print(df5)

print("***Not IMP**List of Dics***")
List7=[{'a':1,'b':2},{'a':5,'b':10,'c':2}]
df7=pd.DataFrame(List7)
print(df7)

print("***give row names***")
List6={'City':['baroda','delhi','surat'],'state':['GJ','DEL','GJ']}
df6=pd.DataFrame(List6,index=['city1','city2','city3'])
print(df6)

print("***Series of Dics***")
List8={'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']),
   'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}
df8=pd.DataFrame(List8)
print(df8)

print("***2 coulms dataframe from 4 columns data***")
List9 = [{'a': 1, 'b': 2},{'a': 5, 'b': 10, 'c': 20, 'd': 0}]
df9 = pd.DataFrame(List9, index=['first', 'second'], columns=['a', 'b'])
print(df9)

print("*****")
List10 = {'a':[15,50], 'b':[22,40] }
df10 = pd.DataFrame(List10, index=['first', 'second'])
print(df10)

# to change datatype
#https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.astype.html

print("**** to add new column to existing df")
data = {'Name': ['Jai', 'Princi', 'Gaurav', 'Anuj'], 
        'Height': [5.1, 6.2, 5.1, 5.2], 
        'Qualification': ['Msc', 'MA', 'Msc', 'Msc']} 
df = pd.DataFrame(data) 

#Method 1
df.insert(2, "Age", [21, 23, 24, 21], True) 
print(df)

print("*****")
#Method 2
address = ['Delhi', 'Bangalore', 'Chennai', 'Patna'] 
df['Address'] = address 
print(df)

print("**** to delete one column")
del df['Age']
print(df)

print("*** see - drop column and row")
#df13=df12.drop(columns=['Age'],index=['new'])
#print(df13)

print("select any particular column or all columns")
#Method 1
print(df.Name)
#Method 2
print(df['Name'])
#Method 3
print(df.iloc[:4,2])

print("to chnage data type")
df.astype({'Height':'float'})
print(df.dtypes)  

List11={'Name':['Tom', 'Jack', 'Steve','John','akhil','khan'],
'Age':[25,40,35,90,14,92]}
df11=pd.DataFrame(List11)
print(df11)

print("*** rename column names and row names - change df **")
df12=df11.rename(columns={'Name':'Fullname'},index={4:'new'})
print(df12)

print("***to insert df")
df1 = pd.DataFrame([[1, 2], [3, 4]], columns=list('AB'))
print(df1)
df2 = pd.DataFrame([[5, 6], [7, 8]], columns=list('AB'))
df1.append(df2)

print(df2)

print("***")
students = [ ('jack', 34, 'Sydeny' , 'Australia') ,
             ('Riti', 30, 'Delhi' , 'India' ) ,
             ('Vikas', 31, 'Mumbai' , 'India' ) ,
             ('Neelu', 32, 'Bangalore' , 'India' ) ,
             ('John', 16, 'New York' , 'US') ,
             ('Mike', 17, 'las vegas' , 'US')  ]
dfObj = pd.DataFrame(students, columns = ['Name' , 'Age', 'City' , 'Country'], index=['a', 'b', 'c' , 'd' , 'e' , 'f'])

print("*** to insert rows with all columns values at the end")
listOfSeries = [pd.Series(['Raju', 21, 'Bangalore', 'India'], index=dfObj.columns ) ,
                pd.Series(['Sam', 22, 'Tokyo', 'Japan'], index=dfObj.columns ) ,
                pd.Series(['Rocky', 23, 'Las Vegas', 'US'], index=dfObj.columns ) ]
modDfObj = dfObj.append(listOfSeries , ignore_index=True)
print(modDfObj)

print("*** to insert rows with few columns values at the end")
modDfObj = dfObj.append({'Name' : 'Sahil' , 'Age' : 22} , ignore_index=True)
print(modDfObj)

print("*** to insert row at particular location")
new_row = pd.DataFrame({'Name':'akhil','Age':32},index =[0]) 
modDfObj = pd.concat([new_row, modDfObj]).reset_index(drop = True) 
print(modDfObj)

List25={'Name':['Tom','Jack','Steve','John','akhil','khan'],
'Age':[25,40,35,90,14,92]}

print("iloc,loc and ix")
lst={"city":["baroda","surat"],
    "zip":["06","05"]}
df=pd.DataFrame(lst)
print(df)
print("Rule 1 : iloc = i am loc = based on location = perfection")
print("Rule 2: when we use loc its mandotory to mention column name")
#Rule 3 : 

print("1-----")
lst2= {"city":["baroda","bangalore","surat","mangalore"],
    "state":["GJ","KA","GJ","KA"]}
df2=pd.DataFrame(lst2)
print(df2)

print("2 not possible ")
#print(df2.loc[2,1]) # row-2 :col-1   

print("3-----")
print(df2.iloc[2,1]) # row-2 :col-1 

print("4------")
print(df2.ix[2,1]) # row-2 :col-1 

print("5------")
print(df2.loc[2,"city"]) # row - 2 :col- city

print("6-----")
print(df2.ix[2,"city"]) # row - 2 :col- city

print("7--IMP")
print(df2.loc[:2,"city"]) # row - 0,1,2 :col- city

print("8--IMP")
print(df2.ix[:2,"city"]) # row - 0,1,2 :col- city

print("9--IMP")
print(df2.iloc[:2,:1]) # row - 0,1 :col- 0 

print("10--IMP  (see)")
print(df2.ix[:2,:1]) # row - 0,1,2 :col- 0  


'''
pivot_table
df.pivot
melt
stack
unstack

columns
rename
drop

what is inplace true/false

fillna/dropna( thresh=4)
head and tail in dataframe


set_index
group by
multiltvel dataframe --> drop level

ternary oprator using if else in one line

take datatype date , decimal for the input
1)
dataframe ma 1 column ni value parthi biji column ni column ni val nakki karo

name    surname gender  applicable
palak   shah    female   no
akhil   shah     male    no
shivani shah    female   no

gender = female --> status-applicaple = yes

2) 
input
name    surname gender  applicable
palak   shah    female    no
akhil   shah1     male    no
shivani shah2    female   no

output
name    surname gender  applicable
palak           female   no
akhil   shah     male    no
shivani shah1    female   no

shift column value to 1 step down

3)
input
name    surname gender  applicable  date
palak   shah    female    no        19-12-26
akhil   shah1     male    no        19-12-27
shivani shah2    female   no        19-12-28
shivani1 shah3    female   no       19-12-29
shivani2 shah4    female   no       19-12-30


output
name    surname gender  applicable  date
shivani2 shah4    female   no      19-12-30

get the last row from the dataframe


4)
name    surname gender  applicable full_name
palak   shah    female    no       palak shah
akhil   shah1     male    no       akhil shah1
shivani shah2    female   no       shivani shah2

get the last column as a combination of first 2 columns

5)

name  a   b    c  d  sum
palak 1   2   3   4  10

get sum column from sum of all the rows

6)
name    a   b   c   d
palak   5  7   nan
palak1  5  8   0
palak2  5  9
palak3  5   5
sum     20 50  0   0

get the sum row from sum of all the columns

'''