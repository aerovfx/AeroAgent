# 003 WiFi Connect Programming Part II en

---

So let's pick up where we left off, because next, we need to find the right handlers for the Wi-Fi

Connect JSON, as well as the Wi-Fi Connect status.

And we'll do that in the ATP service.

Let's go to the C file.

And just as a refresher, we have our wi fi connect status messages we go from initialized to success

to fail.

All right, you.

OK?

And since we need to deal with the Wi-Fi configuration within the web server and within the Wi-Fi application,

we need a way to pass the Wi-Fi configuration around.

So let's go to the Wi-Fi app.

See File.

And let's handle that here.

So at the top of the file, let's say.

Used for returning to Wi-Fi configuration.

And it's a wi fi config type.

And we need to point to and call it wi fi config and set it to No.

Next, let's say.

Used to track the number of retirees.

When a connection attempts fails.

And that's a static int global retry, no.

And next, let's allocate memory for the Wi-Fi config, and we'll do that on the start function.

And here, let's say, allocate memory.

For the Wi-Fi configuration.

And it's why fi config.

Equals y fi config typecast pointer and Malak, the size of the white config structure.

Then we'll set.

The wi fi config.

Two zero for the size of the wi fi config.

OK, next, let's define a function that returns this Y2K config.

So now we'll go to the head of file.

And here will say.

Gets the wife configuration.

And it returns the Wi-Fi config type.

Point to and call it wi fi app, get wi fi config.

And it's void.

So copy that.

And go to the see file.

And drop it here.

And simply say return white flight config.

Next, let's go to the HTP server, had a file.

And coming to you.

Connection status for wi fi.

And that can be a typedef enum.

HTTP server.

WI fi connect status.

First, one can be done.

And let's explicitly set it to zero.

Then HTP Wi-Fi status connecting.

And also HTP wi fi status.

Connect failed.

And HTP wi fi status connects success.

And let's name it.

With an underscore E!

Now, let's go to the C file.

And here, let's create a global variable.

And say why fi connect status.

That is a static int global wi fi connect status.

And said it to none.

OK, now let's copy that variable.

And in the monitor under connect in it said it to status connecting.

And now copy it.

And then under the success case, let's paste it and change it to connect success.

All right, and the now under Connect failed.

Let's change it to connect failed.

And now we can define you are by handlers.

So let's head down there.

And here, let's copy this one.

Let's use it to define a wi fi connect JSON handler.

And call it wi fi connect, Jason.

And the euro is wi fi connect, Jason.

And the method is HTTP post.

And the handler we can call HTP Server WI Fi Connect.

Jason Handler.

Next, let's pass the structure name to register the handler.

OK, now let's copy this one.

And now let's do the wi fi connect status handler.

And call it wi fi connect status, Jason, and the you are right is wi fi connect status.

And then change the handler to verify Konnect status now past the name, to register it.

So now let's proceed by defining a wi fi connect JSON handler.

So now we'll right.

WI fi connect that Jason Handler.

Is invoked after the Connect button is pressed.

And handles receiving the SSA, ID and password.

Entered by the user.

And the parameter R E Q is the CTB request for which the you are right needs to be handled.

And return is OK.

And then it's a static ESP error type, and it's our wi fi connect handler, and it takes an 8TB request

type pointer RFQ.

So let's first ESP log.

That wi fi connect that Jason requested.

Now, let's define some variables for the society and password length received and say size underscored

T Len as this idea equals zero comma len pass.

And set that one to zero as well.

And next, we need care pointers to hold the strings, so here, say care.

Pointer assisted strength equals no.

Karma passed drink, and that's also no.

All right, so next, we'll say get a suicide header.

And it's lean as a side equals httpd request, get header value length.

For the request and from my connect a society.

OK, now let's add one to the length.

And then say if.

Length.

Is greater than one.

Then a suicide string.

Should be allocated memory for the length of the suicide.

And then we'll say if HTP requests get of values string.

For the request and the My Connect as a side field.

For the SSA string.

And size is length of the society.

And if that equals ESP, OK?

Then we'll look.

From this handler.

Found head of.

For my connect as society.

And then pass the society string.

All right, so we could do the same procedure for the password.

So let's copy this.

And then paste below, change this to password.

And change this to pWt.

And then let's copy this of.

I want to double check this is all correct.

OK.

Yes.

Yes, it's the same, so we should be all good.

OK, let's go back.

And change this to lend pass.

And.

And this one as well.

And then change this to pass drink.

OK.

And copy and paste it here.

And you.

OK, do we do everything?

Yes, that all looks good.

OK.

And change this, you.

All right, so now let's update the Wi-Fi networks configuration.

And let the Wi-Fi application, no.

OK, we'll make a wi fi config type point to wi fi config equals the return of our wi fi app.

Get Wi-Fi config function.

All right, then Mims said, if I can config.

Two zeros.

For the size of fi config type.

Then let's copy.

Into the Wi-Fi config.

Stay.

A society.

And that's from the Eastside string.

For the length of the suicide.

And now let's copy that line.

Pastes blow and we'll do the password.

And this is past drink.

And this is Len Pesce.

Now we can send the wi fi app message.

And the ID is five fi app message.

Connecting from HTP server.

Now that's free, the allocated memory for assisted string.

And also free for the password strength.

Now we can return.

He spoke.

And actually, there's one mistake here.

This should be password.

All right, so would.

OK, I think it's time for a short break, and we're going to continue in the next lesson.