# ParaBank QA Testing

## Project Overview

This project is a complete QA testing suite for the ParaBank Demo Banking Application.

The project covers manual testing, functional testing, UI testing, responsive testing, browser compatibility testing, validation testing, bug reporting, Jira bug tracking, and Playwright automation.

## Application Under Test

ParaBank Demo Banking Application

## Testing Types

- Functional Testing
- UI Testing
- Validation Testing
- Responsive Testing
- Browser Compatibility Testing
- Automated Testing

## Test Environment

- Browser: Google Chrome
- Browser: Microsoft Edge
- Responsive Viewport: 375 × 667
- Operating System: Windows
- Automation: Python + Pytest + Playwright

## Manual Testing

A total of 15 manual test cases were executed.

### Test Results

- Total Test Cases: 15
- Passed: 12
- Failed: 3
- Bugs Identified: 3

## Failed Test Cases

The following test cases failed during testing:

- TC-04: Invalid Zip Code Validation
- TC-05: Invalid Phone Number Validation
- TC-06: Invalid SSN Validation

## Bug Reports

Three bugs were identified and documented:

- BUG-01: Invalid Zip Code is accepted during registration
- BUG-02: Invalid Phone Number is accepted during registration
- BUG-03: Invalid SSN is accepted during registration

The bugs were also added to Jira for tracking.

## Automation Testing

Three test cases were automated using Playwright with Python and Pytest.

### Automated Test Cases

- TC-07: Valid Login
- TC-08: Invalid Login
- TC-14: Logout

### Automation Result

- Automated Tests: 3
- Passed: 3
- Failed: 0

All three automated test cases passed successfully.

## Automation Tool

Playwright was used to automate browser interactions and verify application behavior.

The automation script is located in:

`automation/test_login.py`

## Project Structure

```text
ParaBank-QA-Testing/
│
├── automation/
│   └── test_login.py
│
├── Automation_Screenshots/
│   ├── TC-07_Playwright_Valid_Login.png
│   ├── TC-08_Playwright_Invalid_Login.png
│   └── TC-14_Playwright_Logout.png
│
└── README.md
## Tools Used

- Google Sheets
- Jira
- Python
- Pytest
- Playwright
- Visual Studio Code
- Google Chrome
- Microsoft Edge
## Conclusion

The ParaBank Demo Banking Application was tested using multiple QA testing techniques.

A total of 15 manual test cases were executed, with 12 test cases passed and 3 test cases failed. Three defects were identified and documented with screenshots, and the bugs were also added to Jira for tracking.

Three test cases were successfully automated using Playwright with Python and Pytest. All three automated tests passed successfully.

This project demonstrates practical experience in manual testing, test case documentation, defect reporting, Jira bug tracking, responsive and browser compatibility testing, and browser automation.