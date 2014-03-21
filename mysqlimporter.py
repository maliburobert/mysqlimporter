import MySQLdb, getpass, csv

doheader = raw_input('write table from header (1):')
if not doheader: doheader = 1
host = raw_input('host (server15): ')
if not host: host = '192.168.2.15'
port = raw_input('port (3306): ')
if not port: port = 3306
user = raw_input('user (root): ')
if not user: user = 'root'
passwd = getpass.getpass('passwd (password): ')
if not passwd: passwd = 'password'
db = raw_input('db (adhoc): ')
if not db: db = 'adhoc'
table = raw_input('table name (tmp): ')
if not table: table = 'tmp'
fileloc = raw_input('file location (v:/test.csv): ')
if not fileloc: fileloc = 'v:/test.csv'
charset = raw_input('charset (utf8): ')
if not charset: charset = 'utf8'
ddl = raw_input('DDL (varchar(1000)):')
if not ddl: ddl = 'varchar(1000)'
lt = raw_input('line termination (\\r\\n): ')
if not lt: lt = '\r\n'
ft = raw_input('field termination (,): ')
if not ft: ft = ','
tq = raw_input('text qualifier ("): ')
if not tq: tq = '"'

if doheader == 1:
    with open(fileloc, "rb" ) as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',')
        head=[spamreader.next() for x in xrange(1)]
        header = head[0]
        n = 0
        queryheader = 'CREATE TABLE `%s` (' % (table)
        for i in header:
            n += 1
            i = i.replace("(","")
            i = i.replace(")","")
            i = i.replace("-","")
            if len(i)>64: i = i[:60]
            queryheader += '`' + i + '` %s' % (ddl)
            if n < len(header): queryheader += ','
        queryheader += ')'
    
queryloaddata = "LOAD DATA LOCAL INFILE '%s' INTO TABLE %s CHARACTER SET %s FIELDS TERMINATED BY '%s' ENCLOSED BY '%s' LINES TERMINATED BY '%s' IGNORE 1 LINES" % (fileloc, table, charset, ft, tq, lt)

connection = MySQLdb.Connect(host=host, port=port, user=user, passwd=passwd, db=db)
cursor = connection.cursor()
cursor.execute ( 'drop table if exists %s' % (table)) 
cursor.execute ( queryheader )
cursor.execute( queryloaddata )
connection.commit()
