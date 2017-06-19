import arrow
import json


# Lambda - doSomething1
def do_something_1(event, context):

    print "Event: " + str(event)
    print "Context: " + str(vars(context))
    event['output'] = "doSomething1 succeeded!"
    return event


# Lambda - doSomething2
def do_something_2(event, context):

    print "Event: " + str(event)
    print "Context: " + str(vars(context))
    event['output'] = event['output'] + " doSomething2 succeeded!"
    return event


# Lambda - doSomething3
def do_something_3(event, context):

    print "Event: " + str(event)
    print "Context: " + str(vars(context))
    event['output'] = event['output'] + " doSomething3 succeeded!"
    return event
