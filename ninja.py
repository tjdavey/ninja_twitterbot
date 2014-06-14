from google.appengine.api import urlfetch

import json
import logging

NINJA_SENSOR_URL = "https://a.ninja.is/rest/v0/device/{sensor}?user_access_token={token}"

class NinjaLiveData():
    
    def __init__(self, ninja_config):
        
        self.token = ninja_config.get('token')
        self.sensors = ninja_config.get('sensors')
    
    def get_sensors(self):
        all_sensors = {}
        for sensor_name, sensor_guid in self.sensors.iteritems():
            all_sensors[sensor_name] = self.get_sensor(sensor_guid)
            
        return all_sensors
    
    def get_data(self):
        all_data_points = {}
        for sensor_name, sensor_guid in self.sensors.iteritems():
            all_data_points[sensor_name] = self.get_data_point(sensor_guid)
        
        return all_data_points
    
    def get_sensor(self, sensor_guid):
        url = NINJA_SENSOR_URL.format(sensor=sensor_guid, token=self.token)
        logging.info(url)
        fetch_result = urlfetch.fetch(url, deadline=20)
        return json.loads(fetch_result.content)
        
    
    def get_data_point(self, sensor_guid):
        sensor_result = self.get_sensor(sensor_guid)
        
        logging.info(sensor_result)
        
        if 'data' in sensor_result and 'last_data' in sensor_result['data'] and 'DA' in sensor_result['data']['last_data']:
            data_point = sensor_result['data']['last_data']['DA']
        else:
            data_point = None
            
        return data_point