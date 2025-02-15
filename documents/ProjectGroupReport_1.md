# Project Group Report - 1

## Team: `Team DOMinators`

List team members and their GitHub usernames

* `Brandon Proteau`,`bproteau0`
* `Matt Amodea`,`mattsamo66`
* `Chase Carstensen`,`chase12803`
* `Ryan Anderson`,`ryananderson27`

---
**Course** : CS 3733 - Software Engineering

**Instructor**: Sakire Arslan Ay

----
## 1. Schedule

 <!-- * What is your team's weekly schedule of meetings outside of regular class times?  -->
 Our group has typically met ~4 times a week. We have averaged 2 weekly scrum meetings, one on Wednesday from 5-5:15, and the other during a flexible time, like during the weekend. Our scrum meetings have a speculative duration of 15 minutes, but discussion can occasionally last longer time permitting. Besides our scrum meetings, we run work meetings in which project work is done collaboratively. These meetings occur 2 or more times a week and in these, we work on items ranging from writing documents to assigning tasks to programming. Work meetings have no designated week day or time, but are decided at the beginning of each week based on the team's availability.

----
## 2. Iteration 1 - Summary

 <!-- * Include as summary of your `Iteration-1` accomplishments.  -->
 During this past iteration, our team was able to...
 <!-- * List the user stories completed in `Iteration-1`. Mention who worked on those user stories.  -->
 |#|User Story|
 |-|-|
 |38|As a faculty member I would like view my account.|
 |31|As a faculty member, I would like to register an account.|
 |17|As a faculty member, I would like to add information to my research projects such as a description, research fields, and time commitment so that students can be more informed about my project.|
 |15|As a faculty member, I would like to create new research projects.|
 |14|As a faculty member, I would like to list my research projects on my account so that students can find projects which I am associated with.|
 |12|As a faculty member, I would like to edit my account details.|
 |8|As a student, I would like to view details of research projects so that I learn more about projects.|
 |7|As a student, I would like to browse open research projects so that I can find projects to apply to.|
 |6|As a student, I would like to edit my account details so that I can add information into my account.|
 |5|As a student, I would like to view my account.|
 |4|As a student, I would like to login to my account.|
 |3|As a student, I would like to register for account.|


 |#|Task|User Story #|Assignee|
 |-|-|-|-|
 |54|Create an "update project" form for editing project details.|17|Brandon|
 |53|Create a route in the Flask app to handle updating project details.|17|Chase|
 |52|Create routes for project creation form.|15|Chase|
 |51|Design page for project creation with associated html template.|15|Brandon|
 |50|Design a interface for editing research project details and create associated HTML template.|17|Brandon|
 |49|Develop a edit profile form for the Flask app to allow students and faculty to edit their profile information.|6,12|Matt|
 |48|Design HTML template for displaying a faculty members research projects.|14|Brandon|
 |47|Create a Flask route for retrieving the details of a specific research project and passing those details to a template.|8|Matt
 |46|Design an interface for viewing a single research project and its details. Create a corresponding HTML template.|8|Ryan|
 |45|Add a route in the Flask app for retrieving research project listings and rendering the page with all open projects.|7|Chase|
 |44|Faculty "create project" Form.|15|Matt|
 |43|Design a page for browsing open research projects, and create a corresponding HTML template.|7|Brandon|
 |42|Create a "Project" model in the database for storing the details of research projects.|7,8,15,17|Chase|
 |41|Design an edit profile interface for both students and faculty and create a HTML template for each.|5,6,12,38|Ryan|
 |40|Create routes in the Flask app for displaying student profile pages and faculty profile pages.|5,38|Matt|
 |39|Design a student profile page and faculty profile page along with HTML templates for each.|5,38|Ryan|
 |37|Develop a login form for the Flask app and create a route to handle login attempts.|4,10|Chase|
 |35|Design the login interface and create a corresponding HTML template.|4,10|Ryan|
 |34|Create "User", "Student" and "Faculty" models in the database for storing user profile information.|3,31|Chase|
 |33|Develop the user registration form for the Flask app and add route to handle user registrations.|3,31|Matt|
 |32|Design the user registration interface and create a corresponding HTML Template.|3,31|Ryan|



----
## 3. Iteration 1 - Sprint Retrospective

During our Iteration-1 Scrum retrospective, our team reflected on the strengths of our process and identified areas for improvement to enhance our workflow in future iterations.

One of the key successes of our first iteration was maintaining concise and effective meetings. With an average of four Scrum meetings per week—one of which typically served as a working session—we felt well-coordinated and consistently left meetings with a clear sense of direction. This structure allowed us to remain aligned and ensure smooth collaboration throughout the iteration.

However, we also recognized areas where we can improve. First, we want to focus on working more consistently to prevent last-minute crunch situations. By spreading our workload more evenly, we can complete integrations earlier, allowing team members to work with fully developed components. For instance, ensuring that form/routes are created ahead of time will enable smoother testing of HTML templates by other team members.

Another improvement goal is to be more vigilant about testing before pushing code. We identified two potential approaches to this: developers can either create a test stub for their code or wait until the dependent component is ready. If they choose the latter, they will create a Git issue assigned to themselves as a reminder to revisit the implementation once testing becomes possible. Additionally, they will notify the relevant team member to track dependencies and facilitate smoother collaboration.

To further enhance our development process, we will work on breaking down tasks into smaller, well-defined Git issues. This will provide better structure and clarity, making the development process more manageable. Lastly, we aim to be more cognizant of task ownership, ensuring that team members focus on their assigned work without unintentionally overlapping with others’ responsibilities.

Overall, our team felt that our agile implementation was successful for the first iteration, but with these refinements, we believe we can further improve efficiency, collaboration, and code quality in the next iteration.

----
## 4. Product Backlog refinement

 <!-- * Have you made any changes to your `product backlog` after `Iteration-1`? If so, please explain the changes here.  -->

Besides finishing nearly all tasks created for the first iteration, we have moved a couple tasks from iteration 1 to iteration 2: 
 - SSO login
 - Index page for students and faculty members
 
These are currently high priority tasks for us. Also, we decided to add AWS deployment to iteration 2. Otherwise, we remain confident in our existing product backlog. 

----
## 5. Iteration 2 - Sprint Backlog

### Iteration 2 User Stories

| #  | User Story | Assignee |
|----|-----------|----------|
| 27 | As a student, I would like to withdraw pending applications so that I may discontinue my application process for a research position. | Brandon |
| 22 | As a faculty member, I would like to view references for students. | Ryan |
| 21 | As a faculty member, I would like to view applications of students who have applied for my research positions so that I can learn more about them. | Ryan |
| 20 | As a faculty member, I would like to approve or reject students from positions I have posted. | Matt |
| 18 | As a faculty member, I would like to see students who have applied to research positions to determine if they have been accepted into other research projects. | Chase |
| 16 | As a student, I would like to view the status of my completed applications. | Brandon |
| 11 | As a student, I would like to submit a personal statement with my applications. | Brandon |
| 9  | As a student, I would like to apply to open research projects. | Ryan |
| 82 | As a faculty member, I would like to view the list of applied applicants. | Chase |
| 83 | As a faculty member, I would like to view the list of applicants and see their application status, whether I accepted or rejected them, or if their application is still pending. | Chase |
| 84 | As a faculty member, I would like to view any given personal statement that the student has submitted when they applied for my research project. | Ryan |
| 86 | As a faculty member, I would like to have easy viewing access to the applied student’s profile while reviewing their personal statement and their application responses. | Matt |
| 87 | As a faculty member, I would like to view the number of students that I have already accepted into my research project. | Matt |



