## BankWebServicePython
This is webservice project developed in Python and Django Rest Framework.For a given  bank name and a city you can get the details of all
the branches of the bank in the city .For a given bank branch ifsc code you can get the branch details

## Get Branch Details for a given IFSC code
To get the get the bank branch detail for a given ifsc code type the following url in the browser address bar
http://bankservicepython.herokuapp.com/branch/{yourbrachifsccode}
### Example 
(http://bankservicepython.herokuapp.com/branch/ALLA0212106)

## Get list of Bank Branches for a given bank name and city
To get the get the list of bank branches  for a given bank name and city  type the following url in the browser address bar
http://bankservicepython.herokuapp.com/bank/{yourbankname}/city/{yourcityname}
### Example 
(http://bankservicepython.herokuapp.com/bank/state%20bank%20of%20india/city/kolkata)


## Tech/framework used
Ex. -

<b>Built with</b>
- [Python](https://www.python.org/)
- [Django Rest Framework](http://www.django-rest-framework.org/)
- [Postgres SQL](https://www.postgresql.org/)


 ### Heroku App Link
(http://bankservicepython.herokuapp.com/bank/state%20bank%20of%20india/city/kolkata)
