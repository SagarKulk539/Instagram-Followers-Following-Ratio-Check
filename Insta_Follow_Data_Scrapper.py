# Imports
import json
import os
import datetime
import argparse
import traceback

if __name__ == "__main__":
    try:
        # File Path
        parser = argparse.ArgumentParser(description="Path for Instagram json files")
        parser.add_argument("input_file_path", type=str, help="Path for Instagram json files")
        args = parser.parse_args()
        path_to_files = args.input_file_path

        # Part - 1
        # This part will extract followers and following data

        # Input
        followers_path = os.path.join(path_to_files,'followers_1.json')
        following_path = os.path.join(path_to_files,'following.json')

        # Timestamp Folder
        ctTemp = datetime.datetime.now()
        tsTemp = ctTemp.timestamp()

        # ct stores current time
        ct = str(ctTemp)
        # ts stores timestamp of current time
        ts = str(tsTemp)

        listTime = ct.split('-')
        timestamp = listTime[2].split(' ')[0]+"_"+listTime[1]+"_"+listTime[0]+"_"+ts.split('.')[0]

        cust_output_folder_name = "Output"
        output_folder = os.path.join(path_to_files,cust_output_folder_name,timestamp)
        if not os.path.exists(output_folder): 
            os.makedirs(output_folder)

        # Output
        output_followers_path = os.path.join(output_folder,'followers.txt')
        output_following_path = os.path.join(output_folder,'following.txt')
        new_out_1 = os.path.join(output_folder,'not_following_you.txt')
        new_out_2 = os.path.join(output_folder,'you_not_following.txt')

        # Key params to search in the dictionary
        param1 = 'string_list_data'
        param2 = 'value'
        param3 = 'relationships_following'

        #print('---------- Followers - START ----------')

        # Followers Data Parsing
        #print('Parsing followers data')
        input_file_followers = open(followers_path)
        json_array_followers = json.load(input_file_followers)
        followers_list=[]

        for followers in json_array_followers:
            followers_list.append(followers[param1][0][param2])

        # Sort the Data
        followers_list.sort()

        # Debug Print
        #print(followers_list)

        # Output Data to file
        #print('Output followers data to file')
        file_followers = open(output_followers_path,'w')
        for followers in followers_list:
            file_followers.write(followers+"\n")
        file_followers.close()

        #print(f"Followers List in {output_followers_path}")
        #print('---------- Followers - END ----------')
        #print()
        #print('---------- Following - START ----------')

        # Following Data Parsing
        #print('Parsing following data')
        input_file_following = open(following_path)
        json_array_following = json.load(input_file_following)
        following_list=[]

        for following in json_array_following[param3]:
            following_list.append(following[param1][0][param2])

        # Sort the Data
        following_list.sort()

        # Debug Print
        #print(following_list)

        # Output Data to file
        #print('Output following data to file')
        file_following = open(output_following_path,'w')
        out_1 = open(new_out_1,'w')
        flag_1 = False

        for following in following_list:
            file_following.write(following+"\n")
            if following not in followers_list:
                flag_1 = True
                out_1.write(following+"\n")

        if flag_1 == False:
            out_1.write("No entries\n")

        out_1.close()
        file_following.close()

        #print(f"Following List in {output_following_path}")
        #print('---------- Following - END ----------')

        out_2 = open(new_out_2,'w')
        flag_2 = False
        for followers in followers_list:
            if followers not in following_list:
                flag_2=True
                out_2.write(followers+"\n")

        if flag_2 == False:
            out_2.write("No entries\n")

        out_2.close()

        #print("\nAdditional parsed Information:")
        #print(f"{new_out_1}")
        #print(f"{new_out_2}")

        # Part - 2
        # This part will extract members that are not following you (except the list given in path1)

        # Imports
        import os

        # Input
        # Custom made list of pages/people that won't follow you back
        cust_cannot_follow = "cannot_follow_you.txt"
        path1 = os.path.join(path_to_files,cust_cannot_follow)

        # Output
        # Output File with list of members not following you
        output_path = os.path.join(output_folder,'CUSTOM_not_following_you.txt')

        # Read from file and convert to list
        #print("Reading file 1......")
        try:
            input1 = open(path1, "r")
            #list1 = input1.read().split("\n")
            list1 = input1.readlines()
            list1 = [line.strip() for line in list1]
            #print(list1) 
            input1.close() 
        except FileNotFoundError:
            print("NOTE : List of people who cannot follow you back is not given as input")
            list1=[]

        # Proceed to compare if custom text file is not empty
        if len(list1) != 0:
            #print("Reading file 2......")
            input2 = open(new_out_1, "r")
            #list2 = input2.read().split("\n")
            list2 = input2.readlines()
            list2 = [line.strip() for line in list2]
            #print(list2)
            input2.close()

            #print("Parsing Data......")
            out_1 = open(output_path,'w')
            flag1=False
            # Compare and add elements to final list
            for element in list2:
                if element not in list1:
                    out_1.write(element+"\n")
                    flag1=True

            if flag1 == False:
                out_1.write("No Entries")

            out_1.close()
            #print(f"Members not following you: {output_path}")

        # Part - 3
        # This part will extract pending instagram follow requests (i.e the req you've sent)
        pending_follow_path = os.path.join(path_to_files,'pending_follow_requests.json')
        output_pending_follow_path = os.path.join(output_folder,'pending_follow_requests.txt')

        # Key params to search in the dictionary
        param1 = 'string_list_data'
        param2 = 'value'
        param3 = 'relationships_follow_requests_sent'

        #print('---------- Pending Follow Requests - START ----------')

        # Pending Follow Requests Data Parsing
        #print('Parsing pending follow requests data')
        input_file_pending_follow = open(pending_follow_path)
        json_array_pending_follow = json.load(input_file_pending_follow)
        pending_follow_list=[]

        for pending_follow in json_array_pending_follow[param3]:
            pending_follow_list.append(pending_follow[param1][0][param2])

        # Sort the Data
        pending_follow_list.sort()

        # Debug Print
        #print(pending_follow_list)

        # Output Data to file
        #print('Output pending follow requests data to file')
        file_pending_follow = open(output_pending_follow_path,'w')
        for pending_follow in pending_follow_list:
            file_pending_follow.write(pending_follow+"\n")

        #print('---------- Pending Follow Requests - END ----------')

        strLines = "-"*50
        print(strLines)
        print(f"All output files placed in folder: {output_folder}")
        print(strLines)
    except Exception as e:
        print("Runtime Error: Kindly check below error message !!")
        print(traceback.format_exc())


