from collections import OrderedDict
import csv
import json


def main():
    #open csv file
    f = open('naic_codes.csv', 'r')
    #set field names
    reader = csv.DictReader(f, fieldnames = ("code", "description"))
    # Map fields
    codes_map = {}
    for row in reader:
        codes_map[row["code"]]=row["description"]
    # Dump json
    out = json.dumps(codes_map)
    print "JSON parsed!"
    #Set json output file
    f = open('naic_codes.json', 'w')
    f.write(out)
    print "JSON saved!"

main()
