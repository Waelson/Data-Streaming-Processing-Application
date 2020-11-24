
from dataclasses import asdict, dataclass
import json
import random

import faust

@dataclass
class ClickEvent(faust.Record):
    email: str
    timestamp: str
    uri: str
    number: int


app = faust.App("exercise6", broker="kafka://localhost:9092")
clickevents_topic = app.topic("com.udacity.streams.clickevents", value_type=ClickEvent)

uri_summary_table = app.Table("total", default=int)

@app.agent(clickevents_topic)
async def clickevent(clickevents):
    async for ce in clickevents.group_by(ClickEvent.uri):
        uri_summary_table[ce.uri] += 1
        print(f"{ce.uri}: {uri_summary_table[ce.uri]}")


if __name__ == "__main__":
    app.main()
