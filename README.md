
# Web Scrapping with Python

This is a simple  python application to extract data from an html document(table).

## Program Files

1. **data package/**

  Directory is a data package containing the the extracted data, **data.csv** in csv format and json file **datapackage.json** that describes the data.

2. **data.py**

  This is the python script used to scrap data from the web.



### Program Dependencies

1. **requests**
- Was used to make http get request to the webpage

2. **numpy**
- Numpy was not explicitly used in this program but it is a depenncy for pandas

3. **pandas**
- pandas was used to create and manipulate a dataframe object 
- It was also used to export the data into CSV

4. **BeautifulSoup**
- Web scrapping tool.
- It was used in this program to extract data from the HTML(table)