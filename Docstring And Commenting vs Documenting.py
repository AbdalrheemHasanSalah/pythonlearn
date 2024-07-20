#------------------------------------------
#--Doc String & Commenting vs Documenting--
#------------------------------------------
#[1] Documenting String for class Module or Function
#[2] Can be Accessed From the help Documenting and attributes
#[3] Made understanding the functionality of the complex code
#[4] theres one line and multiple Line Doc String 
#-------------------------------------------------------------


def function_doc(name):
    """   function_doc:
            it say hello from function_doc
          parameter:
            name =>person name that use function
          Return:
            return Hello Massage to the person
                         """
    print(f"hello {name} from doc function")

function_doc("abdalrheem")
print(dir(function_doc))
print(function_doc.__doc__)#function_doc:
                                  #it say hello from function_doc
                            #parameter:
                                  # name =>person name that use function
                            #Return:
                                  # return Hello Massage to the person



#help(function_doc)         #function_doc:
                                  #it say hello from function_doc
                            #parameter:
                                  # name =>person name that use function
                            #Return:
                                  # return Hello Massage to the person





