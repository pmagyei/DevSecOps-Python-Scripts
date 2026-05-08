ports_to_scan = {}
active = True
while active: # while loop will run as long as active is true

    restart = (input("\nDo you want start the CLI tool: \n"))
    if restart == 'no':
        active = False
        print("Exiting, the following ports will be scanned:")
        for ps in ports_to_scan.keys():
            print(ps)
       #break
    elif restart == 'yes':
            try:
                port = int(input("\nEnter a port number to scan: \n"))
                ports_to_scan[port] = "scanning"
                print(f"Adding port number: {port} to ports to scan")
                print(ports_to_scan)
            except ValueError:
                print("Invalid characters entered, Try again...")
    else:
        print("Invalid input, try again")