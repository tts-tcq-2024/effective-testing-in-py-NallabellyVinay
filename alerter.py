alert_failure_count = 0

def network_alert_production(celsius):
    print(f'PRODUCTION ALERT: Temperature is {celsius} celsius')
    if celsius > 200:
        return 500
    return 200

def network_alert_stub(celsius):
    print(f'STUB ALERT: Temperature is {celsius} celsius')
    if celsius > 150:  
        return 500
    return 200

def alert_in_celcius(fahrenheit, network_alert_function):
    global alert_failure_count
    
    celsius = (fahrenheit - 32) * 5 / 9
    returnCode = network_alert_function(celsius)
    
    if returnCode != 200:
        alert_failure_count += 1

# Test the alert_in_celcius function with the stub function
alert_failure_count = 0  
alert_in_celcius(400.5, network_alert_stub)  
alert_in_celcius(303.6, network_alert_stub)  

print(f'Test alert_failure_count: {alert_failure_count}')

try:
    assert alert_failure_count == 1, f"Expected 1 failure, but got {alert_failure_count}"
    print('Test passed.')
except AssertionError as e:
    print('FALSE POSITIVE! Expected failure but succeeded')
    print(e)
    raise e

print(f'{alert_failure_count} alerts failed.')
print('All is well (maybe!)')

alert_failure_count = 0

alert_in_celcius(400.5, network_alert_production)
alert_in_celcius(303.6, network_alert_production)

print(f'{alert_failure_count} alerts failed.')
print('All is well (maybe!)')
