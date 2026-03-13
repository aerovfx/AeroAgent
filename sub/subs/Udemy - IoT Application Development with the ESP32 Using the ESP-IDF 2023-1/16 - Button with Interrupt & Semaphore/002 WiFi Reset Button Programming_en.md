# 002 WiFi Reset Button Programming en

---

We'll start off this lesson by adding a couple of new files and domain.

So let's first add the new source file.

And call it Wi-Fi reset button.

Don't seem.

And then let's add a new head of file.

And call this Wi-Fi reset button.

But each.

OK, so we'll get organized to you.

And then go to see make lists.

And to the sources, let's add the wi fi reset button.

That see file.

All right.

And now let's go to tasks common.

And Sheer will add the information for the Wi-Fi reset button task.

And define why fi reset button.

And I'll copy this part.

And it's the stack size.

And make it 20, 48 bytes.

And next is the priority.

As six.

And the next.

The caller ID.

And make it zero.

OK, it looks good.

So next, let's go to the Wi-Fi reset button header file.

And the first thing that we'll do here is create the default interrupt flag.

And define it as ESP into our flag default.

And it's zero.

OK, next, let's define the GPIO and first say wi fi reset button is the boot button.

On the delicate.

And define it as why fi reset button.

And it's A0, right?

OK, nuts, let's make a function prototype and make a comment here.

Configures wi fi reset button.

And interrupt configuration.

And it's void fi reset button.

Config.

And it's void.

All right.

And now let's copy this so we can define it in the C file.

And in the C file, let's just drop it right here.

OK, now let's include fructose.

And the first include.

This free autos.

Slash and I'll just copy this part.

And this one is free autos.

Courage.

And next include Trescothick.

And also include Reata SIM for.

And make sure you note the proper spelling here, it's simple.

And now let's include.

Driver slash GPIO Duddridge.

And also include our ESP lug tonnage.

And that's for our log functions.

And next, let's include our application headers, so first include tasks common.

And also include Wi-Fi app storage.

And of course, we want to include.

Our new wi fi reset button.

All right, and let's do a tag.

Static const care.

And call it wi fi reset button.

And next.

We need a semaphore handle.

And it's semaphore handle underscore T and call it Y5 reset semaphore.

And said it to no.

OK, and now let's go to the Wi-Fi reset button config.

And first, we'll create the binary semaphore.

And that's a wi fi reset, semaphore.

Equals x semaphore create binary.

OK.

And next, let's configure the button.

And set the direction.

And use GPIO pad, select GPIO.

And pass the Wi-Fi reset button.

And then use GPIO set direction.

And then pass the Wi-Fi reset button.

And set the mode as GPIO mode input.

Next, let's enable interrupt.

On the negative edge.

And use of set interrupt tape.

And pass the Wi-Fi reset button.

And for the insert type, it's GPIO into your neck edge.

And next, let's create the Wi-Fi reset button Teske.

With X task creates pinned to core.

And call it with the reference to Wi-Fi reset button.

And the tag is the same fi reset button.

And the depth is a Wi-Fi reset button to ask.

Stack size.

PV parameters are no.

And the priority is a Wi-Fi reset button desk.

And the task handle is no.

And the caller ID is our Wi-Fi reset button to ask.

Korede.

Next will install GPIO, our service.

And use GPIO and still by Assad's service and pass or ISP into your flag default.

OK, next, let's attach the interrupt service routine.

With ISI Handler.

Add.

And pass the Wi-Fi reset button.

And then the ISI handler will define it as wi fi reset button ISI Handler.

And the dogs are no.

OK, so next, we'll have to define the ISI handler and the wi fi reset button to ask.

OK, so let's come up you.

And let's say why fi reset button desk.

Reacts to a boot button event.

By sending a message to the Wi-Fi application.

To disconnect from Wi-Fi.

And clear the saved credentials.

All right, so the parameter TV program.

Is a parameter which can be passed to the task.

So this is a void.

A Wi-Fi reset button test, and it's a void pointer TV program.

OK, now let's create our endless for loop.

And you will need to check if we can obtain the semaphore.

So say if.

Semaphore, take.

And it's the Wi-Fi reset semaphore.

Port Max DeLay.

And if that returns true.

Then let's ESV log.

That wi fi reset button interrupt occurred.

And then we'll say send a message to disconnect wi fi.

And clear credentials.

Let's use our wi fi app, send message.

And pass the Wi-Fi message.

User requested state disconnect.

And now we'll put a delay here, so that quick button presses won't result in sending messages in rapid

succession.

So let's use the task delay.

With the delay of two thousand milliseconds.

All right, that's it.

So next, let's define our ISO handler, and we'll do it up here.

And say ISI Handler.

For the Wi-Fi reset boot button.

And the parameter ARG.

Is a parameter which can be passed.

To the ISI handler.

And it's void, I attribute.

And it's a reset button.

I saw a handler.

And it takes a valid point to ask.

And in here will notify the button to ask.

Using eczema for GIF from ISO and pass a wi fi reset semaphore.

And the second parameter is no.

So to recap, we're going to call the public function wi fi reset button config from Maine Dot C, and

when the user presses the boot button, the interrupt service routine will be invoked, which gives

the semaphore.

Then the wi fi reset button task takes the semaphore, which allows the button task to unblock so that

the message can be sent to the Wi-Fi application to disconnect.

OK, that's it.

But we have to make a couple of changes to the Wi-Fi app that see.

So come here and let's add another status bit.

And we need another status bit to indicate to the application that the ESB thirty two is indeed connected

to an access point before reacting to the Wi-Fi disconnect button press and calling the disconnect function.

OK.

So let's say consent.

WI fi app Stay Connected.

But IP bit.

Equals bid three.

All right, so first, we need to set this bid when the ESP 32 has a connection and is assigned an IP.

So let's first go down to the gut IP case and the Wi-Fi application task.

And Hugh will say X Event Group set bids.

For the event group.

And then passed the gut IP bit.

Now, let's go down to the user request to disconnect case.

And here, let's say event bits.

Equals X event group get bits.

From our event group.

And now let's say if.

Event bits and the gut IP bid.

Then we'll simply take the call we've already written and inserted here.

All right, so let's cut it.

And pasted here.

OK, so whether we arrive here due to a disconnect button press and the web page or via a Wi-Fi reset

button, press here will check if there is indeed an active connection first before setting the user

request to disconnected, setting the retry number to Max tries, disconnecting Wi-Fi, clearing the

station credentials and changing the LTE status.

So now we need to update the disconnected case below.

So let's go there.

And down here, let's say, if event bits and the gut IP bit.

Then we'll go ahead and clear the bits.

From a prevent group, and it's to gut IP bit.

OK, so now let's go to main that can test this out.

First, let's include the Wi-Fi reset button.

And then here, let's configure.

The wi fi reset button.

And call Wi-Fi reset button config.

OK, now let's build and test it.

And flash, when you're ready.

Then open a monitor.

And then connect to the ESP.

I'm already connected here.

So now go to the Web page.

And then I'll connect the ESPN.

OK, we're connected a refresh here.

And now press the boot button on the dead kid.

And there you have it.

We've disconnected Wi-Fi and the station credentials are cleared, and there's our log message.

And if we refresh.

The connection information goes away.

Nice.

OK, so let's continue our development in the next lesson.