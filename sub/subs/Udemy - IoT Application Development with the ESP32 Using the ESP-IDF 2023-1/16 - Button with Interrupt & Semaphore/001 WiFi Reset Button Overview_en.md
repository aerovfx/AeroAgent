# 001 WiFi Reset Button Overview en

---

Welcome to the whitefly reset button section in this section.

I'll describe how we're going to use the boot button to disconnect the ESP 32 and clear the credentials.

So let's jump right into the implementation.

In order to accomplish this, we'll take a few steps.

The boot button will be configured to generate an interrupt on GPIO zero.

And when the interrupt occurs, the message will be sent to the wife by application about the user request

to disconnect and clear the credentials.

Upon receiving the message, the Wi-Fi application will check if there really is an active connection

prior to disconnecting and clearing the credentials because we don't want to call ESP Wi-Fi disconnect

unless there is an active connection.

All right, so let's take a look at some information about GPIO interrupts and binary sigma force.

OK, so just very briefly, an interrupt signal is a signal that indicates the occurrence of a specific

event that requires immediate attention and blocks the normal program execution to run an interrupt

service routine, or ESR, which reacts to the event that occurred.

Also note that Azar's must have a short execution time.

We want to get in and out as quickly as possible.

The GPIO interrupt In our case, we are configuring the interrupt to trigger on the following edge signal

because when you press the boot button, the pin connects to the ground as shown here and the ESP 32

defecates c schematic.

You should see something similar in the schematic for all expressive Typekit.

And additionally, due to the short execution of eyesores, a binary semaphore will be used to notify

the free autos task, which will handle the actions performed when the button is pressed.

And about binary sim, of course, binary SIM offers are SIM affairs, which can assume the value of

zero and one only.

Hence, they can be used as a signalling mechanism.

The ESPN IDF API for Sigma Force can be found here.

I recommend you browse through here briefly, and we'll use the eczema for create binary function to

create our semaphore.

And you can find an example usage of this below.

Also within the interrupt service routine, we'll need to use the API eczema for GIF from my SO.

And we'll use this to notify the button Teske, there's an example usage of this that you can check

out as well.

And within the free autos task, we'll use eczema for take.

And at this point, the task has been notified and Will handled the required actions there.

All right, now, let's briefly review the episode will use for the reset button GPIO configuration.

First of all, I can recommend that you review the impressive API reference here.

Here, you'll find an overview of the thirty four physical GPIO pads.

Each pad can be used as general purpose iyo or can be connected to an internal peripheral signal.

So check out this table and other comments, especially before getting into using ATC Spy or.

Also, you can check application examples here as well.

Part of our configuration will include setting the direction of the GPIO we are working with as an input

using GPIO set direction.

This function will take the GPIO number of the wi fi reset button, which is zero and the mode as well,

which is input mode.

Then we'll set the interrupt type of the GPIO as fall engage.

We'll use the GPIO Ianto NEG Edge as an input parameter to GPIO set interrupt type.

Again, this one takes the GPIO, no.

The wife reset button in our case and the interrupt tape, which will be negative edge.

Next, we'll need to install the ISR service using GPIO, install ISR service.

This function installs the drivers GPIO ISI Handler Service, which allows per pin GPIO interrupt handlers.

Also note if this function is used, the ISR service provides a global GPIO ISO and individual pin handlers

are registered via the GPIO Isaw handler add function.

Which is actually the next API that will use to specify the interrupt service routine that will run

when the interrupt for that pin is triggered for this function.

We'll need the GPIO number and Isaw handler or name of the AI Assad that will define in any arguments.

If we'd like to use any.

And lastly, when we define the ESR, we can place it into the Eyram section by using the Eyram attribute.

We'll use this just as the example shows below.

And if you're interested in learning more, please feel free to browse through this information before

we get started.

All right, so that's it for now.

Let's get started.