#!/usr/bin/python
# 
# PW Dump Verifier
# Authors: Jamie Gambetta, John Franolich
# 


def test_pw_chars(curr_pw):
	uppercase_present = 0
	special_present = 0
	digits_present = 0
	
	for curr_char in curr_pw:
		if curr_char.isalpha():
			if curr_char.isupper():
				uppercase_present += 1
			continue
		if curr_char.isdigit():
			digits_present += 1
			continue
		if curr_char in special_allowed:
			special_present += 1
		else:
			return False

	if uppercase_present < uppercase_req: 
		return False
	if digits_present < digits_req: 
		return False
	if special_present < special_req:
		return False
	return True
		






# Get the password file to verify
pwdump_file = raw_input("Password file: ")

min_length = int(raw_input("Min length: "))
max_length = int(raw_input("Max length: "))
uppercase_req = int(raw_input("Minimum uppercase letters required: "))
digits_req   = int(raw_input("Minimum numbers required: "))
special_req = int(raw_input("Minimum special characters required: "))
special_allowed = raw_input("Special characters allowed: ")

is_valid_pw_dump = True
policy_violations = []

total_pw_count = 0

with open(pwdump_file) as pwfile:
	curr_pw_valid = True
	for line in pwfile:
		total_pw_count += 1
		curr_pw = line.rstrip()
		if len(curr_pw) < min_length or len(curr_pw) > max_length:
			is_valid_pw_dump = False
			policy_violations.append(curr_pw)
		curr_pw_valid = test_pw_chars(curr_pw)
		if(not curr_pw_valid):
			is_valid_pw_dump = False
			policy_violations.append(curr_pw)
	
	msg = ""
	if not is_valid_pw_dump:
		msg += "NOT "
	msg += "ALL PASSWORDS IN DUMP ARE VALID"

	if 0 == total_pw_count:
		print "That was an empty file....";
		exit()

	percent_violators = (len(policy_violations) / float(total_pw_count)) * 100

	print msg
	if not is_valid_pw_dump:
		print "Policy violations made up " + `percent_violators` + " percent of the pw dump"
		list_violators = raw_input("Do you want to see the list of policy violations? (y/n): ")
		if "y" == list_violators:
			for curr in policy_violations:
				print "\t" + curr

