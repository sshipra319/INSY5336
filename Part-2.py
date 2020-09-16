
  
    "def check():                                                #check function to check for integer value\n",
    "    val1 = input(\"Please enter an integer: \")\n",
    "    while(True):\n",
    "        try:                                                #if value is integer then it will return the value\n",
    "            s = int(val1)\n",
    "            return s\n",
    "        except:\n",
    "            print(\"You did not enter an integer.\")          #if not valid integer value will print an error message\n",
    "            val1 = input(\"Please enter an integer: \")\n",
   
    "val = input(\"Enter set of 3 or 4 integers: \")               #ask for the number of values to be entered\n",
    "if val == '3':                                              \n",
    "    x1 = check()                                            #check function use to check for valid integer value\n",
    "    x2 = check()\n",
    "    x3 = check()\n",
    "    num_lst1 = [x1, x2, x3]                                 #created the list of the entered numbers\n",
    "    n1 = len(num_lst1)                                      #length of the list\n",
    "    num_lst1.sort()                                         #sorted the list to find the median\n",
    "    Add = x1 + x2 + x3                                      #sum of three number\n",
    "    Avg = round(Add/n1)                                     #average of numbers is calculated then it is rounded\n",
    "    print(\"The average of three numbers is: \", Avg)\n",
    "    mx = max(num_lst1)                                      #inbuilt function to find the maximum value\n",
    "    print(\"The maximum of the three numbers is: \", mx)\n",
    "    mn = min(num_lst1)                                      #inbuilt function to find the minimum value\n",
    "    print(\"The minimum of the three numbers is: \", mn)\n",
    "    median = num_lst1[n1//2]\n",
    "    print(\"The median of the three numbers is: \", median)\n",
    "elif val == '4':\n",
    "    x1 = check()\n",
    "    x2 = check()\n",
    "    x3 = check()\n",
    "    x4 = check()\n",
    "    num_lst = [x1, x2, x3, x4]                              #created the list of the entered numbers\n",
    "    n = len(num_lst)                                        #length of the list\n",
    "    num_lst.sort()                                          #sorted the list to find the median\n",
    "    Add = x1 + x2 + x3 + x4                                 #sum of three number\n",
    "    Avg = round(Add/n)                                      #average of numbers is calculated then it is rounded\n",
    "    print(\"The average of four numbers is: \", Avg)\n",
    "    mx = max(num_lst)                                       #inbuilt function to find the maximum value\n",
    "    print(\"The maximum of the four numbers is: \", mx)\n",
    "    mn = min(num_lst)                                       #inbuilt function to find the minimum value\n",
    "    print(\"The minimum of the four numbers is: \", mn)\n",
    "    median1 = num_lst[n//2]                                 #as the list contains even number of elements so find\n",
    "    median2 = num_lst[n//2 - 1]                             #the middle two elements of the list\n",
    "    median = (median1 + median2)/2                      #average of the middle two elements of the list gives the median\n",
    "    print(\"The median of the four numbers is: \", median)\n",
    "else:                                                       #error message if number is not 3 or 4.\n",
    "    print(\"Invalid input\")\n",
  