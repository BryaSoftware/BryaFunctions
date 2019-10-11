#First import the package
import bryafunctions.___init__ as bryafunctions


#To use remove_Params, you provide a ParamaterList, if any paramaters are missing a value, then they should not be included as a current parameter
#In this example we do not include the Author Value
#The output should then be a list containing only BookName
ParameterList = [['bookName = ', 'Fancy Book', 'str'],['Author = ', 'null', 'str']]

print (bryafunctions.remove_Params(ParameterList))

#RESULT 
#[['bookName = ', 'Fancy Book', 'str']]