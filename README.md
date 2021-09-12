## Rodadas API

This is a simple API built with Django Rest Framework to support an app for a study group about Latin America. The front end is built in React [here](https://github.com/araleo/rodadas-front).

### Endpoints

* /api/rodadas
    * Returns a list with data about all the group's meetings.


* /api/proxima
    * Returns an object with data about the group's next meeting.


* /api/ultimas
    * Returns a list with data about all the group's past meetings.


### Cloud

The API is configured to be deployed on AWS Elastic Beanstalk, using a PostgreSQL instance hosted on AWS RDS.


