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
