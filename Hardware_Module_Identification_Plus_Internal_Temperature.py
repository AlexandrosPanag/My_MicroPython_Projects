#Source used: https://www.digi.com/resources/documentation/digidocs/PDFs/90002445.pdf
#Source used: https://www.digi.com/resources/documentation/digidocs/pdfs/90001539.pdf
#Source used: https://www.digi.com/resources/documentation/Digidocs/90002002/Reference/r_cmd_TP_xtend.htm?TocPath=AT%20commands%7CDiagnostic%20commands%7C_____6

# This code was edited by Alexandros Panagiotakopoulos

import xbee
import machine

#read the module hardware version

hw_version = hex(xbee.atcmd("HV"))
print("Hardware version: "+hw_version)

# read the module's temperature
temperature = xbee.atcmd('TP')
print("The Internal Temperature is:{} C".format(xbee.atcmd("TP")))