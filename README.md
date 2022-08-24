# Tradlee
Tradlee is an application for individual investors. 
The application is a platform used for planning the investments in shares.
The initial verison gives the opportunity to use one stock technical indicator as a strategy to invest on the 
US stock market.
This strategy is based on Relative Strength Index (RSI). Application allows to check if a user should buy the share 
or sell it.

There is also an option to add own strategy.

Later version will have more choices of public listed companies and other investment strategies.
In the future there will be an option to invest in the shares on other stock exchanges too.

IndexView 
View allows to use subscription form. It loads views of 6 companies on the site. 
The whole function enables the view of the whole homepage.

![main view](https://github.com/Grzegorz9999/Tradlee/blob/main/final/invest/static/img/Tradlee/Tradlee1.jpg?raw=true)

CompanyView
Function enables the view of a separate company. It shows the name, short name, stock, description and the history
of the company. We can log in and check the RSI indicator.

![company view](https://github.com/Grzegorz9999/Tradlee/blob/main/final/invest/static/img/Tradlee/company_view.jpg?raw=true)


CompanyListView
Function enables the view of all of the companies. There is an option to add any company the user want.
There are links to the separate view of any company listed on the site.

AddCompanyView
Allows user to add the company from any stock exchange in the world. It is very important add the TTICKER (short_nam)
from the Yahoo Finance portal. Otherwise the RSIView will not be able to calculate the RSI indicator properly.

IndicatorView
Function enables the view of a separate indicator. It shows the name, short name, and the description of the indicator. 

IndicatorListView
Function enables the view of all of the indicators. There is an option to add any indicator the user want.
There are links to the separate view of any indicator listed on the site.

AddIndicatorView
Allows user to add the technical indicator. Any added Indicator will not be calcualted.

NyseCompaniesView
Function enables the view of all of the companies from NYSE Stock Exchange. 
There are links to the separate view of any company listed on the site.

GpwCompaniesView
Function enables the view of all of the companies from GPW Stock Exchange. 
There are links to the separate view of any company listed on the site.

MyLoginFinal
Enables user to log in to the platform.

MyLogoutView
Enables user to log out of the platform.

RSIView
The function calculates RSI indicator for the companies. It will calculate RSI for any company added 
as long as the user implements proper TICKER from Yahoo Finance website.

![main view](https://github.com/Grzegorz9999/Tradlee/blob/main/final/invest/static/img/Tradlee/rsi.jpg?raw=true)

StrategyView
Function enables the view of a separate strategy. It shows the name, indicators used, and the description of the 
strategy. 

StrategyListView
Function enables the view of all of the strategies. 
There are links to the separate view of any strategy listed on the site.

AddEmailView
Function enables to add the email for subscription.
