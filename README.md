# Plate Calculator
Recently my workout app of choice blocked it's plate calculator tool behind a paid tier. Personally I hate doing mental maths so instead of paying the ~$6 a year I spent 6 hours making this.

To use, go to apps.mattsharp.dev/plate_calculator and append a weight (in pounds) that you'd like the plates for:

ex: `apps.mattsharp.dev/plate_calculator/220`

And voila:

    {"plate_calculation":
        {"target_weight":220,
        "bar_weight":45,
        "plates":
            {"45":2,
            "35":2,
            "5":2,
            "2.5":2},
        "total":220.0,
        "remaining":0.0},
    ...}

If you want to get bit fancier, you can also pass optional query parameters in the url:

- `exclude_plate=35` will perform the calculation without whatever plate size is passed. For multiple, simply repeat as needed. The calculation will round down if the exact weight is unattainable
- `metric_or_imperial=imperial` does what it says on the tin. I have no idea what standard kg weights are so these are mostly just equivalents to imperial counterparts. Default is **Imperial**
- `bar_weight=35` will set the bar weight to 35, for those who are fans of the 'light' bar (which is often yellow). Default is 45 (typically blue).

For example:

- Target weight of 140lbs, without using 45, 2.5 or 1.25lb plates and using a 35lb bar:
`plate_calculator/140?exclude_plates=45&exclude_plates=2.5&exclude_plates=1.25&bar_weight=35`

Result:

        {
            "plate_calculation": {
                "target_weight": 140,
                "bar_weight": 35,
                "plates": {
                    "35": 2,
                    "15": 2
                },
                "total": 135,
                "remaining": 5
            },
            "plate_options": [
                35,
                25,
                15,
                10,
                5
            ],
        "bar_weight": 35
        }

To view all default options for weights, drop the target weight from the url:

`plate_calculator/`

This yields:

    {
        "default imperial": {
            "bars": [
                45,
                35
            ],
            "plates": [
                45,
                35,
                25,
                15,
                10,
                5,
                2.5,
                1.25
            ]
        },
        "metric": {
            "bars": [
                20,
                16
            ],
            "plates": [
                20,
                16,
                11,
                7,
                5,
                2,
                1,
                0.5
            ]
        }
    }

Appending `system=metric` or `system=imperial` here as a query parameter will select only relevant lists
