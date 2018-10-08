# Software Requirement Specification Document 

[TOC]



# 1. Introduction



## 1.1 Purpose

This document introduces the CSE 327 project credit card recommender system. The context of building such a product along with our implementation discussion is written in the later sections. UML diagrams, user workflow diagram, deployment issues and system constraints are features are also discussed.

## 1.2 Document Conventions

This document follows standard markdown convention of breaking up a document into sections with headers and sub-headers. Tables have been used for showing context and information in section 4 and section 6. Diagrams are used for improving clarity of explanation.



## 1.3  Intended Audience and Reading Suggestions

Current intended audience is our CSE327 Instructor Nabil Mohammed, group members, other class members. However in future we wish to show the document to potential buyers of our software such as bank managers to check if they wishes to sponsor advertisement through our system.

## 1.4 Product Scope

We want to build a recommender system that can recommend credit and debit card to new users, old users without any credit card and old users with some credit card. Here new and old refers to consumers of financial services from banks. People who do not have any bank account or credit card are new users, people with bank account but no cards are old users without any credit card and the rest are old users with existing cards who may want to take up a new one. By addressing these classes of financial product consumers we hope to raise financial awareness and make better consumers to develop our economy.

## 1.5 References

Since such a system has not been deployed in Bangladesh so far this section is not applicable.

# 2 Overall Description



## 2.1 Product Perspective

Bangladesh as a developing country do not have many financial advising systems for consumers. However as a growing economy currently we have many options to choose when it comes to credit cards, each with their reward scheme which are integrated into our other social services. A credit card can award the user rewards for grocery shopping, cash back, loyalty programs, restaurant discounts or travel points. A system for credit card recommendations is therefore hard to build as each card has its own trade off. In general people search for blog posts or videos to learn about the credit cards. Some people just ask their family and friends for recommendation, however these choices are not based on hard facts and data. We wish to solve this problem by building our recommendation system.



## 2.2 Product Functions

First of all an user have to search the URL .Then user have to choose sign up vs log in option. For a new user who has selected the sign up option, user will have to give some personal information.After submitted this user will find a search option along with a get recommendations option .User can search cards which are sorted by card limit, bank name,interest rate,annual fee and geographical metrics.

A simplified user workflow diagram is given below. 

![](diagrams/user_workflow.jpg)  

## 2.3 User Classes And Characteristics

There are two types of user classes. User and Admin are the two classes. Users are general users who do not have database privilege. However admins can add new credit cards, edit and delete the cards. Admins can also generally work on user account like verifying password. Both users and admins can sign in and sign out from the system. They can fill up user profile and get recommendations generated via machine learning. They can also search for the cards based on different criteria. 

A UML diagram is added below to show the activities done by different user class.

![ ](Uml/uml_diagram.png) 

## 2.4 Operating Environment 

Operating system independent because we are deploying as web application.

## 2.5 Design And Implementation Constraints

System must send notification to user via sms or email when new cards are added and consider user geographical location when making the recommendations. Recommendations should make sense and consider user eligibility for the cards before making recommendation.



## 2.6 User Documentation

FAQ and tutorial will be provided in the home page.



## 2.7 Assumptions and Dependencies

Not applicable



# 3 External Interface Requirements



## 3.1 User Interfaces

For a web application the user interface is the software interface. For the software interface we discuss general data flow. However user interface wireframes will be worked on later. For communication interface we expand on the notification system.

## 3.2 Hardware Interfaces

Not applicable.

## 3.3 Software Interfaces 

To store the dataset of credit cards we will need a database system. Most likely we will use a relational database system with good integration with python like MongoDb. We will generated the recommendations using python package surprise(former scikit-recommender). The user will submit their profile information through the user profile form, which will be used to generate the recommendations and personalize the search system. Potentially Google Cloud Platform will be used for deployment, however we will choose based on cost comparison of different deployment services. The software interface is mostly divided into 4 parts -- user profile, home page, recommendation and search page.



## 3.4 Communication Interfaces

We will use either email or sms for generating automatic notifications. Potentially a service like Twillio will be used.

# 4 System Features
## 4.1 Use case 1 : Go to Landing Page

Actor : User and Admin. 

Type : Primary 

Typical Course of Events :

| Actor Actions                                            | System Responses                    |
| -------------------------------------------------------- | ----------------------------------- |
| 1. Go to web application home page url via a web browser | 1. Browser serves the landing page. |

## 4.2 Use Case 2 : Logging In

Actor : User 

Type : Primary 

Typical Course of Events :

| Actor Actions                                  | System Responses                                             |
| ---------------------------------------------- | ------------------------------------------------------------ |
| 1. User clicks on Log In Button                | 1. User is shown a form containing username or email and password fields along with forgot password button. |
| 2. User writes the username/email and password | 2. System Redirects to the profile page.                     |

Alternative Course Of Events :

### 4.2.1 Use Case 2.1 : Forgetting Password

| Actor Actions                                | System Responses                                             |
| -------------------------------------------- | ------------------------------------------------------------ |
| 1. User clicks on Log In Button              | 1. User is shown a form containing username or email and password fields along with forgot password button |
| 2. User clicks on the forgot password button | 2. User is sent a email/mobile verification link. Details of how to handle password change will be fixed during implementation of back end. |

## 4.3 Use Case 3 : Sign Up

Actor : User 

Type : Primary 

Typical Course Of Events :

| Actor Actions                      | System Responses                                      |
| ---------------------------------- | ----------------------------------------------------- |
| 1. User goes to landing page URL   | 1. Browser serves the home page.                      |
| 2. User clicks the sign up button. | 2. User is redirected to the create new profile form. |

## 4.4 Use Case 4 : Creating Profile

Actor : User And admin 

Type : Primary 

Typical Course of Events :

| Actor Actions                                                | System Responses                                             |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| 1. User clicks sign up and is redirected to the profile form page. | 1. System stores the data given by user for creating new profile. Credit card recommendations will be generated by this information. User is shown buttons for getting recommendations and search. |

## 4.5 Use Case 5 : Get Recommendation

Actor : User and Admin. 

Type : Primary 

Typical Course Of Events :

| Actor Actions                                                | System Responses                                             |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| 1. User clicks get recommendations button from the profile page. | 1. System redirects to the recommendations page where the user is shown a list of recommendations for future purchasing. |

## 4.6 Use Case 6 : Search

Actor : User and Admin. 

Type : Primary 

Typical Course Of Events :

| Actor Actions                                                | System Responses                                             |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| 1. User clicks the search page from website after logging in or signing up. | 1. System shows user the search page when they can search the credit card database through different search criterias. |

## 4.7 Use Case 7 : Sign Out

Actor : User 

Type : Primary 

Typical Course Of Events :

| Actor Actions                       | System Responses              |
| ----------------------------------- | ----------------------------- |
| 1. User Signs out from the profile. | 1. System signs out the user. |

## 4.8 Use Case 8 : Administrator Usage actions

### 4.8.1 Use Case 8.1 : Adding Credit Card

Actor : Admin 

Type : Primary 

Typical Course Of Events :

| Actor Actions                                                | System Response                          |
| ------------------------------------------------------------ | ---------------------------------------- |
| 1. Admin logs in as admin and clicks on adding credit card button from profile. | 1. Form for adding credit card is shown. |
| 2. Admin fills up the card information form.                 | 2. Card is added to the system.          |

### 4.8.2 Use Case 8.2 : Deleting Credit Card

Actor : Admin 

Type : Primary 

Typical Course Of Events :

| Actor Actions                                                | System Response                                              |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| 1. Admin logs in as admin and clicks on deleting credit card button from profile. | 1. List of credit cards in the system is shown for deletion. |
| 2. Admin selects the cards to be deleted.                    | 2. Card is deleted from the system database.                 |

### 4.8.3 Use Case 8.3 : Edit Credit Card

Actor : Admin 

Type : Primary 

Typical Course Of Events :

| Actor Actions                                                | System Response                                             |
| ------------------------------------------------------------ | ----------------------------------------------------------- |
| 1. Admin logs in as admin and clicks on edit card button from profile. | 1. List of credit cards in the system is shown for editing. |
| 2. Admin selects the cards to be edited.                     | 2. Card is edited.                                          |

### 4.8.4 Use Case 8.4 : Administrator Log In/Sign Out

Actor : Admin 

Type : Primary 

Typical Course Of Events :

| Actor Actions                                 | System Response                                              |
| --------------------------------------------- | ------------------------------------------------------------ |
| 1. Admin logs in as admin from the home page. | 1. Admin is able to do admin privileged actions like adding, removing, editing credit cards. Admin can also do everything a user can do like getting recommendations and search. |
| 2. Admin signs out.                           | 2. Admin is signed out from the system.                      |

## 4.9 System Feature 1 : Send Notifications

Actor : System 

Type : Primary 

Typical Course Of Events : 

| Actor Actions                                                | System Responses                                             |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| 1. User indicates that they want to use the notification system for getting recommendations over sms or email. | 1. System automatically sends notification when new recommendations are added. |

# 5 Other Non Functional Requirements

## 5.1 Performance Requirements

Performance requirements depend on the machine learning model use. Right now as the database is small we are using content based recommendations for bangladeshi credit cards, but most likely a collaborative filtering model will be used for better performance after getting more users. Since it depends heavily on the implementation performance requirement details will be fixed later.

## 5.2 Safety Requirements

Not Applicable as the system only shows recommendations for financial products.

## 5.3 Security Requirements

Not applicable as the system does not store much confidential data about the user such as credit card information.

## 5.4 Software Quality Attributes

Software should be fast with an intuitive user interface for financially less-literate users.

## 5.5 Business Rules

Not applicable as the recommendation system is not doing any explicit business with any bank at this moment.

# 6.1 Appendix A : Glossary

Credit/Debit Card : Credits are financial services given by bank at a certain interest rate for users to spend on consumer products or other purposes. 

Recommender system : Recommender systems are generally used in e-commerce and similar services to give users based recommendations for purchasing or consuming products.

# 6.2 Appendix B : Bank List

 Selection of Potential Banks to consider for recommendation is shown below before data collection. We aim to collect credit card data from following organization.

* Dutch Bangla Bank
* Eastern Bank Ltd
* The City Bank Ltd
* Bank Asia Ltd
* Dhaka Bank Ltd
* IFIC Bank Bangladesh Ltd
* AB Bank Ltd
* Standard Charter Bank
* Mutual Trust Bank Ltd 

# 6.3 Appendix C : Credit Card List

A selection of credit card that will be considered for recommendation is also added to show how the future dataset will look like. Credit cards like these will be added to the database along with their properties for future recommendation.

| Bank Name         | Card Name                    |
| ----------------- | ---------------------------- |
| Dutch Bangla      | Mastercard Titanium          |
| Eastern Bank Ltd  | EBL visa classic credit card |
| City Bank         | City Visa Credit Card        |
| Bank Asia         | Visa Classic Local Card      |
| Brac              | Brac Signature Card          |
| IFIC              | IFIC Credit Card             |
| ABBL              | World Mastercard             |
| Mutual Trust Bank | MTB Visa Classic             |

