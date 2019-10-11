#First import the package
import bryafunctions.___init__ as bryafunctions

#For build_sql_where_clause, you're required to provide a baseSQL and LIST of parameters

#EXAMPLE WITH 2 PARAMATERS
#The ParamaterList must have 3 fields, the SQL Field name with its sql function, its value, and its type, for the purpose of this package
#only str needs to be defined, all else can be int
#IF YOU ONLY PROVIDE ONE PARAMATER, THEN STATEMENT WILL NOT CONTAIN 'AND' else mu;ltiple paramaters will be built using AND

ParameterList = [['bookName = ', 'Fancy Book', 'str'],['Author = ', 'Jacqueline Johnson', 'str']]

#The BaseSQL is simply an SQL Query which can be executed alone or with Paramaters
BaseSQL = 'SELECT * FROM books'

#Now calling the build_sql_where_clause function, takes both requirements, and it will return an SQL Statement
# Containing our BaseSQL with the Parameters provided

print(bryafunctions.build_sql_where_clause(BaseSQL, ParameterList))

#EXAMPLE WITH 1 PARAMETER
ParameterList = [['bookName = ', 'Fancy Book', 'str']]

BaseSQL = 'SELECT * FROM books'

print(bryafunctions.build_sql_where_clause(BaseSQL, ParameterList))

#EXAMPLE WITH INT PARAMATER
ParameterList = [['bookName = ', 1234, 'int']]

BaseSQL = 'SELECT * FROM books'

print(bryafunctions.build_sql_where_clause(BaseSQL, ParameterList))


#RESULTS
#SELECT * FROM books WHERE bookName = "Fancy Book" AND Author = "Jacqueline Johnson";
#SELECT * FROM books WHERE bookName = "Fancy Book";
#SELECT * FROM books WHERE bookName = 1234;