# Kibana Report Downloader
A simple python script that allows the downloading of Kibana reports based on a configurable timeframe and output file size.

## Obtaining Kibana report definitions

You need to log into Kibana to generate a CSV Report link that will include a security token (uaa-auth) and report job (jobParams value). The security token (uaa-auth) will change upon each login session. Also, each report will have a different report job (jobParams value).

1.	Log in to Kibana (I’m using v 7.9.3)
2.	Click Discover
3.	Click Open
4.	Find your report and open it
5.	Click Share, CSV Reports, “Copy POST URL,” which will include the jobParams value.
6.	Save each report job definition (jobParams value) in the run.json file

## Script execution steps
The prerequisite to this section is Obtaining Kibana report definitions.

 1. Clone this repository.
 2. pip install requirements.txt (i.e., pip install -r requirements.txt)
 3. *Suggested step* Create another git repository to store your custom Kibana report definitions.
 4.  Cache your Kibana report definitions in the run.json file in the reports folder. See the [sample .json](/docs/sample_report.json) file format.
 5. Obtain an active Kibana security token (right now this means the value of uaa-auth).
 6. Run the Kibana report downloader script.

## Usage Example (against Kibana running in cloud.gov)

**Updated Example:**
python kibana_report_downloader.py --auth=*put value of uaa-auth here*

 - **auth** = The value of uaa-auth which provides access to Kibana from the script (*future* find another way to obtain authentication information)

**Original Example:** 

python kibana_report_downloader.py --del_wip=false --data_folder=.\data --report_file=.\\reports\\run.json --start_date=2021-12-01T00:00:00.000Z --end_date=2021-12-31T23:59:59.999Z --kibana_api=https://logs.fr.cloud.gov --auth=*put value of uaa-auth here*

 - **del_wip** = true/false flag to determine if the work-in-progress folder should be deleted after report concatenation. It can be useful to keep if you want to debug the processing results.
 - **data_folder** = folder path to where the downloaded report(s) should be saved. 
 - **report_file** = file path to the .json file storing the Kibana report definitions to execute (1 or more).
 - **start_date** = The start date that will be injected into report requests.
 - **end_date** = The end date that will be injected into report requests.
 - **kibana_api** = The endpoint to use to download reports (*future* sniff this value out of report URLs)
 - **auth** = The value of uaa-auth which provides access to Kibana from the script (*future* find another way to obtain authentication information)

## Disclaimer

The United States Environmental Protection Agency (EPA) GitHub project code is provided on an "as is" basis and the user assumes responsibility for its use. EPA has relinquished control of the information and no longer has responsibility to protect the integrity, confidentiality, or availability of the information. Any reference to specific commercial products, processes, or services by service mark, trademark, manufacturer, or otherwise, does not constitute or imply their endorsement, recommendation or favoring by EPA. The EPA seal and logo shall not be used in any manner to imply endorsement of any commercial product or activity by EPA or the United States Government.
