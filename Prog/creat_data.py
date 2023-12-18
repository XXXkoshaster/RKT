import krpc
import json

conn = krpc.connect()
vessel = conn.space_center.active_vessel

altitude = conn.add_stream(getattr, vessel.flight(), 'mean_altitude')
met = conn.add_stream(getattr, vessel, 'met')
mass = conn.add_stream(getattr, vessel, 'mass')
speed = conn.add_stream(getattr, vessel.flight(vessel.orbit.body.reference_frame), 'speed')
fuel = conn.add_stream(vessel.resources.amount, 'LiquidFuel')

data = {'met':[], 'fuel': [], 'mass': [], 'speed':[], 'altitude':[]}

while vessel.mass > 5000:
    data['met'].append(met())
    data['altitude'].append(altitude())
    data['fuel'].append(fuel())
    data['mass'].append(mass())
    data['speed'].append(speed())

with open('data.json', 'w') as out_file:
    json.dump(data, out_file)