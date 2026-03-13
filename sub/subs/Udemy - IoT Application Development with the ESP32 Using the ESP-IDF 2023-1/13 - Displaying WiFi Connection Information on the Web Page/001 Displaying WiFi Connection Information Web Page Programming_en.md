# 001 Displaying WiFi Connection Information Web Page Programming en

---

In order to display the connection information, a few updates are required to the webpage files.

So we'll start here and indexed HTML and make a few updates so that we can display the Access Point,

IP Gateway and netmask info.

Also will include a disconnect button to allow users to disconnect Wi-Fi via the web page.

So let's start off you by creating another div and call it connect info.

Now close the div.

And that a section.

And now within the section, let's create a divide.

For Connected AP label.

And then close it.

Now, create another divide.

For Connected app.

And close that.

And under this section.

Make another divide.

For IP address label.

And close it.

Let's make another four.

WI fi connect IP.

And close that.

Now we'll do another pair of did, so copy this line.

And paste below.

And let's change this one to netmask label.

And this one to wi fi connect netmask.

Now, let's make another blow.

And change this one to Gateway label.

And here it's why Fi Connect Gateway.

Next, let's make our button.

And right here, say, did class buttons.

And now let's close the div.

Then here, let's do an input I'd.

As disconnect, we find.

With the type.

As button.

And the value as disconnect.

And now let's close the input I'd.

And lastly, let's make a horizontal rule.

And that's it for index HTML.

So next, we can go to the stylesheet and let's add some styling to these elements.

So let's go over to access.

Let's move over here.

And right here, let's do the styling for.

Connected AP label.

And a comma for connected AP.

And then here, let's add display in line.

And then let's copy that.

And pasted.

And do IP address label.

And this one as netmask label.

Add a comma for Gateway label.

And this ensures that all of these elements are in line together.

So copy paste.

And now let's do the same with the Wi-Fi Connect IP.

The wi fi connects netmask.

And the Wi-Fi Connect Gateway.

Next, let's add the styling.

Down here for connected AP.

Now, let's add the color, so we can just copy this one.

And paste it.

Now, let's copy this one.

Pace below.

Now we can change it to wi fi connect IP.

And also copy this.

Paced changes to wi fi connect netmask.

Paste and change it to why if I connect Gateway.

Then had the styling for the disconnect, why fi?

And then here, right, display none.

OK, because we only want to display the disconnect button when there's an active connection.

So now let's go to James.

And first, we'll call the Get Connect info from the document ready function.

OK, so let's copy that.

And define it at the bottom of the file.

And comment gets the connection information.

For displaying on the Web page.

And then its function.

Get Connect info.

All right.

And here you'll get Jason.

And it's forward slash wi fi connect info.

Jason?

Function.

And open the curly braces.

And then in here, we want the connected app label.

So, right, connected app label.

HTML.

And right connected to.

Colon with the space.

And that's for our label.

And the next we want.

We want connected AP.

Text.

And for data.

We'll call it AP.

So then we can copy and paste.

And then here we could just change this to IP address label.

And then the text to IP address.

And change this to wi fi connect IP.

And the data is IP.

Now, let's copy paste this one.

And make this one that mask label.

And the text as netmask, Colin.

And change this to wi fi connect netmask.

And the data as netmask.

And let's do this one more time.

For the Gateway, so its gateway label.

And the text to Gateway Colon.

Notes update this one also to Gateway, the data is GW.

And then let's write document get element by ID..

Disconnect why fi?

Dutch style Dutch display.

Equals block.

And this allows us to toggle between showing and hiding the disconnect button element, depending on

whether or not there is connection information.

OK, so now let's close this one with the semicolon.

And now let's copy this function.

And we're going to call it under the successful case within the get why fi status function.

All right, so that's it in the next section, we'll continue programming on the web server side.