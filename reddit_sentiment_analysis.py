import praw
from textblob import TextBlob

# === Authenticate ==============
reddit = praw.Reddit(client_id ='', client_secret = '', user_agent = '', username = '', password = '')
# ===============================

# === Create Variables ==========
overall_subjectivity = 0.0
overall_polarity = 0.0
number_of_sentiments = 0
# ===============================


# === Main loop =================
# Gets submissions and comments from selected subbreddit(s)
# Then analyses them using textblob, and calculates overall subjectivity and polarity
for submission in reddit.subreddit('stocks+investing').search('TSLA', sort = 'relavance', time_filter = 'week'):
	for top_comment in submission.comments:
		comment_analysis = TextBlob(top_comment.body)
		overall_subjectivity = overall_subjectivity + comment_analysis.subjectivity
		overall_polarity = overall_polarity + comment_analysis.polarity
		number_of_sentiments = number_of_sentiments + 1.0

	analysis = TextBlob(submission.title)

	overall_subjectivity = overall_subjectivity + analysis.subjectivity
	overall_polarity = overall_polarity + analysis.polarity
	number_of_sentiments = number_of_sentiments + 1.0


average_subjectivity = overall_subjectivity/number_of_sentiments
average_polarity = overall_polarity/number_of_sentiments
# ===============================


# === Print out data ============
print('The average subjectivity value is ' + str(average_subjectivity))
print('The average polarity value is ' + str(average_polarity))
# ===============================
