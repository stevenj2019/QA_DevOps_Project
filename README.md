# QA_DevOps_Project

* Docker 
* Flask 
* Pytest 
* Selenium 
* GCP 
* Jenkins 
+ Ansible 
+ Nginx

# Helpful Links 

+ Trello Board [here](https://trello.com/b/02kJOwrM/devopsproject)
+ Risk Assessment [here](https://docs.google.com/spreadsheets/d/1e9dNWcu6ro9YcTkmCDNhyVzRHGwjEr3RxXqMkqxVKZE/edit?usp=sharing)

# Planning Stage 

## Preliminary Risk Assessment 

![](README_rss/init_risk_matrix.png) 

This is the initial risk matrix, this was determine by risks we could already determine and already resolve. this will be a document that will be iterated throughout the project 

## Gathering User Requirements 

Gathering User Requirements is done via a user story, an example is below:

![](README_rss/ex_usr_story.png)

This is then broken up into Tasks by someone in the development team, an example from the above user story is below: 

![](README_rss/ex_task_list.png)

This allows the Development team to work on small features to deliver a desired functionality. 

## High Level Application Design 

![](README_rss/high-level-flow.png)

## Infrastructure Design 

![](README_rss/Infra-Diagram.png)

There are multiple points to discuss with this diagram. 

1. The CI Pipeline and the Ansible Deployment Server will be the same machine. This is due to ease of setup during the initial deployment. The Docker Swarm Manager is a separate machine. 
2. The Swarm Workers and Swarm Master are configured the same (with the exception of the docker swarm roles)
3. Nginx will act as a load balancer as well as a reverse proxy in this Infrastructure

## Entity Diagram

![](README_rss/Entity_Diagram.png)

## Main Service Spec 

The Main Service serves the Jinja2 pages to the user, it will then utilise the API's
It will also persist data to the SQL Database 

## Service 2 spec - slot machine Spec 

![](README_rss/service-2-flow.png)

The Slot Machine API will generate 3 results randomly (like a slot machine would normally), it will then give this information to the Main Service for it to be rendered by Jinja2

## Service 3 spec - slot machine multiplier Spec 

![](README_rss/service-3-flow.png)

The Slot Machine Multiplier API will determine a random multiplier, at first it will be entirely random however in further iterations this will favour older accounts more than younger ones 

## Service 4 spec - amount calculator

![](README_rss/service-4-flow.png)

This will then take the information from Service 2 and 3 and work our how much money was won/lost and send this to Service 1 for the database to be updated accordingly 

## CI/CD Pipeline Spec 

![](README_rss/CI-CD.png)

The CI/CD Pipelines will be controlled by the Jenkinsfile 

It will be organised into build -> test -> deploy. 

the build will focus on building the images such as: 

+ 3 Flask Containers (composing the main app + API's)
+ Nginx Container (for reverse proxy)
+ MySQL Container

Testing will utilise multiple technologies as long with methods: 

+ Pytest (mocking API's, unittest)
+ Selenium (Integration Testing)

Deployment will make use of Docker Swarm. This will allow us to build application redundancy. This will also allow us to build rolling updates 

# Sprint 1 

## Trello board to do 

In This Sprint we aim to build the essential software functionality. We Do this by using the MoSCoW method. as you can see below, we have segmented the projects into must have (red), should have (orange) and could have (green).

![](README_rss/sprint_1_trello.png)

Everything which is red defines the MVP (or Minimum Viable Product), Which means ones this is done the iterations are focussed more on improvement, as you can see from the above image all the must haves should be completed by the end of the first sprint

## Changes

+ Software will be in a working state 

## Test Coverage 

Test 1 Coverage is within the Issues due to a problem discovered during testing. 

Test 2 Coverage is below: 

![](README_rss/sprint_1_test_3.png)

Test 3 Coverage is below:

![](README_rss/sprint_1_test_4.png)

Main Service Coverage is below:

![](README_rss/sprint_1_test_5.png)

## Issues 

Due to how the application was coded the test will return a different percentage each time. This will be amended in the next sprint

![](README_rss/sprint_1_test_1.png)

![](README_rss/sprint_1_test_2.png)

## Risk Assessment 

During This Sprint, Some new errors have became of interest. as well as this some previously known issues have been readdressed. 


![](README_rss/risk_matrix_1.png)

so as you can see we have revisited SSH Access and Path Traversal. SSH Access while Firewalls are effective they can restrict those with legitimate access. with the use of PKI (Public Ket Infrastructure) we can secure our environments while still allowing CI Pipeline Servers to communicate in a way that required no human interaction. 

Due to the Issue we experienced during Testing we have added potentially automation Issues. rather than just dry running the application. in future we will deploy with docker and use Integration tests to ensure no bad code makes its way into a production environment. 


## Success and other changes 

+ Created a CRUD Application, Testing above 80%
+ 3 Micro-Services to compliment the app. Testing 100% (with the exception on Service 1)

## Limitations

+ Due to initial design on service 1 pytest does not provide accurate coverage, While this has been confirmed to work, This Code will require refactoring during the next sprint to amend
+ Due to deployment not yet being implemented. Testing is non-existent within the Main Service. While the test case is written (commented out under Main/Testing/test_unit.py). We cannot confirm functionality. Manual Testing revealed positive results. 


# Refactoring

## API 1 

We decided to refactor this with top priority. due to the the issue found during test 1. 

so the problematic function used to to look like this: 

![](README_rss/API_1_before.png)

as you can see the if/elif clauses are dependent on the random number generator. This means if a number isn't generated it wont be tested. 

we changed it to this:

![](README_rss/API_1_after.png)

This provided numerous benefits.

+ More Pythonic (easily readable)
+ More efficient
+ Testing Issue Resolved (see below)

![](README_rss/API_1_test.png)

as well as this some other things were changed

+ Application.models.RegisterForm changed to Application.models.UserForm. Due to being reused in other parts of the application
+ In Testing url_for() is now used consistently 
+ one-line functions used where possible

we also made a change to the win function within API3. 

This is to allow the slot machine to be easily extended to 4/5 wheel machines as oppose to the current 3.

![](README_rss/API_3_before.png)

![](README_rss/API_3_after.png)

## Docker 

We will be using Docker, as well as docker-compose. This is to allow us to build our environments in an automated and consistent manner. 

We will also be using Docker Image Versioning, this will allow us to quickly revert back IF a broken build makes it through Jenkins (refer to the Risk Assessment for further information)

## Changes 

1. ![](README_rss/old_CI-CD.png)

was changed to 

![](README_rss/CI-CD.png)

This is due partially to a change of technology. 
As well as this Configuration Management was deemed to be necessary due to the issues inconsistent host can cause (check Risk Assessment for updates)

2. The Following entries were added into the Risk Assesstment

![](README_rss/risk_matrix_2.png)

This shows new risks we associate with the project. it is mostly involved in our infrastructure and capacity. we have completed the leg work with docker to allow us to containerise these however we now need to create a Ansible Playbook to allow us to ensure our infrastructure is consistent whenever we deploy or whenever we need to provision a new node 
