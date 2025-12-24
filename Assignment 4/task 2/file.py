def file_op() :
    #fh = open("File.txt" , "xt") 

    fh = open("File.txt" , "wt" )
    inp = input("Enter SOmething to write : ").strip()
    fh.write(inp)
    fh.close()
    yes = int(input("Want to append (0|1) :" ))
    match yes :
        case 1 :
            with open("File.txt" , "at" ) as fh :
                inp = input("Enter Something to append : ").strip()
                fh.write("\n"+inp)
            print("Appended Successfully")
        case 0 :
            print("Not Appending")
            exit()
        case _ :
            print("Invalid Input exiting ..")
            exit()



file_op()