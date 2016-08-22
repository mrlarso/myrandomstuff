import uuid
from tincan import (
    RemoteLRS,
    Statement,
    Agent,
    Verb,
    Activity,
    Context,
    LanguageMap,
    ActivityDefinition,
    StateDocument,
)

lrs = RemoteLRS(
    endpoint="http://lrs.tunapanda.org/data/xAPI/",
    username="8337556b1002d3f86bbbe2011b5cd35afc2f18ab",
    password="7dc75f0aee21c46ac4e62fd29fca48046b393190",
)

actor = Agent(
    name='MickLarson',
    mbox='mailto:yoyoyo@tunapanda.org',
)

verb = Verb(
    id='http://adlnet.gov/expapi/verbs/attempted',
    display = LanguageMap({'en-US':'experienced'}),
)

object = Activity(
    id = "http://pythonlrsinsert.org",
    definition = ActivityDefinition(
        name = LanguageMap({'en-US':'TinCanPythonLibrary'}),
        description = LanguageMap({'en-US': 'Use of, or interaction with, the TinCanPython Library'}),
    ),

)


context = Context(
    registration = uuid.uuid4(),
    instructor=Agent(
        name='TI trainer',
        mbox='mailto:mick@tunapanda.org',
    ),
)

statement = Statement(
    actor=actor,
    verb=verb,
    object=object,
    context=context,
)

response = lrs.save_statement(statement)
