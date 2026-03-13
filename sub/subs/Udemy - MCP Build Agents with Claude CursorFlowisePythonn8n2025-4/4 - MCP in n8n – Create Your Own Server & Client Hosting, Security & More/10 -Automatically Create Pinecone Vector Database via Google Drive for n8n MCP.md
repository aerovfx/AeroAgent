# 10 -Automatically Create Pinecone Vector Database via Google Drive for n8n MCP translated

---

We have the possibility to connect vector databases to our MCB server.

Everything that we have to do is of course to press plus,

and here we can search for vector stores.

You already know it. We can use whatever we want.

We can use MongoDB, we can use Pinecom, Postgres, Quadrant,

as inver vector store, SuperBase, and so on.

I do really like Pinecom because Pinecom makes it really, really easy.

If you do have a self-hosted version of SuperBase,

you can also use SuperBase if you want,

and do exactly the same workflow.

Just use SuperBase if you already understand SuperBase.

But like at all you, I want to use Pinecom.

So you can press on Pinecom, and as soon as Pinecom is here,

right now included, of course you need to have an embedding model and so on.

But before you can connect here to a vector database, of course,

we need to upload stuff in a vector database.

Later over the course, I will also show you how we can upload stuff via chat trigger,

so that you can make, for example, a self-improving AI agent

that stores your knowledge all the time.

But what I want to show you in this video is, of course,

how you can create a vector store, we will connect it with Google Drive.

So that you can upload stuff into Google Drive,

and every time as soon as you upload stuff into your Google Drive,

this document will get stored in the vector database and will get split it

and embedded in this vector database.

And then of course, you can access it via the SMCP server.

So basically this will be a two-part video.

In this video, we will basically first of all just delete this.

We come back on personal, we save here the changes,

create workflow, and we start into empty canvas because right now,

we need to do the first part.

I want to create a vector database and we need to make a workflow that can

absurd stuff into a vector database.

For this example, we assume that we like to read

quarterly earning reports from companies.

So we can simply upload the file in our Google Drive and then ask questions.

This is of course practical.

I am on my localhost right now and now we need to include a node.

And I told you that we want to use Google Drive.

So we press plus and we search of course for Google Drive as the trigger node.

So we use Google Drive on changes involving a specific folder.

This thing is now included, but let's just wait for a minute.

We need to give this a name.

Let's just say load data from the right for example.

And let's just make it a bit bigger to bind comb because bind comb will be later our database.

And what we want to do right now is of course to go into our Google Drive

because we have to make a folder.

What I want to do first is of course to make a folder into my Google Drive.

It's called Tesla earnings and here are the Q3 earnings of Tesla.

If you go for example onto the investor relations from Tesla,

you see that the Q3 earnings are of course out.

Also the Q4 earnings are out but I want to show you later how we can update this knowledge base.

That's why I want to download the Q4 later and make these updates.

Right now Q3 is included and that's right now at this minute every single thing that we need.

When I open up this PDF you see that in this PDF is a lot of data.

I have to tell you right now at this minute.

This data is not perfectly structured for an LLM.

An LLM works a lot better with Markdown.

One of the best ways to prepare your data is LamaPars from Lama Index.

You can simply Google LamaPars and press on the first link.

You will be on this webpage and you can press get started.

You most likely need to make an account or login with Google.

And here you see on the left side bars.

And on bars you can simply upload your documents.

And if you upload your documents you will get Markdown back.

I have to tell you I just want to show you this in a brief overview.

Maybe we will insert this data later because first I just want to start as easy as possible.

For this example I have also downloaded Q1 of 2025.

So this is also some data and we will work later with this data.

First I want to train in the older training data so that you can see that we can update our

knowledge really really easy.

So what I am doing right now is of course to upload all of this data because this is not good for an LLM.

All these big charts and so on this is not needed in a red application.

So we simply throw this stuff in here on upload.

And then we can simply parse our document.

You can come unbalanced, fixed premium or custom.

And you always need to keep in check that you have enough credits.

This is completely for free.

I do think you get like a few hundred credits a month for free.

Then you can press on what to parse.

For example if you want to parse just a few pages.

And then lastly the job options.

So you can simply play with this a little bit.

What I am doing right now is to simply press parse.

And then you will see that we will get perfectly structured markdown for an LLM from our PDF.

Of course there are a lot of other ways.

We can use fire crawl.

We can use all of these things.

But if you already have a PDF I do think that LLM parse gives us a really really great approach here.

And boom there we are.

We have right now everything in markdown.

So you see the markdown is right now perfectly structured for an LLM.

We have everything included so that an LLM can read it really really great.

And you also see that we have a normal text file if we want.

We have the chase file if we want.

We have the images.

The images are parsed out because we do not need these images in our rec application and so on.

What works best is usually of course markdown.

So we would simply download this markdown file and later I will upload it.

So you see I have downloaded the markdown and if I open the markdown file up it will get opened up in my

code editor in VS code here.

And here we have everything right now perfectly structured for an LLM

so that the LLM can basically parse all of this information really great.

But like I told you first before we upload this newer data of Q1 I want to train on older data

and also want to show you that even older data that is not necessarily good structured for an LLM

can work with this approach.

But if you have more data please just throw it into markdown.

But for now for the sake of this tutorial we simply leave it as it is.

So this is just the first tutorial we want to make it as easy as possible.

As soon as this is included we come back to an add-in and we press of course on our google drive trigger node.

I have already connected my google drive account but because I see all the time problems here we do this step by step.

We press create new credentials if you do not have any credentials.

You go on to the documentation this is always the same thing with this google cloud console.

So you can simply press on it you go on console then of course you make a new project you can simply

press in this button here then new project.

Let's just give it a name for example.

And then drive test.

Then we press create of course.

As soon as this thing is created in this upper right corner you can press on it and you can use this thing

so use project.

Of course we press here once again we go on apis and services we go on library in the library we

need to search for the thing that we that you need.

So for example google drive and we sent this out you need of course the google drive api.

We need to activate this api and wait for a minute until this is active.

As soon as this is active we press of course on the OAuth consent screen first steps.

We give it a name and then drive we give our email we go on.

Extern we go on our email once again we go on we accept and we go on.

I just want to show this once again because I see here problems all the time.

Now we will make our OAuth client by pressing on this button.

It is of course a web application web client one is here okay.

And once again we need our reader right here.

I'll be pressing it we come back into an add end top it is line we include it here we can scroll down

and we press create.

After this thing is created we press on test group because here on test group we need to use a test

user so we press on that user and we give our mail here.

This is a point where I see problems from time to time.

So we include our mail and we connect this thing.

As soon as this is connected it should work.

So we go on clients we press here and now we have everything that we need.

The client ID of course we copy this.

We come back into an add end throwing the client ID.

Then the client C create key we copy this come back into an add end throw it down here

and now we sign in with Google.

We use our profile we go on we accept everything and go on.

Now this thing will be green hopefully once again we can close this down we can also close this

down and now you see that this thing is connected and here we have the mode we want to use everything

on minute. So every minute this thing will search in our Google Rye folder if new things get

included and if something new gets included we will get updates immediately.

We want to trigger these of course changes involving a specific folder so as soon as we get a

change in our folder this thing will get triggered every single minute.

Then we need to choose from our list.

If we come back here go back you see Tesla earnings.

It's the name here so we simply search from the list for Tesla earnings.

You can simply type it in here if you have a lot of folders.

Tesla earnings so we use this and then watch for you can press on it we use of course file

created because I want to upload files all the time and as soon as something new gets uploaded

we simply want to fetch this event because I already have an event I simply press fetch test

event and then we see if this thing comes through. So we see we have of course some data here

and if you scroll down you see that everything should work. You also find the original file name

and it's of course test lock U3. Exactly this file. So the fetching was correct we can close this down.

The next thing that I like to do from time to time is to press save and as soon as we have fetched

our test event here we press plus we use once again Google Drive because we need to download this

thing so we press on Google Drive, download file and we include this and here is everything set

right of course it's our Google Drive account the resources of file we want to download this file

and now this is important download you do not want to download from list so you do not want to

download every time the same file you need to find your file right here and if you scroll down you

will find the file ID so if you scroll down under spaces you find the ID of this file so the name

is of course DSLA and the ID is this right here and you can throw in the ID right here and then this

thing will simply gets downloaded every time as soon as we upload a new file and this will be

automatically if you press test step you will become of course the data or you will download the

data from this file so there we have it if we press view it's binary right now let's just download

it so that we can see it yes it's the same report so this worked of course and like I said this

pictures they are of course not perfect for our rack application this is just so that we can

make it simple for our first rack chatbot so we have downloaded our file and what we want to do

right now is of course to upload this files into a vector database and for the vector database

I like bindcomb for this so you can press plus and then we search some notes but before we do that

we simply go on google and we search for bindcomb then you press on this first link you need to

login or sign up if you do not have an account just simply sign up if you have an account with

simply login in this account I have already an account you can work with this thing completely

for free as soon as you are here this thing will be most likely empty for you and you can simply press

create index then we will give it a name let's just say an a then of course the sLA let's just do

with this way then you need the dimensions and for the dimension we simply use the text embeddings

free small you can simply press on these and the dimensions will be automatically it's important

that you remember what you chose here the text embeddings free small from open AI are perfect

simply use them and then you can scroll down and press create index as soon as this index is

created let's just wait for a minute then we can connect these things the next step is of course

to press on api keys create a key and then of course create key then we need to copy this key

we come back into an add-on and here of course we search for bindcomb so if you type in

vector store you will find a lot of different vector stores one of the easiest is also the in

memory vector store you can also use this like you can play with these things a little bit but I

really like bindcomb vector store if you press on these we use of course add documents to

vector store and here of course you need to connect your account because I have already accounts we

will create a new one so simply create new credentials and here you're throwing the credentials

from the api key that we have created then you press safe the credentials will be connected successfully

hopefully and then you are connected with bindcomb the operation mode is of course insert documents

this is important and then the bindcomb index from list you can also search for a bindcomb index

so from the bindcomb index you simply press on it and we use n8 and course dsl a so we simply use

this and now what I like to do is to give a namespace to bindcomb you can also give namespaces here

directly into bindcomb on your databases but I like to do it in an add-on because makes it a

little bit easier and simpler you can press on this thing you can simply press bindcomb namespaces

and I call this namespace simply dsl a and add-on this thing is now set you can close this down

but first you need here of course a lot of stuff let's just connect these two things

then we need the embedding models so we press plus I like to use the embeddings from openAI

you already know this you need to connect of course with an openAI account of course you have

already some credentials just use some credentials that we have made in this course and here it's

important that you use the same model that you have used in bindcomb in bindcomb we used the

text embeddings free small and that's what you need to use right here then this thing is connected

so it works then the next thing is of course that you need here this document so you press plus

I like to use the default the data loader so you simply press on the default data loader

and here you need to chose of course the right data the type of this data is of course not chasing so

you press on these this is binary data because we use a PDF in this example the mode is load all

input data you can also load specific data if you do not want to load specific stuff and the data

format is in our case it would be a PDF but you can also just use automatically detect by my

type if it's let's just say that you want to upload sometimes text files or whatever you can

also choose this right here and you close this down and this thing is still read because you

need to have a text splitter you simply press on this text splitter and what I like to use is

the recursive character text splitter splits texts into chunks by character recursively

recommended for most use cases more on text splitter for this embeddings later which just

want to do it really simple and really easy here we always have chunk size and chunk overlap

for a PDF in this size I like to use yeah like roughly let's just say 800 chunks and with an

overlap of I think 50 is fine here you can also go up to 900 if you work with this deval

data this will also eventually work more on chunk size and chunk overlap later we want to do this

a little bit faster should so just use this for a normal PDF and if your document is a lot smaller

you can use of course smaller chunk size and smaller chunk overlap now this thing is also here

connected so this thing should be perfect right now if you come back for example into bindcomb

here in bindcomb we go on our database and you see in this database is of course right now at

least empty if we come back into an add-on and we press test workflow we should load this data into

our bindcomb vector database so you see this thing gets loaded in right now and after this thing is

done hopefully we get all of the stuff in our bindcomb that vector database so you see 94 items

get added and if we come back into bindcomb right now it's empty let's just wait a minute this

thing should come through I just can simply can reload this page and there we have it so you see

it we have right now 49 documents in this database and they are all split it and embedded in our

vector database if you want to organize this even better you can come back into an add-on and buy

your data loader you can press on it and you can also use metadata so you can press on options

you press on metadata you can use apply property you give a name let's just say dsl a of course

is q3 and then the value you can find the value here if you go on schema you can find on the left

side the ID and under the ID is of course the name so you can simply throw this thing here and of

course this only works if you go on mapping and then schema under the ID is the name and we can

simply throw this value in here and this is how we can include metadata so until now we do not

have metadata this is of course not perfect if you go into bindcomb of course we can delete all

of this data and re-upload it so that we have metadata in our files this is not really necessary

but this can help to organize your vector database a little bit better so here you see we do not have

any metadata but if you go on namespaces we can simply delete all of this namespace by pressing on

this free dots delete here you need to type in dsl a and a then for our example delete namespace

now this thing is gone this thing will be completely empty as soon as all of this is deleted so you

see zero records and if you come back once again into an add-in and you test your workflow once again

we will embed this data once again but this time we also apply metadata and as soon as metadata is

implied we are a little bit better organized we come back into bindcomb want to reload it now we have

of course once again our namespace and if we come back to browser you see if you scroll down

that we have right now the metadata with the name and also the exact name of the file and we are

a little bit more organized so 49 documents all with metadata included thanks to our workflow

from an add-in and our goal is right now of course that we can simply upload stuff into our google

and our bindcomb vector database will update this stuff automatically in order to do that so let's

just see we have 49 documents included right now at this minute and if we come back into an add-in

we need to make this thing here from inactive to active and as soon as this thing is active this

thing will search every single minute if in my google drive account comes new data and to the new

data that I want to have is of course q4 so I can simply download q4 I want to download the

theorem my desktop the next thing that I want to do is to go into my google drive and here in this

google drive folder I simply throw the q4 from tesla and as soon as this thing is updated or

uploaded my add-in workflow will simply try to search for these updates all the time and then

will make updates automatically if we come to here into executions let's just see I think in a

minute or so a new execution will come through and everything will get included in our bindcomb

vector database completely automatically here you see that this thing is right now running so it

seems to work and right now we see that we had our success so this thing was perfect so every time

as soon as I upload something here my workflow will simply get triggered automatically but just

if we have this active this is important if you do not have this active you need to press test

workflow all the time as soon as this is active our trigger node will get executed every minute and see

if new stuff gets included here and if new stuff gets included we will simply automatically update

our bindcomb vector database if we come back right now into our bindcomb vector database we

have 188 records this simply means that we have included these two files so q3 and q4 if we want

to upload q1 of 2025 so basically this file but of course we not want to have this messy data this

time I want to show you how we can include markdown so how we can upload this nicely structured data it

is actually a little bit different in order to show you this as quickly as possible we will not wait

until our execution came through after we upload this stuff here we will do something like this

I just want to delete this two files don't worry because they are once again in our vector database

if I come to my workflow right now and I make it inactive so no longer active and I throw my markdown

file right here of course I can also come manually here and press execute workflow but right now

this will not work boom there we have an error and I want to show you why do we have this error

maybe you already guessed it right because right here we have binary data and right now we have markdown

so here we need to switch this up to chasen and if we press chasen this workflow will come through

if I press execute workflow right now once again remember it will work so if you want to absurd

markdown files you have to chose chasen here that's also why I wanted to show you both ways

so it always depends on what you want to do if you upload right now here only markdown files

leave this workflow right here at chasen and if you want to upload pdf files so something like this

even if it's not optimal of course you need to choose right here in this loader binary and right

now if we come into our bank investor database we actually have 276 records included and we can ask

questions about q3 q4 and q1 and that's basically it and in the next video of course we need to

connect this vector database to our mcp server and that's basically our automation the first part

of the automation this is our vector database and it was relatively easy we started with a google

rift trigger it searches every single minute for updates into our google drive folder then the

thing gets downloaded by an airfile and uploaded into a bank investor database so see you in the

next video