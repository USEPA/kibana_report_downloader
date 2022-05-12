import sys

print("Starting cleanup of Kibana reports ...")

## Cleanup of CAMPD - Prod APP ERROR Checks

if sys.argv[1] == '.\reports\run-1.json':
    print("Starting Cleanup of CAMPD - Prod APP ERROR Checks")
    with open('./.data/CAMPD - Prod APP ERROR Checks.csv', 'r') as input:
        lines = input.readlines()

    with open('./.data/final-CAMPD-Prod-APP-ERROR-Checks.csv', 'w') as output:
        for line in lines:
                output.write(line)

    print("Finished creating final-CAMPD-Prod-APP-ERROR-Checks.csv")
    print("Completed clean up of CAMPD - Prod APP ERROR Checks...")

## Cleanup of CAMPD - Prod CELL DESTROYED Audit

if sys.argv[1] == '.\reports\run-2.json':
    print("Starting Cleanup of CAMPD - Prod CELL DESTROYED Audit")
    with open('./.data/CAMPD - Prod CELL DESTROYED Audit.csv', 'r') as input:
        lines = input.readlines()

    with open('./.data/final-CAMPD-Prod-CELL-DESTROYED-Audit.csv', 'w') as output:
        for line in lines:
                output.write(line)

    print("Finished creating final-CAMPD-Prod-CELL-DESTROYED-Audit.csv")
    print("Completed clean up of CAMPD - Prod CELL DESTROYED Audit...")


## Cleanup of CAMPD - Staging STG Checks
if sys.argv[1] == '.\reports\run-3.json':
    print("Starting cleanup of CAMPD - Staging STG Checks")
    with open('./.data/CAMPD - Staging STG Checks.csv', 'r') as input:
        lines = input.readlines()

    with open('./.data/final-CAMPD-Staging-STG-Checks.csv', 'w') as output:
        for line in lines:
                output.write(line)
                

    print("Finished creating final-CAMPD-Staging-STG-Checks.csv")
    print("Completed clean up of CAMPD - Staging STG Checks ...")

## Cleanup of CAMPD - Prod RTR Checks (4xx, 5xx)

if sys.argv[1] == '.\reports\run-4.json':
    print("Starting cleanup of CAMPD - Prod RTR Checks (4xx, 5xx)")
    with open('./.data/CAMPD - Prod RTR Checks.csv', 'r') as input:
        lines = input.readlines()

    with open('./.data/final-CAMPD-Prod-RTR-Checks.csv', 'w') as output:
        for line in lines:
                output.write(line)
                

    print("Finished creating final-CAMPD-Prod-RTR-Checks.csv")
    print("Completed clean up of CAMPD - Prod RTR Checks (4xx, 5xx)...")


print("Completed cleanup of Kibana reports ...")
