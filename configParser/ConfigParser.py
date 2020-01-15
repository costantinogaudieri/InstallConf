import configparser

parser = configparser.ConfigParser()
parser.read('application.properties.ini')


def getPlatform():
    activePlatforms = parser.get('PLATFORM', 'activeDeploy')
    return activePlatforms.split(',')


def getPathFormat(tag):
    x = {}
    for each_section in parser.sections():
        if each_section == tag:
            for (each_key, each_val) in parser.items(each_section):
                x[each_key] = each_val
    return dict(x)
