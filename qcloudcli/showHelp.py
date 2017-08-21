from . import handleData
import platform
class showHelp:
    def __init__(self):
        if 'Linux' in platform.system():
            self.begin = '\033[1m'
            self.red = '\033[31m'
            self.end = '\033[0m'
        if 'Windows' in platform.system():
            self.begin = ''
            self.red = ''
            self.end = ''
        else:
            self.begin = ''
            self.red = ''
            self.end = ''

        self.handleData = handleData.handleData()

    def showComMes(self):
        print("You should use the qcloudcli as follow format:")
        print(self.red + "qcloudcli <module> <action> [options and parameters]"+self.end)

    def showExample(self):
        print("show example")

    def showModuleError(self):
        self.showComMes()
        print("The module name you input is error! qcloudcli support the valid module as follows:\n")
        modules = self.handleData.getAllmodules()
        self.showAsTwoLines(modules)


    def showActionError(self, module):
        self.showComMes()
        operations = []
        if module == "cvm":
            operations, newoperations = self.handleData.getModuleActionsForVersion(module)
            print("The action name you input is error!\nThe old API for module "+self.red + "["+module+"]"+self.end+" support the valid action as follows:\n")
            self.showAsTwoLines(operations)
            print("\nThe new API for module " + self.red + "[" + module + "]" + self.end + " support the valid action as follows(\"Verison\" parameters must be passed in ):\n")
            self.showAsTwoLines(newoperations)
        else:
            print("The action name you input is error! The module " + self.red + "[" + module + "]" + self.end + " support the valid action as follows:\n")
            operations = self.handleData.getModuleActions(module)
            self.showAsTwoLines(operations)

    def showParameterError(self, module, action, is_version, parameterlist0, parameterlist1, parameterlist2, parameterlist3):
        self.showComMes()
        if is_version == 1:
            print('The old API for action '+self.red + '['+module+"."+action+']' +self.end+' can uses the options and parameters as follow :\n\nOld API Global Options:\n')
            self.showAsTwoLines(parameterlist0)
            print('\nOld API Action parameters:\n')
            self.showAsTwoLines(parameterlist1)
            print('\nThe new API for action ' + self.red + '[' + module + "." + action + ']' + self.end + ' can uses the options and parameters as follow (\"Verison\" parameters must be passed in ):\n\nNew API Global Options:\n')
            self.showAsTwoLines(parameterlist2)
            print('\nNew API Action parameters:\n')
            self.showAsTwoLines(parameterlist3)
        else:
            print('The action '+self.red + '['+module+"."+action+']' +self.end+' can uses the options and parameters as follow :\n\nGlobal Options:\n')
            self.showAsTwoLines(parameterlist0)
            print('\nAction parameters:\n')
            self.showAsTwoLines(parameterlist1)
        pass

    def showAsTwoLines(self, data):
        mlist = list()
        for item in data:
            mlist.append(item)
        mlist.sort()
        if len(mlist)%2 == 0:
            k=len(mlist) // 2
        else:
            k=len(mlist) // 2 + 1
        mlist2 = list()
        for item in mlist:
            mlist2.append(item)
        for i in range(0,k):
            mlist2[2 * i] = mlist[i]
        for i in range(k,2*k-1):
            mlist2[i-(2*k-1-i)] = mlist[i]
        count = 0
        tmpList = list()
        for item in mlist2:
            tmpList.append(item)
            count = count+1
            if len(tmpList) == 2:
                print('{0:40}'.format(tmpList[0])+'\t|'+format(tmpList[1],'<10'))
                tmpList = list()
            if len(tmpList) == 1 and count == len(mlist2):
                print(tmpList[0])
