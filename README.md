
# Intro to regression lines

### Learning Objectives

* Understand how regression lines can help us make predictions about data
* Understand how the components of slope and y-intercept determine the output of a regression line 
* Understand how to represent a line as a function

### A not so simple problem

Now that we know a little bit about plotting data, let's see if we can make sense of some data.  We'll start with trying to use data to predict how much money a movie will make.  In trying to predict the box office success of a movie, screen writer William Goldman famously said, "nobody knows anything."  Well, let's try to know something.  

### The benefit of a buck

Imagine we are hired as a consultant for a movie executive.  The movie executive receives a budget proposal, and wants to see how much money the movie might make.  We can help him by trying to see the relationship between money spent on a movie, and money made. 

Here are five movies:


```python
movies = [{'title': 'American Hustle', 'budget': 40000000, 'revenue': 148430908}, {'title': 'Captain Phillips', 'budget': 55000000, 'revenue': 107136417}, {'title': 'Frozen', 'budget': 150000000, 'revenue': 393050114}, {'title': 'Gravity', 'budget': 110000000, 'revenue': 271814796}, {'title': 'Despicable Me 2', 'budget': 76000000, 'revenue': 368065385}]
```

Remember that when we want to plot data, we translate the values to $x$ and $y$ values.  We'll have `budget` as the x value and the y value as `revenue`.  Let's just plot a few movies to get started.

So using our `trace_values` method, we can plot these points, so long as we pass through the list of `x_values`, `y_values`, and `text_values`.  You can see the functions that we built out previously in our [graph.py](https://github.com/learn-co-curriculum/single-variable-regression/blob/master/graph.py) file.


```python
x_values = list(map(lambda movie: movie['budget'], movies))
y_values = list(map(lambda movie: movie['revenue'], movies))
text_values = list(map(lambda movie: movie['title'], movies))
```


```python
import plotly
from plotly.offline import iplot, init_notebook_mode
init_notebook_mode(connected=True)
from graph import trace_values, plot, layout

movie_trace = trace_values(x_values, y_values, text_values = text_values, name = 'movie revenue')
movie_layout = layout(options = {'title': 'Movie Spending and Revenue'})
plot([movie_trace], movie_layout)
```


<script>requirejs.config({paths: { 'plotly': ['https://cdn.plot.ly/plotly-latest.min']},});if(!window.Plotly) {{require(['plotly'],function(plotly) {window.Plotly=plotly;});}}</script>



<script>requirejs.config({paths: { 'plotly': ['https://cdn.plot.ly/plotly-latest.min']},});if(!window.Plotly) {{require(['plotly'],function(plotly) {window.Plotly=plotly;});}}</script>



<div id="81cfc06a-b140-4d9a-ac73-36a1262a0b95" style="height: 525px; width: 100%;" class="plotly-graph-div"></div><script type="text/javascript">require(["plotly"], function(Plotly) { window.PLOTLYENV=window.PLOTLYENV || {};window.PLOTLYENV.BASE_URL="https://plot.ly";Plotly.newPlot("81cfc06a-b140-4d9a-ac73-36a1262a0b95", [{"x": [40000000, 55000000, 150000000, 110000000, 76000000], "y": [148430908, 107136417, 393050114, 271814796, 368065385], "mode": "markers", "name": "movie revenue", "text": ["American Hustle", "Captain Phillips", "Frozen", "Gravity", "Despicable Me 2"]}], {"title": "Movie Spending and Revenue"}, {"showLink": true, "linkText": "Export to plot.ly"})});</script>


This plot shows us that as the movie budget increases the movie revenue tends to increase.  For example, look at point furthest left at a bugdet of 40 million.  That point represents the movie "American Hustle", with 40 million dollars spent and 148 million dollars earned domestically.  Gravity, in the center of our plot, spent over twice as much and earned almost twice as much.

So, at least we now know **something**.

Ok, now imagine our movie executive tells us that a movie came across his desk with a budget of $55 million.  Based on the data we graphed, how much money do you think the movie would bring in?

### Representing linear regression graphically

To predict movie revenue based on a budget, let's draw a single straight line that approximates the relationship between a movie's budget and revenue using our previous data as a benchmark.  

> Later, we'll worry about how well a line like the one below describes our data.  For now, let's use this.   


```python
regression_trace = trace_values([0, 150000000], [0, 450000000], mode = 'lines', name = 'estimated revenue')
plot([movie_trace, regression_trace], movie_layout)
```


<div id="6f805e39-2309-424c-a914-d01c74319fdd" style="height: 525px; width: 100%;" class="plotly-graph-div"></div><script type="text/javascript">require(["plotly"], function(Plotly) { window.PLOTLYENV=window.PLOTLYENV || {};window.PLOTLYENV.BASE_URL="https://plot.ly";Plotly.newPlot("6f805e39-2309-424c-a914-d01c74319fdd", [{"x": [40000000, 55000000, 150000000, 110000000, 76000000], "y": [148430908, 107136417, 393050114, 271814796, 368065385], "mode": "markers", "name": "movie revenue", "text": ["American Hustle", "Captain Phillips", "Frozen", "Gravity", "Despicable Me 2"]}, {"x": [0, 150000000], "y": [0, 450000000], "mode": "lines", "name": "estimated revenue", "text": []}], {"title": "Movie Spending and Revenue"}, {"showLink": true, "linkText": "Export to plot.ly"})});</script>


One of the benefits of using a line is that we can see how much money will be brought in for any point on this line.  All we need to do is look at a given $x$ value, and find the y value of the line at that point. So spend 60 million, and expect to bring in about 180 million.  Spend 20 million, and expect to bring in 60 million.  This approach of modeling a linear relationship (that is a drawing a straight line) between an input and an output is called **linear regression**.  We call the input our explanatory variable, and the output the dependent variable.  So in this case, we are saying budget explains our dependent variable, revenue.

### Representing linear regression with functions

Instead of just representing this line visually, we would also like to represent this line with a function. This way, instead of us needing to **see** the $y$ value of the line at a given point of $x$, we can simply write a function that gives us that same information.  

Let's take an initial (wrong) guess as to how to turn this line into a function.  First we represent the line as a mathematical formula:

$y = x$

And then we turn this formula into a function:


```python
def y(x):
    return x

y(0)
```




    0




```python
y(10000000)
```




    10000000



This is pretty nice.  We just wrote a function that automatically calculates the expected revenue given a movie budget.  This function says that for every value of $x$ that we input to the function, we get back an equal value $y$.  So according to the function, if the movie has a budget of $30$ million, it will earn $30$ million. 

But take a look at the line that we drew.  Our line says something different.  The line says that spending 30 million brings predicted earnings of 90 million.  

So we need to change our function so that it lines up with our line.  In fact, we need a consistent way to turn lines into functions, and vice versa.  Ok, let's get to it.

We can start by taking a look at our chart below, which shows how our line relates x-values and y-values -- that is budget, and revenue.

| X (budget)       | Y (revenue)           | 
| ------------- |:-------------:| 
| 0      |0 | 
| 30 million      |90 million | 
| 60 million      |180 million | 

Ok, so now we need an equation that will allow us to input 0 and get back 0, input 30 million and get back 40 million, and input 60 million and get back 80 million?  What equation is that.

Well it's $y = 3*x$.  Take a look to see for yourself.

* 0 = 30 million * 0
* 90 million =  3 * 30 million 
* 180 million = 3 * 60 million 

Let's see it in the code, and then in the next section we'll show how we figured this out. 

Ok, this is what this formula looks like in code.


```python
def y(x):
    return 4/3*x

y(30000000)
```




    40000000.0




```python
y(0)
```




    0.0



Progress! So we added a number to multiply each value of $x$ by, 3.  And now, we can describe the line in our chart with a function that given a value of $x$, corresponds the value of $y$ along our graphed line.  

### The Slope Variable 

What you just saw, that value of 3, is called the slope variable.  It's generally used in describing a line.  You will see represented generally as $m$ as in:

$y = mx$ 

Let's make sure we understand what all of these variables stand for.  Here they are: 

* $y$: the value that is returned, also called the **response variable**, as it responds to values of $x$
* $x$: the input variable, also called the **explanatory variable**, as it explains the value of $y$
* $m$: the **slope variable**, determines how vertical or horizontal the line will be

In our movie example, these terms make sense.  The $y$ value is our revenue earned from the movie, which we say is in response to our budget.  Our explanatory variable of our budget, $x$, explains our revenue, and the $m$ corresponds to our value of 3, which describes how much money is earned for each dollar spent.  So with this value of $m$, our line is saying that for every dollar spent expect to earn 3 dollars in return.  A $m$ of 2.0 would say that two dollars is earned for every dollar spent.

The variable $m$ is referred to as the slope variable because it refers to the slope of our line.  So a higher value of $m$ means a steeper line.  It also means that we expect a more money earned per dollar spent on our movies.  Imagine the line pivoting to a steeper tilt as we guess a higher amount of money earned per dollar spent.  

### The y-intercept

Ok, there is just one more thing that we need to be able to learn before being able to describe every straight line in a two dimensional world.  That is the y-intercept.

The y-intercept is the $y$ value of the line when it intersects the y-axis.  Or to put it another way, the y-intercept is the value of $y$ when $x$ equals zero.  Let's add another trace to our movie plot.


```python
regression_trace_increased = trace_values([0, 150000000], [50000000, 500000000], mode = 'lines', name = 'increased est. revenue')
plot([movie_trace, regression_trace, regression_trace_increased], movie_layout)
```


<div id="6e48efda-6c58-44c5-8131-77f12bb5f298" style="height: 525px; width: 100%;" class="plotly-graph-div"></div><script type="text/javascript">require(["plotly"], function(Plotly) { window.PLOTLYENV=window.PLOTLYENV || {};window.PLOTLYENV.BASE_URL="https://plot.ly";Plotly.newPlot("6e48efda-6c58-44c5-8131-77f12bb5f298", [{"x": [40000000, 55000000, 150000000, 110000000, 76000000], "y": [148430908, 107136417, 393050114, 271814796, 368065385], "mode": "markers", "name": "movie revenue", "text": ["American Hustle", "Captain Phillips", "Frozen", "Gravity", "Despicable Me 2"]}, {"x": [0, 150000000], "y": [0, 450000000], "mode": "lines", "name": "estimated revenue", "text": []}, {"x": [0, 150000000], "y": [50000000, 500000000], "mode": "lines", "name": "increased est. revenue", "text": []}], {"title": "Movie Spending and Revenue"}, {"showLink": true, "linkText": "Export to plot.ly"})});</script>


So looking at the graph, what is the y intercept of the original estimated revenue line?  Well it's the value of $y$ when that line crosses the y-axis.  That value is zero.  Now you can imagine shifting up the entire line up, so that the y-intercept increases to to 50 million, and that for every value of $x$, the corresponding value of $y$ increases by 50 million.  So our formula is no longer y = 3x.  It is $y = 3 x + 50,000,000$. 

In addition to determining the y-intercept from a line on a graph, you can also see the y-intercept by looking at a chart of points.  So in the chart below, we can see that 50 million is our y-intercept of the new line.  After all, its the value of $y$, when $x$ is zero. 

| X        | Y           | 
| ------------- |:-------------:| 
| 0      |50 million | 
| 40 million      |170 million | 
| 60 million      |230 million | 

Great, so now we have our all of the information we need to describe any straight line.  

$y = mx + b $

In this formula, $m$ is our slope of the line, and $b$ is the value of $y$ when $x$ equals zero.  So thinking about it graphically, increasing $m$ makes the line steeper, and increasing $b$ will raise up the line.   

In the context of our movies, we said that the the line with values of $m$ = 3 and $b$ = 20 million describes our line, giving us $y = 4/3x + 20,000,000 $.

Now let's translate our formula into a function, so that for any input of $x$ it will return the value of $y$ along that line.  


```python
def y(x):
    return 3*x + 50000000
```


```python
y(30000000)
```




    140000000




```python
y(60000000)
```




    230000000



### Summary

In this section, we saw how we can estimate the relationship between an input variable and an output.  We did so by plotting our points and then drawing a straight line right through them.  We can see any output on a line for a given input simply by looking at the y-value of the line at that point of $x$.  We then saw how to represent a line as a mathematical formula, and ultimately a function.  We can describe lines through the formula $y = mx + b $ where $m$ represents the slope of the line, and $b$ represents the value of $y$ when $x$ equals zero.  So our $b$ variable shifts the line up or down while the $m$ variable tilts the line forwards or backwards.  Then our formula tells us that given an input number of $x$ we can find an expected return value $y$.  Translating this formula into a function, we can write a function that returns an exepceted value of $y$ for a provided value of $x$.
