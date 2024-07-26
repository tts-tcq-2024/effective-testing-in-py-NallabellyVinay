alert_failure_count = 0

def network_alert_stub(celsius):
    print(f'ALERT: Temperature is {celsius} celsius')
    
    # Stub returns 500 for temperatures above a certain threshold to simulate failure
    if celsius > 200:
        return 500
    return 200

def alert_in_celcius(fahrenheit):
    global alert_failure_count
    
    celsius = (fahrenheit - 32) * 5 / 9
    returnCode = network_alert_stub(celsius)
    
    if returnCode != 200:
        alert_failure_count += 1

# Test the alert_in_celcius function with values that should trigger failures
alert_in_celcius(400.5)  # This should fail
alert_in_celcius(303.6)  # This should not fail

# Check if the failure count is correct
assert alert_failure_count == 1, f"Expected 1 failure, but got {alert_failure_count}"

print(f'{alert_failure_count} alerts failed.')
print('All is well (maybe!)')
