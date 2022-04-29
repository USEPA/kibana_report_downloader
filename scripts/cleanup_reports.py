

print("Starting cleanup of Kibana reports ...")

## cleanup of CAMPD - Staging STG Checks

print("Starting cleanup of CAMPD - Staging STG Checks")
with open('./.data/CAMPD - Staging STG Checks.csv', 'r') as input:
    lines = input.readlines()

with open('./.data/final-CAMPD-Staging-STG-Checks.csv', 'w') as output:
    for line in lines:
        if 'campd-ui' in line:
            output.write(line)
            

print("Finished creating final-CAMPD-Staging-STG-Checks.csv")
print("Completed clean up of CAMPD - Staging STG Checks ...")


print("Completed cleanup of Kibana reports ...")
