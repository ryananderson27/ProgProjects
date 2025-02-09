# Project Design Document

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
- [2. Software Design](#2-software-design)
    - [2.1 Database Model](#21-model)
    - [2.2 Modules and Interfaces](#22-modules-and-interfaces)
    - [2.2.1 Overview](#221-overview)
    - [2.2.2 Interfaces](#222-interfaces)
    - [2.3 User Interface Design](#23-view-and-user-interface-design)
- [3. References](#3-references)
<!-- - [Appendix: Grading Rubric](#appendix-grading-rubric) -->

<a name="revision-history"> </a>

### Document Revision History

| Name | Date | Changes | Version |
| ------ | ------ | --------- | --------- |
|Revision 1 |2024-11-15 |Initial draft | 1.0        |
|      |      |         |         |


# 1. Introduction

<!-- Explain the purpose of this document. If this is a revision of an earlier document, please make sure to summarize what changes have been made during the revision (keep this discussion brief).  -->

This document serves to overview the structure and design of our team's software.

# 2. Software Design

<!-- (**Note**: For all subsections of Section-2: You should describe the design for the end product (completed application) - not only your iteration1 version. You will revise this document and add more details later.) -->

## 2.1 Database Model

<!-- Provide a list of your tables (i.e., SQL Alchemy classes) in your database model and briefly explain the role of each table.  -->

<!-- Provide a UML diagram of your database model showing the associations and relationships among tables.  -->

## 2.2 Modules and Interfaces

### 2.2.1 Overview

<!-- Describe the high-level architecture of your software:  i.e., the major components/modules and how they fit together. Provide a UML component diagram that illustrates the architecture of your software. Briefly mention the role of each module in your architectural design. Please refer to the "System Level Design" lectures in Week 4.  -->

### 2.2.2 Interfaces

<!-- Include a detailed description of the routes your application will implement. 
* Brainstorm with your team members and identify all routes you need to implement for the **completed** application.
* For each route specify its “methods”, “URL path”, and “a description of the operation it implements”.  
* You can use the following table template to list your route specifications. 
* Organize this section according to your module decomposition, i.e., include a sub-section for each module and list all routes for that sub-section in a table.   -->

#### 2.2.2.1 /main Routes

|   | Function           | URL Path   | Methods  | Description  |
|:--|:------------------|:-----------|:-------------| :-------------|
|1. |index|/,/index|GET| Renders home page dependant on current user type, requires login, redirects to login if no user is signed in.
|2. |displayProfile|/user/\<user-id\>|GET|Renders the correct profile template based on the current users type and populates it with current user info. Redirects to index if user not signed in.|
|3. |updateUser|/user/\<user-id\>/edit|GET, POST| Renders user profile edit template and parses edit profile form to update account, redirects to profile.
|4. |createTopic|/topic/create|GET, POST|Renders topic (research field or programming language) creation form/template, adds new topic to the database. Requires current user to be faculty, redirects to index if not.|
|5. |createProject|/project/create|GET, POST|Renders project creation form/template, adds new project to the database. Requires current user to be faculty, redirects to index if not.|
|6. |editProject|/project/\<project-id\>/edit|GET, POST|Renders project edit form/template, edits project details in database. Requires current user to be faculty, redirects to index if not.|
|7. |displayProjects|/project/view|GET|Renders project browser template, displays all projects in database. Requires login, redirects to index.|

#### 2.2.2.2 /auth Routes

|   | Function           | URL Path   | Methods  | Description  |
|:--|:------------------|:-----------|:-------------| :-------------|
|1. |registerUser|/user/register| GET, POST | Renders user registration template and parses registration form to make new users, redirects to index.|
|2. |login|/user/login|GET, POST| Renders login template with the login form and parses data to authenticate the user, redirects to index.|
|3. |logout|/user/logout|POST|Logs the current user out, redirects to login.|
|4. |                   |            |              |
|5. |                   |            |              |
|6. |                   |            |              |


#### 2.2.2.2 /errors Routes

|   | Function           | URL Path   | Methods  | Description  |
|:--|:------------------|:-----------|:-------------|:-------------|
|1. |not_found_error|/error/404|GET| Handles invalid route errors|
|2. |internal_error|/error/500|GET|Handles internal/server errors.|

### 2.3 User Interface Design 

<!-- Provide a list of the page templates you plan to create and supplement your description with UI sketches or screenshots.  -->

  ## Mock Up Pages
  <kbd>
    Image of login template
    <img src="images/Login.jpg"></img>
    Image of home template
    <img src="images/Home.jpg"></img>
    Image of home page with user dashboard dropdown template 
    <img src="images/Home_Dropdown.jpg"></img>
    Image of user profile template
    <img src="images/Profile.png"></img>
    Image of edit user profile template
    <img src="images/Edit_Profile.png"></img>
    Image of user inbox template
    <img src="images/Inbox.jpg"></img>
    Image of project submission template
    <img src="images/Submissions.png"></img>
    Image of project browser 
    <img src="images/Browser.jpg"></img>
    Image of project search template 
    <img src="images/Search.png"></img>
    Image of individual project research page
    <img src="images/Project_Page.png"></img>
    Image of project proposal page
    <img src="images/Project_Proposal.jpg"></img>
    
  </kbd>

# 3. References

None

<!-- Cite your references here.

For the papers you cite give the authors, the title of the article, the journal name, journal volume number, date of publication and inclusive page numbers. Giving only the URL for the journal is not appropriate.

For the websites, give the title, author (if applicable) and the website URL. -->

----
<!-- # Appendix: Grading Rubric
(Please remove this part in your final submission)

 * You will first  submit a draft version of this document:
    * "Project 3 : Project Design Document - draft" (5pts). 
* We will provide feedback on your document and you will revise and update it.
    * "Project 5 : Project Design Document - final" (80pts) 

Below is the grading rubric that we will use to evaluate the final version of your document. 

|**MaxPoints**| **Design** |
|:---------:|:-------------------------------------------------------------------------|
|           | Are all parts of the document in agreement with the product requirements? |
| 8         | Is the architecture of the system ([2.2.1 Overview](#221-overview)) described well, with the major components and their interfaces?         
| 8        | Is the database model (i.e., [2.1 Database Model](#21-database-model)) explained well with sufficient detail? Do the team clearly explain the purpose of each table included in the model?| 
|          | Is the document making good use of semi-formal notation (i.e., UML diagrams)? Does the document provide a clear UML class diagram visualizing the DB model of the system? |
| 18        | Is the UML class diagram complete? Does it include all classes (tables) and does it clearly mark the PK and FKs for each table? Does it clearly show the associations between them? Are the multiplicities of the associations shown correctly? ([2.1 Database Model](#21-database-model)) |
| 25        | Are all major interfaces (i.e., the routes) listed? Are the routes explained in sufficient detail? ([2.2.2 Interfaces](#222-interfaces)) |
| 13        | Is the view and the user interfaces explained well? Did the team provide the screenshots of the interfaces they built so far.  ([2.3 User Interface Design](#23-user-interface-design)) |
|           | **Clarity** |
|           | Is the solution at a fairly consistent and appropriate level of detail? Is the solution clear enough to be turned over to an independent group for implementation and still be understood? |
| 5         | Is the document carefully written, without typos and grammatical errors?  |
| 3         | Is the document well formatted? (Make sure to check your document on GitHub. You will loose points if there are formatting issues in your document.  )  |
|           |  |
| 80         | **Total** |
|           |  | -->