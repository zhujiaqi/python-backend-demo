from twilio_server import TwilioClient
twilio_client = TwilioClient()

# twilio_client.create_phone_number(213, os.environ['RETELL_AGENT_ID'])
# twilio_client.delete_phone_number("+12133548310")
# twilio_client.register_phone_agent("+14154750418", os.environ['RETELL_AGENT_ID'])
# twilio_client.create_phone_call("+14154750418", "+13123156212", os.environ['RETELL_AGENT_ID'])

phone_numbers = [
    ("+61401909771", "CJ")
    ("+61861020619", "Zakk")
]

def poll_call_status(call_sid, interval=5, timeout=60):
    start_time = time.time()
    while time.time() - start_time < timeout:
        call = twilio_client.calls(call_sid).fetch()
        print(f"Call SID: {call.sid}, Call Status: {call.status}")
        if call.status in ['completed', 'canceled', 'failed']:
            print("Call has ended. Exiting poll.")
            break
        time.sleep(interval)

if __name__ == "__main__":
    print("List of phone numbers:")
    for index, number in enumearate(phone_numbers):
        print(f"{index}. {number[0]}: {number[1]}")
    phone_number_index = input("Please enter the index you want to call: ")
    phone_number_index = int(phone_number_index)
    number = phone_numbers[phone_number_index]
    call = twilio_client.create_phone_call("+14154750418", number[0], os.environ['RETELL_AGENT_ID'])
    poll_call_status(call.sid, timeout=600)
