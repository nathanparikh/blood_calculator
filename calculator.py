def interface():
    print("My Program")
    while 1:
	    print("Options:")
	    print ("1 - HDL")
	    print("9 - Quit")
	    choice = input("Enter your choice: ")
	    if choice=='9':
	        return
	    elif choice == '1':
	    	HDL_driver()

def HDL_driver():
	hdl_input = HDL_input()
	hdl_message = HDL_normal(hdl_input)
	hdl_output (hdl_input,hdl_message)


def HDL_input():
	hdl_input = input("Enter your HDL test result: ")
	return int(hdl_input)

def HDL_normal(hdl):
	if hdl>=60:
		return "Normal"
	if (hdl>=40 and hdl<60):
		return "Borderline Low"
	if (hdl<40):
		return "Low"

def HDL_output(hdl, analysis):
	print("The HDL test result is {}".format(hdl))
	print ("That is {}".format(analysis))


if __name__ == "__main__":
	interface()