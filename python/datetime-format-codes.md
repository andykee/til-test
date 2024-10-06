# datetime formatting

* `datetime.strftime(format)` returns a string according to *format*
* `datetime.isoformat()` returns a string formatted as YYYY-MM-DDTHH:MM:SS.ffffff
* `datetime.strptime(date_string, format)` returns a `datetime` object corresponding to *date_string*, parsed according to *format*

## datetime format codes

Here we have some **bold** and *italic* stylings. How about an _underline_ too?

| Directive | Meaning               | Example                      |
|-----------|-----------------------|------------------------------|
| `%a`      | Weekday (abbreviated) | Sun, Mon, ..., Sat           |
| `%A`      | Weekday (full)        | Sunday, Monday, ..., Saturday|


### h3

#### h4

![Alt text]({attach}dog.png)


##### h5

1. numero uno
2. nombre deux
3. number three

![Alt text]({attach}slack.png)

This paragraph has `inline code`

```python
class EventProcessor:
    def __init__(self, expected_events, false_positive_rate):
        self.processed_events = BloomFilter(expected_events, false_positive_rate)

    def process_event(self, event_id):
        if event_id in self.processed_events:
            print(f"Event {event_id} likely duplicate, skipping.")
            return

        # Process the event here
        print(f"Processing event: {event_id}")

        # Add to Bloom Filter after processing
        self.processed_events.add(event_id)

processor = EventProcessor(expected_events=1000000, false_positive_rate=0.01)
for event in ['play_song_123', 'skip_ad_456', 'play_song_123', 'like_song_789']:
    processor.process_event(event)
```


```
this
has
no
syntax!
hint?
```

Below is an indented code block

    this
    is
    tab-indented <>
    woo hoo

back to normal

And now we have $x = y$ inline math

$$F = \frac{\sqrt{3}}{2}$$

fin.