alert_failure_count = 0

def network_alert_production(celsius):
    # This function would contain the actual network communication code
    print(f'PRODUCTION ALERT: Temperature is {celsius} celsius')
    if celsius > 200:
        return 500
    return 200

def network_alert_stub(celsius):
    print(f'STUB ALERT: Temperature is {celsius} celsius')
    if celsius > 200:
        return 500
    return 200

def alert_in_celcius(fahrenheit, network_alert_function):
    global alert_failure_count
    
    celsius = (fahrenheit - 32) * 5 / 9
    returnCode = network_alert_function(celsius)
    
    if returnCode != 200:
        alert_failure_count += 1

# Test the alert_in_celcius function with the stub function
alert_failure_count = 0  # Reset the alert_failure_count for the test
alert_in_celcius(400.5, network_alert_stub)  # This should fail
alert_in_celcius(303.6, network_alert_stub)  # This should not fail

# Debug output to understand the state
print(f'Test alert_failure_count: {alert_failure_count}')

# Check if the failure count is correct
assert alert_failure_count == 1, f"Expected 1 failure, but got {alert_failure_count}"

print(f'{alert_failure_count} alerts failed.')
print('All is well (maybe!)')

# Reset the alert_failure_count for production
alert_failure_count = 0

# Use the production function
alert_in_celcius(400.5, network_alert_production)
alert_in_celcius(303.6, network_alert_production)

print(f'{alert_failure_count} alerts failed.')
print('All is well (maybe!)')
