#!/bin/sh
userid=${1}
password=${2}
csv_filename=${3}

echo $userid
echo $password

curl --cookie-jar cjar --output firstpageoutput.html \
https://www.att.com/olam/loginAction.olamexecute

curl --cookie cjar --cookie-jar cjar \
--location \
--data "reportActionEvent=A_LGN_LOGIN_SUB&rootPath=%2Folam%2FEnglish&isPromoGraphicValid=false&wirelineLoginURL=https%3A%2F%2Fcprodmasx.att.com%2FcommonLogin%2Figate_wam%2FmultiLogin.do%3F&isSlidLogin=true&ispLoginType=false&remember_me=Y&source=MYATT&flow_ind=LGN&wireless_num=&pass=&vhname=www.att.com&urlParameters=reportActionEvent%3DA_LGN_LOGIN_SUB%26loginSource%3Dolam&cancelURL=https%3A%2F%2Fwww.att.com%2Folam%2FloginAction.olamexecute&loginType=SLID&isPassThroughURL=false&ajaxSupported=&domain=.att.com&tGuardOn=true&isTarget=false&customerType=&ck_userId=&ck_userType=&wireLineOn=true&localeInRequest=&style=account&userid=$userid&password=$password&x=32&y=16" \
--output loginresult.html \
https://myattp1w85.att.com/commonLogin/igate_wam/multiLogin.do

curl --cookie cjar \
--output $csv_filename \
https://www.att.com/pmt/jsp/mypayment/viewbill/download_csv/download_csv.jsp?reportActionEvent=A_VB_WIRELESS_DETAILS_DOWNLOAD_CSV_SUBMIT


