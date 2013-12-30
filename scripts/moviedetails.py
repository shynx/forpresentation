import psycopg2
import cgi

def getmovieinfo(movieid):
    constr = """
       dbname='sharondb'
       user='sharon'
       password='sharon123'
       host='pythonista.learning.edu'
    """
    conn = psycopg2.connect(constr)
    curr = conn.cursor()
    curr.execute("select * from moviedetail where movieid = " + str(movieid))
    rows = curr.fetchall()
    return rows[0]



def index(req, movieid):
    movieid = cgi.escape(movieid)
    header = """
	<!DOCTYPE html>
	<html>
	<head>
	<title>Movies Database Example</title>
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<!-- Bootstrap -->
	<link href="bootstrap/css/bootstrap.min.css" rel="stylesheet">

	<!-- HTML5 Shim and Respond.js IE8 support of HTML5 elements and media queries -->
	<!-- WARNING: Respond.js doesn't work if you view the page via file:// -->
	<!--[if lt IE 9]>
	    <script src="https://oss.maxcdn.com/libs/html5shiv/3.7.0/html5shiv.js"></script>
	    <script src="https://oss.maxcdn.com/libs/respond.js/1.3.0/respond.min.js"></script>
	    <![endif]-->
	</head>
	    """
    bodybegin = """
       <body>
        <h1>&nbsp;&nbsp;&nbsp;~&nbsp;Movie Details&nbsp;~</h1>
        <br><br>
                <a href="http://pythonista.learning.edu/~sharon/viewdetails1.py" class="btn btn-success btn-sm active">Back</a></br></br>
    """
    bodyend = """
           <!-- jQuery (necessary for Bootstrap's JavaScript plugins) -->
             <script src="https://code.jquery.com/jquery.js"></script>
           <!-- Include all compiled plugins (below), or include individual files as needed -->
           <script src="js/bootstrap.min.js"></script>
           </body>
           </html>
    """
    movie = getmovieinfo(movieid)
    moviecontainer = '<div class="container"> '
    moviecontainer += ' <div class="starter-template"> '
    moviecontainer +=  ' <h4>Code: '+str(movie[0])+'</h4> '
    moviecontainer +=  ' <h3>Title: '+movie[1]+'</h3> '
    moviecontainer +=   '<p class="lead">Genre:&nbsp;' + movie[2] + ' <br>'
    moviecontainer +=   '<p class="lead">Price:&nbsp;' + movie[3] + ' <br>'
    moviecontainer +=  'Release Year:&nbsp;&nbsp;'+ str(movie[4])
    moviecontainer += '<br /> <a href="http://pythonista.learning.edu/~sharon/index1.py"'
    moviecontainer += 'class="btn btn-success btn-sm active">Back to Main Page</a></p></div></div>'

    return header + bodybegin  + moviecontainer + bodyend