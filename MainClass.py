from xmlReader import XmlReader
from gitConfig import GitConfig
from jsonReader import JsonReader
from configParser import ConfigParser

# GitConfig.checkoutDev()
#release = XmlReader.readRelease('C:/MyProjects/terminaliniwifi.server/pom.xml')
#release_ = JsonReader.readRelease('C:/MyProjects/terminaliniwifi.client/package.json')
#print(release_)
#print(release)

# map = ConfigParser.getPathFormat(var)
# print(map)

listPlatforms = ConfigParser.getPlatform()


for platform in listPlatforms:
    print(platform)
    mapConfig = ConfigParser.getPathFormat(platform)
    if 'path' in mapConfig:
        endPath = mapConfig['path']+'\pom.'+mapConfig['extension']
        release = XmlReader.readRelease(endPath)
        GitConfig.configureGit(mapConfig['path'])
        GitConfig.checkoutDev()
        GitConfig.executeRelease(release, endPath)
        #GitConfig.upgradeRelease()

