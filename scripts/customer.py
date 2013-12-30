import psycopg2

def getmovies():
    constr = """
       dbname='sharondb'
       user='sharon'
       password='sharon123'
       host='pythonista.learning.edu'
    """
    conn = psycopg2.connect(constr)
    curr = conn.cursor()
    curr.execute("select * from customer")
    rows = curr.fetchall()
    return rows

def index(req):
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
        &nbsp;&nbsp; <h2>~&nbsp;List of Customer's&nbsp;~</h2>
        <br>
        <a href="http://pythonista.learning.edu/~sharon/index1.py" class="btn btn-success btn-sm active">Back to Main Page</a></br>
    """
    bodyend = """
           <!-- jQuery (necessary for Bootstrap's JavaScript plugins) -->
             <script src="https://code.jquery.com/jquery.js"></script>
           <!-- Include all compiled plugins (below), or include individual files as needed -->
           <script src="js/bootstrap.min.js"></script>
           </body>
           </html>
    """

    panelbegin = """
      <div class="panel panel-default">
      <!-- Default panel contents -->
      """
    tablebegin = """<table class="table table-hover table-condensed">"""
    tableend = "</table>"
    panelend = """
       </div>
      </div>
    """

    movies = getmovies()
    tablecontents = ""
    i = 1
    for movie in movies:
        if i % 2 == 0:
            class_ = 'class="warning"'
        else:
            class_=""

        tablecontents += "<tr "+class_+">"
        tablecontents += "<td>"+movie[0]+"</td>"
        tablecontents += "<td>"+str(movie[1])+"</td>"
        tablecontents += "<td>"+str(movie[2])+"</td>"
        tablecontents += "<td>"+str(movie[3])+"</td>"
        tablecontents += "<td>"+str(movie[4])+"</td>"
        tablecontents += "<td>"+str(movie[5])+"</td>"
        tablecontents += "<td>"+str(movie[6])+"</td>"
        tablecontents += '<td><a href="http://pythonista.learning.edu/~sharon/moviedetails.py"</td>'
        tablecontents += "</tr>"
        i = i + 1




    return header + bodybegin + panelbegin + tablebegin + tablecontents + tableend + panelend + bodyend