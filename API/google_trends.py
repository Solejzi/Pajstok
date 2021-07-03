from pytrends.request import TrendReq
import matplotlib.pyplot as plt
import numpy as np
from static import StaticInfo as sti

pytrends = TrendReq(hl='en-US')

all_keywords = sti.google_trends_kw
keywords = []

timeframes = ['today 5-y', 'today 12-m',
              'today 3-m', 'today 1-m']
cat = '0'
geo = ''
gprop = ''

countries = ['india', 'united_states', 'united_kingdom',
             'netherlands', 'brazil']


# Part 1 - Google trends analysis

def check_trends():

    pytrends.build_payload(keywords,
                           cat,
                           timeframes[0],
                           geo,
                           gprop)


    data = pytrends.interest_over_time()
    mean = round(data.mean(), 2)
    avg = round(data[kw][-52:].mean(), 2)  # Last year average
    avg2 = round(data[kw][:52].mean(), 2)  # Yearly average of 5 years ago.
    trend = round(((avg / mean[kw]) - 1) * 100, 2)
    trend2 = round(((avg / avg2) - 1) * 100, 2)
    print('The average 5 years interest of ' + kw + ' was ' + str(mean[kw]) + '.')
    print('The last year interest of ' + kw + ' compared to the last 5 years'
          + ' has changed by ' + str(trend) + '%.')
    # Stable trend
    if mean[kw] > 75 and abs(trend) <= 5:
        print('The interest for ' + kw + ' is stable in the last 5 years.')
    elif mean[kw] > 75 and trend > 5:
        print('The interest for ' + kw + ' is stable and increasing in the last 5 years.')
    elif mean[kw] > 75 and trend < -5:
        print('The interest for ' + kw + ' is stable and decreasing in the last 5 years.')

    # Relatively stable
    elif mean[kw] > 60 and abs(trend) <= 15:
        print('The interest for ' + kw + ' is relatively stable in the last 5 years.')
    elif mean[kw] > 60 and trend > 15:
        print('The interest for ' + kw + ' is relatively stable and increasing in the last 5 years.')
    elif mean[kw] > 60 and trend < -15:
        print('The interest for ' + kw + ' is relatively stable and decreasing in the last 5 years.')

    # Seasonal
    elif mean[kw] > 20 and abs(trend) <= 15:
        print('The interest for ' + kw + ' is seasonal.')

    # New keyword
    elif mean[kw] > 20 and trend > 15:
        print('The interest for ' + kw + ' is trending.')

    # Declining keyword
    elif mean[kw] > 20 and trend < -15:
        print('The interest for ' + kw + ' is significantly decreasing.')

    # Cyclinal
    elif mean[kw] > 5 and abs(trend) <= 15:
        print('The interest for ' + kw + ' is cyclical.')

    # New
    elif mean[kw] > 0 and trend > 15:
        print('The interest for ' + kw + ' is new and trending.')

    # Declining
    elif mean[kw] > 0 and trend < -15:
        print('The interest for ' + kw + ' is declining and not comparable to its peak.')

    # Other
    else:
        print('This is something to be checked.')

    # Comparison last year vs. 5 years ago
    if avg2 == 0:
        print('This didn\'t exist 5 years ago.')
    elif trend2 > 15:
        print('The last year interest is quite higher compared to 5 years ago.'
              + ' It has increased by ' + str(trend2) + '%.')
    elif trend2 < -15:
        print('The last year interest is quite lower compared to 5 years ago.'
              + ' It has decreased by ' + str(trend2) + '%.')
    else:
        print('The last year interest is comparable to 5 years ago. '
              + ' It has changed by ' + str(trend2) + '%.')

    print('')

def relative_comparison():
    plt.figure(figsize=(10, 8))
    x_pos = np.arange(len(all_keywords))

    # Last 5-years
    pytrends.build_payload(all_keywords,
                           cat,
                           timeframes[0],
                           geo,
                           gprop)

    data = pytrends.interest_over_time()
    mean = data.mean()
    mean = round(mean / mean.max() * 100, 2)
    ax1 = plt.subplot2grid((3, 2), (0, 0), rowspan=1, colspan=1)
    ax2 = plt.subplot2grid((3, 2), (0, 1), rowspan=1, colspan=1)
    for kw in all_keywords:
        ax1.plot(data[kw], label=kw)
    ax2.bar(x_pos, mean, align='center')
    plt.xticks(x_pos, all_keywords)

    # Last 12-months
    pytrends.build_payload(all_keywords,
                           cat,
                           timeframes[1],
                           geo,
                           gprop)

    data = pytrends.interest_over_time()
    mean = data.mean()
    mean = round(mean / mean.max() * 100, 2)
    ax3 = plt.subplot2grid((3, 2), (1, 0), rowspan=1, colspan=1)
    ax4 = plt.subplot2grid((3, 2), (1, 1), rowspan=1, colspan=1)
    for kw in all_keywords:
        ax3.plot(data[kw], label=kw)
    ax4.bar(x_pos, mean, align='center')
    plt.xticks(x_pos, all_keywords)

    # Last 3-months
    pytrends.build_payload(all_keywords,
                           cat,
                           timeframes[2],
                           geo,
                           gprop)




relative_comparison()
plt.show()

# Part 2 - Relative keyword comparison

