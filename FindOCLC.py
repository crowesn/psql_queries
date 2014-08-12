#TechProCheck.py
import sys, subprocess, os

elif len(sys.argv) == 5:
	SessionUser = sys.argv[1]
	SessionPass = sys.argv[2]
	inputFile = sys.argv[3]
	outputFile = sys.argv[4]
else:
	SessionUser = raw_input('Type Sierra username: ')
	SessionPass = raw_input('Type Sierra password: ')
	inputFile = raw_input('Type input filename from current directory')
	outputFile = raw_input('Type desired output filename ()')

def submit_query(SessionUser, SessionPass, Recipient1):
	submitted_query = os.popen(query)
try:

query = """create temporary table OCLC(id text);
\copy OCLC from '{0}'
\copy (select concat('b',b.record_num,'a') as bibno from OCLC o JOIN sierra_view.varfield v ON (o.id = v.field_content and v.varfield_type_code = 'o') LEFT JOIN sierra_view.bib_view b ON (v.record_id = b.id)) TO {1} WITH CSV HEADER;""".format(inputFile, outputFile)
"""
	submit_query(SessionUser, SessionPass, Recipient1)

except: 
	print "Unexpected error:", sys.exc_info()[0]
