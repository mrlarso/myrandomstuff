import uuid
import json
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


lrs_local = RemoteLRS(
    endpoint="http://lrs.tunapanda.org/data/xAPI/",
    username="4429f0474aa7e82b23d73e2d6bfa59e634baeb56",
    password="b7dd813c7ffe8bc92fe7edfa07943944857c0c1e",
)
lrs_remote = RemoteLRS(
    endpoint="http://lrs.tunapanda.org/data/xAPI/",
    username="8337556b1002d3f86bbbe2011b5cd35afc2f18ab",
    password="7dc75f0aee21c46ac4e62fd29fca48046b393190",
)

print "Gathering data from remote LRS"
response = lrs_remote.query_statements({"since":"2010-08-11T12:38:33.265900+00:00","format":"exact"})
remote_data = json.loads(response.data)

remote_statement_ids = []
for statement in remote_data["statements"]:
    remote_statement_ids.append(statement["id"])

print "Gathering new statements"
response = lrs_local.query_statements({"since":"2010-08-11T12:38:33.265900+00:00","format":"exact"})
local_data = json.loads(response.data)

for statement in local_data["statements"]:
    if statement["id"] in remote_statement_ids:
        print "skip"
    else:
        response = lrs_remote.save_statement(statement)
        if not response:
            raise ValueError("statements failed to save")
        print "...saved"
