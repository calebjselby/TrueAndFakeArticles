
import pandas as pd
import matplotlib.pyplot as mpl
import statistics as st
import chart_studio as cs
import chart_studio.plotly as py
import chart_studio.tools as tls
import matplotlib.pyplot as plt

# chart_studio credentials
username = "calebjselby"
api_key = "WTdUDIDEW8y8EaH0pgzN"

cs.tools.set_credentials_file(username = username, api_key = api_key)

# read in data
true = pd.read_csv("C:/Users/caleb/Desktop/Python/News/True.csv")
fake = pd.read_csv("C:/Users/caleb/Desktop/Python/News/Fake.csv")

# remove periods and commas from title
grammar = [",", ".", "(", ")", "*", "^", "@", "%", "!", "'", ":", ";"]

## loop over each entry in title column and replace all characters in grammar
for i in range(1,len(true["title"])):
    title = str(true["title"][i-1])
    for c in grammar:
        title = title.replace(c, "")
    true["title"][i-1] = title

for i in range(1,len(fake["title"])):
    title = fake["title"][i-1]
    for c in grammar:
        title = str(title.replace(c, ""))
    fake["title"][i-1] = title

# find average character length of title, real vs. fake
def avg_title_length(column):
    sum = 0
    n = 0
    for title in column:
        sum =+ len(title)
        n=+1
    return float(sum/n)

avg_true_title_len = avg_title_length(true["title"])
avg_fake_title_len = avg_title_length((fake["title"]))

# chart to show difference between averages
def make_title_lengths(column):
    title_lengths = []

    for title in column:
        title_lengths.append(len(title))

    return title_lengths

true_title_lengths = make_title_lengths(true["title"])
fake_title_lengths = make_title_lengths(fake["title"])

fig = mpl.figure()

ax1 = fig.add_subplot(2,1,1)
ax2 = fig.add_subplot(2,1,2)

ax1.hist(true_title_lengths)
ax2.hist(fake_title_lengths)

ax1.set_xlim((0,200))
ax2.set_xlim((0,200))
ax1.set_title("Lengths of Article Titles Perceived as True")
ax2.set_title("Lengths of Article Titles Perceived as False")

# test to see if py.plot will only accept plotly objects
fig_py = plt.hist(true_title_lengths)

# put on my plotly workspace to embed
mpl.show()
# py.plot(fig_py, filename="Lengths of Article Titles", auto_open=True)

# find average length of article, real vs. fake
true_article_lengths = make_title_lengths(true["text"])
fake_article_lengths = make_title_lengths(fake["text"])

fig2 = mpl.figure()

ax3 = fig2.add_subplot(2,1,1)
ax4 = fig2.add_subplot(2,1,2)

ax3.hist(true_title_lengths)
ax4.hist(fake_article_lengths)

# put figure on my plotly workspace
fig2.show()


true_article_mean = st.mean(true_article_lengths)
fake_article_mean = st.mean(fake_article_lengths)

# find average paragraph length, real vs. fake


# look at distributional differences between real and fake
## distribution of title length, real vs. fake


## distribution of paragraoh length, real vs. fake


## disbritubion of article length, real vs. fake

