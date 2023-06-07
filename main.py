import boto3
ec2 = boto3.resource('ec2')
for instance in ec2.instances.all():
    print (instance.id , instance.state)

print("Select an option:")
print("1. Start EC2 instances")
print("2. Stop EC2 instances")
print("3. Terminate EC2 instances")

option = input("Enter your choice (1/2/3): ")

if option == "1":
    instances = ec2.instances.filter(Filters=[{'Name': 'instance-state-name', 'Values': ['stopped']}])
    for instance in instances:
        instance.start()
    print("Started all stopped instances.")
elif option == "2":
    instances = ec2.instances.filter(Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])
    for instance in instances:
        instance.stop()
    print("Stopped all running instances.")
elif option == "3":
    confirmation = input("Are you sure you want to terminate all instances? (y/n): ")
    if confirmation.lower() == "y":
        instances = ec2.instances.filter(Filters=[{'Name': 'instance-state-name', 'Values': ['running', 'stopped']}])
        for instance in instances:
            instance.terminate()
        print("Terminated all instances.")
    else:
        print("Termination canceled.")
else:
    print("Invalid option. Please choose 1, 2, or 3.")
