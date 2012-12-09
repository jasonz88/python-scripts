outputdir = 'out'

dsn = 'osr_atiic2'
is_mssql = True
sqlserver = 'sql01.austin.utexas.edu'
sqluser = 'osrstudy'
sqlpass = 'lac2110c'
sqldb = 'OSR_atiic2'

dblookupanswer = True
dbanswervarname = 'anstable'

is_cf_required = False
to_print_label = True
to_print_qnumbers = False

qfile = 'atiic2.q'
page_title = '''
Real Time Location Services Survey

'''
page_prefix = 'page_'
page_suffix = '.cfm'

tablerootname = 'result'
keyword = 'cid'
keyvalue = '#client.cid#'
curr_page_n = 0

## enforcing lastpage to be 38
#lastpage = 38

is_lastpage_verification_needed = True

standardFieldsForTableRoot = [ [ "cid", "varchar(16) NOT NULL" ],
                               [ "primary key", "(cid)" ],
                               [ "lastlogin", "DATETIME" ],
                               [ "farthestnode", "varchar(5)" ],
                               [ "lastnode", "varchar(5)" ] ]

standardFieldsForTablePage = [ [ "cid", "varchar(16) NOT NULL" ],
                               [ "primary key", "(cid)" ],
                               [ "lastaccessed", "DATETIME" ],
                               [ "submitdate", "DATETIME" ] ]

# multipleAllowed = ( "cid", "lastaccessed", "submitdate" )

###--- FOR EVERY PAGE EXCEPT THE INTRO AND LAST PAGE
###----------------------------------------

#-- header that goes to every page except the starter page and the last page
header = []
header_vars = []

# common header
header.append('''
<html>
<head>
<title>
%s
</title>
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
<style type="text/css">@import "page.css";</style>
<script type="text/javascript" src="page.js"></script>
<script type="text/javascript">
<!--
%s
// -->
</script>
</head>

<CFQUERY DATASOURCE="%s" NAME="%s">
  SELECT * FROM %s_page_%s WHERE %s like '%s'
</CFQUERY>

<body>
<div class=title>
%s
</div>

<CFOUTPUT>
<!--- Bring to login page when users are not accessing the page properly
--->
<CFIF NOT Isdefined("client.cid") and NOT Isdefined("form.cid")>
  <CFLOCATION url="login.cfm">

<CFELSE>

<!--- Store the last node in the database --->
<CFQUERY DATASOURCE="%s">
  UPDATE %s SET %s='%s' WHERE %s like '%s'
</CFQUERY>
''')

header_vars.append('''(
#title
page_title,
#thenecessaryjavascript
javascript,
#answer
dsn, dbanswervarname, tablerootname, curr_page_n, keyword, keyvalue,
#title
page_title.replace('\\n','<br />'),
#lastnode
dsn, tablerootname, "lastnode", curr_page_n, keyword, keyvalue,
)''')

# to print what all pages are available to jump around
header.append('''
<CFQUERY DATASOURCE="%s" NAME="howfar">
  SELECT * FROM %s WHERE cid = '#client.cid#'
</CFQUERY>

<CFQUERY DATASOURCE="%s" NAME=stats>
  SELECT * FROM %s_stats WHERE attrname='lastpage'
</CFQUERY>
<cfset thelastpage = (#stats.attrval[1]# - 1)>

<div class="jumpto">
<table>
<tr><td>
Progress: &nbsp;
<cfloop index=i from=1 to=#thelastpage#>

  <cfif #i# eq %s>
     <td class="page_index_current">
     #i# 
     &nbsp;
     </td>
  <cfelseif #i# lte %s>
     <td class="page_index">
     <a href="page_#i#.cfm">#i#</a>&nbsp;
     </td>
  <cfelse>
     <td class="page_index_inactive">
     #i#
     &nbsp;
     </td>
  </cfif>

  <cfif #i# mod 20 is 0>
  <tr><td>&nbsp;
  </cfif>
</cfloop>
</table>
</div>
''')

header_vars.append('''(
    dsn, tablerootname,
    dsn, tablerootname,
    curr_page_n,
    curr_page_n
    )''')

# the form header
header.append('''
<CFFORM ACTION='%s' METHOD='POST' OnSubmit='return onSubmitVerification()'>
<INPUT TYPE="hidden" NAME="%s" VALUE="%s">
%s
''')

#prevpagebuttonclause = '''
#<INPUT TYPE="button" VALUE="Previous" onclick="window.location='page_%d.cfm'"> 
#'''

header_vars.append('''(
#cfform action
dbintfilename, keyword, keyvalue,
#additional cfscript needed to support this
cfscript
)''')

# the caller should be able to run:
#    header % eval(header_vars) 
# provided that it defines all the necessary variables listed in the header_vars


#-- footer that goes to every page except the introduction and last page
footer = []
footer.append('''
<div class="navibottom">
<input id="toexit" type="hidden" name="toexit" value="no">
%s
<INPUT TYPE="submit" VALUE="Next" onclick="fillToExitField(false)">
&nbsp;&nbsp;&nbsp;&nbsp;
<INPUT TYPE="submit" VALUE="Save responses, return later to continue" onclick="fillToExitField(true)"> 
</div>
</CFFORM>

</CFIF>
</CFOUTPUT>
</body>
</html>
''')

footer_vars = []
footer_vars.append('''(prevpagebutton)''')

dbheader = []
dbheader.append('''
<CFQUERY DATASOURCE="%s" NAME="ques">
  SELECT %s FROM %s WHERE %s like '%s'
</CFQUERY>

<cfif #ques.RecordCount# IS 0>
  <CFQUERY DATASOURCE="%s">
    INSERT INTO %s (%s) VALUES ('%s')
  </CFQUERY>
</CFIF>

<CFQUERY DATASOURCE="%s">
  UPDATE %s SET lastaccessed=getdate() WHERE %s like '%s'
</CFQUERY>
''')

dbheader_vars = []
dbheader_vars.append('''(
dsn, keyword, tablename, keyword, keyvalue,
dsn, tablename, keyword, keyvalue,
dsn, tablename, keyword, keyvalue
)''')

###-- DBFOOTER --###

dbfooter = []
dbfooter_vars = []

dbfooter.append('''
<!--- Store the submitdate in the database --->
<CFQUERY DATASOURCE="%s">
  UPDATE %s SET submitdate=getdate() WHERE %s like '%s'
</CFQUERY>
''')
dbfooter_vars.append('''(
dsn, tablename, keyword, keyvalue,
)''')


#lastnode
dbfooter.append('''
<!--- Store the last node in the database --->
<!--- only update last node if users do not press save and exit --->
<cfif #form.toexit# neq "yes">
<CFQUERY DATASOURCE="%s">
  UPDATE %s SET %s='%s' WHERE %s like '%s'
</CFQUERY>
</cfif>
''')

dbfooter_vars.append('''(
dsn, tablerootname, "lastnode", curr_page_n+1, keyword, keyvalue,
)''')


#farthestnode
dbfooter.append('''
<!--- To decide if the lastNode is greater than the farthest node --->
<CFQUERY DATASOURCE="%s" NAME="howfar">
  SELECT %s FROM %s WHERE %s = '%s'
</CFQUERY>
''')

dbfooter_vars.append('''(
dsn, "farthestnode", tablerootname, keyword, keyvalue,
)''')

#decide whether to register curr_page_n+1 as farthest node or not
dbfooter.append('''
<!--- only update farthest node if users do not press save and exit --->
<cfif #form.toexit# neq "yes">
<cfif #howfar.farthestnode[1]# eq "" or #howfar.farthestnode[1]# lt %s >
  <CFQUERY DATASOURCE="%s">
    UPDATE %s SET %s='%s' WHERE %s = '%s'
  </CFQUERY>
</cfif>
</cfif>
''')

dbfooter_vars.append('''(
curr_page_n+1, dsn, tablerootname, "farthestnode" , curr_page_n+1, keyword, keyvalue
)''')

#goto next page automatically
dbfooter.append('''
<cfif #form.toexit# eq "yes">
<cflocation url="save_exit_page.cfm">
<cfelse>
  <!--- check if there is an endurl defined due to a skip pattern --->
  <cfif Isdefined("endurl")>
    <cflocation url="#endurl#">
  <cfelse>
    <CFLOCATION url="%s">
  </cfif>
</cfif>
''')

dbfooter_vars.append('''(
nextpage
)''')

###--- FOR LAST PAGE
###----------------------------------------

#-- header that goes to the very last page
endheader = []
endheader.append('''
<html>
<head>
<title>
%s
</title>
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
<style type="text/css">@import "page.css";</style>
<script type="text/javascript" src="page.js"></script>
</head>

<body>
<div class=title>
%s
</div>

<CFOUTPUT>
<!--- Bring to login page when users are not accessing the page properly
--->
<CFIF NOT Isdefined("client.cid") and NOT Isdefined("form.cid")>
  <CFLOCATION url="login.cfm">

<CFELSE>

<!--- Store the last node in the database --->
<CFQUERY DATASOURCE="%s">
  UPDATE %s SET %s='%s' WHERE %s like '%s'
</CFQUERY>

''')

endheader_vars = []
endheader_vars.append('''(
#title
page_title,
#title displayed
page_title.replace('\\n','<br />'),
#lastnode
dsn, tablerootname, "lastnode", curr_page_n, keyword, keyvalue
)''')

#-- footer that goes to the very last page
endfooter = []
endfooter.append('''
</CFIF>
</CFOUTPUT>

<div class="navibottom">
<center>
<input type=button value="CLOSE WINDOW" onclick="javascript:window.close()">
</center>
</div>

</body>
</html>
''')

endfooter_vars = []
endfooter_vars.append('''()''')


###--- FOR INTRO PAGE / LOGIN PAGE
###----------------------------------------
loginpage = []
loginpage.append('''
<html>
<head>
<title>

Dimensions of Nursing Work Time (DNWT)


</title>
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
<style type="text/css">@import "page.css";</style>
<script type="text/javascript" src="page.js"></script>
</head>
<body>
<div class=title>
<br />Dimensions of Nursing Work Time (DNWT) <br />
</div>
<br />
<div class=login>
    <u><strong>Instructions</strong></u>:<br />
    Please enter your Login ID to start the survey.  <br />
    When you have responded to all the questions on a page,  
    click the 'Next' button to continue.  <br />
<br />
    At any time, you can click the 'Save responses, return later to continue' 
    button to exit the survey. <br />You will be brought back to the last page
    you visited the next time you login.<br />
    <br />
    You will be prompted when the survey is complete.<br /><br />
</div>    
    <cfform action="dbint_login.cfm" method="post">
<div class=login>
    <b>Login ID</b><br />
    <CFINPUT type="text" size="16" maxlength="16" name="cid" required="Yes" message="Please enter the Login ID provided to you" onValidate="ValidateLogin"> <br/>
    <b>Password</b><br />
    <CFINPUT type="password" size="16" maxlength="16" name="password" required="Yes" message="Please enter the password provided to you">
</div>
    <span class="navibottomlogin">
<span class=login>
    <input name="submit" type="submit" value="Submit">
</span>
    </span>
    </cfform>
</body>
</html>
''')

loginpage_vars = []
loginpage_vars.append('''()''')

dbloginpage = []
dbloginpage.append('''

<cfset client.cid = "#form.cid#">

<cfinclude template="template_isvalid.cfm">
''')

dbloginpage_vars = []
dbloginpage_vars.append('''()''')
