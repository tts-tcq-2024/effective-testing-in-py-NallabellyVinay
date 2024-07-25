alert_failure_count = 0

def network_alert_stub(celcius):
    print(f'ALERT: Temperature is {celcius:.1f} celcius')
    
    # Simulate a failure for testing
    if celcius > 100:  # Simulate a failure condition
        return 500
    return 200

def alert_in_celcius(farenheit):
    celcius = (farenheit - 32) * 5 / 9
    returnCode = network_alert_stub(celcius)
    
    if returnCode != 200:
        global alert_failure_count
        alert_failure_count += 1

# Test cases
alert_in_celcius(400.5)  # This should simulate a failure (as it's above 100°C)
alert_in_celcius(303.6)  # This should simulate a failure (as it's above 100°C)

# Print the failure count
print(f'{alert_failure_count} alerts failed.')

# Ensure the failure count is as expected
#assert(alert_failure_count == 2), f"Expected 2 failures, but got {alert_failure_count}"

print('All is well (maybe!)')
