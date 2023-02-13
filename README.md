# GVE DevNet Webex License Report 

This sample script creates a simple report about all users (email and name) within a Webex organization who have a certain set of licenses assigned. 
The script can only be executed by an admin of the Webex organization.

## Contacts
* Ramona Renner

## Solution Components
* Webex REST APIs
* Webex Control Hub (Webex admin access)

## Related Sandbox Environment

This sample code can be tested using a [Cisco Developer Sandbox](https://developer.webex.com/docs/developer-sandbox-guide) which provides you with administrator access to a licensed Webex organization manageable via Webex Control Hub. A licensed org lets you create and test capabilities of the Webex platform not available with Webex free plans.

## Prerequisites
**Webex API Personal Token**:

To use the Webex REST API, you need a Webex admin account backed by Cisco Webex Common Identity (CI). 
1. Login at https://developer.webex.com with a Webex admin account.
2. Obtain an access token as described [here](https://developer.webex.com/docs/getting-started). When making a request to the Webex REST API, the request must contain a header that includes the access token. 

> Note: This token has a short lifetime - only 12 hours after logging into this site - so it shouldn't be used outside of app development.


## Installation/Configuration

3. Make sure you have [Python 3.8.10](https://www.python.org/downloads/) and [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) installed.

4. (Optional) Create and activate a virtual environment for the project ([Instructions](https://docs.python.org/3/tutorial/venv.html))   

5. Access the created virtual environment folder
    ```
    cd [add name of virtual environment here] 
    ```

6. Clone this GitHub repository into the local folder:  
    ```
    git clone [add GitHub link here]
    ```
    * For GitHub link: 
      In GitHub, click on the **Clone or download** button in the upper part of the page > click the **copy icon**  
      ![/IMAGES/giturl.png](/IMAGES/giturl.png)
  * Or simply download the repository as zip file using 'Download ZIP' button and extract it

7. Access the downloaded folder:  
    ```
    cd gve_devnet_webex_license_report
    ```

8. Install all dependencies:
    ```
    pip3 install -r requirements.txt
    ```

9. Fill in your variables in the .env file. 

  ```python
    ADMIN_TOKEN=<Add the token from step 2 here>
    LICENSE_NAME_LIST=<Add a list of license names to check for, e.g. ["Meeting 25 party"]>
  ```

> Note: Mac OS hides the .env file in the finder by default. View the demo folder for example with your preferred IDE to make the file visible.

> Note: The interactive documentation can be a great help in identifying the actual name of the license. Use the [List People](https://developer.webex.com/docs/api/v1/people/list-people) call with a specific email parameter to retrieve the licenses assigned to a user. Execute and compare the result, after adding and removing the desired license to a user in Control Hub. By doing so, you can find out which license ID in the response correlates to the license in Control Hub. Use the [Get License Details](https://developer.webex.com/docs/api/v1/licenses/get-license-details) call to retrieve further information about a license based on its ID, e.g. the license name.

> Note: Assigned licenses can be viewed and adapted in [Webex Control Hub](https://admin.webex.com/) under **Users** > Click **Name of User** > **Section: Licenses** > Click: **Edit Licenses**.

## Usage

10. Run the script:   

```python3 report.py```


# Screenshots

![/IMAGES/screenshot.png](/IMAGES/screenshot.png)


## LICENSE
Provided under Cisco Sample Code License, for details see [LICENSE](LICENSE.md)

## CODE_OF_CONDUCT
Our code of conduct is available [here](CODE_OF_CONDUCT.md)

## CONTRIBUTING
See our contributing guidelines [here](CONTRIBUTING.md)

#### DISCLAIMER:
<b>Please note:</b> This script is meant for demo purposes only. All tools/ scripts in this repo are released for use "AS IS" without       any warranties of any kind, including, but not limited to their installation, use, or performance. Any use of these scripts and tools       is at your own risk. There is no guarantee that they have been through thorough testing in a comparable environment and we are not          responsible for any damage or data loss incurred with their use.
You are responsible for reviewing and testing any scripts you run thoroughly before use in any non-testing environment.
