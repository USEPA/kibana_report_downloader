

print("Starting cleanup of Kibana reports ...")

## Cleanup of CAMPD - Prod APP ERROR Checks

print("Starting Cleanup of CAMPD - Prod APP ERROR Checks")
with open('./.data/CAMPD - Prod APP ERROR Checks.csv', 'r') as input:
    lines = input.readlines()

with open('./.data/final-CAMPD-Prod-APP-ERROR-Checks.csv', 'w') as output:
    for line in lines:
        if '@timestamp' in line or 'campd-ui' in line or 'emissions-api' in line or 'facilities-api' in line or 'accounts-api' in line or 'mdm-api' in line or 'ssh-tunnel' in line:
            output.write(line)

print("Finished creating final-CAMPD-Prod-APP-ERROR-Checks.csv")
print("Completed clean up of CAMPD - Prod APP ERROR Checks...")

## Cleanup of CAMPD - Prod CELL DESTROYED Audit

print("Starting Cleanup of CAMPD - Prod CELL DESTROYED Audit")
with open('./.data/CAMPD - Prod CELL DESTROYED Audit.csv', 'r') as input:
    lines = input.readlines()

with open('./.data/final-CAMPD-Prod-CELL-DESTROYED-Audit.csv', 'w') as output:
    for line in lines:
        if '@timestamp' in line or 'campd-ui' in line or 'emissions-api' in line or 'facilities-api' in line or 'accounts-api' in line or 'mdm-api' in line or 'ssh-tunnel' in line:
            output.write(line)

print("Finished creating final-CAMPD-Prod-CELL-DESTROYED-Audit.csv")
print("Completed clean up of CAMPD - Prod CELL DESTROYED Audit...")


## Cleanup of CAMPD - Staging STG Checks

print("Starting cleanup of CAMPD - Staging STG Checks")
with open('./.data/CAMPD - Staging STG Checks.csv', 'r') as input:
    lines = input.readlines()

with open('./.data/final-CAMPD-Staging-STG-Checks.csv', 'w') as output:
    for line in lines:
        if '@timestamp' in line or 'campd-ui' in line or 'emissions-api' in line or 'facilities-api' in line or 'accounts-api' in line or 'mdm-api' in line or 'ssh-tunnel' in line:
            output.write(line)
            

print("Finished creating final-CAMPD-Staging-STG-Checks.csv")
print("Completed clean up of CAMPD - Staging STG Checks ...")

## Cleanup of CAMPD - Prod RTR Checks (4xx, 5xx)

print("Starting cleanup of CAMPD - Prod RTR Checks (4xx, 5xx)")
with open('./.data/CAMPD - Prod RTR Checks.csv', 'r') as input:
    lines = input.readlines()

with open('./.data/final-CAMPD-Prod-RTR-Checks.csv', 'w') as output:
    for line in lines:
        if '@timestamp' in line or 'campd-ui' in line or 'emissions-api' in line or 'facilities-api' in line or 'accounts-api' in line or 'mdm-api' in line or 'ssh-tunnel' in line:
            output.write(line)
            

print("Finished creating final-CAMPD-Prod-RTR-Checks.csv")
print("Completed clean up of CAMPD - Prod RTR Checks (4xx, 5xx)...")


print("Completed cleanup of Kibana reports ...")
