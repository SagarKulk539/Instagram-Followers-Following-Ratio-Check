# Utility Python script to scrape necessary information from instagram followers and following data

## Usage:
`python <filename.py> <path to input files>`

[Works on all platforms - Win/Linux/Mac]

## Input
Input Parameters (command line - required): Path to the below 3 json files
Input files (required): followers_1.json, following.json, pending_follow_requests.json
[Update filenames in script if they change over-time]

## Output
This is a utility python script that gives below output, based on input data from instagram (i.e followers, following):
1. Complete list of followers/following
2. List of accounts/profiles that do not follow you back
3. List of accounts/profiles that you do not follow back
4. Pending follow requests (outgoing)

### Note: There is an optional input file named 'cannot_follow_you.txt', which has to be user defined. This should contain a list of accounts/profiles that practically cannot follow you back (eg. celebrities, influencers, meme pages etc)
### If this is given as input, then the output of "accounts that don't follow you back" would be more refined !!
### [In above file, each profile name has to be on new line]
