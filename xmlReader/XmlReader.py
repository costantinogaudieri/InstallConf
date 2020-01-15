import xmltodict
import xml.etree.ElementTree as ET

def readRelease(path):

    with open(path) as fd:
        output = fd.read()
        doc = xmltodict.parse(output)
        x = doc['project']['version']
        release, snapshot = str.split(x, "-")
        return release

def removeSNAPSHOT(path,release):
    #with open(path, 'r+') as fd:
        #doc = xmltodict.parse(fd.read())
        #print(doc['project']['version'])
        #doc['project']['version'] = release
        #fd.write(xmltodict.unparse(doc))


    readfile = open(path, 'r')
    rstring = readfile.read()
    readfile.close()
    parser = ET.XMLParser()
    tree = ET.XML(rstring, parser)
    root = tree

    ET.register_namespace('', 'http://maven.apache.org/POM/4.0.0')

    namespaces = {'xmlns:xsi' : 'http://www.w3.org/2002/07/owl',
                  'xsi:schemaLocation' : 'http://maven.apache.org/POM/4.0.0 http://maven.apache.org/maven-v4_0_0.xsd'}
    for trans in tree.findall('project', namespaces):
        print(trans)
    wfile = open(path, 'wb')
    wfile.write(ET.tostring(root))
    wfile.close()






