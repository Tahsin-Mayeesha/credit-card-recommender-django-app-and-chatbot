# 1 Introduction

## 1.1 Purpose

This document has the information on the application architecture and backend details for the credit card recommender course project developed by team 2 in CSE 327 Fall 2018 class.

## 1.2 Document Conventions

The document follows standard markdown conventions. Bold/Italics will be used to emphasize key words while important information will be presented using tables.

## 1.3  Intended Audience 

Course instructor, other team members. 

## 1.4 Reading Suggestions

Please use the table of contents to navigate.

# 2 Project Overview 

In this project we are developing a credit card recommender to recommend credit and debit cards to professionals, students and general people. We generate the recommendations using machine learning. 

# 2.1 Application Architecture 

The final product for this project is a responsive web application which will take user preferences into account and generate recommendations with machine learning. For the web application we use python as the backend language and implement the web application using the **MVC**(Model-View-Controller) paradigm.

# 3 UML Class Diagrams



# 4 UML Sequence Diagram



# 5 Database Definitions



## List Of Tables

* User
* Card
* Bank
* user_has_bank_account
* bank_has_card

## ER Diagram

![](diagrams/erdplus-diagram.png)

## Table Descriptions

|            TABLE: USER (ATTRIBUTES)             |          Description of Attributes          |
| :---------------------------------------------: | :-----------------------------------------: |
|                     User id                     |     Id of user to log in (Primary key)      |
|                      name                       |              Name of the user               |
|                      email                      |           Email used for sign up            |
|                    password                     |          User's password to log in          |
|                       age                       |                 User's age                  |
|                     address                     |               User's address                |
|               professional status               |           Current status of user            |
|               preferred card type               |                                             |
|             preferred interest rate             |                                             |
|           preferred max credit limit            |                                             |
|              preferred annual fee               |                                             |
|               visa vs master card               |                                             |
|         preferred reward airport lounge         |   if user wants airport lounge as reward    |
|       preferred reward cashback available       |        if user wants cashback or not        |
|      preferred reward cashback percentage       | how much cashback percentage user wants etc |
|         preferred reward luxury resort          |                                             |
|         preferred reward insurance plan         |                                             |
|        preferred reward death insurance         |                                             |
|        preferred reward travel emergency        |                                             |
|          preferred reward fine dining           |                                             |
|        preferred reward buffet discount         |                                             |
|        preferred reward medical discount        |                                             |
|        preferred reward airlines ticket         |                                             |
|          preferred cash withdrawal fee          |                                             |
| preferred cash withdrawal limit per transaction |                                             |
|     preferred cash withdrawal limit per day     |                                             |





|       TABLE: CARD (ATTRIBUTES)        |                  DESCRIPTION OF ATTRIBUTES                   |
| :-----------------------------------: | :----------------------------------------------------------: |
|                card id                |                    card id (Primary Key)                     |
|               card name               |                         name of card                         |
|               card type               |                  if card is credit or debit                  |
|               bank name               |      bank the card is from, foreign key from bank table      |
|           minimum age limit           |                minimum age for card approval                 |
|            card issue fee             |                fee required for issuing card                 |
|             interest rate             |              interest rate for the credit card               |
|              annual fee               |                 annual fee given to the bank                 |
|         card replacement fee          |           card replacement fee if the card is lost           |
|     captured card replacement fee     | card replacement fee if the card is captured in an ATM machine |
|          cash withdrawal fee          |           cash withdrawal fee for each transaction           |
| cash withdrawal limit per transaction | maximum amount of money that can be withdrawn in one transaction |
|     cash withdrawal limit per day     |    maximum amount of money that can be withdrawn per day     |
|            vat percentage             |              annual VAT percentage for the card              |
|         minimum credit limit          |            minimum credit limit for credit cards             |
|         maximum credit limit          |                maximum amount of credit limit                |
|         interest free period          |                interest free period in months                |
|        fund transfer facility         | boolean . whether the card can transfer fund with other cards |
|  international transaction available  | boolean. if card can be used for international transaction.  |
|        dual currency available        |    boolean. if card can be used for multiple currencies.     |
|           dual currency fee           |                           boolean                            |
|                is_visa                |                    if card is visa or not                    |
|             is_mastercard             |                 if card is mastercard or not                 |
|         reward airport lounge         |       if card rewards users with airport lounge usage        |
|       reward cashback available       |            if card has cashback available or not             |
|      reward cashback percentage       |               percentage of cashback available               |
|         reward luxury resort          |                if card awards resort discount                |
|         reward insurance plan         |           if card awards discounted insurance plan           |
|   reward accidental death insurance   |             if card awards death insurance plan              |
|        reward travel emergency        |         if card awards emergency help during travel          |
|          reward fine dining           |        if card awards fine dining experience discount        |
|        reward buffet discount         |                if card awards buffet discount                |
|        reward medical discount        |               if card awards medical discount                |
|        reward airlines ticket         |                if card awards airlines ticket                |
|           upgrade possible            |                if card has upgraded versions                 |
|         sms service available         |              if card has sms based transactions              |





| TABLE: BANK (ATTRIBUTES) | DESCRIPTION OF ATTRIBUTES |
| :----------------------: | :-----------------------: |
|         bank id          |      Id of the bank       |
|        bank name         |       name of bank        |
| number of ATMS available |      Available ATMs       |





| TABLE: USER BANK (ATTRIBUTES) |   DESCRIPTION OF ATTRIBUTES    |
| :---------------------------: | :----------------------------: |
|            User id            | foreign key(from table 'USER') |
|            bank id            | foreign key(from table 'BANK') |





| TABLE: USER CARD (ATTRIBUTES) |     DESCRIPTION OF ATTRIBUTES     |
| :---------------------------: | :-------------------------------: |
|            User id            |  foreign key(from table 'USER')   |
|            bank id            |  foreign key(from table 'BANK')   |
|   card recommendation score   | AI will recommend a card for user |



# 4 Technical Stack

## Front End



## Back End



## Deployment





# 5 Work Plan 

## Task List and Assignee Name

| Task Name | Assignee |
| --------- | -------- |
|           |          |
|           |          |
|           |          |
|           |          |
|           |          |



# 6 References 



