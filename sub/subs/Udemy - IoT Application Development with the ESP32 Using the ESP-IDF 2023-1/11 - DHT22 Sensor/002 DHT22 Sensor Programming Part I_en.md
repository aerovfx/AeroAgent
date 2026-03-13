# 002 DHT22 Sensor Programming Part I en

---

OK, so let's start off by inserting the DHT 22 censored driver files into a project, be sure to have

the resource files handy and we'll include them down.

I have my resources folder here, so I'm going to copy the source and header files and paste them under

the main folder.

OK, so now let's maximize eclipse.

And then let's refresh the project by right clicking and going down to refresh.

Then let's go to the see make list file and add the DHT 20 to see file to the list.

Now, save that, and let's open the DHT twenty two files.

OK, now let's go to tasks, come and take.

And let us into the information for the DHT 22 censored task.

Next to find the DHT 22 task stack size.

As four thousand ninety six bytes.

Now to find the DHT 22.

Task priority.

And we can make it five.

And now that's defined the DHT 22 Task Corps.

As core one.

OK, so now all of the other tasks are on course zero.

And the DHT 22 is on court one.

All right.

So next go to DHT 22 Dot H.

And here, let's define.

DHT GPIO.

As I 25.

Then let's create a prototype that.

Starts the DHT 22 censored task.

And this will be a void DHT 22 Tests start.

And it's void.

OK, so copy that.

Go to the see file.

But first, let's include the tasks common Duddridge.

And then we'll go to the bottom of the file.

And defined the task start function.

OK, now, right void.

And it's a task start, and it's void.

And first, we'll use the next test create PIN to call.

They we'll call the test function DHT 22 task.

And the tech can be the same.

And the depth is DHT 22 task stack size.

The PV parameters is no.

The priority is DHT 22 task priority.

And also, the handle is no.

The core idea is DHT 22 task core idea.

And now we could define the DHT 22 censored task.

All right, so we could say DHT 22 two censored task.

Which is a static void.

And it's our ADHD 22 task.

And it takes avoid pointed PV parameter.

Then we'll call set DHT GPIO.

And this is a function from the driver, which sets the GPIO, so let's pass a defined DHT GPIO.

Then let's print.

Starting DHT task.

Next will make an endless for loop.

And then print.

Reading DHT.

Then they'll say hint return equals and call read DHT function from the driver.

Then we'll use the air handler from the driver, which is air handler.

And give it the return.

And now let's print out humidity and temperature.

So we'll print the humidity to one decimal place.

And give it the result of the get humidity function from the driver.

And also print the temperature in the same manner.

And give it the result of the get temperature function from the driver.

Now, let's wait at least two seconds before reading again.

Now, those also say the interval of the whole process must be more than two seconds.

All right, and that is simply what is recommended by the creators of this driver.

So here we can try a delay of four seconds.

So four thousand.

Milliseconds.

And see how that works for now.

Now, call the test start function from men, so we'll copy this.

Go to Maine.

And that will include the DHT 22 Dot H file.

And then, let's say start DHT 22 censored task.

Well, let's paste our function here.

And then build the project.

Let's let the bill finish.

And in the meantime, be sure that you've connected the DHT 22 sensor to your death kit because we're

going to test our functions to be sure that we can read and print the sensor data.

Now, flesh.

Once you're ready.

And we can ignore that because it's only referring to some unresolved includes from the DHT 22 files

here.

Now it's resolved.

And this one, this one is resolved to.

OK, now let's open the monitor.

And we have sensor data ratings, great.

And in my home, the humidity is under 55 percent, so that's also good news.

All right.

So let's continue in the next lesson and we'll send the sensor data to the webpage.