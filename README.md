# AutoLogger
    This project is used to enable traces in C/C++ files. This will add a statement to the entry of each function.
                                        

## Prerequisites:
  - Python 3.5.x or above 
  
## Steps:
  1) Add print statement in "Enter Trace" section(you can take given hint) 
  2) Choose file (select any c/c++ file)
  3) This will generate a file output.log in the same directory of the application 
  4) You can see original as well as modified file contents in the text field
     (Each modified content will appear in red)

Note:- Your original file will not be affected here

## Advantage:

  You can keep track of function calls which will help in debugging.
  ex: printf("  %s  %s  line no = %d ",__FILE__,__FUNCTION__,__LINE__);'
