<h2> Design Rationale </h2>

My design was largely (if not entirely) inspired by the theme of the data. I knew that if I wanted to have an orbital menu and a general space theme with a star background. 
I thought a lot about having something other than lines for my graph (and in my MVP, I used circles to be more "planetary"). But throughout the design process, I found that the line is just the most intuitive for money over time (something we've seen in class many times, too).


Based on the questions I got from informal testing with friends and the peer reviews, my methods of interaction were pretty easy to decide on. Obviously, I had to get the planet scroller working well. Then, I knew the mission lines would mean nothing if you couldn't hover to see what mission they applied to. Lastly, inflation adjustment is such a small interaction to add, but brings so much value in a big "ah-hah" moment. Getting these interactions working smoothly took a lot of my time (and some of my methods are still a little hacky).
<h2> Development Process </h2>

If I had to guess, I spent upwards of 90 or 100 hours on this assignment. 

When I started making my MVP, there was a lot of time spent deciding what to do with the data, since it's easy to want to show all the data you possibly can. Then, I spent considerable time cleaning it, largely because The Planetary Society's original dataset structure was not helpful for extracting columns needed in code. Then, I started in on how to use D3.js. I actually gave up on D3 for the MVP and ended up using the Vega-lite + Python tool called Altair. Due to the time constraint of the MVP, I was only able to get a simple graph working, but it was enough to illicit some really excellent feedback about what people would want to see.

Once I started the final product, actually with D3.js this time, I spent a large fraction of time on design specifics (finding good planet images, adjusting the brightness of backgrounds, etc.). Of course, this pattern of being too picky at first happens with many projects. I was adament that I wanted an orbital menu so I tried out a variety of carousel methods. I didn't have much success building out the carousel myself (I'm not a great web developer), so the package I finally found worked perfectly.

Each time I'd make a new design decision or start an interaction, I'd find that my old method of enter/update/exit states wouldn't work, so I probably re-coded my graph about five different ways. Debugging each of these took the most time since I still struggle with D3.
I had a hiccup late in the design process where I realized I hadn't organized my graph well for inflation adjustment. I made it work, but my code is definitely not of the highest quality from adding that in. 

There would be a lot of cool interactions I could add if I spent more time on this, such as breakdowns of cost, and something that shows how far planets are (which results in higher costs).

<h2>Sources</h2>
Dataset: https://www.planetary.org/space-policy/planetary-exploration-budget-dataset

Carousel package: https://github.com/PAIO-CO-KR/carousel-3d

I also drew inspiration from a few code saviors online:
- Multi-line graph https://bl.ocks.org/d3noob/50666f4f5ac86f5ca739b250715a2e12
- Scroll events https://developer.mozilla.org/en-US/docs/Web/API/Document/scroll_event