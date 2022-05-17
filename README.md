# Kibana Report Downloader
A simple python script that allows the downloading of Kibana reports based on a configurable timeframe and output file size.

## Obtaining Kibana report definitions

You need to log into Kibana to generate a CSV Report link that will include a security token (uaa-auth) and report job (jobParams value). The security token (uaa-auth) will change upon each login session. Also, each report will have a different report job (jobParams value).

1.	Log in to Kibana (I’m using v 7.9.3)
2.	Click Discover
3.	Click Open
4.	Find your report and open it
5.	Click Share, CSV Reports, “Copy POST URL,” which will include the jobParams value.
6.	Save each report job definition (jobParams value) in it's own  run-#.json file

## Script execution steps
The prerequisite to this section is Obtaining Kibana report definitions.

 1. Clone this repository.
 2. pip install requirements.txt (i.e., pip install -r requirements.txt)
 3. *Suggested step* Create another git repository to store your custom Kibana report definitions.
 4.  Cache your Kibana report definitions in the run-#.json file in the reports folder. See the [sample .json](/docs/sample_report.json) file format.
 5. Insert an active Kibana security token (right now this means the value of uaa-auth) into the [bash script](./scripts/run).
 6. Reuse and modify the SAMPLE RUN REPORT COMMANDS for as many reports as you need in the [bash script](./scripts/run). 
 7. Modify the [kibana_report_download script](./kibana_report_downloader.py) startDateGBL and endDateGBL to meed your download needs. 
        *IMPORTANT - If you're comparing the kibana report results with the online Kibana reports, you need to adjust the online Kibana report filter depending on daylight or standard time. For example, there is a 4-hour adjustment during daylight savings time, meaning the online Kibana report filter of 2022-05-04 @00:00:00.000Z ->  2022-05-12 @00:00:00.000Z would result in a kibana script adjust with a the start time: 2022-05-04 @04:00:00.000Z and an end time: 2022-05-12 @04:00:00.000Z. Standard time to UTC has a 5-hour adjustment.*
 8. Run the bash script to run Kibana report downloader script.

    ```
    bash run
    ```

## Disclaimer

The United States Environmental Protection Agency (EPA) GitHub project code is provided on an "as is" basis and the user assumes responsibility for its use. EPA has relinquished control of the information and no longer has responsibility to protect the integrity, confidentiality, or availability of the information. Any reference to specific commercial products, processes, or services by service mark, trademark, manufacturer, or otherwise, does not constitute or imply their endorsement, recommendation or favoring by EPA. The EPA seal and logo shall not be used in any manner to imply endorsement of any commercial product or activity by EPA or the United States Government.
