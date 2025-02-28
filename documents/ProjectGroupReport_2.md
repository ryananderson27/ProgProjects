# Project Group Report - 2

## Team: `Team DOMinators`

List team members and their GitHub usernames

* `Brandon Proteau`,`bproteau1`
* `<member2>`,`<username2>`
* `<member3>`,`<username3>`
* `<Ryan Anderson>`,`<ryananderson27>`

---
**Course** : CS 3733 - Software Engineering

**Instructor**: Sakire Arslan Ay

----
## 1. Iteration 2 - Summary

 <!-- * Include a summary of your `Iteration-2` accomplishments. 
 * List the user stories completed in `Iteration-2`. Mention who worked on those user stories. -->
  
  Last iteration, we found that the scale of our assigned tasks were too great in scope, causing features to be occasionally missed and forgotten. To remedy this issue, we attempted to create 'atomically sized' tasks, which not only were crystal clear what they entailed, but also had no more than exactly one feature each. 
  
  This could be assigning someone the task of creating a single new template, or the task of making a new relationship between existing models.
  This new style of task-writing worked well with our team for both assigning and distributing work and for assisting in ensuring every major use case gets covered. 

  The following are our user stories for this past iteration and our associated tasks, with who they were assigned to.
  
 |#|User Story|
 |-|-|
 |9|As a student, I would like to apply to open research projects.|
 |11|As a student, I would like to submit a personal statement with my applications.|
 |16|As a student, I would like to view the status of my completed applications.|
 |18|As a faculty member, I would like to see students who have applied to research positions so that I may know their qualifications and if they are approved for other research positions.|
 |20|As a faculty member, I would like to approve or reject students from positions I have posted.|
 |21|As a faculty member, I would like to view applications of students who have applied for my research positions so that I can learn more about them.|
 |24|As a faculty member, I would like to view the status of my research projects.|
 |27|As a student, I would like to withdraw pending applications so that I may discontinue my application process for a research position.|
 |82|As a faculty member, I would like to view the list of applied applicants.|
 |83|As a faculty member, I would like to view the list of applicants and see their application status, whether I accepted or rejected them, or if their application is still pending.|
 |84|As a faculty member, I would like to view any given personal statement that the student has submitted when they applied for my research project.|
 |85|As a faculty member, I would like to view the responses and information they gave when they filled out the application to my research project.|
 |86|As a faculty member, I would like to have easy viewing access to the applied student’s profile while reviewing their personal statement and their application responses.|
 |87|As a faculty member, I would like to view the number of students that I have already accepted into my research project.|


 |#|Task|User Story #|Assignee|
 |-|-|-|-|
 |62|Create 'apply' button on research project template and on _project template|#9|Brandon|
 |63|Add "Withdrawl" Button to the existing research_project.html template|#27|Matt, Chase|
 |64|Create 'apply' template for applying to projects|#11, 9|Brandon|
 |65|Add "Withdrawl" button route to existing main.routes.py|#27|Chase|
 |66|Add "Widthdrawl" object to existing main.forms|27|Matt|
 |67|Create 'ProjectApplication' form with fields corresponding to necessary information for applying to a research position|9,11|Brandon|
 |68|Update research_project.html to display the current group count, number of applicants, and their pending status, visible only to the project's faculty creator|82,87|Matt|
 |69|Create /project/<project_id>/apply route for applying to projects|9|Chase|
 |71|In the 'ProjectApplication' form, create text field 'statement' for users to write a personal statement regarding their interest|11,9|Brandon|
 |73|For student users, research_project template should include the status of the student's application(s)|16|Chase|
 |75|In research project template, loop over and list students who have applied to the project|82,83|Matt|
 |77|Create application template for faculty which displays information from a student's application|86,21|Matt|
 |79|Create 'project/<project_id>/application/<user_id>' route for 'application' template|86,11,9,84,21|Chase|
 |80|Create many -> one association between Students to ResearchProjects for applied students|87,82|Chase|
 |81|Create faculty index page, 'faculty_index'||Brandon|
 |90|Create Application model which has a one to one relationship with students and a one to one association with research projects||Chase|
 |91|Create a page (or a popup) that displays the personal statement of an applied student, only viewable by faculty and applied student|84,86,21|Ryan|
 |92|Add a List to each students profiles that displays the projects they were accepted too|18,87,84|Ryan|
 |93|Add an option to the list of students shown on the project page to either 'Accept' or 'Reject' any given in student in the list|20,87|Matt|
 |94|Edit create project form/template to include a text area field for a project description||Brandon|
 |95|Edit research_project template to display project description|94|Brandon|
 |96|Rework edit project form to add a text area field to edit the project description. Edit the edit_project template to render this field|94,95|Brandon|
 |97|Add links to each application a student has applied to on Student Index page||Brandon|


----
## 2. Iteration 2 - Sprint Retrospective

During this iteration, our team demonstrated strong collaboration and communication. Our Scrum meetings were productive, timely, and consistent, occurring at least four times a week. However, there were areas that needed improvement. One major challenge was task management, as individuals were creating their own tasks rather than assigning them collectively during Scrum meetings. Additionally, branch management was inconsistent, and we encountered issues where there wasn’t always a stable working branch. Another area for improvement was testing, as there were instances where team members didn’t always thoroughly test their own code before merging. 

Moving forward into Iteration 3, we are implementing several changes to address these issues. We will create and assign tasks as a team during Scrum meetings rather than individually. To improve branch management, we will communicate more consistently and ensure that there is always a stable working branch. We will also rigorously test our own code before merging it, preventing issues from propagating. Finally, we will start working on Iteration 3 immediately to maintain momentum and avoid unnecessary delays. By making these adjustments, we aim to enhance our efficiency and overall project workflow.

----
## 3. Product Backlog refinement

 * Have you made any changes to your `product backlog` after `Iteration-2`? If so, please explain the changes here. 

----
## 4. Iteration 3 - Sprint Backlog

Include a draft of your `Iteration-3 sprint backlog`. 
 * List the user stories you plan to complete in `Iteration-3`. Make sure to break down the larger user stories into smaller size stories. Mention the team member(s) who will work on each user story. 
 * Make sure to update the "issues" on your GitHub repo accordingly.  

| #  | User Story | Assignee |
|----|-----------|----------|
| 30 | As a faculty member, I would like to view reminders for reference requests so I don't forget any. | Ryan |
| 29 | As a faculty member, I would like to optionally write a recommendation letter so that I may speak on a student's qualifications. | Matt |
| 28 | As a faculty member, I would like to accept or reject a student's request for me to recommend them. | Matt |
| 26 | As a faculty member, I would like to view my inbox so that I can know if a student needs a recommendation from me.  | Chase |
| 25 | As a student, I would like to check my inbox so I can view acceptance and rejection letters. | Chase |
| 23 | As a student, I would like to send a reminder to faculty members about reference requests.  | Ryan |
| 22 | As a faculty member, I would like to view references for students.  | Ryan |
| 19 | As a student, I would like to check my inbox so that I know if a faculty member has submitted recommendations for me. | Brandon |
| 13 | As a student, I would like to request letters of recommendation from faculty members so that I can have references for applications. | Brandon |
| 100 | As a faculty, I would like to sort through my inbox to look for specific recommendation request be it by person, major, or graduating class | Brandon |
