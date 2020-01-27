import csv
import string
import untangle
rId ,sN ,sNN ,sT ,sA ,pN ,fN , eM , lat , lon = [],[],[],[],[],[],[],[],[],[]
def getData():
    with open('Fire_Stations', 'r') as f:
        latlong = getLatLon()
        rr = csv.reader(f)
        for r in rr:
            region = ''.join([x if x in string.printable else '' for x in r[0]])
            if(region=="BR"):
                rId.append("1")
            if (region == "CR"):
                rId.append("2")
            if (region == "FNR"):
                rId.append("3")
            if (region == "NCR"):
                rId.append("4")
            if (region == "NR"):
                rId.append("5")
            if (region == "SER"):
                rId.append("6")
            if (region == "SWR"):
                rId.append("7")
            sN.append(''.join([x if x in string.printable else '' for x in r[2]]))
            sNN.append(''.join([x if x in string.printable else '' for x in r[1]]))
            sT.append(''.join([x if x in string.printable else '' for x in r[3]]))
            sA.append(''.join([x if x in string.printable else '' for x in r[4]]))
            pN.append(''.join([x if x in string.printable else '' for x in r[6]]))
            if(len(r) == 8):
                fN.append(''.join([x if x in string.printable else '' for x in r[7]]))
            else:
                fN.append("")
            s = r[1][:-13]
            ss = ''.join([x if x in string.printable else '' for x in s])
            if ss.upper() in latlong:
                lat.append(latlong[ss.upper()][0])
                lon.append(latlong[ss.upper()][1])
            else:
                lat.append("")
                lon.append("")
            email = "enquiry@" +''.join(ss.split()).lower()+ ".qfes.gov.au"
            eM.append(email)
def getLatLon():
    result = dict()
    xmlinput = "Station_Locations"
    obj = untangle.parse(xmlinput)
    for i in obj.root.STATION:
            result.update({i.NAME.cdata : [i.LAT.cdata,i.LONG.cdata]})
    return result

def storingData():
    getData()
    with open('Fire_Station_locations.csv', 'w') as cf:
        fw = csv.writer(cf, delimiter=',',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        fw.writerow(['RegionID', 'Station Number', 'Station Name', 'Station Type', 'Street Address', 'Phone Number', 'Fax Number', 'E-Mail', 'Lat', 'Lon'])
        for i in range(1,len(rId)-1):

            fw.writerow([rId[i], sN[i], sNN[i], sT[i], sA[i], pN[i], fN[i], eM[i], lat[i], lon[i]])


if __name__ == '__main__':
    storingData()