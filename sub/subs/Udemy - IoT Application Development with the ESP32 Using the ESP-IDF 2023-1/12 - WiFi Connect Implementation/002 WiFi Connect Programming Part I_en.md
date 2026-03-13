# 002 WiFi Connect Programming Part I en

---

In order to connect Y5 via the Web page, we need to make a few updates to index HTML.

So let's create a new section here.

And here, let's create a div.

And call it wi fi connect.

Then create an H2.

That says ESP thirty two.

WI fi connect.

And close the two.

Then let's make a section.

And copy it.

So we can close the section.

And within the section right, input ID equals connect, underscore aside and specify the type as text.

And the maxlength.

As 32.

And the placeholder that says assisted.

And the value can be blink.

Let's copy that.

And paste below for the password information.

Change the input ID to pass.

And the tape as password.

And the Max should be 64.

And placeholder as password.

All right, now, let's do input type for a checkbox.

Which on click shows the password.

So let's specify a function here by saying on Click Show Password.

Function and now on the Web page, let's write here some text that says Show password.

Next, let's use our Div Class four buttons.

And first, let's close this div.

And within a year, we'll have an input ID.

For Connect wi fi.

And this tape will be button.

And the value will say connect.

Then do a divide for.

WI fi connect credentials airs.

Then making age for.

For wi fi connect status.

All right, now, we can close our Wi-Fi connectivity.

And let's fix that.

And now that looks OK.

All right, so now we can go to Epcot CSIS and add the styling.

And now we want some red and green lettering, so let's come right here.

And say your.

And right.

Color, Colin Green.

OK.

And let's do one for red.

And say color, coal and red.

And that's it.

So now we can go over to James.

And first, let's set up our own click function, and here, just follow me.

And that's for a connect underscore Wi-Fi and then say Dot on click.

Comma function.

And open the curly braces and its check credentials.

And they'll close it with the semicolon.

OK, so now let's go down to the bottom of the file.

And let's create a function here.

Which clears the connection status interval.

And say function.

Stop wi fi connect status interval.

And let's not define it yet, because we need a few more.

So let's create another function below it.

And this one gets the Wi-Fi connection status.

So it's a function.

Get wi fi connect status.

And let's create another.

And this one starts the interval.

For checking the connection status.

And its function.

Start Wi-Fi Connect status interval.

Now, let's do another.

Let's right here, connect Wi-Fi function.

Called using the SSA, ID and password.

Entered into the text fields.

And that's function connect Wi-Fi.

Next, let's do the last one.

And this one checks credentials.

On Connect wi fi.

Button, click.

And that's a function check credentials.

OK, now let's define this one and then work our way up the file.

So first, let's say our list.

Equals and leave it blank.

Then let's write creds, OK, and set it to true.

And now selected society equals and just follow what I do here.

It's dollar sign from the Connect society.

Value.

OK, so we want the value from that element and then say password equals the connect pass element value.

Now, let's write, if selected, a suicide.

Is blank.

Then we will set the error list.

And just follow what I do here.

It's an age for.

And let's use our red color and then say a suicide cannot be empty.

And then close it.

Then creds OK, equals false.

Now, copy this block of code.

And then let's paste it and then write password here.

And password here.

Then say, if creds OK equals false.

Then we want the wi fi connect credentials errors.

We want the credentials heirs to display the error list.

All right, so now let's copy this.

And then right else.

The credentials heirs are blank.

And then we can call the Connect Wi-Fi function.

OK, so to recap, this function only checks at the site and password are empty.

And if they are, we display some error messages and if not, it calls the Connect Wi-Fi function.

Also, we're already enforcing the maximum length in the index HTML for the text fields, so we don't

have to check for that here.

Now let's go to connect Wi-Fi.

And say get the SSA, ID and password.

And then selected as a side.

Equals the value from Connect society.

And then password.

Is the value from Connect Pass?

And now just follow me and we'll use Ajax here.

OK.

And the URL.

His forward slash wife, I connect.

And the data type.

This, Jason.

And the method is post.

And Cash said it's a false.

And the headers.

Are called my connect assisted.

From selected as a side.

And the password you can call my Connect password.

From pWt.

And data.

Timestamp.

Is detente now?

All right, then close that with the semicolon, and then now we can call start why fi connect status

interval?

OK, so connect Wi-Fi calls.

Start wi fi connect status interval.

Let's go to find that now just above the first, let's go to the top of the file and let's create a

variable to hold the Wi-Fi Connect interval.

And said it to no.

All right, so now let's copy that and let's go back.

And in the function, let's say wi fi connect interval equals set interval and past the Get wi fi connect

status and let's call it every two point eight seconds.

OK, so here was saying call to get wi fi connect status function every 2.8 seconds.

So next, let's go to get wi fi connect status.

And let's say VR x HBO equals new XML http request.

And then VAR requests, you are well.

Equals forward slash wi fi connect status.

And then let's X8 shortcut open post.

Then say request you are well and false.

And now let's send.

WI fi connect status.

And then, right, if experts are ready state.

Is for.

Meaning that it's been sent and ex HIV status is 200.

Meaning that it's OK.

Then let's say via response equals, Jason, that parse parentheses x h r Typekit response text.

And now we can document don't get element by it for wi fi connect status.

Dot inner html.

Equals connecting.

And then, right, if response start wi fi connect status.

Is to.

Then we'll say document get element by ID..

WI fi connect status.

That inner HTML equals, and then we'll write a message and read.

That says failed to connect.

Please check your AP credentials and compatibility.

OK, then stop wi fi connect status interval.

All right now, copy this, and let's say else, if response thought wi fi connect status.

Is three.

Then let's paste below.

And now change this to green.

And change the message to Connection's success.

All right.

So here in this function, we are checking the status response on the web server side, and depending

on that response, we write a message to the user and stop the connection status interval and we'll

create those responses in the web server later.

OK, so now let's go to stop Wi-Fi Connect status interval, and we'll say if Wi-Fi Connect interval.

Is not no.

Then we will use clear interval.

For the interval variable.

And we will set this variable here.

We'll set it to No.

OK.

Just like that.

And lastly, let's define the show password function.

And that one shows the Wi-Fi password.

If the boxes checked.

And it's a function show password.

And right, VAR X equals document get element by ID.

Connect underscore.

Pass.

And then say, if X-Type.

Is password.

Then X-Type equals text.

Then say else.

X-Type equals password.

That's it.

So if the box is checked, we show the password.

Otherwise, we don't show it.

OK, so I have one mistake up here, so let's fix that.

This should be in her HTML.

All right, so be sure that you don't have any errors here, either.

And in the next lesson, we'll program the web server.