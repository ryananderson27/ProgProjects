# Software Requirements and Use Cases

## Your Project Title
--------
Prepared by:

* `Brandon Proteau`,`WPI`
* `Matthew Amodea`,`WPI`
* `Chase Carstensen`,`WPI`
* `Ryan Anderson`,`WPI`

---

**Course** : CS 3733 - Software Engineering

**Instructor**: Sakire Arslan Ay

---

## Table of Contents
- [1. Introduction](#1-introduction)
- [2. Requirements Specification](#2-requirements-specification)
  - [2.1 Customer, Users, and Stakeholders](#21-customer-users-and-stakeholders)
  - [2.2 User Stories](#22-user-stories)
  - [2.3 Use Cases](#23-use-cases)
- [3. User Interface](#3-user-interface)
- [4. Product Backlog](#4-product-backlog)
- [4. References](#4-references)
- [Appendix: Grading Rubric](#appendix-grading-rubric)

<a name="revision-history"> </a>

## Document Revision History

| Name | Date | Changes | Version |
| ------ | ------ | --------- | --------- |
|Revision 1 |2024-11-07 |Initial draft | 1.0        |
|      |      |         |         |
|      |      |         |         |

----
# 1. Introduction

  A web service where WPI undergraduates and professors can connect for research opportunities. Professors propose research projects and students browse for projects relevant to their interests. Students can view project prerequisites and professors can view student qualifications. 

<!-- 
Provide a short description of the software being specified. Describe its purpose, including relevant benefits, objectives, and goals. -->

----
# 2. Requirements Specification

This section specifies the software product's requirements. Specify all of the software requirements to a level of detail sufficient to enable designers to design a software system to satisfy those requirements, and to enable testers to test that the software system satisfies those requirements.

## 2.1 Customer, Users, and Stakeholders

<!-- A brief description of the customer, stakeholders, and users of your software. -->

  This application will be used by WPI students looking to contribute to research projects and WPI professors requiring research assistance.

----
## 2.2 User Stories
<!-- This section will include the user stories you identified for your project. Make sure to write your user stories in the form : 
"As a **[Role]**, I want **[Feature]** so that **[Reason/Benefit]** " -->

| As a student, I would like to... | As a faculty member, I would like to... |
|---|---|
|Login/Register. | Login/Register. |
|View my account. | View my account. |
|Edit my account details so that I can add qualifying information into my account. | Edit my account details. |
|| List my research projects on my account so that students can find projects which I am associated with. |
|Browse open research projects so that I can find projects to apply to. | Create new research projects. |
|Sort/Filter the search results for research projects so that I can find projects more similar to my interests. | Add information to my research projects such as a description, research fields, and time commitment so that students can be more informed about my project. |
|View details of research projects so that I learn more about projects. | See students who have applied to research positions so that I may know their qualifications and if they are approved for other research positions. |
|Apply to open research projects. | Approve or reject students from positions I have posted. |
|Submit a personal statement with my applications. | View applications of students who have applied for my research positions so that I can learn more about them. |
|Request letters of recommendation from faculty members so that I can have references for applications. | View references for students. |
|View the status of my completed applications. | View the status of my research projects. |
|Check my inbox so that I know if a faculty member has submitted recommendations for me. | View my inbox so that I can know if a student needs a recommendation from me. |
|Send a reminder to faculty members about reference requests. |View reminders for reference requests so I don't forget any. |
|Check my inbox so that I can view acceptance and rejection letters. | Accept or reject a student's request to me to recommend them. |
|Withdraw pending applications so that I may discontinue my application process for a research position. | Optionally write a recommendation letter so that I may speak on a student's qualifications. |


----
## 2.3 Use Cases

This section will include the specification for your project in the form of use cases. 

Group the related user stories and provide a use case for each user story group. You don't need to draw the use-case diagram for the use cases; you will only provide the textual descriptions.  **Also, you don't need to include the use cases for "registration" and "login" use cases for both student and faculty users.**

  * First, provide a short description of the actors involved (e.g., regular user, administrator, etc.) and then follow with a list of the use cases.
  * Then, for each use case, include the following:

    * Name,
    * Participating actors,
    * Entry condition(s) (in what system state is this use case applicable),
    * Exit condition(s) (what is the system state after the use case is done),
    * Flow of events (how will the user interact with the system; list the user actions and the system responses to those),
    * Alternative flow of events (what are the exceptional cases in the flow of events and they will be handles)
    * Iteration # (which sprint do you plan to work on this use case) 

Each use case should also have a field called "Iteration" where you specify in which iteration you plan to implement this feature.

You may use the following table template for your use cases. Copy-paste this table for each use case you will include in your document.

| Use case # 1      |   |
| ------------------ |--|
| Name              | Account Creation |
| Participating actor  | Student  |
| Entry condition(s)     | User has to be a currently enrolled WPI Student  |
| Exit condition(s)           | User will receive their customized student account along with the inputted profile information  |
| Flow of events | 1. The user enters their account username and password.<br>2. The user enters their contact information, including name, last name, WPI ID, email, and phone number.<br>3. The user enters additional information, such as their major, cumulative GPA, expected graduation date, etc.<br>4. The user selects the research topics they are interested in (e.g., “Machine Learning,” “High Performance Computing,” etc.).<br>5. System responds with a list of research fields.<br>6. User selects one or multiple fields from the given list.<br>7. The user selects the programming languages they are familiar with.<br>8. System responds with a list of programming languages.<br>9. User selects one or multiple languages from the given list.<br>10. User submits the account information.<br>11. System validates given account information.<br>12. If the inputted information is valid, the system adds the user’s new account to the database. |
| Alternative flow of events    | In step 10, if the system doesn’t validate the user's information due to unfilled account information or incorrect details, the system prompts the user to correct the fields. |
| Iteration # | 1  |

---

| Use case # 2      |   |
| ------------------ |--|
| Name              | View and Edit Account |
| Participating actor  | Student  |
| Entry condition(s)     | User has an account  |
| Exit condition(s)           | User’s account will be updated with valid inputted data  |
| Flow of events | 1. User clicks “View Profile” button.<br>2. System responds by displaying the student’s current profile information.<br>3. User clicks on “Edit Profile.”<br>4. System responds with a similar form seen in the registration process but with the user’s current data filled in, except password.<br>5. User makes changes and submits the account information.<br>6. System validates the given account information.<br>7. If inputted information is valid, the system updates the user’s account in the database. |
| Alternative flow of events    | In step 5, if the system doesn’t validate the user's information due to unfilled or incorrect fields, the system prompts the user to correct them. |
| Iteration # | 1  |

---

| Use case # 3      |   |
| ------------------ |--|
| Name              | Browse Research Positions |
| Participating actor  | Student  |
| Entry condition(s)     | User has an account  |
| Exit condition(s)           | User views a wide variety of available research projects  |
| Flow of events | 1. User searches for research projects by filtering through multiple criteria, such as:<br> &nbsp; a. Title<br> &nbsp; b. Start/End Date<br> &nbsp; c. Required Time Commitment<br> &nbsp; d. Related Research Fields<br> &nbsp; e. Required Programming Languages (Boolean)<br> &nbsp; f. Research Project Leader<br>2. System takes these inputs and displays relevant available research projects.<br>3. User selects a specific research project to view expanded details.<br>4. System displays the detailed view of the selected research project. |
| Alternative flow of events    | If the system does not validate the user’s search criteria due to missing or incorrect details, the system informs the user that no matching research projects exist. |
| Iteration # | 1  |

---

Assuming the user wants to apply to the position and that the student can exit at any time by canceling the application.

| Use case # 4      |   |
| ------------------ |--|
| Name              | Apply |
| Participating actor  | Student  |
| Entry condition(s)     | User has an account and is currently viewing an available research position  |
| Exit condition(s)           | User’s application for a given research project is submitted  |
| Flow of events | 1. User clicks the “Apply” button on a research project.<br>2. System prompts the user to:<br> &nbsp; a. Fill out a brief statement describing why they are interested in the research topic and what they hope to gain from participating.<br> &nbsp; b. Input the name and email of one faculty member who can provide a reference for the position.<br>3. User fills out the required information.<br>4. The system validates the information, sends a message to the faculty member for a recommendation, and updates the application status to pending. |
| Alternative flow of events    | In step 2, if the user submits an empty “Position Interest” field or enters a faculty member who doesn’t exist in the database, the system prompts the user to correct these fields. |
| Iteration # | 2  |

---

| Use case # 5      |   |
| ------------------ |--|
| Name              | View Application Status |
| Participating actor  | Student  |
| Entry condition(s)     | User has an account and has submitted an application to an available research position  |
| Exit condition(s)           | User’s application can either be accepted, denied, or rescinded by the user  |
| Flow of events | 1. User selects the “View Application Status” button in their profile.<br>2. System responds by displaying the applied research projects, including:<br> &nbsp; - Title<br> &nbsp; - Start/End Date<br> &nbsp; - Research Lead<br> &nbsp; - The research position applied for<br> &nbsp; - The status of their application<br> &nbsp; - The recommendation status from their requested faculty member. |
| Alternative flow of events    | In step 2, if the application is still pending, the user has the option to withdraw the application from the given research project. |
| Iteration # | 2  |

---

| Use case # 6      |   |
| ------------------ |--|
| Name              | View Reference Request Status |
| Participating actor  | Student  |
| Entry condition(s)     | A student has already provided the name and email of a faculty member who can provide them the reference  |
| Exit condition(s)           | The student views the status of the reference.  |
| Flow of events | 1. The user views the application statuses page and selects References.<br>2. The software responds by presenting the name of each faculty member listed as a reference and the status of their reference as "Pending" or "Complete". |
| Alternative flow of events    |- In step 2, the user can select reference and remove them.<br>- In step 2, if a faculty member has rejected a reference request, it should appear as "Rejected."<br>- In step 2, if a reference appears as pending, the student may send a reminder to the faculty member. The student selects the "Send a Reminder" option. The software responds by asking for a message to send with the reminder. The student inputs a message and selects "Send." The software responds by confirming that the reminder was sent and notifying the faculty member. |
| Iteration # | 3  |

---

| Use case # 1F      |   |
| ------------------ |--|
| Name              | Create Research Listing |
| Participating actor  | Faculty  |
| Entry condition(s)     | User is a WPI faculty member with an existing research project that has unfilled position slots and is currently viewing their project page.  |
| Exit condition(s)           | Research project job specifications are posted according to faculty preferences.  |
| Flow of events | 1. User presses "Add Undergraduate Research Position".<br>2. System prompts the user to fill out the following fields:<br> &nbsp; a. Research project title<br> &nbsp; b. Brief description of project goals and objectives<br> &nbsp; c. Start and end date<br> &nbsp; d. Required time commitment (e.g., 10 hours per week)<br> &nbsp; e. Number of available positions for the given role<br> &nbsp; f. Research field<br> &nbsp; g. Required experience with programming languages (e.g., "C++", "Java", "Python").<br>3. User fills out the required fields and presses the "Submit" button.<br>4. System validates the input data and adds the job posting to the database. |
| Alternative flow of events    | In step 3, if the system doesn’t validate the user's information due to missing or incorrect details, the system prompts the user to correct the fields. |
| Iteration # | 1  |

---

| Use case # 2F      |   |
| ------------------ |--|
| Name              | View Applied Students |
| Participating actor  | Faculty  |
| Entry condition(s)     | User is a WPI faculty member with an account who has previously posted a research position and is currently viewing the research project page.  |
| Exit condition(s)           | User views all students who have applied for a given undergraduate research position.  |
| Flow of events | 1. User selects the "View Applicants" button.<br>2. System displays a list of applicants, including:<br> &nbsp; a. Name<br> &nbsp; b. Major<br> &nbsp; c. Graduation Year<br> &nbsp; d. WPI ID<br> 3. System allows the user to expand an applicant’s profile to view their full application. <br> 4. User selects filter and sorting preferences for applied students list. <br> 5. System responds by sorting the list of students who have applied based on specifications of the user.|
| Alternative flow of events    | If no one has applied for the position, the system displays a "No Applicants Yet" message. |
| Iteration # | 2  |

---

| Use case # 3F      |   |
| ------------------ |--|
| Name              | View Student Qualifications |
| Participating actor  | Faculty  |
| Entry condition(s)     | User clicked on the “View Profile” button of a student who has applied for their research position.  |
| Exit condition(s)           | User reviews the applicant’s qualifications.  |
| Flow of events | 1. System displays the applicant’s profile, including:<br> &nbsp; a. GPA<br> &nbsp; b. Research topics of interest<br> &nbsp; c. Programming language proficiency<br> &nbsp; d. Prior research experience<br> &nbsp; e. Faculty reference and whether the recommendation is approved<br> &nbsp; f. Student’s submitted statement of interest. |
| Alternative flow of events    | None specified. |
| Iteration # | 2  |

----

| Use case # 4F     |   |
| ------------------ |--|
| Name              | Accept / Reject Student Applicants |
| Participating actor  | Faculty  |
| Entry condition(s)     | User clicked on the “View Profile” button of a student who has applied for their research position.  |
| Exit condition(s)           | User exits the “View Profile” page of the student they are reviewing. |
| Flow of events | 1. System displays a green “accept” button and a red “reject” button on the profile page of a student who has applied for their research position. <br> 2. User can accept as many students as there are positions available under the research position. <br> 3. System will set the status on the student's application as either “Approved” or “Rejected”. |
| Alternative flow of events    | If the user attempts to accept more students than there are positions available, the user will be advised that all positions for the position are filled. |
| Iteration # | 2  |

---

| Use case # 5F      |   |
| ------------------ |--|
| Name              | Completing a Reference Request |
| Participating actor  | Faculty  |
| Entry condition(s)     | A student has entered the faculty member as a reference for their application. |
| Exit condition(s)           | The faculty member has completed the request for a reference. |
| Flow of events | 1. The user views the profile page and selects References.<br>2. The software responds by presenting the name of each student who has submitted a reference request to the user.<br>3. The user responds by selecting a student and accepting the reference request.<br>4. The software responds by prompting the user for a letter of recommendation.<br> 5. The user responds by inputting a letter of recommendation and submitting the reference.<br>6. The software responds by confirming that the request is complete and notifying the student that the reference has been received.<br>7. The software also removes the students name from the list of pending reference requests. |
| Alternative flow of events    |- In step 3, the user can reject the reference request. The software responds by confirming that the request is complete and notifying the student that the reference request has been rejected. The software also removes the students name from the list of pending reference requests.|
| Iteration # | 3  |

---

| Use case # 6F      |   |
| ------------------ |--|
| Name              | View and Edit Account |
| Participating actor  | Faculty  |
| Entry condition(s)     | User has an account  |
| Exit condition(s)           | User’s account will be updated with valid inputted data  |
| Flow of events | 1. User clicks “View Profile” button.<br>2. System responds by displaying the faculty’s current profile information.<br>3. User clicks on “Edit Profile.”<br>4. System responds with a similar form seen in the registration process but with the user’s current data filled in, except password.<br>5. User makes changes and submits the account information.<br>6. System validates the given account information.<br>7. If inputted information is valid, the system updates the user’s account in the database. |
| Alternative flow of events    | In step 5, if the system doesn’t validate the user's information due to unfilled or incorrect fields, the system prompts the user to correct them. |
| Iteration # | 1  |

---

| Use case # 7F      |   |
| ------------------ |--|
| Name              | Edit Research Listing |
| Participating actor  | Faculty  |
| Entry condition(s)     | User is a WPI faculty member with an existing research project and is currently viewing their project page.  |
| Exit condition(s)           | Updated research project specifications are posted according to faculty preferences.  |
| Flow of events | 1. User presses "Edit Research Project Listing".<br>2. System prompts the user to edit the following fields:<br> &nbsp; a. Research project title<br> &nbsp; b. Brief description of project goals and objectives<br> &nbsp; c. Start and end date<br> &nbsp; d. Required time commitment (e.g., 10 hours per week)<br> &nbsp; e. Number of available positions for the given role<br> &nbsp; f. Research field<br> &nbsp; g. Required experience with programming languages (e.g., "C++", "Java", "Python").<br>3. User fills out the desired fields and presses the "Submit" button.<br>4. System validates the input data and adds the job posting to the database. |
| Alternative flow of events    | In step 3, if the system doesn’t validate the user's information due to missing or incorrect details, the system prompts the user to correct the fields. |
| Iteration # | 1  |

---

# 3. User Interface

<!-- Here you should include the sketches or mockups for the main parts of the interface.
You may use Figma to design your interface: -->
  ## Mock Up Pages
  <kbd>
    <img src="images/Login.jpg"></img>
    <img src="images/Home.jpg"></img>
    <img src="images/Home_Dropdown.jpg"></img>
    <img src="images/Profile.png"></img>
    <img src="images/Edit_Profile.png"></img>
    <img src="images/Inbox.jpg"></img>
    <img src="images/Submissions.png"></img>
    <img src="images/Browser.jpg"></img>
    <img src="images/Search.png"></img>
    <img src="images/Project_Page.png"></img>
    <img src="images/Project_Proposal.jpg"></img>
    
  </kbd>
  
----
# 4. Product Backlog

[Product Backlog Link](https://github.com/WPI-CS3733-2025C/team-dominators/issues) 

----
# 5. References

Cite your references here.

For the papers you cite give the authors, the title of the article, the journal name, journal volume number, date of publication and inclusive page numbers. Giving only the URL for the journal is not appropriate.

For the websites, give the title, author (if applicable) and the website URL.

----
----
# Appendix: Grading Rubric
(Please remove this part in your final submission)

These is the grading rubric that we will use to evaluate your document. 

| Max Points  | **Content** |
| ----------- | ------- |
| 4          | Do the requirements clearly state the customers’ needs? |
| 2          | Do the requirements avoid specifying a design (note: customer-specified design elements are allowed)? |
| | |  
|    | **Completeness** |
| 14 | Are user stories complete? Are all major user stories included in the document?  |
| 5 | Are user stories written in correct form? | 
| 14 |  Are all major use cases (except registration and login) included in the document? |
| 15 | Are use cases written in sufficient detail to allow for design and planning? Are the "flow of events" in use case descriptions written in the form of "user actions and system responses to those"? Are alternate flow of events provided (when applicable)? | 
| 6 |  Are the User Interface Requirements given with some detail? Are there some sketches, mockups?  |
| | |  
|   | **Clarity** |
| 5 | Is the document carefully written, without typos and grammatical errors? <br> Is each part of the document in agreement with all other parts? <br> Are all items clear and not ambiguous? |
| | |
|**65**|**TOTAL**|


