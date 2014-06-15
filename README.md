# Ninja Twitterbot

Ninja Twitterbot is a simple automated tweeting bot designed to run on Google App Engine. It is capable of tweeting the latest data from NinjaBlock connected sensors stored in the Ninja Cloud.

This application duplicates the twitter features available through the Ninja Cloud, and if you're only looking to tweet values at a regular interval, or according to a certain rule, using a basic message this can be achieved utilising the Ninja Cloud rule engine. This bot was designed to offer the same functionality but offer the ability to more closely control triggers, or alternatively, integrate additional functionality which can not be integrated into the Ninja Cloud rule engine. 

## Google App Engine

The Ninja Twitterbot is designed to run on Google App Engine (GAE). Whilst the webapp2 framework it utilises is compatible with any WSGI compatable environments, some parts of the implementation use proprietary APIs specific to the GAE environment. It should be simple enough to swap out these APIs with other libraries in other Python environments. In a case where this service is hosted alone on a GAE application, it should be capable of running on a GAE project without billing configured. 

## Configuration

Ninja Twitterbot is configured using a single `config.json` file in the application's root directory. This file must be deployed to GAE with the other components of this application. `config_default.json` includes a default configuration which can be copied into config.js with the necessary fields completed.

### Configuration File Options

The following options are available in the `config.js` file.

#### `tweet` - Tweet Configuration
| field           | required | description                                                              |
|-----------------|----------|--------------------------------------------------------------------------|
| tweet.template  | Y        | A string containing any sensor data attribute substitutions (based on the sensor name specified in the NinjaBlocks sensor configuration) in the [Python Format language](https://docs.python.org/2/library/string.html#formatspec).
eg. `"Current Temperature and Humidity: {temp} degrees Celcius, {humid}% relative humidity"`            |
| tweet.latitude  | N        | The latitude of the location to be associated with the tweet.
eg. `"-19.260565"`                                                                                      |
| tweet.longitude | N        | The longitude of the location to be associated with the tweet.
eg. `"146.818502"`                                                                                      |
| tweet.place_id  | N        | The ID of the Twitter location this tweet will be associated with. You can select this from the results of the [Twitter reverse_geocode endpoint](https://dev.twitter.com/docs/api/1.1/get/geo/reverse_geocode) using above co-ordinates.
eg. `"0013cae44d65aff9"`                                                                                 |

#### `twitter` - Twitter API Configuration


#### `ninja` - Ninja Cloud API Configuration

### Tweeting

#### Remote Triggers

#### Cron



## HTTP API Endpoints

### Server Endpoint - `/`

The server endpoint will provide basic details about the Ninja Twitterbot server including the Google App Engine application identifier and the deployed version the request was served by. It is designed to provide information on the server and test its availability. 

#### Example Response

```
{
    "server": "ninjatemptwitterbot",
    "version": "1.760934143892241511"
}
```

### Tweet Endpoint - `/tweet`

The tweet endpoint will trigger the configured sensor values to be collected from the NinjaBlocks Cloud service and  substituting into the tweet template. This endpoint can be hit manually with a browser or other HTTP client, or utilise a cron or another remote trigger to automatically tweet information at pertinant times. 

This endpoint will return a simple object containing the tweeted message under the `message` key. 

#### Example Response

```
{
    "message": "Current Temperature and Humidity: 19.6 degrees Celcius, 68% relative humidity"
}
```
