import concurrent.futures
import psycopg2
import csv
import requests
from queue import Queue




import arcpy

fc = 'Polygon'
f_list = []
id_list = []
arcpy.SelectLayerByAttribute_management(fc, "CLEAR_SELECTION")
# For each row, print the Object ID field, and use the SHAPE@AREA
#  token to access geometry properties
with arcpy.da.SearchCursor(fc, ['OID@', 'SHAPE@XY']) as cursor:
    for row in cursor:
        # easting = row[1][0]
        # northing = row[1][1]
        item = str(row[1])
        if item not in f_list:
            f_list.append(item)
            id_list.append(row[0])
            #   arcpy.SelectLayerByAttribute_management(fc, "ADD_TO_SELECTION", f'OBJECTID = {row[0]}')
sql_query = tuple(id_list)
print(sql_query)

arcpy.SelectLayerByAttribute_management(fc, "NEW_SELECTION", f'OBJECTID IN {sql_query}')
arcpy.SelectLayerByAttribute_management(fc, "SWITCH_SELECTION")
#f'OBJECTID IN {sql_query}'


myList = []
rows = arcpy.SearchCursor("layername")
for row in rows:
  if str(row.UniqueIdentifier) in myList:
    #value duplicated
    row.DuplicateColumnName = "y"
  else:
    #not there, add it
    myList.append(row.UniqueIdentifier)
  rows.updateRow(row)

import itertools, arcpy

fc = r'Point Notes'

def findOverlaps(x):
    with arcpy.da.SearchCursor(x, ['SHAPE@']) as cur:
        for feature1,feature2 in itertools.combinations(cur, 2):
            if feature1[1].equals(feature2[1]):
                print("{} equals {}".format(feature1[0],feature2[0]))
            if feature1[1].overlaps(feature2[1]):
                print("{} overlaps {}".format(feature1[0],feature2[0]))
            if feature1[1].contains(feature2[1]):
                print("{} contains {}".format(feature1[0],feature2[0]))

findOverlaps(fc)


with open('MOCK_DATA(2).csv') as csv_file:
    next(csv_file)
    reader = csv.reader(csv_file)
    values = list(reader)
q = Queue()

for i in values:
    q.put(i)

while not q.empty():
    print(q.get())


input('fini')
conn = psycopg2.connect(host="localhost", database="postgres", user="postgres", password="richard")
cursor = conn.cursor()


def d_base_(value):
    cursor.execute(
        "INSERT INTO people (id, first_name, last_name, email, gender, ip_address) VALUES(%s, %s, %s, %s, %s, %s)",
        (value[0], value[1], value[2], value[3], value[4], value[5]))
    conn.commit()
    print(value)


with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
    executor.map(d_base_, values)

cursor.close()
conn.close()

test = 3 == 3
if bool(test):
    print('hi')
print(test)

input()

def get_token():
    params = {
        'client_id': "p9WAKtrAVMF8hmA3",
        'client_secret': "9d51c284107248fe97424d1728a5226f",
        'grant_type': "client_credentials"
    }
    request = requests.get('https://www.arcgis.com/sharing/rest/oauth2/token',
                          params=params)
    response = request.json()
    token = response["access_token"]
    return token
token = get_token()
print(token)

params2 = {
    'f': 'json',
    'token': 'J-S0KLO***MyB9g..',
    'studyAreas': '[{"geometry":{"x":-117.1956,"y":34.0572}}]'
}
url = 'https://services2.arcgis.com/4mdxlPzHnZKtJJX9/ArcGIS/rest/services/Geopal_API_test/FeatureServer/0/addFeatures'
data = requests.post(url, params=params2)
print(data.json())
quit()
input()



def count_down(n):
    print(n)

    if n == 0:
        return n
    else:
        count_down(n - 1)


count_down(10)
point_two = 0.2
point_one = 0.1
add_them = point_one + point_two
print(0.3 == add_them)
# function checkDownload() {
#   const filename = "filefffff.jpg";
#   const xhr = new XMLHttpRequest();
#   xhr.responseType = "blob";
#   xhr.open('GET', 'https://helpx.adobe.com/content/dam/help/en/photoshop/using/convert-color-image-black-white/jcr_content/main-pars/before_and_after/image-before/Landscape-Color.jpg');
#   xhr.onreadystatechange = () => {
#     if(xhr.readyState === 4) {
#       if(xhr.status === 200) {
#       var reader = new FileReader();
#       reader.readAsArrayBuffer(xhr.response);
#       reader.addEventListener("loadend", function() {
#        var a = new Int8Array(reader.result);
#       console.log(JSON.stringify(a, null, '  '));
# });
#       }
#     }
#   }
#   xhr.send();
# }
#
# checkDownload()
#
# async function downloadImage(imageSrc) {
#   const image = await fetch(imageSrc)
#   const imageBlog = await image.blob()
#   const imageURL = URL.createObjectURL(imageBlog)
#
#   const link = document.createElement('a')
#   link.href = imageURL
#   link.download = 'image.jpg'
#   document.body.appendChild(link)
#   link.click()
#   document.body.removeChild(link)
# }
#
# var imageSrc = 'https://helpx.adobe.com/content/dam/help/en/photoshop/using/convert-color-image-black-white/jcr_content/main-pars/before_and_after/image-before/Landscape-Color.jpg'
# downloadImage(imageSrc)
