# 4 - Introduction to Fine Tuning Data Cleaning English

---

WEBVTT

Welcome back. In this lecture we will

start an exciting hands-on journey into

fine-tuning language models using the

Olama platform. Think of

Olama as a friendly and

intuitive workspace that

simplifies even the most

complex tasks like fine-tuning

a cutting-edge model such as

Mistral. By the end of this session, you

will not only understand the process. but

also feel confident enough to dive

in on your own. Fine tuning

is the process of customizing a

pre-trained language model like MISTRAL

to perform specific tasks or cater

to specialized domain. Olama

provides a seamless interface

and a set of tools that guide you every

step of the way, making the process

approachable and efficient. To get

started with Olama, familiarize yourself

with its platform. It combines

powerful tools with an intuitive

workspace, making it suitable for

seasoned developers and beginners

alike.

First, visit the Olama website

and create an account. Once signed in,

you will see a clean, user-friendly

dashboard that serves as your

command center. From here, you can manage

datasets, fine-tune models, and monitor

performance. For those who prefer the

command line,

Install it using the following command.

Once installed, configure your

environment in the dashboard. Define your

default model. Choose compute

resources like CU or

GU.

The quality and relevance of your data

are critical to successful fine-tuning.

Start by identifying the task you want

the model to perform, such as

summarizing legal documents, classifying

emails, or generating creative writing

prompts. Gather a data set aligned

with your goals and upload it to

Ollama in formats like

ESON. CSV

or plain text. Navigate to the datasets

tab and click upload dataset.

Ensure your data is clean

and well organized by removing

duplicates, fixing tables

and standardizing formats. Let's walk

through the process of cleaning a dataset

using Python and the pandas library.

First, we begin by importing the

necessary library pandas.

This library provides powerful tools

for data manipulation and analysis.

Next, we define a function called

cleandataset that takes in one parameter

filepath. This parameter is the best to

the raw dataset we want to

clean. Inside the function, the first

step is to load the dataset

into a pandas dataframe using the

bdeReadySAV

This allows us to work with the dataset

in a structured format.

Once the data is loaded, we remove

any duplicate rows using the drop

duplicates method This ensures that

all rows in our data set are unique

Following that, we handle missing

values by replacing values by replacing

them with the string This step makes

our data set more consistent and

avoids issues caused by null values

during analysis

Next, we standardize the text data in the

text column by converting all the text

to lowercase using the

zc.lower method. This helps

ensure uniformity in our

textual data. Finally, we save

the cleaned data set to a new

CSV file named

cleandataset CS

The indexfalse argument ensuresThat

the index column isn't included in the

save file. To wrap up, the

function prints a message confirming that

the data set has been cleaned and saved.

At the end of the script, we call the

cleandataset function, passing in the

name of our raw data set file

to begin the cleaning process. This

results in a ready to use cleaned data

set saved to a new file. Once your

data set is ready, you can roceed to

fine tune the maestral model.

Mistral is a robust and efficient

language model ideal for

customization.