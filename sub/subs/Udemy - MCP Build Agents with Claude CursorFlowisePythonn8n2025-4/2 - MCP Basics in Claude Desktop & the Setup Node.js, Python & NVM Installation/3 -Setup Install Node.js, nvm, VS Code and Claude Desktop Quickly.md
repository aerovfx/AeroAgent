# 3 -Setup Install Node.js, nvm, VS Code and Claude Desktop Quickly translated

---

In this video we will install the first things that we need in order to work with MCPs in Cloud Desktop.

And also the documentation can help us a tiny bit.

First of all, we need of course Cloud Desktop.

Then we also need Node.js and I want to show you how you can use NVM in order to make updates or

downgrades most likely to your Node version because sometimes there can be bugs and you need to

be able to fix this bugs. So if we come to this documentation, they tell us that in this tutorial

they show us how to use Cloud Desktop. If you scroll down the first step is of course

to download Cloud for Desktop. So simply open this link, then you are on this web page.

Right now it's also English excuse me and as soon as you are on this you can download it for

your machine. So you can either use Windows, Windows with ARM or you can use Mac OS.

For me it's of course Windows so you can simply press on these. Then you come to your downloads.

This thing is relatively small. I think it's only 100 megabyte. You can open this thing up and

then it's an normal installation so simply double click on this setup exit. Simply press OK,

two or three times and then you are done. As soon as this is done something like this will also

pop up on your Desktop and if you press on it, Cloud Desktop will open up. Most likely we'll have no

chats right now, at least I assume and in the next video we will take a closer look at the interface

how you can use Cloud Desktop in more detail but first let's just install the next things that we

need. So if we come down into the documentation they tell us why we should use Cloud Desktop and

not Cloud AI on this web page because basically a lot of servers they work like locally. That's why

you need Cloud Desktop. Then they show you how to add servers but before we can do this we need to

install Node.js so they are not that clear you need to scroll down and then you see you also need

Node.js so if you basically open up Node.js you can also google it so if you come to Google and type

in Node.js you can simply press on the first link and then you can download the newest version

but I have to tell you the newest version can make mistakes from time to time. If you do not know if

you have Node.js already installed just search for the Node.js command prompt or you can also

type in Terminal or even CMD or PowerShell and if you can simply type in Node.js version and send it

out and then you see if you have a Node version already installed. This is just a quick fix but if

here is nothing included you absolutely need to install Node.js but I generally would recommend you

to install it once again if you do not know if you have installed it and by the way if you type in

Clear you can always clear your Terminal. If you come here to download for example you can also

download the right version for your machine so you can either press right here and the default

setting is version 22.16.0 and I would recommend you to use this version. The newest version is the

version 24.1.0 and this can have some bugs from time to time with the model context protocol.

Over time this versions will change. Over time the model context protocol will also include

newer versions but keep in mind I want to show you everything how you can update your instances

and do a lot more. Then you use your operating system for me it's Windows of course. Then you can

also use Docker and VM and so on just leave it as it is and if you want to do it really really easy

like I told you you can simply press download Node.js right here on this button then you will have your

install or you can come do your downloads once again you open this up once again and then you press

next, accept, next then you basically use like the path where you want to save it you press next

a few times and then you are done. This is a really really simple installation maybe they also

ask you if you want to install chocolatey this is not necessary needed but you can install it if

you want like I said it's really easy just press next a few times and then you are done. So I

cancel this right now because I have Node already installed so let's just close this down and now I

want to show you the problem with these versions from time to time. The model context protocol sometimes

does not use the latest versions and if you have a version installed that is not supported you will

get errors and bugs and that's why we will use NVM over this course. If you google NVM you find the

Node version manager and if you press on this GitHub repo don't worry I will give you all the links

you already have there big five with all these links you can scroll down and then we can use

NVM now I have a Windows machine and that's why I need to use also the Windows installation so what I

do is I go back once again and type in NVM for Windows you can also see it here I press on these

but I think this works on every single system like nearly the same then you can scroll down and

you come to download now then we scroll down a tiny bit once again and we use the NVM setup

X so you press on it then also NVM will be right here and you can install it once again with just

a few clicks so you simply press on it and go on and as soon as everything is installed right here

so cloud desktop no JS and also the NVM setup X then you can manage your versions if you have problems

and I want to show you right now at this minute of what version I am using and how you can switch

your versions if we come back to Node.js.org we can simply see for ourself what versions are

available and there are a lot of versions and what you should do right now is to come to the Node.js

command prompt simply type in Node on your search bar on your machine Windows Mac whoever you are

you can press on these and then because we have NVM installed you can type in NVM list

and as soon as you type in NVM list you will have most likely just one version or if you have no

JS already installed from previous maybe you have also some more versions and you can basically see

what version is installed and what version gets used so you see I have one two three four five

six versions installed and the version where we have this star this is the version that we

currently use so type in NVM list and see for yourself what's installed and what you are using

the version 20.16.0 is an older version but I really like this version because this version

supports and like nearly everything we don't have any bugs and if we have problems we would use

something a little bit newer right now I want to show you how you can use these versions so first

let's just say that I want to install what version do I want to install 22.16.0 because this should

also be a version that supports nearly everything so you don't have to use NVM I do think with this

version you can do everything but right now I have not included this version that's why I want to

type in NVM install and then the version that I want to install let's just see once again 22.16.0

22.16.0 and then you can simply send this out this will take a tiny bit and then everything will be

installed and boom we have an error why do we have an error I have misspelled install install is of

course not correct so let's just do it again NVM install 22.16.0 and we send it out once again

and right now we are downloading we are installing everything should work just fine then you see

that you can use this version by simply typing NVM use but first let's just see if this is working

NVM list right now you see that we also have 22.16.0 included and then you can switch your

versions NVM use 22.16.0 and if you send it out you need to accept maybe you do not see this but I

have a pop up I accept it and then we are using this and if I type in NVM list once again you see

that this version right now is active by the way you can also type in note dash dash version in order

to check your version and you see this is the version that I am using right now right now at this

minute I want to switch back once again to this version so NVM use 20.16.0 and I send it out I need

to accept once again then one last time and we am list and boom I am once again at this version

and this is a version that never makes problems for me so I would recommend you to use either this

version or the version that gets automatically installed and only change these versions if you

run into problems but most of the time if you run into problems it's because of this version

and right now you know how to fix it one software that you should also install is for example visual

studio code this is just a code editor you should use this later in order to edit your config files

yes you can do this with every software that is on your computer but I do like vs code because vs

code makes it really simple makes it really easy you just have to press download and install it

and later this thing will pop up automatically you can also code in this thing for coding we will use

mostly cursor cursor by the way just a fork for vs code so I would also recommend you to install

visual studio code because this will make it easy later in cloud desktop to edit your config files

I think this is the easiest way to go but you don't have to install vs code if you want to use

a other code editor and that's basically what you need to do so first install cloud desktop then

install no chairs normally you are completely fine but I would strongly recommend you to install

also nvm because with nvm you can always switch your versions really really fast and easy you can

type in nvm list to see all the versions that you have installed nvm install to install other versions

and then nvm use to switch your versions it's really that easy and then you will be in a good spot

because you can update downgrade do whatever you want if you run into problems and I see you of course

in the next video because now we need to start using the model context protocol